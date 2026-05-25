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
# Part 119 (index 120) - La vie - hadith 1797 manquant
# ============================================================
p119 = 120
s597 = find_subpart(p119, "597")
s597['hadiths'].append({
    "number": "1797",
    "text": "L'Imām 'Alī (as) a dit : Le monothéisme est la vie de l'âme.<sup>2046</sup>"
})

# ============================================================
# Part 120 (index 121) - Les animaux (page 325)
# ============================================================
p120 = 121
s598 = find_subpart(p120, "598")
# Keep only hadiths already inserted (if any pre-existing), otherwise clear
s598['hadiths'] = []

s598['hadiths'].extend([
    {
        "number": "1798",
        "text": "Le Messager d'Allah (s) a dit en voyant une chamelle attachée alors que sa charge était encore sur son dos : Où est son propriétaire ? Dites-lui de se préparer au procès [concernant cette chamelle] demain [au Jour de la Résurrection].<sup>2047</sup>"
    },
    {
        "number": "1799",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime la douceur et Il aide à son application. Ainsi, lorsque vous montez une bête maigre, descendez-en à un endroit approprié. Si le sol est aride, éloignez-vous en, et si la terre est verdoyante, mettez pied à terre [et laissez-la s'y reposer].<sup>2048</sup>"
    },
    {
        "number": "1800",
        "text": "Le Messager d'Allah (s) a dit : Montez les bêtes en bonne santé et gardez-les en bonne santé. Lors de vos discussions, ne les utilisez pas comme des chaises dans les rues et les marchés, car il se peut que la bête montée soit meilleure que celui qui la monte et pratique davantage le rappel d'Allah le Béni et le Très-Haut que lui.<sup>2049</sup>"
    },
    {
        "number": "1801",
        "text": "Le Messager d'Allah (s) a dit : La bête a six droits sur son propriétaire : ce dernier doit l'autoriser à paître lorsqu'il met pied à terre, l'abreuver lorsqu'il passe près d'une source d'eau, ne pas la frapper sauf si elle le mérite vraiment, ne pas lui faire porter ce qu'elle ne peut supporter, ne pas l'engager dans un voyage qu'elle ne peut supporter, et ne pas rester assis sur elle de façon trop longue.<sup>2050</sup>"
    }
])


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1797-1801")
