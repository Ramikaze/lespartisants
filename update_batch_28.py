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

def clear_hadiths(s):
    if s:
        s['hadiths'] = []
        if 'introduction' in s:
            del s['introduction']

# ============================================================
# Part 121 (index 122) - La pudeur - s604 (page 329)
# ============================================================
p121 = 122
s604 = find_subpart(p121, "604")
clear_hadiths(s604)
s604['hadiths'].append({
    "number": "1827",
    "text": "L'Imām 'Alī (as) a dit : Le sommet de la pudeur est que la personne soit pudique vis-à-vis d'elle-même.<sup>2077</sup>"
})

# ============================================================
# Part 122 (index 123) - L'Issue (page 329)
# ============================================================
p122 = 123
s605 = find_subpart(p122, "605")
s606 = find_subpart(p122, "606")

clear_hadiths(s605)
s605['hadiths'].extend([
    {
        "number": "1828",
        "text": "Le Messager d'Allah (s) a dit : Le croyant est dans la crainte constante d'une issue funeste [de sa vie], et jusqu'au moment de la prise de son âme et de l'apparition de l'ange de la mort face à lui, il n'est pas certain qu'il atteigne la satisfaction d'Allah.<sup>2078</sup>"
    },
    {
        "number": "1829",
        "text": "Le Messager d'Allah (s) a dit : En vérité, il se peut qu'un homme agisse pendant très longtemps selon les actes des gens du Paradis, mais qu'il finisse sa vie en commettant les actes des gens de l'Enfer.<sup>2079</sup>"
    },
    {
        "number": "1830",
        "text": "Le Messager d'Allah (s) a dit : Ne soyez pas émerveillés par [les bonnes actions d'] un être avant qu'il ait vu l'issue [de sa vie] car en vérité, quelqu'un peut faire le bien pendant une longue période de sa vie ou une partie de sa vie et s'il venait alors à mourir, il irait au Paradis. Cependant, il change par la suite et commet des actes vils.<sup>2080</sup><br><br><span class=\"hadith-footnote\">(Voir également : 190. Le bonheur, section 948)</span>"
    }
])

# s606 already has hadith 1832, now prepend 1831
s606['hadiths'].insert(0, {
    "number": "1831",
    "text": "L'Imām 'Alī (as) a dit : Si tu veux qu'Allah t'épargne une mauvaise issue, sache que le bien qui t'arrive est dû à la grâce d'Allah et à Sa faveur, et que pour ce qui t'arrive de mal, [sache qu'] Allah t'a donné un sursis et un répit. Crains Sa clémence et à Son pardon à ton égard.<sup>2081</sup>"
})

# ============================================================
# Part 125 (index 126) - La perte - s613 hadith 1847 (page 334)
# ============================================================
p125 = 126
s613 = find_subpart(p125, "613")
s613['hadiths'].append({
    "number": "1847",
    "text": "L'Imām 'Alī (as) a dit : En vérité, le plus grand perdant et celui dont les efforts sont les plus vains est l'homme qui a usé son corps dans la quête de sa fortune, bien que le destin ne l'ait pas aidé dans son dessein. Il a ainsi quitté ce monde avec regret et fait face à l'Au-delà avec ses [funestes] conséquences.<sup>2101</sup>"
})

# ============================================================
# Part 126 (index 127) - L'Humilité (page 334-335)
# ============================================================
p126 = 127
s614 = find_subpart(p126, "614")
s615 = find_subpart(p126, "615")

clear_hadiths(s614)
clear_hadiths(s615)

