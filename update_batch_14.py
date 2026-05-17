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

# Part 89 (index 90) - Le hadīth
p89 = 90
s468 = find_subpart(p89, "468")
s469 = find_subpart(p89, "469")
s470 = find_subpart(p89, "470")
s471 = find_subpart(p89, "471")
s472 = find_subpart(p89, "472")

for s in [s468, s469, s470, s471, s472]:
    clear_hadiths(s)

s468['hadiths'].extend([
    {
        "number": "1427",
        "text": "Le Messager d'Allah (s) a dit : Il n'y a aucun mal à transmettre un <i>ḥadīth</i> en changeant l'ordre de certains mots si le sens [exact] est conservé.<sup>1640</sup>"
    },
    {
        "number": "1428",
        "source": "Biḥār al-Anwār",
        "text": "rapporte de Muḥammad ibn Muslim : J'ai dit à Abū 'Abdillāh [l'Imām al-Ṣādiq] (as) : «J'entends l'une de tes paroles, puis je la rallonge ou la raccourcis.» Il dit : «Si tu vises par cela à transmettre sa signification, il n'y a aucun mal.»<sup>1641</sup>"
    }
])

s469['hadiths'].extend([
    {
        "number": "1429",
        "text": "Le Messager d'Allah (s) a dit : De mes paroles, ne transmettez à ma communauté que celles qui peuvent être comprises par leur intelligence.<sup>1642</sup>"
    },
    {
        "number": "1430",
        "text": "L'Imām 'Alī (as) a dit : Lorsque vous narrez un <i>ḥadīth</i>, appuyez-le et authentifiez-le auprès de la personne qui vous l'a narré. Si ce qu'elle a dit est vrai, le bénéfice vous reviendra et si elle a menti, ce sera aux dépens d'elle-même.<sup>1643</sup>"
    }
])

s470['hadiths'].append({
    "number": "1431",
    "text": "L'Imām al-Ṣādiq (as) a dit : Ma parole est la parole de mon père, la parole de mon père est la parole de mon grand-père, la parole de mon grand-père est celle de Ḥusayn (as), la parole de Ḥusayn (as) est la parole de Ḥasan (as), la parole de Ḥasan (as) est la parole de l'Emir des croyants (as), la parole de l'Emir des croyants est la parole du Messager d'Allah (s), et la parole du Messager d'Allah (s) est la parole d'Allah le Tout-Puissant.<sup>1644</sup>"
})

s471['hadiths'].append({
    "number": "1432",
    "source": "Biḥār al-Anwār",
    "text": "rapporte d'Abū Usāma: J'étais chez Abū 'Abdillah [l'Imām al-Ṣādiq] (as) alors qu'il y avait auprès de lui un homme d'Al-Mughīriyya. Ce dernier l'interrogea à propos d'une tradition, et il dit : «Il existe une tradition d'Allah et de Son Messager pour toute chose dont ont besoin les fils d'Adam. S'il n'en était pas ainsi, Il [Allah] ne nous aurait pas apporté l'argument comme Il l'a fait.» L'homme d'Al-Mughīriyya dit alors : «Et quel est cet argument ?» Et l'Imām (as) répondit : «[C'est] Sa parole <i>«Aujourd'hui, J'ai parachevé pour vous votre religion et accompli sur vous Mon bienfait. Et J'agrée l'islam comme religion pour vous»</i><sup>1645</sup>.»<sup>1646</sup>"
})

s472['hadiths'].append({
    "number": "1433",
    "text": "L'Imām al-Riḍā (as) a dit : En vérité, certaines de nos paroles sont équivoques comme les [versets] équivoques du Coran, et certaines sont claires et sans équivoque, comme [les versets] clairs et sans équivoque du Coran. Par conséquent, expliquez ce qui est équivoque avec ce qui est clair et sans équivoque, et ne suivez pas [aveuglément] l'équivoque sans vous référer à ce qui est clair, sinon vous vous égarerez.<sup>1647</sup>"
})

# Part 90 (index 91) - Les limites et peines légales (al-ḥudūd)
p90 = 91
s473 = find_subpart(p90, "473")
s474 = find_subpart(p90, "474")
s475 = find_subpart(p90, "475")
s476 = find_subpart(p90, "476")
s477 = find_subpart(p90, "477")
s478 = find_subpart(p90, "478")
s479 = find_subpart(p90, "479")
s480 = find_subpart(p90, "480")

for s in [s473, s474, s475, s476, s477, s478, s479, s480]:
    clear_hadiths(s)

s473['hadiths'].append({
    "number": "1434",
    "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Béni et le Très-Haut... a attribué une limite à toute chose et a donné à chacune un indice qui permet de la déterminer, puis Il a fait en sorte que celui qui outrepasse la limite soit soumis à une peine légale.<sup>1648</sup>"
})

s474['hadiths'].extend([
    {
        "number": "1435",
        "text": "Le Messager d'Allah (s) a dit : Épargnez aux musulmans les peines légales tant que vous le pouvez, et si vous pouvez trouver une échappatoire au musulman, ouvrez cette voie pour lui. En vérité, il vaut mieux que l'Imām se trompe dans le pardon, qu'il ne se trompe dans la punition.<sup>1649</sup>"
    },
    {
        "number": "1436",
        "text": "Le Messager d'Allah (s) a dit : Epargnez l'application des peines légales par le doute [il faut s'abstenir d'appliquer la peine légale en cas de doute].<sup>1650</sup>"
    }
])

