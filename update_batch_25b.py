import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(part_index, search_str):
    for s in data[part_index].get('subparts', []):
        if search_str in s['title']:
            return s
    return None

# ============================================================
# Part 117 (index 118) - Le besoin - s592 (page 323)
# ============================================================
p117 = 118
s592 = find_subpart(p117, "592")
if s592:
    s592['hadiths'] = []
    if 'introduction' in s592:
        del s592['introduction']

s592['hadiths'].extend([
    {
        "number": "1787",
        "text": "L'Imām 'Alī (as) a dit : Ô Allah ! Fais que je n'aie pas à solliciter un besoin auprès des mauvais parmi Ta création ; et lorsque Tu fais que j'ai besoin d'une chose, fais que je la sollicite auprès de ceux qui ont le plus beau [et heureux] visage, ceux dont l'âme est la plus généreuse, ceux qui sont les plus éloquents, et ceux qui feront le moins sentir [le bienfait qu'ils ont réalisé].<sup>2035</sup>"
    },
    {
        "number": "1788",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit à celui qui dit en sa présence «Ô Allah, rends-moi indépendant de [tout besoin vis-à-vis de] Tes créatures !» : «Ce n'est pas comme cela qu'il faut dire les choses, car les gens ont besoin les uns des autres. Dis plutôt : «Ô Allah, rends-moi indépendant de [tout besoin vis-à-vis des] mauvais parmi Ta création !»»<sup>2036</sup>"
    },
    {
        "number": "1789",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, le besoin vis-à-vis d'une personne nouvellement riche est comme un dirham dans la gueule d'un serpent : tu en as besoin, mais en même temps elle te met en danger.<sup>2037</sup><br><br><span class=\"hadith-footnote\">(Voir également : La demande (2), section 911)</span>"
    }
])

# ============================================================
# Part 118 (index 119) - La précaution (page 323)
# ============================================================
p118 = 119
s593 = find_subpart(p118, "593")
# Remove the single entry already inserted (1792) and rebuild correctly
s593['hadiths'] = []

s593['hadiths'].extend([
    {
        "number": "1790",
        "text": "L'Imām 'Alī (as) a dit : Ton frère est ta religion, fais preuve de précaution vis-à-vis de ta religion autant que tu le peux.<sup>2038</sup>"
    },
    {
        "number": "1791",
        "text": "L'Imām al-Ṣādiq (as) a dit : Il t'incombe d'être résolu et de faire preuve de précaution vis-à-vis de ta religion.<sup>2039</sup>"
    },
    {
        "number": "1792",
        "text": "L'Imām al-Ṣādiq (as) a dit : Fais preuve de précaution en toute chose que tu as la possibilité de réaliser.<sup>2040</sup>"
    }
])


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done filling hadiths 1787-1792")
