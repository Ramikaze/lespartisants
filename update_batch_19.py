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

# Part 100 (index 101) - Les comptes
p100 = 101
s527 = find_subpart(p100, "527") # 1587 already appended, continuing with 1588-1591
s528 = find_subpart(p100, "528")

clear_hadiths(s528)

s527['hadiths'].extend([
    {
        "number": "1588",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Lorsqu'Allah rassemblera les premiers et les derniers des gens, un appel sera lancé : «Où sont les patients afin qu'ils entrent tous au Paradis sans comptes ?» Les anges leur demanderont : «Qui êtes-vous ?» Ils diront : «Les patients.» Ils leur demanderont : «Pour quoi avez-vous patienté ?» Ils répondront : «Nous avons patienté dans la voie de l'obéissance à Allah et nous avons patienté pour ne pas désobéir à Allah.»<sup>1816</sup>"
    },
    {
        "number": "1589",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Lorsqu'Allah le Tout-Puissant rassemblera les premiers et les derniers, un crieur se lèvera et lancera un appel qui sera entendu par l'ensemble des gens : «Où sont ceux qui se sont aimés les uns les autres pour Allah ?» Un groupe de personnes se lèvera et il leur sera dit : «Allez au Paradis sans comptes.»<sup>1817</sup>"
    },
    {
        "number": "1590",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour de la Résurrection, un groupe de personnes se lèvera, se rendra à la porte du Paradis et frappera à sa porte. Il leur sera demandé : «Qui êtes-vous ?» Elles répondront : «Nous sommes les pauvres.» Il leur sera dit : «[Voulez-vous entrer au paradis] avant les comptes ?!» Elles diront : «Vous ne nous avez rien donné pour que vous nous demandiez des comptes !» Et Allah le Tout-Puissant dira : «Elles disent vrai, entrez au Paradis.»<sup>1818</sup>"
    },
    {
        "number": "1591",
        "text": "L'Imām al-Ṣādiq (as) rapporte du Messager d'Allah (s) : «Lorsque les recueils consignant les actes seront déployés et les balances installées, aucune balance ne sera installée pour les personnes qui ont souffert, ni leur recueil déployé.» Puis il récita ce verset : <i>«Les endurants auront leur pleine récompense sans compter.»</i><sup>1819, 1820</sup>"
    }
])

s528['hadiths'].append({
    "number": "1592",
    "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Tout-Puissant dressera les comptes de toutes les créatures sauf de celle qui a associé une créature à Allah. On ne dressera pas ses comptes le Jour de la Résurrection, et il sera ordonné de l'emmener [directement] en Enfer.<sup>1821</sup>"
})


# Part 101 (index 102) - La jalousie
p101 = 102
s529 = find_subpart(p101, "529")
s530 = find_subpart(p101, "530")
s531 = find_subpart(p101, "531")
s532 = find_subpart(p101, "532")

for s in [s529, s530, s531, s532]:
    clear_hadiths(s)