s614['introduction'] = "«Le moment n'est-il pas venu pour ceux qui ont cru, que leurs cœurs s'humilient à l'évocation d'Allah et devant ce qui est descendu de la Vérité ?»<sup>2102</sup>"
s614['hadiths'].extend([
    {
        "number": "1848",
        "source": "Irshād al-Qulūb",
        "text": "Dans le <i>ḥadīth</i> de l'ascension (<i>mi'rāj</i>), [Allah a dit] : Dès qu'un serviteur vient à Me connaître et s'humilie devant Moi, toute chose s'humilie devant lui.<sup>2103</sup>"
    },
    {
        "number": "1849",
        "text": "L'Imām 'Alī (as) a dit : Quelle aide à l'invocation est l'humilité !<sup>2104</sup>"
    },
    {
        "number": "1850",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans une invocation : Je me réfugie auprès de Toi d'une âme qui n'est pas satisfaite, d'un ventre qui n'est jamais rassasié et d'un cœur qui n'est pas humble.<sup>2105</sup>"
    }
])

s615['hadiths'].extend([
    {
        "number": "1851",
        "text": "Le Messager d'Allah (s) a dit : Les traits caractéristiques de l'humble sont au nombre de quatre : l'attention constante à Allah en secret et en public, faire ce qui est beau, réfléchir au sujet du Jour de la Résurrection, et réaliser des entretiens intimes [des prières] avec Allah.<sup>2106</sup>"
    },
    {
        "number": "1852",
        "text": "L'Imām 'Alī (as) a dit : Celui dont le cœur est humble verra l'ensemble de ses membres devenir humbles.<sup>2107</sup><br><br><span class=\"hadith-footnote\">(Voir également : 47. Pleurer ; 334. Le cœur, section 1554)</span>"
    }
])

# ============================================================
# Part 129 (index 130) - La sincérité - suite (page 338)
# ============================================================
p129 = 130
s618 = find_subpart(p129, "618")
s619 = find_subpart(p129, "619")
s620 = find_subpart(p129, "620")
s621 = find_subpart(p129, "621")

for s in [s619, s620, s621]:
    clear_hadiths(s)

# Add 1870 to s618
s618['hadiths'].append({
    "number": "1870",
    "text": "L'Imām 'Alī (as) a dit : Heureux soit celui dont les actes et le savoir, l'amour et la haine, l'acceptation et le refus, les mots et le silence ainsi que les actes et paroles ont été seulement et sincèrement pour Allah.<sup>2129</sup>"
})

s619['hadiths'].extend([
    {
        "number": "1871",
        "text": "L'Imām 'Alī (as) a dit : Rendre l'acte sincère est plus difficile que la réalisation de l'acte en lui-même, et purifier l'intention de la corruption est plus difficile pour ceux qui agissent que de s'engager dans un long combat (<i>jihād</i>).<sup>2130</sup>"
    },
    {
        "number": "1872",
        "text": "L'Imām al-Ṣādiq (as) a dit : Persister dans l'accomplissement d'un acte jusqu'à ce qu'il devienne pur et sincère est plus difficile que [la réalisation de] l'acte en lui-même.<sup>2131</sup>"
    }
])

s620['hadiths'].extend([
    {
        "number": "1873",
        "source": "Al-Kāfī",
        "text": "Allah le Béni et le Très-Haut a dit lors de l'un de Ses entretiens intimes avec Moïse (as) : Ô Moïse ! L'acte accompli pour Moi sera important même s'il est modeste, tandis que l'acte accompli pour un autre que Moi sera insignifiant même s'il est important.<sup>2132</sup>"
    },
    {
        "number": "1874",
        "text": "Le Messager d'Allah (s) a dit : Purifie et rends ton cœur sincère, et peu d'actes te suffiront.<sup>2133</sup>"
    }
])

s621['hadiths'].append({
    "number": "1875",
    "source": "'Uddat al-Dā'ī",
    "text": "rapporte d'al-Mufaḍḍal ibn Ṣāliḥ : L'Imām al-Ṣādiq (as) a dit : «En vérité, Allah a des serviteurs qui ont agi vis-à-vis de Lui avec sincérité en secret, et Allah a agi vis-à-vis d'eux avec une pure bonté, car ce sont eux qui, le Jour de la Résurrection, feront partie des ceux à qui Allah accordera Son secours.»"
})


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done filling gaps: 1827-1832, 1847-1852, and extending 1870-1875")
