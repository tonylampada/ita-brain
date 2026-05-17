#!/usr/bin/env python3
"""
Build banco_questoes.jsonl and taxonomia.md from all prova{...}.md files.

Reads every `<materia>/prova*.md` under the brain root, parses each question
block, and rewrites both index files. The .md files are the source of truth;
this script makes the index files always reflect them.

Usage:
    build_index.py [brain_root]   # default: ./
"""
import json
import re
import sys
from pathlib import Path

MATERIAS = ["matematica", "fisica", "quimica", "ingles", "portugues", "redacao"]
MATERIA_SHORT = {
    "matematica": "mat", "fisica": "fis", "quimica": "qui",
    "ingles": "ing", "portugues": "por", "redacao": "red",
}

# parse filename: prova{YEAR}.md or prova{YEAR}_f2.md
PROVA_RE = re.compile(r"^prova(\d{4})(?:_f(\d))?\.md$")
# question block: ## Q01 ... until next ## or EOF
QBLOCK_RE = re.compile(r"^## Q(\d+)\s*$", re.MULTILINE)


def parse_prova(md_path: Path, materia: str, ano: int, fase: int):
    text = md_path.read_text()
    matches = list(QBLOCK_RE.finditer(text))
    out = []
    for i, m in enumerate(matches):
        numero = int(m.group(1))
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]

        def field(name):
            mm = re.search(rf"\*\*{name}:\*\*\s*(.+)", block)
            return mm.group(1).strip() if mm else None

        assunto = field("Assunto") or ""
        comps_raw = field("Compet[êe]ncias") or ""
        tipo = field("Tipo") or ""
        gabarito = field("Gabarito")
        tema = field("Tema")
        genero = field("G[êe]nero")

        comps = [c.strip() for c in comps_raw.split(",") if c.strip()]
        tipo_slug = (
            "multipla_escolha" if "ltipla" in tipo
            else "discursiva" if "discursiva" in tipo
            else "redacao" if "reda" in tipo
            else tipo.lower().replace(" ", "_")
        )

        qid = f"{MATERIA_SHORT[materia]}-{ano}-f{fase}-q{numero:02d}"
        rec = {
            "id": qid,
            "materia": materia,
            "ano": ano,
            "fase": fase,
            "numero": numero,
            "assunto": assunto,
            "competencias": comps,
            "tipo": tipo_slug,
            "imagem": f"{materia}/{md_path.stem}/q{numero:02d}.png",
            "arquivo": f"{materia}/{md_path.name}",
        }
        if gabarito:
            rec["gabarito"] = gabarito
        if tema:
            rec["tema"] = tema
        if genero:
            rec["genero"] = genero
        out.append(rec)
    return out


def collect_all(root: Path):
    all_q = []
    for materia in MATERIAS:
        mdir = root / materia
        if not mdir.is_dir():
            continue
        for md in sorted(mdir.glob("prova*.md")):
            m = PROVA_RE.match(md.name)
            if not m:
                continue
            ano = int(m.group(1))
            fase = int(m.group(2)) if m.group(2) else 1
            all_q.extend(parse_prova(md, materia, ano, fase))
    return all_q


def write_jsonl(records, out_path: Path):
    with out_path.open("w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def build_taxonomy(records):
    """Group by materia → assunto → competencia → [qids]."""
    tax = {}
    for r in records:
        m, a = r["materia"], r["assunto"] or "(sem assunto)"
        tax.setdefault(m, {}).setdefault(a, {})
        for c in r["competencias"] or ["(sem competência)"]:
            tax[m][a].setdefault(c, []).append(r["id"])
    return tax


def write_taxonomy(tax, materias_order, out_path: Path):
    lines = ["# Taxonomia ITA — Assuntos & Competências", "",
             "> Catálogo vivo dos assuntos e competências observados nas provas do ITA. ",
             "> Gerado automaticamente por `scripts/build_index.py` a partir dos arquivos `prova*.md`.", ""]
    for m in materias_order:
        title = m.capitalize()
        if m == "matematica":
            title = "Matemática"
        elif m == "fisica":
            title = "Física"
        elif m == "quimica":
            title = "Química"
        elif m == "ingles":
            title = "Inglês"
        elif m == "portugues":
            title = "Português"
        elif m == "redacao":
            title = "Redação"
        lines.append(f"## {title}")
        lines.append("")
        if m not in tax or not tax[m]:
            lines.append("_(vazio)_")
            lines.append("")
            continue
        for assunto in sorted(tax[m].keys()):
            lines.append(f"### {assunto}")
            for comp in sorted(tax[m][assunto].keys()):
                qids = tax[m][assunto][comp]
                refs = ", ".join(f"[[{q}]]" for q in qids)
                lines.append(f"- {comp} — {refs}")
            lines.append("")
    out_path.write_text("\n".join(lines))


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    records = collect_all(root)
    write_jsonl(records, root / "banco_questoes.jsonl")
    tax = build_taxonomy(records)
    write_taxonomy(tax, MATERIAS, root / "taxonomia.md")
    print(f"Indexed {len(records)} questions across {len({r['materia'] for r in records})} matérias")


if __name__ == "__main__":
    main()
