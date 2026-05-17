import json
import re

def clean_html(raw_html):
    cleantext = re.sub(r'<[^>]+>', ' ', str(raw_html))
    return re.sub(r'\s+', ' ', cleantext).strip()

search_index = []

# ─── 1. chiisme-repond.html ─────────────────────────────────────────────────
try:
    with open("chiisme-repond.html", "r", encoding="utf-8") as f:
        content = f.read()
    # Find the CH array - it ends with ];  at start of line
    match = re.search(r'const CH = (\[.*?\n\]);', content, re.DOTALL)
    if match:
        ch_data = json.loads(match.group(1))
        for i, chap in enumerate(ch_data):
            title = chap.get("title", "")
            text_content = " ".join(s.get("content","") for s in chap.get("sections",[]))
            search_index.append({
                "type": "Chiisme Répond", "title": title,
                "content": clean_html(text_content[:700]),
                "idx": 0, "state": str(i)
            })
        print(f"chiisme-repond: {len(ch_data)} chapitres")
    else:
        print("chiisme-repond: pattern not found")
except Exception as e:
    print(f"Error chiisme: {e}")

# ─── 2. douze-imams.html ────────────────────────────────────────────────────
try:
    with open("douze-imams.html", "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'var IMAMS = \[(.*?)\];\s*\n', content, re.DOTALL)
    if match:
        imams_raw = "[" + match.group(1) + "]"
        imams = json.loads(imams_raw)
        for i, im in enumerate(imams):
            search_index.append({
                "type": "Les 12 Imams",
                "title": im.get("name","") + " (" + im.get("sur","") + ")",
                "content": clean_html(im.get("bio","")) + " " + " ".join(im.get("tags",[])),
                "idx": 12, "state": str(i)
            })
        print(f"douze-imams: {len(imams)} imams")
    else:
        print("douze-imams: pattern not found")
except Exception as e:
    print(f"Error douze-imams: {e}")

# ─── 3. invocations.html ────────────────────────────────────────────────────
try:
    with open("invocations.html", "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'var DATA = (\{.*?\});\s*\n', content, re.DOTALL)
    if match:
        data = json.loads(match.group(1))
        for theme in data.get("themes", []):
            for item in theme.get("items", []):
                if item.get("type") == "header":
                    continue
                item_id = item.get("id","")
                label = item.get("label","")
                search_index.append({
                    "type": "Invocations",
                    "title": label,
                    "content": theme.get("label","") + " " + item.get("emoji",""),
                    "idx": 4, "state": item_id
                })
        print(f"invocations: {len(search_index)} entries so far")
    else:
        print("invocations: DATA pattern not found")
except Exception as e:
    print(f"Error invocations: {e}")

# ─── 4. 99-noms.html (HTML content extraction) ──────────────────────────────
try:
    with open("99-noms.html", "r", encoding="utf-8") as f:
        content = f.read()
    cards = re.findall(
        r'<div class="nom-card">.*?<div class="nom-num">(\d+)</div>.*?<div class="nom-arabic">(.*?)</div>.*?<div class="nom-translit">(.*?)</div>.*?<div class="nom-desc">(.*?)</div>',
        content, re.DOTALL
    )
    for num, ar, translit, desc in cards:
        search_index.append({
            "type": "99 Noms d'Allah",
            "title": f"{ar.strip()} — {translit.strip()}",
            "content": clean_html(desc),
            "idx": 16, "state": num.strip()
        })
    print(f"99-noms: {len(cards)} noms")
except Exception as e:
    print(f"Error 99-noms: {e}")

# ─── 5. aune-sagesse-data.js ────────────────────────────────────────────────
try:
    with open("aune-sagesse-data.js", "r", encoding="utf-8") as f:
        content = f.read()
    # Locate the JSON object
    match = re.search(r'window\.AUNE_DATA\s*=\s*', content)
    if match:
        start = match.end()
        # find balanced braces
        depth = 0; json_start = None; json_end = None
        for ci, ch in enumerate(content[start:], start):
            if ch == '{':
                if json_start is None: json_start = ci
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0: json_end = ci+1; break
        if json_start and json_end:
            data = json.loads(content[json_start:json_end])
            count = 0
            for pi, part in enumerate(data.get("parts",[])):
                p_title = part.get("title","")
                for si, sub in enumerate(part.get("subparts",[])):
                    s_title = sub.get("title","")
                    hadiths_text = " ".join(
                        h.get("text","") for h in sub.get("hadiths",[])[:4]
                    )
                    search_index.append({
                        "type": "Aune de la Sagesse",
                        "title": p_title + " — " + s_title,
                        "content": clean_html(hadiths_text[:600]),
                        "idx": 17, "state": f"{pi},{si}"
                    })
                    count += 1
            print(f"aune-sagesse: {count} sections")
    else:
        print("aune-sagesse: AUNE_DATA not found")
except Exception as e:
    print(f"Error aune: {e}")

# ─── 6. Article & other static pages ────────────────────────────────────────
static_pages = [
    {"file": "article-connaissance.html", "idx": 7, "type": "Connaissance & Raison"},
    {"file": "usul-al-din.html", "idx": 9, "type": "Usul al-Din"},
    {"file": "tawheed.html", "idx": 13, "type": "Al-Tawhid"},
    {"file": "nubuwwa.html", "idx": 14, "type": "Al-Nubuwwa & Imāmah"},
    {"file": "resister.html", "idx": 15, "type": "Résister"},
    {"file": "hadith-kisa.html", "idx": 10, "type": "Hadith al-Kisa'"},
    {"file": "chronologie.html", "idx": 1, "type": "Chronologie"},
    {"file": "verset-trone.html", "idx": 2, "type": "Verset du Trône"},
]
for finfo in static_pages:
    try:
        with open(finfo["file"], "r", encoding="utf-8") as f:
            raw = f.read()
        heads = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', raw, re.DOTALL)
        paras = re.findall(r'<p[^>]*>(.*?)</p>', raw, re.DOTALL)
        text = " ".join(clean_html(h) for h in heads[:15]) + " " + " ".join(clean_html(p) for p in paras[:20])
        search_index.append({
            "type": finfo["type"], "title": finfo["type"],
            "content": text[:900],
            "idx": finfo["idx"], "state": ""
        })
        print(f"{finfo['file']}: 1 entry")
    except Exception as e:
        print(f"Error {finfo['file']}: {e}")

# ─── Write output ────────────────────────────────────────────────────────────
with open("global-search-data.js", "w", encoding="utf-8") as f:
    f.write("window.GLOBAL_SEARCH_INDEX = ")
    json.dump(search_index, f, ensure_ascii=False)
    f.write(";\n")

print(f"\n✅  Total: {len(search_index)} entries → global-search-data.js")
