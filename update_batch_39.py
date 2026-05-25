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
# Part 160 (index 161) - LA SUBSISTANCE (2547-2554, 2560-2566)
# ============================================================
p160 = 161

# Subpart 814 - La garantie de la subsistance (2547-2551)
s814 = find_subpart(p160, "814"); eh(s814)
s814['hadiths'].extend([
    {
        "number": "2547",
        "text": "L'Imām 'Alī (as) a dit : Tout être vivant a une nourriture [qui lui est assignée].<sup>2879</sup>"
    },
    {
        "number": "2548",
        "text": "L'Imām 'Alī (as) a dit : Celui-ci est un corbeau et celui-là un aigle ; celle-ci est une colombe et celle-là une autruche. Il a appelé chaque oiseau par son nom et Il a garanti à chacun sa subsistance.<sup>2880</sup>"
    },
    {
        "number": "2549",
        "text": "L'Imām 'Alī (as) a dit : Ses créatures sont à Sa charge, Il leur a garanti leur subsistance et Il leur a assigné leur nourriture.<sup>2881</sup>"
    },
    {
        "number": "2550",
        "text": "L'Imām 'Alī (as) a dit : Allez à la quête de votre subsistance, car elle a été garantie à celui qui est à sa quête.<sup>2882</sup>"
    },
    {
        "number": "2551",
        "text": "L'Imām al-'Askarī (as) a dit : Que la [préoccupation] pour la subsistance qui est garantie ne te détourne pas de l'accomplissement d'un acte obligatoire.<sup>2883</sup>"
    }
])

# Subpart 815 - L'avidité et l'accroissement de la subsistance (2552-2554)
s815 = find_subpart(p160, "815"); eh(s815)
s815['hadiths'].extend([
    {
        "number": "2552",
        "text": "Le Messager d'Allah (s) a dit : En vérité, la subsistance ne peut être attirée par l'avidité de la personne avide ni repoussée par la répugnance d'une personne répugnante.<sup>2884</sup>"
    },
    {
        "number": "2553",
        "text": "L'Imām 'Alī (as) a dit : Sachez que même si un serviteur est dénué de perspicacité et doté de peu de ruse, cela ne réduira pas la subsistance qu'Allah lui a assignée, alors que même si un serviteur est très perspicace et doté d'une grande ruse, cela n'augmentera pas ce qu'Allah lui a assigné.<sup>2885</sup>"
    },
    {
        "number": "2554",
        "text": "L'Imām al-Ṣādiq (as) a dit : Étant donné que la subsistance est assignée, pourquoi donc faire preuve d'avidité ?!<sup>2886</sup>"
    }
])

# Subpart 817 - La subsistance et celui qui la recherche (2560-2562)
s817 = find_subpart(p160, "817"); eh(s817)
s817['hadiths'].extend([
    {
        "number": "2560",
        "text": "L'Imām 'Alī (as) a dit : La subsistance cherche celui qui n'est pas à sa recherche.<sup>2892</sup>"
    },
    {
        "number": "2561",
        "text": "L'Imām 'Alī (as) a dit : Il y a deux sortes de subsistances : une subsistance que tu cherches, et une subsistance qui te cherche. Ainsi, même si tu ne viens pas à elle, elle viendra à toi.<sup>2893</sup>"
    },
    {
        "number": "2562",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant a placé la subsistance des croyants là où ils ne l'attendent pas ; ceci parce que lorsque le serviteur ignore où se trouve sa subsistance, il multiplie ses invocations.<sup>2894</sup>"
    }
])

# Subpart 818 - Le fait de se soucier de sa subsistance du lendemain (2563-2564)
s818 = find_subpart(p160, "818"); eh(s818)
s818['hadiths'].extend([
    {
        "number": "2563",
        "text": "Le Messager d'Allah (s) a dit : Ne te soucie guère de la subsistance de demain, car chaque jour arrive avec sa propre subsistance.<sup>2895</sup>"
    },
    {
        "number": "2564",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui se soucie de sa subsistance, cela sera inscrit pour lui comme péché.<sup>2896</sup>"
    }
])

# Subpart 819 - L'impatience vis-à-vis de l'arrivée de la subsistance (2565-2566)
s819 = find_subpart(p160, "819"); eh(s819)
s819['hadiths'].extend([
    {
        "number": "2565",
        "text": "Le Messager d'Allah (s) a dit : Allah - loué soit le Très-Haut - a dit : «Que Mon serviteur soit prévenu que s'il est impatient vis-à-vis de l'arrivée de Ma subsistance, Je Me mettrai en colère et ouvrirai devant lui la porte de [l'attachement à] ce monde.»<sup>2897</sup>"
    },
    {
        "number": "2566",
        "text": "Le Messager d'Allah (s) a dit : Que celui à qui Allah le Très-Haut accorde une grâce Le loue, et que celui qui est impatient vis-à-vis de [l'arrivée de] la subsistance implore le pardon d'Allah.<sup>2898</sup>"
    }
])

# ============================================================
# Sequential Sorting for all modified subparts
# ============================================================
modified_sections = [
    (p160, "814"), (p160, "815"), (p160, "817"), (p160, "818"), (p160, "819")
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

print("✅ Data successfully saved! Hadiths 2547-2554 and 2560-2566 injected.")
