import re
import os
import json

base_dir = '/Users/rami/.gemini/antigravity/brain/c19c01bf-89e7-4ddf-9caa-e3f8c098d398/.system_generated/steps'

def extract_triplets(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()
    
    lines = md.split('\n')
    triplets = []
    in_prayer = False
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if 'بِسْمِ اللّهِ الرَّحْمنِ الرَّحِيمِ' in line or 'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ' in line or 'بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّحِيمِ' in line:
            in_prayer = True
            
        if not in_prayer:
            i += 1
            continue
            
        if 'Donate !' in line or 'Rejoignez-nous' in line or '[Donate !]' in line or 'Boutique' in line:
            break
            
        if re.search(r'[\u0600-\u06FF]', line):
            ar = line
            tr = ""
            fr = ""
            if i + 1 < len(lines):
                tr_cand = lines[i+1].strip()
                if tr_cand and not re.search(r'[\u0600-\u06FF]', tr_cand):
                    tr = tr_cand
                    if i + 2 < len(lines):
                        fr_cand = lines[i+2].strip()
                        if fr_cand and not re.search(r'[\u0600-\u06FF]', fr_cand):
                            fr = fr_cand
            triplets.append({'ar': ar, 'tr': tr, 'fr': fr})
        i += 1
    return triplets

for day, md_path in [
    ('dimanche', f'{base_dir}/1181/content.md'),
    ('mardi', f'{base_dir}/1182/content.md'),
    ('mercredi', f'{base_dir}/1183/content.md'),
    ('jeudi', f'{base_dir}/1184/content.md'),
    ('vendredi', f'{base_dir}/1185/content.md'),
    ('samedi', f'{base_dir}/1186/content.md')
]:
    t = extract_triplets(md_path)
    print(f"\n================ {day.upper()} ================")
    for idx, tr in enumerate(t):
        print(f"[{idx}] FR_cand: {tr['fr']}")
