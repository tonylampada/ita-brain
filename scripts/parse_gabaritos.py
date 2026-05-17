import re
import subprocess
import json
from pathlib import Path

MATERIA_MAP = {
    "Física": "fisica",
    "Inglês": "ingles",
    "Português": "portugues",
    "Matemática": "matematica",
    "Química": "quimica"
}

def extract_text(pdf_path):
    r = subprocess.run(["pdftotext", "-layout", str(pdf_path), "-"], capture_output=True, text=True)
    return r.stdout

def parse_gabarito(text):
    lines = text.splitlines()
    
    header_line = None
    for i, line in enumerate(lines):
        if any(m in line for m in MATERIA_MAP.keys()):
            header_line = i
            break
    
    if header_line is None:
        return {}

    headers = []
    for m_pt, m_en in MATERIA_MAP.items():
        start = lines[header_line].find(m_pt)
        if start != -1:
            headers.append({"name": m_en, "start": start, "pt": m_pt})
    
    headers.sort(key=lambda x: x["start"])
    
    results = {h["name"]: {} for h in headers}
    
    # Extract pairs: (number, answer, start_pos)
    # Pattern: Digit(s) followed by Answer (A-E or *)
    # Some have (*) or (**) or (1)
    pair_re = re.compile(r"(\d+)\s+(?:\([^)]+\)\s+)?([A-E*]|\(\*\*?\))")
    
    for line in lines[header_line+1:]:
        if not line.strip(): continue
        if "anulada" in line.lower(): continue
        
        for m in pair_re.finditer(line):
            num = int(m.group(1))
            ans = m.group(2)
            pos = m.start()
            
            if "*" in ans:
                ans = "ANULADA"
            
            # Assign to closest header
            closest = min(headers, key=lambda h: abs(h["start"] + len(h["pt"])//2 - pos))
            results[closest["name"]][num] = ans

    return results

def main():
    inbox = Path("_inbox")
    all_data = {}
    for f in sorted(inbox.glob("gabarito_*.pdf")):
        year = f.stem.split("_")[1]
        print(f"Parsing {f}...")
        text = extract_text(f)
        data = parse_gabarito(text)
        all_data[year] = data
    
    with open("gabaritos.json", "w") as f:
        json.dump(all_data, f, indent=2)

if __name__ == "__main__":
    main()
