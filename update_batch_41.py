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
# Part 160 (index 161) - LA SUBSISTANCE (cont.)
# ============================================================
p160 = 161

# Subpart 820 - Ce qui fait venir la subsistance et qui l'augmente (2576-2579)
s820 = find_subpart(p160, "820"); eh(s820)
s820['hadiths'].extend([
    {
        "number": "2576",
        "text": "L'Imām al-Bāqir (as) a dit : L'aumône (zakāt) accroît la subsistance.<sup>2909</sup>"
    },
    {
        "number": "2577",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui a été particulièrement bienfaisant envers sa famille verra sa subsistance augmenter.<sup>2910</sup>"
    },
    {
        "number": "2578",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la bienfaisance augmente la subsistance.<sup>2911</sup>"
    },
    {
        "number": "2579",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le bon caractère augmente la subsistance.<sup>2912</sup>"
    }
])

# Subpart 821 - Ce qui coupe la subsistance (2580-2582)
s821 = find_subpart(p160, "821"); eh(s821)
s821['hadiths'].extend([
    {
        "number": "2580",
        "text": "Le Messager d'Allah (s) a dit : Allah interdit la bénédiction de la subsistance à celui qui a privé son frère musulman de l'un de ses droits, sauf s'il se repent.<sup>2913</sup>"
    },
    {
        "number": "2581",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, lorsque le serviteur commet un péché, sa subsistance lui échappe.<sup>2914</sup>"
    },
    {
        "number": "2582",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le gain de nombreux bénéfices illicites coupe la subsistance.<sup>2915</sup><br>(Voir également : 41. La bénédiction, section 235)"
    }
])

# Subpart 822 - L'incitation à rechercher [la subsistance] par des moyens licites (2583-2590)
s822 = find_subpart(p160, "822"); eh(s822)
s822['hadiths'].extend([
    {
        "number": "2583",
        "text": "Le Messager d'Allah (s) a dit : L'adoration est constituée de dix parties, dont neuf sont liées à la quête d'une subsistance licite.<sup>2916</sup>"
    },
    {
        "number": "2584",
        "text": "Le Messager d'Allah (s) a dit : Celui qui travaille dur en vue [de pourvoir aux besoins] de sa famille [de façon licite] est comme le combattant (mujāhid) dans le sentier d'Allah.<sup>2917</sup>"
    },
    {
        "number": "2585",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Très-Haut aime voir Son serviteur épuisé dans sa quête d'une subsistance licite.<sup>2918</sup>"
    },
    {
        "number": "2586",
        "text": "Le Messager d'Allah (s) a dit : La quête de la subsistance licite est un devoir pour tout musulman et musulmane.<sup>2919</sup>"
    },
    {
        "number": "2587",
        "text": "Le Messager d'Allah (s) a dit : Celui qui se nourrit du travail de ses propres mains traversera le pont Ṣirāṭ comme un éclair furtif.<sup>2920</sup>"
    },
    {
        "number": "2588",
        "text": "Le Messager d'Allah (s) a dit : Allah regardera avec miséricorde celui qui se nourrit du travail de ses propres mains, et Il ne le châtiera jamais.<sup>2921</sup>"
    },
    {
        "number": "2589",
        "text": "Le Messager d'Allah (s) a dit : Maudit, maudit soit celui qui entraîne la privation et le manque des personnes qui dépendent de lui.<sup>2922</sup>"
    },
    {
        "number": "2590",
        "text": "Biḥār al-Anwār : Al-Mufaḍḍal ibn 'Umar a dit : Aidez-vous de certaines choses de la vie d'ici-bas pour l'Au-delà. En effet, j'ai entendu l'Imām al-Ṣādiq (as) dire : «Aidez-vous de certaines choses de la vie d'ici-bas pour l'Au-delà, et ne soyez pas un fardeau pour les autres.»<sup>2923</sup>"
    }
])

# Subpart 823 - La meilleure des subsistances est celle qui suffit (2591-2593)
s823 = find_subpart(p160, "823"); eh(s823)
s823['hadiths'].extend([
    {
        "number": "2591",
        "text": "Le Messager d'Allah (s) a dit : Ô Allah, accorde à Muḥammad et à la famille de Muḥammad, ainsi qu'à ceux qui aiment Muḥammad et sa famille, la modération et ce qui suffit, et accorde à ceux qui détestent Muḥammad et la famille de Muḥammad, la richesse et la progéniture.<sup>2924</sup>"
    },
    {
        "number": "2592",
        "text": "Le Messager d'Allah (s) a dit : La meilleure subsistance est celle qui suffit.<sup>2925</sup>"
    },
    {
        "number": "2593",
        "text": "Le Messager d'Allah (s) a dit : Ce qui est peu mais suffisant est meilleur que ce qui est profus et qui distrait [de la voie d'Allah].<sup>2926</sup>"
    }
])

# ============================================================
# Part 161 (index 162) - LES POTS-DE-VIN (2594-2599)
# ============================================================
p161 = 162

