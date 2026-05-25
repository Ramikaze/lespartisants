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
# Part 111 (index 112) - La sagesse (suite pages 310-312)
# ============================================================
p111 = 112

s562 = find_subpart(p111, "562")
s562['hadiths'].append({
    "number": "1701",
    "text": "L'Imām 'Alī (as) a dit : La sagesse est le bien perdu du croyant, prenez donc la sagesse même chez les hypocrites.<sup>1944</sup>"
})

s563 = find_subpart(p111, "563")
clear_hadiths(s563)
s563['hadiths'].extend([
    {
        "number": "1702",
        "text": "L'Imām 'Alī (as) a dit : N'est pas sage celui qui recherche la satisfaction de ses besoins auprès de quelqu'un qui n'est pas [lui-même] un sage.<sup>1945</sup>"
    },
    {
        "number": "1703",
        "text": "L'Imām 'Alī (as) a dit : Celui qui ne ménage pas une personne dont le ménagement est la seule solution n'est pas sage.<sup>1946</sup>"
    }
])

s564 = find_subpart(p111, "564")
clear_hadiths(s564)
s564['hadiths'].extend([
    {
        "number": "1704",
        "text": "L'Imām 'Alī (as) a dit : Le début de la sagesse est de délaisser les plaisirs [illicites], et son sommet est d'avoir en aversion les choses éphémères.<sup>1947</sup>"
    },
    {
        "number": "1705",
        "text": "L'Imām 'Alī (as) a dit : Parmi la sagesse figure le fait de ne pas entrer en conflit avec celui qui t'est supérieur, de ne pas mépriser celui qui t'est inférieur, et de ne pas entreprendre ce qui est au-dessus de tes forces. Et que tes paroles ne soient pas en contradiction avec ton cœur, ni tes actes avec tes paroles. Ne parle pas de ce que tu ignores, n'abandonne pas une chose qui vient vers toi pour courir après elle lorsqu'elle te tourne le dos.<sup>1948</sup>"
    },
    {
        "number": "1706",
        "text": "Interrogé par Abū Baṣīr au sujet de la parole divine <i>«Et celui à qui la sagesse est donnée, vraiment c'est un bien immense qui lui est donné»</i><sup>1949</sup>, l'Imām al-Bāqir (as) répondit : Il s'agit de l'obéissance à Allah et de la connaissance de l'Imām.<sup>1950</sup>"
    },
    {
        "number": "1707",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la sagesse est la connaissance et la compréhension profonde de la religion. En conséquence, celui parmi vous qui comprend est véritablement sage.<sup>1951</sup>"
    },
    {
        "number": "1708",
        "text": "L'Imām al-Kāẓim (as) a dit : Il fut demandé à Luqmān : «Qu'est-ce qui résume ta sagesse ?» Il répondit : «Je ne demande pas ce que je sais déjà et je ne me charge pas d'une chose qui ne me concerne pas.»<sup>1952</sup>"
    }
])

s565 = find_subpart(p111, "565")
clear_hadiths(s565)
s565['hadiths'].extend([
    {
        "number": "1709",
        "text": "Le Messager d'Allah (s) a dit : La crainte d'Allah est la source de la sagesse.<sup>1953</sup>"
    },
    {
        "number": "1710",
        "text": "Le Messager d'Allah (s) a dit : En vérité, la plus noble des paroles est le rappel d'Allah et la source de la sagesse est de Lui obéir.<sup>1954</sup>"
    },
    {
        "number": "1711",
        "text": "Le Messager d'Allah (s) a dit : En vérité, la clémence est la source de la sagesse.<sup>1955</sup>"
    },
    {
        "number": "1712",
        "text": "L'Imām 'Alī (as) a dit : La source de la sagesse est de s'astreindre à la vérité et d'obéir à la personne [qui est sur le chemin] de la vérité.<sup>1956</sup>"
    }
])

s566 = find_subpart(p111, "566")
clear_hadiths(s566)
s566['hadiths'].extend([
    {
        "number": "1713",
        "text": "L'Imām 'Alī (as) a dit : Vaincs ton [bas] désir et ta sagesse sera parfaite.<sup>1957</sup>"
    },
    {
        "number": "1714",
        "text": "L'Imām 'Alī (as) a dit : La sagesse ne s'obtient qu'en se maîtrisant face aux péchés.<sup>1958</sup>"
    },
    {
        "number": "1715",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah affermit la sagesse dans le cœur de celui qui a renoncé à ce bas-monde et Il la rend manifeste au travers de ses paroles.<sup>1959</sup>"
    }
])

s567 = find_subpart(p111, "567")
clear_hadiths(s567)
s567['hadiths'].extend([
    {
        "number": "1716",
        "text": "Le Messager d'Allah (s) a dit : Le cœur porte la sagesse quand le ventre est vide, et le cœur rejette la sagesse lorsque le ventre est plein.<sup>1960</sup>"
    },
    {
        "number": "1717",
        "text": "L'Imām 'Alī (as) a dit : Les [bas] désirs et la sagesse ne se réunissent jamais.<sup>1961</sup>"
    },
    {
        "number": "1718",
        "text": "L'Imām al-Ṣādiq (as) a dit : La colère anéantit le cœur du sage, et celui qui ne peut maîtriser sa colère ne maîtrise pas sa raison.<sup>1962</sup>"
    },
    {
        "number": "1719",
        "text": "L'Imām al-Kāẓim (as) a dit : En vérité, la graine pousse dans la terre et non sur la pierre; de même, la sagesse s'accroît dans le cœur de l'humble et elle ne prend pas racine dans le cœur de l'orgueilleux arrogant, car Allah a fait en sorte que l'humilité soit l'instrument de la raison.<sup>1963</sup>"
    },
    {
        "number": "1720",
        "text": "L'Imām al-Hādī (as) a dit : La sagesse n'a pas d'effet sur les natures corrompues.<sup>1964</sup>"
    }
])

