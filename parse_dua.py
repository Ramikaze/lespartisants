import re
import json

with open('dua_simaat_extracted.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove headers and footers
text = re.sub(r'(?m)^DUA AS’SIMAT\s*$', '', text)
text = re.sub(r'(?m)^L\'INVOCATION DES MARQUES\s*$', '', text)
text = re.sub(r'(?m)^Les Partisans des Ahlul Beyt.*$', '', text)
text = re.sub(r'(?m)^« Le du’a est l’arme du croyant.*$', '', text)
text = re.sub(r'(?m)^des cieux et de la terre\.\s*»\s*$', '', text)
text = re.sub(r'(?m)^Imam Ali ibn Abi Taleb\s*$', '', text)
text = re.sub(r'(?m)^QU’EST QUE LA DUA AL’SIMAT.*$', '', text)
text = re.sub(r'(?m)^CONTENU.*$', '', text)
text = re.sub(r'(?m)^L’INVOCATION AL’SIMAT.*$', '', text)
text = re.sub(r'(?m)^SO MMAIRE.*$', '', text)
text = re.sub(r'(?m)^\d+\s*$', '', text)
text = re.sub(r'(?m)^Du`a Al Simat\s*$', '', text)
text = re.sub(r'(?m)^Pour l’amour de nos Ahlul Beyt \(as\)\s*$', '', text)
text = re.sub(r'(?m)^Nous vous avons traduit la Dua Simat\s*$', '', text)

lines = [l.strip() for l in text.split('\n') if l.strip()]

intro = []
body = []

idx = 0
while idx < len(lines):
    if "ﻋَﲆ  ﺑِﻪِ  دُﻋﯿﺖَ" in lines[idx] or "اﻟﻠﻬُﻢﱠ" in lines[idx] and is_arabic(lines[idx]):
        break
    # Check if Arabic
    if len(re.findall(r'[\u0600-\u06FF]', lines[idx])) > len(lines[idx]) * 0.3:
        break
    intro.append(lines[idx])
    idx += 1

def is_arabic(text):
    return len(re.findall(r'[\u0600-\u06FF]', text)) > len(text) * 0.2

# We will group by Arabic, Translit, French
# Instructions:
instr_keywords = ["-Ensuite,", "Je dis :", "Ensuite dire :", "Il est recommandé de dire"]

while idx < len(lines):
    l = lines[idx]
    
    is_instr = any(l.startswith(k) for k in instr_keywords) or "Evoquer son besoin" in l
    
    if is_instr:
        body.append({'t': 'instruction', 'tx': l})
        idx += 1
        continue
        
    if is_arabic(l):
        ar = []
        while idx < len(lines) and is_arabic(lines[idx]):
            ar.append(lines[idx])
            idx += 1
        
        tr = []
        while idx < len(lines) and not is_arabic(lines[idx]) and not any(lines[idx].startswith(k) for k in instr_keywords) and not "Mon Dieu" in lines[idx] and not "l’ensemble" in lines[idx] and not "Agis avec moi" in lines[idx] and not "Tu as retenu" in lines[idx] and not "par Tes Mots" in lines[idx] and not "l’ensemble des créatures" in lines[idx] and not "par Ta Grandeur" in lines[idx] and not "dont Tu as comblé" in lines[idx] and not "la plus Noble" in lines[idx] and not "par laquelle" in lines[idx] and not "je Te demande" in lines[idx] and not "Ô Dieu" in lines[idx] and not "Evoquer son besoin" in lines[idx]:
            # Simple heuristic: French parts usually start with translation phrases or have typical French sentences.
            # Actually, looking at the text, the TR is always Latin text that is NOT French.
            # Let's just collect until we hit French.
            # French starts with "Mon Dieu", "la plus Noble", "et par Ta Parole", "par laquelle", "je Te demande", "Tu as retenu", "par Tes Mots", "l'ensemble", "par Ta Grandeur", "dont Tu as comblé", "Agis avec", "Ô Dieu", "Evoquer"
            tr.append(lines[idx])
            idx += 1
            
        fr = []
        while idx < len(lines) and not is_arabic(lines[idx]) and not any(lines[idx].startswith(k) for k in instr_keywords):
            fr.append(lines[idx])
            idx += 1
            
        body.append({
            't': 'tri',
            'ar': ' '.join(ar),
            'tr': ' '.join(tr),
            'fr': ' '.join(fr)
        })
    else:
        idx += 1

out = "    'dua-simaat': {\n"
out += "      source: 'Du\\'â as-Simât',\n"
out += "      title: 'L\\'Invocation des Marques (as-Simât)',\n"
out += "      subtitle: 'A réciter dans les dernières heures du vendredi',\n"
out += "      body: [\n"

# Add intro as prose
if intro:
    out += "        {t:'intro', tx:'Introduction'},\n"
    for p in intro:
        if p == "Qu’est que la Dua Al’simat": continue
        out += f"        {repr(p)},\n"

out += "        {t:'intro', tx:'Invocation as-Simât'},\n"

for b in body:
    if b['t'] == 'instruction':
        out += f"        {{t:'instruction', tx:{repr(b['tx'] )}}},\n"
    elif b['t'] == 'tri':
        out += "        {t:'tri', "
        if b['ar']: out += f"ar:{repr(b['ar'])}, "
        if b['tr']: out += f"tr:{repr(b['tr'])}, "
        if b['fr']: out += f"fr:{repr(b['fr'])}"
        out += "},\n"

out += "      ]\n"
out += "    },\n"

with open('dua_simaat_parsed.js', 'w', encoding='utf-8') as f:
    f.write(out)

print("Done")