s824 = find_subpart(p161, "824"); eh(s824)
s824['hadiths'].extend([
    {
        "number": "2594",
        "text": "Le Messager d'Allah (s) a dit : Gare aux pots-de-vin car c'est une pure mécréance, et celui qui les reçoit ne sentira pas le parfum du Paradis.<sup>2927</sup>"
    },
    {
        "number": "2595",
        "text": "Le Messager d'Allah (s) a dit : Allah maudit celui qui donne des pots-de-vin, celui qui les reçoit, et l'intermédiaire entre les deux.<sup>2928</sup>"
    },
    {
        "number": "2596",
        "text": "L'Imām 'Alī (as) a dit : En vérité, vos prédécesseurs ont été anéantis car ils ont privé les gens de leurs droits, et ces derniers les ont donc achetés [de force par des pots-de-vin] ; ils les ont incités à utiliser des moyens immoraux, et ils les ont suivis.<sup>2929</sup>"
    },
    {
        "number": "2597",
        "text": "L'Imām 'Alī (as) a dit : Vous savez bien que celui qui est en charge des mœurs, de la vie des gens, des butins [et biens], des préceptes légaux et de la guidance des musulmans ne doit pas être un avare... ni une personne qui accepte les pots-de-vin dans ses jugements car dans ce cas, il bafouera les droits et ne garantira pas à chacun ce qui lui est dû.<sup>2930</sup>"
    },
    {
        "number": "2598",
        "text": "L'Imām 'Alī (as) a dit en commentant la parole du Très-Haut «voraces de gains illicites»<sup>2931</sup>: Cela fait référence à un homme qui satisfait le besoin de son frère [en religion] puis qui accepte un cadeau de sa part.<sup>2932</sup>"
    },
    {
        "number": "2599",
        "text": "L'Imām al-Ṣādiq (as) a dit : Accepter un pot-de-vin en tant que juge ou gouvernant est une mécréance envers Allah.<sup>2933</sup>"
    }
])

# ============================================================
# Part 162 (index 163) - L'ALLAITEMENT (2600-2605)
# ============================================================
p162 = 163

s825 = find_subpart(p162, "825"); eh(s825)
s825['introduction'] = (
    "«<i>Les mères qui veulent donner un allaitement complet, allaiteront leurs bébés deux "
    "ans complets.</i>»<sup>2934</sup><br><br><span class=\"reference-note\">(Voir également : "
    "Coran 46:15 et 65:6)</span>"
)
s825['hadiths'].extend([
    {
        "number": "2600",
        "text": "Le Messager d'Allah (s) a dit : Il n'y a pas meilleur lait pour le nouveau-né que le lait de sa mère.<sup>2935</sup>"
    },
    {
        "number": "2601",
        "text": "L'Imām 'Alī (as) a dit : Considérez qui allaite vos enfants car en vérité, l'enfant grandira à partir de cela [les caractéristiques de la personne qui l'allaite].<sup>2936</sup>"
    },
    {
        "number": "2602",
        "text": "L'Imām al-Bāqir (as) a dit : Faites allaiter vos enfants par de belles nourrices, et éloignez-vous des laides, car le lait a un effet [sur l'enfant].<sup>2937</sup>"
    }
])

s826 = find_subpart(p162, "826"); eh(s826)
s826['hadiths'].extend([
    {
        "number": "2603",
        "text": "Le Messager d'Allah (s) a dit : Ne faites pas allaiter par une nourrice sotte ou par celle qui a les yeux chassieux, car le lait a un effet [sur l'enfant].<sup>2938</sup>"
    },
    {
        "number": "2604",
        "text": "L'Imām 'Alī (as) a dit : Protégez vos enfants du lait de la prostituée et de l'aliénée, car le lait a un effet [sur l'enfant].<sup>2939</sup>"
    },
    {
        "number": "2605",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'allaitement d'une nourrice juive ou chrétienne est préférable à l'allaitement d'une nassibiya<sup>2940</sup>.<sup>2941</sup>"
    }
])

# ============================================================
# Part 163 (index 164) - LA SATISFACTION (1) (2606-2610)
# ============================================================
p163 = 164

s827 = find_subpart(p163, "827"); eh(s827)
s827['hadiths'].extend([
    {
        "number": "2606",
        "text": "L'Imām 'Alī (as) a dit : Quel bon compagnon est la satisfaction !<sup>2942</sup>"
    },
    {
        "number": "2607",
        "text": "L'Imām Ḥasan (as) a dit : Celui qui s'appuie et a confiance en le fait que ce qu'Allah a choisi pour lui est le bien ne souhaitera jamais être dans une autre situation que celle qu'Allah a choisie pour lui.<sup>2943</sup>"
    },
    {
        "number": "2608",
        "text": "L'Imām Ḥasan (as) a dit : Comment un croyant peut-il prétendre être croyant s'il est mécontent de son destin et déteste sa situation alors que l'autorité au-dessus de lui est Allah ?<sup>2944</sup>"
    },
    {
        "number": "2609",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le plus haut degré du détachement est le plus bas degré de la dévotion et de la piété. Le plus haut degré de la dévotion et de la piété est le plus bas degré de la certitude. Le plus haut degré de la certitude est le plus bas degré de la satisfaction [envers Allah].<sup>2945</sup>"
    },
    {
        "number": "2610",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : La satisfaction face au destin non agréable [et semé d'adversités] fait partie des plus hauts degrés de certitude.<sup>2946</sup>"
    }
])

# ============================================================
# Sequential Sorting for all modified subparts
# ============================================================
modified_sections = [
    (p160, "820"), (p160, "821"), (p160, "822"), (p160, "823"),
    (p161, "824"),
    (p162, "825"), (p162, "826"),
    (p163, "827")
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

print("✅ Data successfully saved! Hadiths 2576-2610 injected.")
