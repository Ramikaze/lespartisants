import json
import re

files = [
    {"file": "chiisme-repond.html", "idx": 0},
    {"file": "chronologie.html", "idx": 1},
    {"file": "verset-trone.html", "idx": 2},
    {"file": "arbre-genealogique.html", "idx": 3},
    {"file": "invocations.html", "idx": 4},
    {"file": "bibliotheque.html", "idx": 5},
    {"file": "videos.html", "idx": 6},
    {"file": "article-connaissance.html", "idx": 7},
    {"file": "coran-lecture.html", "idx": 8},
    {"file": "usul-al-din.html", "idx": 9},
    {"file": "hadith-kisa.html", "idx": 10},
    {"file": "verset-apprentissage.html", "idx": 11},
    {"file": "douze-imams.html", "idx": 12},
    {"file": "tawheed.html", "idx": 13},
    {"file": "nubuwwa.html", "idx": 14},
    {"file": "resister.html", "idx": 15},
    {"file": "99-noms.html", "idx": 16},
    {"file": "aune-sagesse.html", "idx": 17}
]

search_index = []

def clean_html(raw_html):
    cleantext = re.sub(r'<[^>]+>', ' ', raw_html)
    return re.sub(r'\s+', ' ', cleantext).strip()

# Parse chiisme-repond.html
try:
    with open("chiisme-repond.html", "r", encoding="utf-8") as f:
        content = f.read()
        match = re.search(r'const CH = (\[.*\]);', content, re.DOTALL)
        if match:
            ch_data = json.loads(match.group(1))
            for i, chap in enumerate(ch_data):
                title = chap.get("title", "")
                text_content = ""
                for sec in chap.get("sections", []):
                    text_content += sec.get("content", "") + " "
                search_index.append({
                    "type": "Chiisme Répond", "title": title,
                    "content": clean_html(text_content[:600]),
                    "idx": 0, "state": str(i)
                })
            print(f"chiisme-repond: {len(ch_data)} chapitres")
except Exception as e:
    print(f"Error chiisme: {e}")

# Parse aune-sagesse-data.js 
try:
    with open("aune-sagesse-data.js", "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'window\.AUNE_DATA\s*=\s*\{', content)
    if match:
        # Find the variable assignment and parse it
        idx_start = match.start()
        idx_eq = content.index('=', idx_start) + 1
        # Extract the JSON structure
        brace_depth = 0
        idx_json_start = None
        idx_json_end = None
        for ci, ch in enumerate(content[idx_eq:], idx_eq):
            if ch == '{':
                if idx_json_start is None:
                    idx_json_start = ci
                brace_depth += 1
            elif ch == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    idx_json_end = ci + 1
                    break
        if idx_json_start and idx_json_end:
            data = json.loads(content[idx_json_start:idx_json_end])
            count = 0
            for pi, part in enumerate(data.get("parts", [])):
                p_title = part.get("title", "")
                for si, sub in enumerate(part.get("subparts", [])):
                    s_title = sub.get("title", "")
                    hadiths_text = ""
                    for h in sub.get("hadiths", [])[:5]:
                        hadiths_text += h.get("text", "") + " "
                    search_index.append({
                        "type": "Aune de la Sagesse", 
                        "title": p_title + " — " + s_title,
                        "content": clean_html(hadiths_text[:700]),
                        "idx": 17, "state": f"{pi},{si}"
                    })
                    count += 1
            print(f"aune-sagesse: {count} sections")
except Exception as e:
    print(f"Error aune: {e}")

# Parse douze-imams
try:
    with open("douze-imams.html", "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'const IMAMS\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not match:
        match = re.search(r'const imams\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not match:
        # Try to find any array with imam data
        match = re.search(r'IMAMS_DATA\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if match:
        imams = json.loads(match.group(1))
        for i, im in enumerate(imams):
            name = im.get("name", im.get("nom", ""))
            bio = im.get("bio", im.get("desc", ""))
            search_index.append({
                "type": "Les 12 Imams", "title": name,
                "content": clean_html(bio[:600]),
                "idx": 12, "state": str(i)
            })
        print(f"douze-imams: {len(imams)} imams")
    else:
        print("douze-imams: no match found")
except Exception as e:
    print(f"Error douze-imams: {e}")

# Parse 99 noms
try:
    with open("99-noms.html", "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'const NAMES\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not match:
        match = re.search(r'const noms\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if match:
        noms = json.loads(match.group(1))
        for i, n in enumerate(noms):
            fr = n.get("fr", n.get("name", ""))
            ar = n.get("ar", "")
            desc = n.get("desc", n.get("meaning", ""))
            search_index.append({
                "type": "99 Noms d'Allah", "title": ar + " — " + fr,
                "content": clean_html(desc),
                "idx": 16, "state": str(i)
            })
        print(f"99-noms: {len(noms)} noms")
    else:
        print("99-noms: no match found")
except Exception as e:
    print(f"Error 99-noms: {e}")

# Parse invocations
try:
    with open("invocations.html", "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'const INVS\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not match:
        match = re.search(r'const INVOCATIONS\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if match:
        invs = json.loads(match.group(1))
        for i, inv in enumerate(invs):
            title = inv.get("title", "")
            content_text = inv.get("subtitle", "") + " " + inv.get("intro", "") + " " + inv.get("content", "")[:400]
            search_index.append({
                "type": "Invocations", "title": title,
                "content": clean_html(content_text),
                "idx": 4, "state": str(i)
            })
        print(f"invocations: {len(invs)} invocations")
    else:
        print("invocations: no match found for data")
except Exception as e:
    print(f"Error invocations: {e}")

# Parse Hadith Kisa
try:
    with open("hadith-kisa.html", "r", encoding="utf-8") as f:
        content = f.read()
    # Extract text from the HTML
    body_match = re.search(r'<body[^>]*>(.*)</body>', content, re.DOTALL)
    if body_match:
        body_text = clean_html(body_match.group(1))[:1000]
        search_index.append({
            "type": "Hadith al-Kisa", "title": "Hadith al-Kisa'",
            "content": body_text,
            "idx": 10, "state": ""
        })
        print("hadith-kisa: 1 entry")
except Exception as e:
    print(f"Error hadith-kisa: {e}")

# Parse articles / others (text body extraction)
for finfo in [
    {"file": "article-connaissance.html", "idx": 7, "type": "Connaissance & Raison"},
    {"file": "usul-al-din.html", "idx": 9, "type": "Usul al-Din"},
    {"file": "tawheed.html", "idx": 13, "type": "Al-Tawhid"},
    {"file": "nubuwwa.html", "idx": 14, "type": "Al-Nubuwwa"},
    {"file": "resister.html", "idx": 15, "type": "Résister"},
]:
    try:
        with open(finfo["file"], "r", encoding="utf-8") as f:
            content = f.read()
        # Extract paragraphs
        paras = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
        text = " ".join(clean_html(p) for p in paras[:20])
        # Extract headings
        heads = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', content, re.DOTALL)
        heads_text = " ".join(clean_html(h) for h in heads[:10])
        search_index.append({
            "type": finfo["type"], "title": finfo["type"],
            "content": (heads_text + " " + text)[:800],
            "idx": finfo["idx"], "state": ""
        })
        print(f"{finfo['file']}: 1 entry")
    except Exception as e:
        print(f"Error {finfo['file']}: {e}")

with open("global-search-data.js", "w", encoding="utf-8") as f:
    f.write("window.GLOBAL_SEARCH_INDEX = ")
    json.dump(search_index, f, ensure_ascii=False)
    f.write(";\n")

print(f"\nTotal: {len(search_index)} entries in global-search-data.js")
