import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(pi, ss):
    for s in data[pi].get('subparts', []):
        if ss in s['title']:
            return s
    return None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# Part 160 (index 161) - LA SUBSISTANCE (2555-2559)
# ============================================================
p160 = 161

# Subpart 815 - L'avidité et l'accroissement de la subsistance (2555)
s815 = find_subpart(p160, "815"); eh(s815)
s815['hadiths'].extend([
    {
        "number": "2555",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Très-Haut a distribué abondamment la subsistance même aux sots, afin que les personnes intelligentes en tirent une leçon et sachent que la richesse de ce monde ne s'obtient pas par le travail ni par la ruse.<sup>2887</sup>"
    }
])

# Subpart 816 - L'incitation à rechercher sa subsistance par des moyens honnêtes (2556-2558)
s816 = find_subpart(p160, "816"); eh(s816)
s816['hadiths'].extend([
    {
        "number": "2556",
        "text": "Le Messager d'Allah (s) a dit : En vérité, l'Esprit probe [Gabriel] m'a inspiré qu'aucune âme ne mourra avant d'avoir reçu la totalité de la subsistance [qui lui a été destinée dans ce monde]. Craignez donc Allah et recherchez votre subsistance par des moyens honnêtes, et ne laissez pas un retard dans l'octroi de la subsistance vous conduire à la rechercher de manière illicite car en vérité, ce qu'il y a auprès d'Allah n'est atteint qu'en Lui obéissant.<sup>2888</sup>"
    },
    {
        "number": "2557",
        "text": "L'Imām 'Alī (as) a dit : Prends de la vie de ce monde ce qui vient à toi, et détourne-toi de ce qui se détourne de toi [ce qui ne t'est pas destiné]. Et si tu n'agis pas ainsi, recherche au moins ta subsistance avec des moyens honnêtes.<sup>2889</sup>"
    },
    {
        "number": "2558",
        "text": "L'Imām al-Ṣādiq (as) a dit : Que ta quête de la subsistance ne soit pas comme le gain du gaspilleur, ni comme la quête du cupide qui aime ce monde et en dépend. Reviens plutôt au niveau de la modération et de la chasteté, élève-toi au-dessus du niveau de l'incapacité et de la faiblesse, et cherche à gagner tes revenus de la façon dont doit le faire un croyant.<sup>2890</sup>"
    }
])

# Subpart 817 - La subsistance et celui qui la recherche (2559)
s817 = find_subpart(p160, "817"); eh(s817)
s817['hadiths'].extend([
    {
        "number": "2559",
        "text": "Le Messager d'Allah (s) a dit : Si l'homme fuyait sa subsistance comme il fuit la mort, elle l'atteindrait néanmoins tout comme l'atteint la mort.<sup>2891</sup>"
    }
])

# ============================================================
# Sequential Sorting for modified subparts
# ============================================================
modified_sections = [
    (p160, "815"), (p160, "816"), (p160, "817")
]

for p_idx, s_title in modified_sections:
    s = find_subpart(p_idx, s_title)
    if s and 'hadiths' in s:
        s['hadiths'].sort(key=lambda h: int(h['number']))
        print(f"Sorted Subpart {s_title} (Part index {p_idx}). Hadiths: {[h['number'] for h in s['hadiths']]}")

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Data successfully saved! Hadiths 2555-2559 injected.")
