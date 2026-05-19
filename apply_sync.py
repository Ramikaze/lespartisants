import re
import os

base_dir = '/Users/rami/.gemini/antigravity/brain/c19c01bf-89e7-4ddf-9caa-e3f8c098d398/.system_generated/steps'

mappings = {
    'dimanche': {
        'md': f'{base_dir}/1181/content.md',
        'map': [[1], [2, 3, 4], [5, 6], [7, 8], [9, 10, 11], [12, 13], [14, 15, 16]]
    },
    'mardi': {
        'md': f'{base_dir}/1182/content.md',
        'map': [[1, 2], [3], [4], [5, 6], [7], [8, 9, 10], [11, 12], [13, 14], [15], [16]]
    },
    'mercredi': {
        'md': f'{base_dir}/1183/content.md',
        'map': [[1], [2, 3], [4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14, 15]]
    },
    'jeudi': {
        'md': f'{base_dir}/1184/content.md',
        'map': [[1, 2], [3, 4, 5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15]]
    },
    'vendredi': {
        'md': f'{base_dir}/1185/content.md',
        'map': [[1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16]]
    },
    'samedi': {
        'md': f'{base_dir}/1186/content.md',
        'map': [[1, 2, 3], [4], [5, 6, 7, 8, 9, 10, 11]]
    }
}

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
            triplets.append({'ar': ar, 'tr': tr})
        i += 1
    return triplets

with open('invocations.html', 'r', encoding='utf-8') as f:
    html = f.read()

for day, info in mappings.items():
    triplets = extract_triplets(info['md'])
    
    # Extract existing French verses
    m = re.search(r'    '+day+r': \{(.*?)\n    \},', html, re.DOTALL)
    if not m:
        continue
    block = m.group(1)
    
    # Replace single quotes properly if needed
    verses_fr = []
    for match in re.finditer(r"\{t:'v',n:\d+,\s*tx:\s*'(.*?)'\}", block):
        verses_fr.append(match.group(1))
    
    if len(verses_fr) != len(info['map']):
        print(f"ERROR on {day}: {len(verses_fr)} FR verses != {len(info['map'])} mapping arrays")
        continue
    
    # Build new body
    new_body = "      body: [\n"
    # Intro
    new_body += "        {t:'tri', ar:'بِسْمِ اللّهِ الرَّحْمنِ الرَّحِيمِ', tr:'Bi-smi-llâhi ar-rahmâni ar-rahîmi', fr:\"Au Nom de Dieu, le Clément, le Très Miséricordieux\"},\n"
    new_body += "        {t:'salawat'},\n"
    
    for i, fr_text in enumerate(verses_fr):
        ar_parts = []
        tr_parts = []
        for chunk_idx in info['map'][i]:
            # chunk_idx is 1-indexed, so -1
            c = triplets[chunk_idx]
            ar_parts.append(c['ar'])
            tr_parts.append(c['tr'])
        
        ar_merged = " ".join(ar_parts).replace("'", "\\'")
        tr_merged = " ".join(tr_parts).replace("'", "\\'")
        # FR text already has escaped single quotes inside, but since we'll wrap in double quotes, we can unescape them
        fr_escaped = fr_text.replace("\\'", "'").replace('"', '\\"')
        
        new_body += f"        {{t:'tri', ar:'{ar_merged}', tr:'{tr_merged}', fr:\"{fr_escaped}\"}},\n"
    
    new_body += "        {t:'salawat'},\n      ]"
    
    # Replace the old body in the block
    old_body_m = re.search(r'      body: \[\n.*?\n      \]', block, re.DOTALL)
    if old_body_m:
        new_block = block[:old_body_m.start()] + new_body + block[old_body_m.end():]
        # Replace the block in HTML
        html = html[:m.start(1)] + new_block + html[m.end(1):]
    else:
        print(f"Could not find body for {day}")

with open('invocations.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Successfully updated invocations.html")