s529['introduction'] = "«Et contre le mal de l'envieux quand il envie.»<sup>1824</sup>"
s529['hadiths'].extend([
    {
        "number": "1593",
        "source": "Tanbīh al-Khawāṭir",
        "text": "Le Messager d'Allah (s) a dit : «Six [groupes de gens] iront en Enfer avant les comptes à cause de six [raisons].» Ils dirent : «Ô Messager d'Allah, que les prières d'Allah soient sur toi, qui sont-ils ?» Il répondit : «Les gouvernants pour leur tyrannie, les Arabes pour leur fanatisme envers leur tribu, les propriétaires terriens pour leur arrogance, les commerçants pour leurs tricheries, les villageois pour leur ignorance, et les savants pour leur jalousie.»<sup>1822</sup>"
    },
    {
        "number": "1594",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah fera entrer trois [groupes de] personnes en Enfer sans aucun compte : un chef oppresseur, un commerçant menteur, et un homme âgé ayant commis l'adultère.<sup>1823</sup>"
    },
    {
        "number": "1595",
        "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit en s'adressant à Moïse ibn 'Imrān (as) : «En vérité, le jaloux est exaspéré par Mes bienfaits, il rejette le partage que J'ai établi entre Mes serviteurs.»<sup>1825</sup>"
    },
    {
        "number": "1596",
        "text": "L'Imām 'Alī (as) a dit : La jalousie est l'emprisonnement de l'esprit.<sup>1826</sup>"
    },
    {
        "number": "1597",
        "text": "L'Imām 'Alī (as) a dit : La jalousie est la pire des maladies.<sup>1827</sup>"
    },
    {
        "number": "1598",
        "text": "L'Imām 'Alī (as) a dit : Le chef des vices est la jalousie.<sup>1828</sup>"
    },
    {
        "number": "1599",
        "text": "L'Imām 'Alī (as) a dit : Comme la jalousie est capable, et comme elle est juste ! Elle commence par [faire souffrir] son auteur, et provoque sa mort.<sup>1829</sup>"
    },
    {
        "number": "1600",
        "text": "L'Imām 'Alī (as) a dit : Le résultat de la jalousie est le malheur dans ce bas-monde et dans l'Au-delà.<sup>1830</sup>"
    },
    {
        "number": "1601",
        "text": "L'Imām 'Alī (as) a dit : Le jaloux voit la disparition d'une grâce de celui qu'il a jalousé comme une grâce pour lui-même.<sup>1831</sup>"
    },
    {
        "number": "1602",
        "text": "L'Imām 'Alī (as) a dit : Je n'ai vu d'oppresseur aussi semblable à l'opprimé que le jaloux : son âme est épuisée, son cœur errant, et sa tristesse persistante.<sup>1832</sup>"
    },
    {
        "number": "1603",
        "text": "L'Imām 'Alī (as) a dit : Ce dont il souffre suffit [comme tourment] au jaloux.<sup>1833</sup>"
    },
    {
        "number": "1604",
        "text": "L'Imām 'Alī (as) a dit : Les regrets du jaloux sont innombrables et ses vices sont multiples.<sup>1834</sup>"
    },
    {
        "number": "1605",
        "text": "L'Imām 'Alī (as) a dit : Le jaloux ne triomphe jamais.<sup>1835</sup>"
    }
])

s530['hadiths'].append({
    "number": "1606",
    "text": "Le Messager d'Allah (s) a dit : Recherchez l'assistance de la discrétion pour la satisfaction de vos besoins, car toute personne étant l'objet de grâces est jalousée.<sup>1836</sup>"
})

s531['hadiths'].extend([
    {
        "number": "1607",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, la jalousie consume la foi de la même manière que le feu consume le bois sec.<sup>1837</sup>"
    },
    {
        "number": "1608",
        "text": "L'Imām al-Ṣādiq (as) a dit : Prenez garde à ne pas vous jalouser les uns les autres, car la racine de la mécréance est la jalousie.<sup>1838</sup>"
    }
])

s532['hadiths'].append({
    "number": "1609",
    "text": "L'Imām al-Ṣādiq (as) a dit : Luqmān a dit à son fils : Le jaloux a trois caractéristiques: il médit la personne pendant son absence, il la flatte en sa présence et il se réjouit du malheur des autres.<sup>1839</sup>"
})


# Part 102 (index 103) - Le regret
p102 = 103
s533 = find_subpart(p102, "533")
clear_hadiths(s533)