s475['hadiths'].extend([
    {
        "number": "1437",
        "text": "Le Messager d'Allah (s) a dit : Le maintien de l'une des peines légales [prescrites par] Allah est meilleure que la chute de pluie pendant quarante jours sur les terres d'Allah.<sup>1651</sup>"
    },
    {
        "number": "1438",
        "text": "Le Messager d'Allah (s) a dit : Une peine légale appliquée sur terre est plus bénie que l'adoration de soixante années.<sup>1652</sup>"
    },
    {
        "number": "1439",
        "text": "L'Imām al-Ṣādiq (as) rapporte de ses pères (as) : En vérité, une femme honorable parmi les siens fut amenée devant le Messager d'Allah (s) alors qu'elle avait volé. Il ordonna qu'on lui coupe [la main]. Des hommes qurayshites vinrent chez le Prophète (s) et lui dirent : «Ô Messager d'Allah, vas-tu couper [la main d'] une femme aussi distinguée pour une faute si petite ?» Il répondit : «Oui, car ceux qui vous ont précédé ont péri en raison de cela. Ils appliquaient les peines légales sur les faibles parmi eux, et ils en exemptaient leurs puissants et leurs nobles ; ils ont donc péri.»<sup>1653</sup>"
    }
])

s476['hadiths'].extend([
    {
        "number": "1440",
        "text": "Le Messager d'Allah (s) a dit : Tout homme dont l'intercession a empêché l'application de l'une des peines légales [prescrites] par Allah subira le courroux d'Allah jusqu'à ce qu'il cesse.<sup>1654</sup>"
    },
    {
        "number": "1441",
        "text": "Le Messager d'Allah (s) a dit : Point d'intercession, point de caution et point de serment dans les peines légales.<sup>1655</sup>"
    },
    {
        "number": "1442",
        "text": "L'Imām 'Alī (as) a dit : Point de caution pour aucune des peines [prescrites par Allah].<sup>1656</sup>"
    },
    {
        "number": "1443",
        "text": "L'Imām al-Ṣādiq (as) rapporte de son père qui rapporte de ses pères (as) que le Messager d'Allah (s) a interdit d'avoir recours à l'intercession dans [l'application] les peines légales et a dit : Celui qui intercède en vue de l'annulation de l'une des peines légales [prescrites par] Allah et s'efforce d'abolir Ses peines légales sera châtié par Allah le Très-Haut le Jour de la Résurrection.<sup>1657</sup>"
    }
])

s477['hadiths'].append({
    "number": "1444",
    "text": "L'Imām al-Bāqir (as) : Trois hommes témoignèrent contre un autre ayant commis l'adultère. L'Emir des croyants (as) demanda : «Où est le quatrième [témoin] ?» Ils répondirent: «Il va arriver d'un moment à l'autre.» Et l'Emir des croyants (as) dit : «Appliquez-lui la peine, car une peine ne doit pas être ajournée ne serait-ce d'une heure.»<sup>1658</sup>"
})

s478['introduction'] = "«Voilà les limites établies par Allah. Ne les transgressez donc pas. Et ceux qui transgressent les limites établies par d'Allah, ceux-là sont les injustes.»<sup>1659</sup>"
s478['hadiths'].extend([
    {
        "number": "1445",
        "text": "Le Messager d'Allah (s) a dit : [Au Jour de la Résurrection], un gouverneur ayant allégé la peine légale d'un coup de fouet sera amené et il dira «Ô Seigneur, c'est par miséricorde envers Tes serviteurs [que j'ai fait cela] !» Il lui dira : «Serais-tu plus miséricordieux envers eux que Moi-même ?!» Il sera alors ordonné de [l'amener] en Enfer. De même, celui qui a rajouté un coup de fouet sera amené et il dira «[Ô Seigneur ! J'ai fait cela] pour les dissuader de Te désobéir». Il sera également ordonné de [l'amener] en Enfer.<sup>1660</sup>"
    },
    {
        "number": "1446",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, l'Emir des croyants (as) a ordonné à Qanbar d'appliquer la peine légale à l'encontre d'un homme. Qanbar, par dureté, rajouta trois coups de fouet. 'Alī (as) condamna alors Qanbar à trois coups de fouet.<sup>1661</sup>"
    }
])

s479['hadiths'].append({
    "number": "1447",
    "text": "L'Imām 'Alī (as) a dit : Je n'applique aucune peine légale sur une terre de l'ennemi avant qu'il ne la quitte, afin que [la personne à laquelle doit s'appliquer la peine] ne soit pas envahie par la fureur et ne rejoigne l'ennemi.<sup>1662</sup>"
})

s480['hadiths'].extend([
    {
        "number": "1448",
        "text": "Le Messager d'Allah (s) a dit : Celui qui commet un péché et à qui on a appliqué la peine légale liée à ce péché, cela sera son expiation.<sup>1663</sup>"
    },
    {
        "number": "1449",
        "text": "L'Imām 'Alī (as) a dit : Allah est plus Généreux et plus Glorieux pour qu'Il châtie un serviteur croyant dans ce bas-monde et le châtie une seconde fois [pour le même péché] le Jour de la Résurrection.<sup>1664</sup>"
    }
])

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1427-1449")
