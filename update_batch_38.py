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
# Part 158 (index 159) - LA MISÉRICORDE (cont.)
# ============================================================
p158 = 159

s807 = find_subpart(p158, "807"); eh(s807)
s807['hadiths'].extend([
    {
        "number": "2524",
        "text": "Kanz al-'Ummāl : Le Messager d'Allah (s) a dit : «Nulle personne n'entrera au Paradis sauf par la miséricorde d'Allah.» Ils dirent : «Même pas toi ?» Il (s) répondit : «Même pas moi, sauf si Allah m'enveloppe de Sa miséricorde.»<sup>2852</sup>"
    },
    {
        "number": "2525",
        "text": "Le Messager d'Allah (s) a dit : Si vous saviez la valeur de la miséricorde d'Allah le Très-Haut, vous vous appuieriez sur elle.<sup>2853</sup>"
    },
    {
        "number": "2526",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : L'étonnement ne réside pas dans celui qui a été sauvé [le Jour du Jugement], mais dans celui qui a été damné : comment a-t-il été damné malgré l'immensité de la miséricorde d'Allah ?<sup>2854</sup>"
    },
    {
        "number": "2527",
        "text": "Le Messager d'Allah (s) a dit : Bénéficiez de la miséricorde d'Allah en effectuant les actes d'obéissance qu'Il vous a ordonnés.<sup>2855</sup>"
    },
    {
        "number": "2528",
        "text": "L'Imām 'Alī (as) a dit : La pratique du rappel d'Allah fait descendre la miséricorde.<sup>2856</sup>"
    },
    {
        "number": "2529",
        "text": "L'Imām 'Alī (as) a dit : En répandant la miséricorde sur les autres, on fait descendre la miséricorde [d'Allah].<sup>2857</sup>"
    }
])

# ============================================================
# Part 159 (index 160) - LES LIENS FAMILIAUX (2530-2543)
# ============================================================
p159 = 160

s808 = find_subpart(p159, "808"); eh(s808)
s808['hadiths'].extend([
    {
        "number": "2530",
        "text": "Le Messager d'Allah (s) a dit : En vérité, la récompense liée au maintien des liens familiaux est donnée plus vite que celle de toute bonne action.<sup>2858</sup>"
    },
    {
        "number": "2531",
        "text": "Le Messager d'Allah (s) a dit : Si tu veux être heureux durant toute l'année, maintiens tes liens familiaux.<sup>2859</sup>"
    }
])

s809 = find_subpart(p159, "809"); eh(s809)
s809['hadiths'].extend([
    {
        "number": "2532",
        "text": "Fāṭima al-Zahrā (as) a dit : Allah a ordonné le maintien des liens familiaux pour augmenter la croissance de la population.<sup>2860</sup>"
    },
    {
        "number": "2533",
        "text": "L'Imām Ḥusayn (as) a dit : Que celui qui veut que sa vie soit prolongée et sa subsistance augmentée, maintienne ses liens familiaux.<sup>2861</sup>"
    },
    {
        "number": "2534",
        "text": "L'Imām al-Bāqir (as) a dit : Le maintien des liens familiaux purifie les actes, suscite l'augmentation des richesses, repousse le mal, facilite les comptes [le Jour du Jugement] et retarde l'échéance [de la vie].<sup>2862</sup>"
    },
    {
        "number": "2535",
        "text": "L'Imām al-Bāqir (as) a dit : Le maintien des liens familiaux améliore le caractère, rend généreux, adoucit l'âme, accroît la subsistance et retarde l'échéance [de la vie].<sup>2863</sup>"
    },
    {
        "number": "2536",
        "text": "L'Imām al-Hādī (as) a dit : Lorsqu'Allah le Tout-Puissant permis à Moïse ibn 'Imrān (as) de converser avec Lui, il demande : «Mon Dieu... Quelle est la récompense de celui qui maintient ses relations avec ses proches ?» Il répondit : «Ô Moïse, Je retarderai l'échéance [de sa vie] et Je lui faciliterai les difficultés de l'agonie.»<sup>2864</sup>"
    }
])

s810 = find_subpart(p159, "810"); eh(s810)
s810['hadiths'].extend([
    {
        "number": "2537",
        "text": "Le Messager d'Allah (s) a dit : Ne romps pas les liens with ton proche, même s'il les rompt avec toi.<sup>2865</sup>"
    },
    {
        "number": "2538",
        "text": "L'Imām Ḥusayn (as) a dit : La personne qui maintient le mieux ses liens familiaux est celle qui renoue des liens avec celui qui les a coupés.<sup>2866</sup>"
    }
])

s811 = find_subpart(p159, "811"); eh(s811)
s811['introduction'] = (
    "«<i>Si vous vous détournez, ne risquez-vous pas de semer la corruption sur terre et de "
    "rompre vos liens de parenté ? Ce sont ceux-là qu'Allah a maudits, a rendus sourds et a "
    "rendu leurs yeux aveugles.</i>»<sup>2867</sup>"
)
s811['hadiths'].extend([
    {
        "number": "2539",
        "text": "Le Messager d'Allah (s) a dit : En vérité, les anges ne vont pas [rendre visite] à des gens parmi lesquels se trouve une personne ayant rompu ses liens familiaux.<sup>2868</sup>"
    },
    {
        "number": "2540",
        "text": "L'Imām 'Alī (as) a dit : S'ils rompent leurs liens familiaux, leurs richesses seront placées entre les mains des malveillants.<sup>2869</sup>"
    },
    {
        "number": "2541",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le péché qui hâte la mort est la rupture des liens familiaux.<sup>2870</sup>"
    }
])