s533['introduction'] = "«Avertis-les du Jour du Regret, quand tout sera réglé ; alors qu'ils sont [dans ce monde] inattentifs et qu'ils ne croient pas.»<sup>1840</sup><br>«Avant qu'une âme ne dise : «Malheur à moi pour mes manquements envers Allah. Car j'ai été, certes, parmi les railleurs.»»<sup>1841</sup><br>«Le jour où l'injuste se mordra les deux mains et dira : «Si seulement j'avais suivi chemin avec le Messager !»<sup>1842</sup>"
s533['hadiths'].extend([
    {
        "number": "1610",
        "text": "Le Messager d'Allah (s) a dit : La personne qui aura le plus intense regret le Jour de la Résurrection sera un homme qui a vendu sa vie de l'Au-delà pour la vie d'ici-bas des autres.<sup>1843</sup>"
    },
    {
        "number": "1611",
        "text": "L'Imām 'Alī (as) a dit : Le plus grand regret le Jour de la Résurrection sera celui d'un homme qui a gagné de l'argent en désobéissant à Allah, qui a ensuite été hérité par une autre personne qui l'a dépensé dans l'obéissance d'Allah - loué soit-Il. Elle entrera grâce à [cet argent] au Paradis, tandis que le premier ira en Enfer à cause de lui.<sup>1844</sup>"
    },
    {
        "number": "1612",
        "text": "L'Imām al-Ṣādiq (as) a dit : La personne qui aura le plus de regret le Jour de la Résurrection sera celle qui parlait de justice et agissait dans le sens contraire vis-à-vis d'autrui.<sup>1845</sup>"
    }
])


# Part 103 (index 104) - La bonne action
p103 = 104
s534 = find_subpart(p103, "534")
s535 = find_subpart(p103, "535")
for s in [s534, s535]:
    clear_hadiths(s)

s534['hadiths'].append({
    "number": "1613",
    "text": "Le Messager d'Allah (s) a dit : J'ai trouvé que la bonne action était une lumière dans le cœur, un embellissement du visage, et une force dans l'action ; et j'ai trouvé que le péché était un assombrissement du cœur, une paresse dans l'action et une laideur sur le visage.<sup>1846</sup><br><br><span class=\"hadith-footnote\">(Voir également : 385. La lumière)</span>"
})

s535['introduction'] = "«Quiconque viendra avec le bien aura dix fois autant ; et quiconque viendra avec le mal ne sera rétribué que par son équivalent. Et on ne leur fera aucune injustice.»<sup>1847</sup>"
s535['hadiths'].extend([
    {
        "number": "1614",
        "source": "Tuḥaf al-'Uqūl",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : «Malheur à celui dont les unités ont dépassé les dizaines !» - Il voulait ainsi dire que le mal n'est comptabilisé qu'une seule fois alors que le bien l'est dix fois.<sup>1848</sup>"
    },
    {
        "number": "1615",
        "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le croyant excelle dans son action, Allah multipliera chaque bonne action par sept cents, et c'est ce que signifie la parole d'Allah le Béni et le Très-Haut : <i>«Allah multiplie la récompense à qui Il veut.»</i><sup>1849, 1850</sup>"
    }
])


# Part 104 (index 105) - La bienfaisance
p104 = 105
s536 = find_subpart(p104, "536")
s537 = find_subpart(p104, "537")

for s in [s536, s537]:
    clear_hadiths(s)

s536['hadiths'].append({
    "number": "1616",
    "source": "Tafsīr Nūr al-Thaqalayn",
    "text": "au sujet de Sa parole <i>«Qui est meilleur en religion que celui qui soumet à Allah son être, tout en faisant le bien»</i><sup>1851</sup> : Il est rapporté que lorsque le Prophète (s) fut interrogé au sujet de la bienfaisance, il répondit : «C'est d'adorer Allah comme si tu Le voyais car si tu ne Le vois pas, Lui, en vérité, te voit.»<sup>1852</sup>"
})

s537['introduction'] = "«Si vous faites le bien, vous le faites à vos propres âmes ; et si vous faites le mal, vous le leur faites [aussi].»<sup>1853</sup>"
s537['hadiths'].append({
    "number": "1617",
    "text": "L'Imām 'Alī (as) a dit : En vérité, si tu fais le bien, c'est ta propre âme que tu honores et à qui tu fais du bien ; en revanche, si tu fais le mal, c'est ta propre âme que tu avilis et que tu lèses.<sup>1854</sup><br><br><span class=\"hadith-footnote\">(Voir également : 342. La noblesse, section 1599)</span>"
})


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1588-1617")