s568 = find_subpart(p111, "568")
clear_hadiths(s568)
s568['hadiths'].extend([
    {
        "number": "1721",
        "text": "L'Imām 'Alī (as) a dit : Celui en qui s'enracine la sagesse connaîtra les leçons [données par les choses].<sup>1965</sup>"
    },
    {
        "number": "1722",
        "text": "L'Imām al-Ṣādiq (as) a dit : La longue méditation sur la sagesse rend féconde la raison.<sup>1966</sup>"
    }
])

s569 = find_subpart(p111, "569")
clear_hadiths(s569)
s569['hadiths'].extend([
    {
        "number": "1723",
        "text": "L'Imām 'Alī (as) a dit : En vérité, les sages ont détruit et perdu la sagesse lorsqu'ils l'ont déposée auprès de ceux qui n'en étaient pas dignes.<sup>1967</sup>"
    },
    {
        "number": "1724",
        "text": "L'Imām al-Kāẓim (as) a dit : N'accordez pas la sagesse aux ignorants car vous commettrez une injustice envers elle, et n'en privez pas ceux qui la méritent car vous commettrez une injustice envers eux.<sup>1968</sup>"
    }
])


# ============================================================
# Part 112 (index 113) - Le serment (pages 313-314)
# ============================================================
p112 = 113

s570 = find_subpart(p112, "570")
s571 = find_subpart(p112, "571")
s572 = find_subpart(p112, "572")

for s in [s570, s571, s572]:
    clear_hadiths(s)

s570['introduction'] = "«Et n'usez pas du nom d'Allah dans vos serments, pour vous dispenser de faire le bien, d'être pieux ou de réconcilier les gens. Et Allah est Audient et Omniscient.»<sup>1969</sup>"
s570['hadiths'].append({
    "number": "1725",
    "text": "L'Imām al-Ṣādiq (as) a dit : Ne prêtez pas serment en utilisant le Nom d'Allah, que vos paroles soient véridiques ou mensongères, car Allah le Tout-Puissant a dit : <i>«Et n'usez pas du nom d'Allah dans vos serments»</i><sup>1970, 1971</sup>"
})

s571['hadiths'].extend([
    {
        "number": "1726",
        "source": "Thawāb al-A'māl",
        "text": "Allah le Tout-Puissant a dit : Je n'accorde pas Ma miséricorde à celui qui profère un serment mensonger.<sup>1972</sup>"
    },
    {
        "number": "1727",
        "text": "Le Messager d'Allah (s) a dit : Gare aux faux serments car en vérité, ils vident les maisons de leurs habitants.<sup>1973</sup>"
    },
    {
        "number": "1728",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui profère un serment en sachant qu'il ment s'est engagé dans un combat contre Allah le Tout-Puissant.<sup>1974</sup>"
    },
    {
        "number": "1729",
        "text": "L'Imām al-Ṣādiq (as) a dit : Mentir en prononçant un faux serment suscitera la pauvreté de la descendance de son auteur.<sup>1975</sup>"
    }
])

s572['hadiths'].append({
    "number": "1730",
    "text": "L'Imām 'Alī (as) a dit : Faites prêter serment à l'oppresseur lorsque vous le voulez de telle façon qu'il soit exempt de la puissance et de la force d'Allah, car s'il y prête faussement serment, il aura hâté sa punition, et s'il se prête serment par Allah à propos duquel il n'y a de divinité que Lui, elle ne sera pas hâtée car il a reconnu l'unicité d'Allah le Très-Haut.<sup>1976</sup>"
})


# ============================================================
# Part 113 (index 114) - Le licite (page 314)
# ============================================================
p113 = 114

s573 = find_subpart(p113, "573")
s574 = find_subpart(p113, "574")

for s in [s573, s574]:
    clear_hadiths(s)

s573['introduction'] = "«Ils t'interrogeront sur ce qui leur est permis. Dis : «Vous sont permises les bonnes nourritures.»»<sup>1977</sup><br>«Ô gens ! De ce qui existe sur la terre, mangez le licite et le pur ; ne suivez point les pas du Diable car il est vraiment pour vous un ennemi déclaré.»<sup>1978</sup>"
s573['hadiths'].append({
    "number": "1731",
    "text": "L'Imām 'Alī (as) a dit : Astreins-toi à ne manger que ce qui est licite, à être bon envers tes enfants, et à te souvenir d'Allah en toute situation.<sup>1979</sup>"
})

s574['hadiths'].append({
    "number": "1732",
    "text": "L'Imām al-Ṣādiq (as) a dit : Affronter les sabres est plus aisé que la quête du licite.<sup>1980</sup>"
})


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1701-1732")