s812 = find_subpart(p159, "812"); eh(s812)
s812['hadiths'].extend([
    {
        "number": "2542",
        "text": "Le Messager d'Allah (s) a dit : Maintenez vos liens familiaux, ne serait-ce qu'en adressant des salutations.<sup>2871</sup>"
    },
    {
        "number": "2543",
        "text": "L'Imām al-Ṣādiq (as) a dit : Maintiens tes relations avec tes proches, ne serait-ce qu'en leur offrant une gorgée d'eau. La meilleure façon de maintenir ses liens familiaux est de s'abstenir d'offenser [ses proches].<sup>2872</sup>"
    }
])

# ============================================================
# Part 160 (index 161) - LA SUBSISTANCE (2544-2546, 2567-2575)
# ============================================================
p160 = 161

s813 = find_subpart(p160, "813"); eh(s813)
s813['introduction'] = (
    "«<i>En vérité, c'est Allah qui est le Grand Pourvoyeur, le Détenteur de la force, "
    "l'Inébranlable.</i>»<sup>2873</sup><br>"
    "«<i>En vérité, ton Seigneur étend Ses dons largement à qui Il veut ou les accorde avec "
    "parcimonie. Il est, sur Ses serviteurs, parfaitement Connaisseur et Clairvoyant.</i>»<sup>2874</sup>"
)
s813['hadiths'].extend([
    {
        "number": "2544",
        "text": "L'Imām 'Alī (as) a dit : Seul le Grand Pourvoyeur [Allah] a le pouvoir de retenir ou d'accorder la subsistance.<sup>2875</sup>"
    },
    {
        "number": "2545",
        "text": "L'Imām 'Alī (as) a dit : Il [Allah] assigne les subsistances de façon abondante ou avec parcimonie, et Il les distribue à ceux qui sont dans le besoin et à ceux qui sont dans l'aisance. Il fait preuve de justice en les allouant afin d'éprouver celui qu'Il veut par l'aisance ou la difficulté, et Il teste par ce biais la reconnaissance et la patience des riches et des pauvres.<sup>2876</sup>"
    }
])

s814 = find_subpart(p160, "814"); eh(s814)
s814['introduction'] = (
    "«<i>Il n'est point de bête sur terre dont la subsistance n'incombe à Allah qui connaît son "
    "gîte et son dépôt ; tout est dans un Livre explicite.</i>»<sup>2877</sup>"
)
s814['hadiths'].extend([
    {
        "number": "2546",
        "text": "Le Messager d'Allah (s) a dit : Ne te laisse pas préoccuper par ce qui t'est garanti [ta subsistance] au détriment de ce qui t'a été ordonné car en vérité, tu ne seras pas privé de ce qui t'a déjà été destiné et tu n'atteindras pas ce que l'on a écarté de toi.<sup>2878</sup>"
    }
])

s819 = find_subpart(p160, "819"); eh(s819)
s819['hadiths'].extend([
    {
        "number": "2567",
        "text": "Le Messager d'Allah (s) a dit : Que celui qui est impatient vis-à-vis de [l'arrivée de] la subsistance multiplie les takbīr<sup>2899</sup>, et que celui qui s'inquiète et se fait beaucoup de souci [pour ses moyens de subsistance] augmente ses demandes de pardon.<sup>2900</sup><br>(Voir également : 303. La demande de pardon, section 1431)"
    }
])

s820 = find_subpart(p160, "820"); eh(s820)
s820['hadiths'].extend([
    {
        "number": "2568",
        "text": "Le Messager d'Allah (s) a dit : L'arrivée de la subsistance de la personne qui nourrit les autres est plus rapide qu'un couteau qui coupe la chair.<sup>2901</sup>"
    },
    {
        "number": "2569",
        "text": "Lorsqu'il lui fut dit : «J'aimerais que ma subsistance augmente», le Messager d'Allah (s) répondit : «Sois toujours en état de pureté (tahāra), et ta subsistance sera augmentée.»<sup>2902</sup>"
    },
    {
        "number": "2570",
        "text": "Le Messager d'Allah (s) a dit : Augmentez votre charité (sadaqa) et [Allah] vous donnera votre subsistance.<sup>2903</sup>"
    },
    {
        "number": "2571",
        "text": "L'Imām 'Alī (as) a dit : Aider un frère en religion avec sa richesse pour Allah le Tout-Puissant augmente la subsistance.<sup>2904</sup>"
    },
    {
        "number": "2572",
        "text": "L'Imām 'Alī (as) a dit : Agir avec intégrité augmente la subsistance.<sup>2905</sup>"
    },
    {
        "number": "2573",
        "text": "L'Imām 'Alī (as) a dit : Faites descendre la subsistance par la charité (sadaqa).<sup>2906</sup>"
    },
    {
        "number": "2574",
        "text": "L'Imām 'Alī (as) a dit : Celui qui a une intention bonne et sincère verra sa subsistance augmenter.<sup>2907</sup>"
    },
    {
        "number": "2575",
        "text": "L'Imām al-Bāqir (as) a dit : Prie avec ferveur pour tes frères [en religion] en secret, et la subsistance sera déversée [abondamment] sur toi.<sup>2908</sup>"
    }
])

# ============================================================
# Sequential Sorting for all modified subparts
# ============================================================
modified_sections = [
    (p158, "807"),
    (p159, "808"), (p159, "809"), (p159, "810"), (p159, "811"), (p159, "812"),
    (p160, "813"), (p160, "814"), (p160, "819"), (p160, "820")
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

print("✅ Data successfully saved! Hadiths 2524-2546 and 2567-2575 injected.")
