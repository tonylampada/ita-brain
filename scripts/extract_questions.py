#!/usr/bin/env python3
"""
Extract per-question images from an ITA exam PDF.

Usage:
    extract_questions.py <pdf> <out_dir> [--dpi 200] [--margin 6]

Detects question boundaries via "Questão N." anchors from `pdftotext -bbox-layout`,
then crops the rendered PNG pages with ImageMagick, stitching multi-page questions
into a single tall image.

Requires: pdftoppm, pdftotext, magick (ImageMagick) in PATH.

Output:
    {out_dir}/q01.png, q02.png, ...
    {out_dir}/manifest.json  with [{numero, image, pages}, ...]
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path


PAGE_RE = re.compile(r'<page\s+width="([\d.]+)"\s+height="([\d.]+)"')
LINE_RE = re.compile(
    r'<line\s+xMin="([\d.]+)"\s+yMin="([\d.]+)"\s+xMax="([\d.]+)"\s+yMax="([\d.]+)">(.*?)</line>',
    re.DOTALL,
)
WORD_RE = re.compile(r'<word[^>]*>(.*?)</word>', re.DOTALL)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(f"FAIL: {' '.join(cmd)}\n{r.stderr}\n")
        sys.exit(1)
    return r.stdout


def parse_pages(layout_html: str):
    """Return list of (page_idx, [lines]) where lines = list of (yMin,yMax,words_joined).

    `words_joined` is the line's text content (all words concatenated with single
    spaces). Keeping the whole line lets the anchor finder tolerate stray
    inline characters that some PDFs emit between "Questão" and the number
    (e.g. `Questão√ 25.` in matematica_2012.pdf).
    """
    pages = []
    page_splits = re.split(r'(<page\s+width="[\d.]+"\s+height="[\d.]+"[^>]*>)', layout_html)
    page_idx = 0
    for chunk in page_splits:
        if chunk.startswith("<page"):
            page_idx += 1
            pages.append((page_idx, []))
            continue
        if page_idx == 0:
            continue
        for line_m in LINE_RE.finditer(chunk):
            y_min = float(line_m.group(2))
            y_max = float(line_m.group(4))
            words = [w.strip() for w in WORD_RE.findall(line_m.group(5))]
            text = " ".join(w for w in words if w)
            pages[-1][1].append((y_min, y_max, text))
    return pages


NUM_TOKEN_RE = re.compile(r"^(\d+)[.,]?$")


def _first_number(tokens):
    for tok in tokens[:5]:
        m = NUM_TOKEN_RE.match(tok)
        if m:
            return int(m.group(1))
    return None


def find_question_anchors(pages):
    """Return list of (numero, page_idx_1based, y_min, y_max).

    A line is an anchor when its first token is "Questão" and one of the next
    few tokens is a question number (`NN` or `NN.`).

    Some PDFs (e.g. matematica_2012.pdf) split the title across two pdftotext
    lines that share the same yMin — typically when a tall inline character
    (like `√`) raises the bbox of the rest of the line. When the "Questão"
    line lacks a number, we look at sibling lines whose yMin is within ±5pts.
    """
    anchors = []
    for page_idx, lines in pages:
        for idx, (y_min, y_max, text) in enumerate(lines):
            tokens = text.split()
            if not tokens or tokens[0] not in ("Questão", "Questao"):
                continue
            numero = _first_number(tokens[1:])
            if numero is None:
                for jdx, (yj_min, _yj_max, tj) in enumerate(lines):
                    if jdx == idx or abs(yj_min - y_min) > 5.0:
                        continue
                    numero = _first_number(tj.split())
                    if numero is not None:
                        break
            if numero is None:
                continue
            anchors.append((numero, page_idx, y_min, y_max))
    anchors.sort(key=lambda a: (a[1], a[2]))

    # Fallback: some PDFs (fisica_2012.pdf) print Q1 as just "1. <word>..."
    # without "Questão". If Q2 was found but Q1 wasn't, look for "1. <word>..."
    # in the area above Q2's anchor on the same page or earlier pages.
    if anchors and anchors[0][0] == 2:
        q2_page, q2_y = anchors[0][1], anchors[0][2]
        for page_idx, lines in pages:
            if page_idx > q2_page:
                break
            for y_min, y_max, text in lines:
                if page_idx == q2_page and y_min >= q2_y:
                    break
                tokens = text.split()
                if len(tokens) < 3:
                    continue
                m = NUM_TOKEN_RE.match(tokens[0])
                if not m or int(m.group(1)) != 1:
                    continue
                if not tokens[1] or not tokens[1][0].isalpha():
                    continue  # filter formula lines like "1. x = 5"
                anchors.insert(0, (1, page_idx, y_min, y_max))
                return anchors
    return anchors


def last_text_ymax(pages, page_idx):
    for pi, lines in pages:
        if pi == page_idx and lines:
            return max(l[1] for l in lines)
    return None


def effective_top(pages, page_idx, anchor_ymin, anchor_ymax, lookback=30.0,
                  overlap_eps=2.0):
    """The 'logical top' of a question. Accounts for tall inline math whose
    fragments pdftotext emits at smaller yMin than the title's baseline.

    Iterative flood-fill upward: extend `top` to any line whose yMax overlaps
    (or nearly touches) the current `top`. This chains numerator → exponent →
    other fragments. A gap larger than `overlap_eps` stops the extension,
    preventing the prior question's tail content from being absorbed.
    """
    floor = anchor_ymin - lookback
    page_lines = []
    for pi, lines in pages:
        if pi == page_idx:
            page_lines = lines
            break
    top = anchor_ymin
    changed = True
    while changed:
        changed = False
        for y_min, y_max, _text in page_lines:
            if y_min >= top or y_min < floor:
                continue
            if y_max >= top - overlap_eps:
                top = y_min
                changed = True
    return top


def page_size_pts(layout_html: str):
    m = PAGE_RE.search(layout_html)
    if not m:
        sys.stderr.write("Could not find page dimensions.\n")
        sys.exit(5)
    return float(m.group(1)), float(m.group(2))


def crop_one(png_path: Path, top_pts: float, bottom_pts: float, dpi: int,
             out_path: Path):
    """Crop a single page PNG between top_pts and bottom_pts (PDF points). Caller
    must apply any desired top/bottom margin before calling."""
    scale = dpi / 72.0
    top_px = max(0, int(top_pts * scale))
    bot_px = int(bottom_pts * scale)
    height_px = max(1, bot_px - top_px)
    run([
        "magick", str(png_path),
        "-crop", f"x{height_px}+0+{top_px}",
        "+repage",
        str(out_path),
    ])


def stitch_vertical(parts: list, out_path: Path):
    if len(parts) == 1:
        parts[0].rename(out_path)
        return
    run(["magick", *[str(p) for p in parts], "-append", str(out_path)])
    for p in parts:
        p.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("out_dir")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--margin", type=float, default=4.0,
                    help="vertical margin in PDF points around each question")
    ap.add_argument("--page-top-skip", type=float, default=40.0,
                    help="when a question continues onto a new page, start at this y to skip headers")
    args = ap.parse_args()

    pdf = Path(args.pdf).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1) layout for question anchors
    layout_html = run(["pdftotext", "-bbox-layout", str(pdf), "-"])
    # Some PDFs (e.g. fisica_2015) emit text in NFD form (e.g. "Questão");
    # normalize so the anchor comparison against "Questão" works.
    layout_html = unicodedata.normalize("NFC", layout_html)
    width_pts, height_pts = page_size_pts(layout_html)
    pages = parse_pages(layout_html)
    anchors = find_question_anchors(pages)
    if not anchors:
        sys.stderr.write("No 'Questão N' anchors found.\n")
        sys.exit(2)

    # 2) render pages to PNG
    with tempfile.TemporaryDirectory() as td:
        run(["pdftoppm", "-png", "-r", str(args.dpi), str(pdf), f"{td}/page"])
        png_pages = sorted(Path(td).glob("page-*.png"))
        if not png_pages:
            sys.stderr.write("pdftoppm produced no PNGs.\n")
            sys.exit(3)
        n_pages = len(png_pages)

        # Precompute effective tops (accounts for tall inline math above title)
        eff_tops = []
        for i, (numero, page_i, y_min, y_max) in enumerate(anchors):
            eff_tops.append(effective_top(pages, page_i, y_min, y_max))

        # 3) for each question, compute crop range and stitch
        manifest = []
        for i, (numero, page_i, _y_min, _y_max) in enumerate(anchors):
            y_top = eff_tops[i]
            has_next = (i + 1 < len(anchors))
            if has_next:
                next_page = anchors[i + 1][1]
                next_y = eff_tops[i + 1]
                if next_page == page_i and next_y <= y_top:
                    next_y = anchors[i + 1][2]  # safety: don't invert
            else:
                last_y = last_text_ymax(pages, n_pages) or (height_pts - 40)
                next_page, next_y = n_pages, last_y

            # Build crop ranges: (page, top, bottom) in PDF points.
            ranges = []
            cur_page = page_i
            cur_top = max(0, y_top - args.margin)
            while cur_page < next_page:
                # take till bottom of this page (with margin), then move to next
                page_bottom = last_text_ymax(pages, cur_page) or (height_pts - 40)
                ranges.append((cur_page, cur_top, min(height_pts, page_bottom + args.margin)))
                cur_page += 1
                cur_top = args.page_top_skip
            # final segment: stop ABOVE the next question's title (or at last text)
            if has_next:
                bot = max(cur_top + 1, next_y - args.margin)
            else:
                bot = min(height_pts, next_y + args.margin)
            ranges.append((cur_page, cur_top, bot))

            parts = []
            for j, (pg, top, bot) in enumerate(ranges):
                src = Path(td) / f"page-{pg}.png"
                if not src.exists():
                    cands = sorted(Path(td).glob(f"page-*{pg}.png"))
                    if not cands:
                        sys.stderr.write(f"missing page {pg}\n")
                        sys.exit(4)
                    src = cands[0]
                part_out = out_dir / f"_tmp_q{numero:02d}_p{j}.png"
                crop_one(src, top, bot, args.dpi, part_out)
                parts.append(part_out)
            final = out_dir / f"q{numero:02d}.png"
            stitch_vertical(parts, final)
            manifest.append({
                "numero": numero,
                "image": final.name,
                "pages": [r[0] for r in ranges],
            })

    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"Extracted {len(manifest)} questions to {out_dir}")


if __name__ == "__main__":
    main()
