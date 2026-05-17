import json
import re
from pathlib import Path

def apply_gabaritos():
    with open("gabaritos.json", "r") as f:
        gabaritos = json.load(f)

    for materia_dir in ["fisica", "matematica", "quimica", "ingles", "portugues"]:
        p = Path(materia_dir)
        if not p.is_dir(): continue
        
        for md_path in p.glob("prova*.md"):
            # Parse year and fase from filename
            # e.g., prova2008.md -> 2008, f1
            # e.g., prova2019_f1.md -> 2019, f1
            m = re.match(r"prova(\d{4})(?:_f(\d))?", md_path.stem)
            if not m: continue
            
            year = m.group(1)
            fase = int(m.group(2)) if m.group(2) else 1
            
            if fase != 1 and year not in ["2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]:
                # In older years, there was only one phase or phase 1 was the only objective one.
                # Actually, most of these gabaritos are for the objective part.
                # If it's explicitly f2, skip for now unless we know it has objective questions.
                continue

            if year not in gabaritos: continue
            if materia_dir not in gabaritos[year]: continue
            
            year_data = gabaritos[year][materia_dir]
            if not year_data: continue
            
            # Detect offset
            # If file has Q01 but gabarito starts at 13, offset is 12
            g_nums = sorted([int(k) for k in year_data.keys()])
            min_g = g_nums[0]
            
            content = md_path.read_text()
            parts = re.split(r"(## Q\d+)", content)
            
            # Check if we have Q01 or something small
            has_low_q = False
            for i in range(1, len(parts), 2):
                q_num = int(parts[i].replace("## Q", ""))
                if q_num < min_g:
                    has_low_q = True
                    break
            
            offset = (min_g - 1) if has_low_q else 0
            
            for i in range(1, len(parts), 2):
                q_header = parts[i]
                q_num_str = q_header.replace("## Q", "")
                q_num = int(q_num_str) + offset
                
                if str(q_num) in year_data:
                    ans = year_data[str(q_num)]
                    if "**Gabarito:**" not in parts[i+1]:
                        parts[i+1] = re.sub(
                            r"(\*\*Tipo:\*\*\s*.+)",
                            r"\1\n**Gabarito:** " + ans,
                            parts[i+1]
                        )
            
            new_content = "".join(parts)
            
            if new_content != content:
                print(f"Updating {md_path}")
                md_path.write_text(new_content)

if __name__ == "__main__":
    apply_gabaritos()
