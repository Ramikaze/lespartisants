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
# Part 120 (index 121) - Les animaux - suite page 326
# ============================================================
p120 = 121
s598 = find_subpart(p120, "598")
# Already has 4 hadiths (1798-1801), extend with 1802-1810
s598['hadiths'].extend([
    {
        "number": "1802",
        "text": "Le Messager d'Allah (s) a dit : Ne frappez pas les animaux sur leurs gueules car en vérité, ils glorifient Allah et lui rendent grâce.<sup>2051</sup>"
    },
    {
        "number": "1803",
        "text": "Le Messager d'Allah (s) a dit : Une prostituée qui passait près d'un chien au pied d'un puits qui haletait et était sur le point de mourir de soif a été pardonnée car elle a enlevé sa chaussure, l'a nouée à son voile, et a puisé de l'eau pour lui. Ainsi, pour ce geste, Allah lui a pardonné.<sup>2052</sup>"
    },
    {
        "number": "1804",
        "text": "Le Messager d'Allah (s) a dit : Tout animal - oiseau ou autre - qui est tué injustement et sans raison se plaindra [à la personne qui l'a tué] le Jour de la Résurrection.<sup>2053</sup>"
    },
    {
        "number": "1805",
        "text": "Le Messager d'Allah (s) a dit : Celui qui a tué un oiseau sans raison verra cet oiseau se plaindre le Jour de la Résurrection auprès d'Allah en disant : «Ô Seigneur, untel m'a tué en vain, il ne m'a pas tué pour une raison utile.»<sup>2054</sup>"
    },
    {
        "number": "1806",
        "text": "Le Messager d'Allah (s) a dit : Si vous étiez pardonnés pour tout ce que vous faites [subir comme injustices] aux animaux, un grand nombre [de vos péchés] serait pardonné.<sup>2055</sup>"
    },
    {
        "number": "1807",
        "text": "Le Messager d'Allah (s) a dit : Ne crains-tu pas Allah vis-à-vis de cet animal qu'Allah t'a autorisé à posséder ?! En vérité, il s'est plaint à moi de la faim et de la peine que tu lui fais subir.<sup>2056</sup>"
    },
    {
        "number": "1808",
        "text": "Le Messager d'Allah (s) a dit : Qu'Allah maudisse celui qui traite durement un animal.<sup>2057</sup>"
    },
    {
        "number": "1809",
        "source": "Kanz al-'Ummāl",
        "text": "[Le Messager d'Allah (s)] a interdit de tuer tout être vivant sauf s'il est nuisible.<sup>2058</sup>"
    },
    {
        "number": "1810",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, une femme a été en proie au châtiment pour avoir attaché une chatte jusqu'à ce qu'elle meure de soif.<sup>2059</sup>"
    }
])

# ============================================================
# Part 121 (index 122) - La pudeur (pages 327-328)
# ============================================================
p121 = 122
s599 = find_subpart(p121, "599")
s600 = find_subpart(p121, "600")
s601 = find_subpart(p121, "601")
s602 = find_subpart(p121, "602")
s603 = find_subpart(p121, "603")
s604 = find_subpart(p121, "604")

for s in [s599, s600, s601, s602, s603, s604]:
    clear_hadiths(s)

s599['hadiths'].extend([
    {"number": "1811", "text": "L'Imām 'Alī (as) a dit : La pudeur est le moyen d'arriver à toute beauté.<sup>2061</sup>"},
    {"number": "1812", "text": "L'Imām 'Alī (as) a dit : La pudeur est la clé de tout bien.<sup>2062</sup>"},
    {"number": "1813", "text": "L'Imām 'Alī (as) a dit : La plus intelligente des personnes est la plus pudique.<sup>2063</sup>"},
    {"number": "1814", "text": "L'Imām 'Alī (as) a dit : La pudeur préserve de l'acte laid.<sup>2064</sup>"},
    {"number": "1815", "text": "L'Imām 'Alī (as) a dit : La pudeur est la cause de la chasteté.<sup>2065</sup>"}
])

s600['hadiths'].extend([
    {"number": "1816", "text": "Le Messager d'Allah (s) a dit : En vérité, chaque religion a une disposition naturelle, et la disposition naturelle de l'islam est la pudeur.<sup>2066</sup>"},
    {"number": "1817", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui n'a pas de pudeur est dépourvu de foi.<sup>2067</sup>"}
])

s601['hadiths'].append({
    "number": "1818",
    "text": "Le Messager d'Allah (s) a dit : La pudeur est de deux sortes : la pudeur intelligente et la pudeur stupide. La pudeur intelligente est le savoir, et la pudeur stupide est l'ignorance.<sup>2068</sup>"
})

s601['hadiths'].extend([
    {"number": "1819", "text": "L'Imām 'Alī (as) a dit : La pudeur [mêlée de honte] va de pair avec la privation.<sup>2069</sup>"},
    {"number": "1820", "text": "L'Imām 'Alī (as) a dit : La pudeur [mêlée de honte] empêche la subsistance.<sup>2070</sup>"},
    {"number": "1821", "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve de pudeur [mêlée de honte] en n'osant pas dire une parole de vérité est un sot.<sup>2071</sup>"}
])

s602['hadiths'].extend([
    {"number": "1822", "text": "Le Messager d'Allah (s) a dit : Il ne reste des proverbes des prophètes antérieurs que cette parole des gens : «Si tu n'as pas de pudeur, alors agis à ta guise.»<sup>2072</sup>"},
    {"number": "1823", "text": "L'Imām 'Alī (as) a dit : Celui qui n'a pas de pudeur face aux gens n'a pas de pudeur face à Allah - loué soit-Il.<sup>2073</sup>"}
])

s603['hadiths'].extend([
    {"number": "1824", "text": "Le Messager d'Allah (s) a dit : Fais preuve de pudeur vis-à-vis d'Allah comme tu fais preuve de pudeur vis-à-vis de tes voisins vertueux, car cela augmente la certitude.<sup>2074</sup>"},
    {"number": "1825", "text": "Le Messager d'Allah (s) a dit : Chacun de vous doit faire preuve de pudeur vis-à-vis de Ses deux anges qui vous accompagnent comme vous le feriez avec deux de vos voisins vertueux qui seraient avec vous nuit et jour.<sup>2075</sup>"},
    {"number": "1826", "text": "L'Imām al-Kāẓim (as) a dit : Faites preuve de pudeur vis-à-vis d'Allah dans votre intimité comme vous pouvez le faire en public vis-à-vis des gens.<sup>2076</sup>"}
])

# s604 is on page 329 (missing) - hadiths 1827-1831 will be filled later

# ============================================================
# Part 122 (index 123) - L'Issue - hadith 1832 (page 330 top)
# hadiths 1827-1831 are on page 329 (missing)
# ============================================================
p122 = 123
s606 = find_subpart(p122, "606")
clear_hadiths(s606)
s606['hadiths'].append({
    "number": "1832",
    "text": "L'Imām al-Ṣādiq (as) a dit en s'adressant à une personne : Si tu veux que tes actions aient une bonne issue et que l'on prenne ton âme alors que tu as accompli les meilleures œuvres, alors honore les droits d'Allah, n'utilise pas Ses grâces pour Lui désobéir, que Sa clémence vis-à-vis de toi ne soit pas source d'illusion [et de négligence], et honore toute personne qui nous évoque en bien et a de l'affection pour nous.<sup>2082</sup>"
})

# ============================================================
# Part 123 (index 124) - Le service (page 330)
# ============================================================
p123 = 124
s607 = find_subpart(p123, "607")
clear_hadiths(s607)
s607['hadiths'].extend([
    {"number": "1833", "text": "Le Messager d'Allah (s) a dit : Dès qu'un musulman rend service à un groupe de musulmans, Allah lui donnera des serviteurs dont le nombre sera équivalent [au groupe à qui il a rendu service] au Paradis.<sup>2083</sup>"},
    {"number": "1834", "text": "Le Messager d'Allah (s) a dit : Le service rendu par un croyant à son frère [mérite l'atteinte d'] une station dont la grandeur ne peut être perçue qu'en rendant le même service.<sup>2084</sup>"},
    {
        "number": "1835",
        "source": "Al-Kāfī",
        "text": "Jamīl a dit : l'Imām al-Ṣādiq (as) a dit : «Les croyants sont les serviteurs les uns des autres.» [Jamīl dit :] Je demandai : «Comment sont-ils les serviteurs les uns des autres ?» Il répondit : «En étant bénéfiques les uns aux autres.»<sup>2085</sup>"
    },
    {"number": "1836", "text": "L'Imām al-Ṣādiq (as) a dit : Rends service à ton frère et s'il abuse de toi, pas de marque d'honneur [ne le sers pas].<sup>2086</sup><br><br><span class=\"hadith-footnote\">(Voir également : 288. Le savoir, section 1353 ; 2. La rémunération)</span>"}
])

# ============================================================
# Part 124 (index 125) - Les kharidjites (pages 331-332)
# ============================================================
p124 = 125
s608 = find_subpart(p124, "608")
s609 = find_subpart(p124, "609")
s610 = find_subpart(p124, "610")

for s in [s608, s609, s610]:
    clear_hadiths(s)

s608['introduction'] = "«Dis : «Voulez-vous que Nous vous apprenions lesquels sont les plus grands perdants en œuvres? Ceux dont l'effort, dans la vie présente, s'est égaré, alors qu'ils s'imaginent faire le bien.»»<sup>2087</sup>"
s608['hadiths'].extend([
    {
        "number": "1837",
        "source": "Kanz al-'Ummāl",
        "text": "'Abdullāh Ibn Amrū a dit : Un homme vint voir le Prophète (s) le jour de [la bataille de] Ḥunayn alors qu'il était occupé à partager le butin. L'homme lui dit : «Ô Muhammad ! Sois équitable.» Le Prophète (s) lui dit : «Malheur à toi ! Qui peut être équitable si je ne le suis pas ?» - ou bien il (s) dit - «Auprès de qui aspires-tu trouver l'équité si ce n'est pas auprès de moi ?» Le Prophète (s) dit ensuite : «Bientôt viendra un groupe semblable à cet homme, [dont les membres] rechercheront le Livre d'Allah alors qu'ils seront ses ennemis, ils liront le Livre d'Allah et il ne dépassera pas leur gorge. Ils auront la tête rasée. Ainsi, lorsqu'ils sortiront [pour se révolter], frappez-les au cou.»<sup>2088</sup>"
    },
    {
        "number": "1838",
        "text": "L'Imām 'Alī (as) dit lorsqu'un homme récita ces versets<sup>2089</sup> : Les gens de Ḥarūrā' [les Kharidjites] font partie d'eux.<sup>2090</sup>"
    },
    {
        "number": "1839",
        "text": "L'Imām 'Alī (as) a dit : J'ai entendu le Messager d'Allah (s) dire : «Il viendra, à la fin des temps, un groupe d'hommes jeunes et aux esprits irréfléchis. Leurs paroles seront les meilleures paroles des vertueux, leurs prières sont plus nombreuses que les vôtres, leur récitation [du Coran] sera plus importante que vos récitations ; pourtant, leur foi ne dépassera pas leurs clavicules - ou il (s) dit : leurs gorges - ; ils quitteront la religion aussi rapidement que la flèche quitte l'arc; aussi, éliminez-les.»<sup>2091</sup>"
    }
])

s609['hadiths'].extend([
    {
        "number": "1840",
        "text": "L'Imām 'Alī (as) a dit alors qu'il passait près des corps des personnes tuées parmi les kharidjites : «Malheur à vous ! Celui qui vous a trompé a causé du tort.» On lui demanda: «Qui les a trompés, ô Emir des croyants ?» Il répondit : «Satan qui égare, ainsi que l'âme qui ordonne le mal les a trompés par de faux espoirs, ouvrant ainsi pour eux un vaste espace de désobéissance, et leur promettant la victoire. Ils les ont ainsi poussés dans le Feu.»<sup>2092</sup>"
    },
    {
        "number": "1841",
        "text": "Lorsque l'on demanda à l'Imām 'Alī (as) après que l'on ait tué les Kharidjites : «Ô Emir des croyants ! L'ensemble du groupe a-t-il été éliminé ?» Il répondit : «Pas du tout ! Par Allah, ils continuent à exister dans les lombes des hommes et dans les matrices des femmes. À chaque fois qu'une branche [un chef] émerge, il faut la couper jusqu'à ce que les derniers d'entre eux soient des brigands et des pillards.»<sup>2093</sup>"
    },
    {
        "number": "1842",
        "text": "L'Imām 'Alī (as) a dit : Ô gens ! J'ai percé l'œil de la dissension et nul n'aurait osé le faire à part moi, et ce alors que son obscurité s'était répandue et que sa férocité s'était intensifiée [que le soulèvement avait atteint son sommet].<sup>2094</sup>"
    }
])

s610['hadiths'].append({
    "number": "1843",
    "text": "L'Imām 'Alī (as) a dit : Ne combattez (tuez) pas les Kharidjites après moi, car celui qui aspire à la vérité et qui se trompe en la prenant pour autre chose n'est pas comme celui qui aspire au faux et qui l'a atteint.<sup>2095, 2096</sup>"
})

# ============================================================
# Part 125 (index 126) - La perte (page 333)
# ============================================================
p125 = 126
s611 = find_subpart(p125, "611")
s612 = find_subpart(p125, "612")
s613 = find_subpart(p125, "613")

for s in [s611, s612, s613]:
    clear_hadiths(s)

s611['hadiths'].extend([
    {"number": "1844", "text": "Le Messager d'Allah (s) a dit : Le perdant est celui qui a négligé de réformer [et de préparer] l'Au-delà.<sup>2096</sup>"},
    {"number": "1845", "text": "Le Messager d'Allah (s) a dit : Celui qui passe sa vie dans la quête de la vie d'ici-bas sera perdant dans sa transaction et il sera privé de toute réussite.<sup>2097</sup>"}
])

s612['introduction'] = "«Il en est parmi les gens qui adorent Allah d'une manière indécise. S'il leur arrive quelque bien, ils s'en tranquillisent, et s'il leur arrive une épreuve, ils détournent leur visage, perdant ainsi [le bien] de l'ici-bas et de l'Au-delà. Telle est la perte évidente !»<sup>2098</sup>"
s612['hadiths'].append({
    "number": "1846",
    "text": "Lorsqu'on lui demanda : «Qui a le [plus] grand malheur ?», l'Imām 'Alī (as) répondit: «C'est l'homme qui a abandonné la vie de ce monde pour la vie de ce monde. Il a ainsi manqué la vie de ce bas-monde et perdu l'Au-delà. C'est aussi un homme qui a adoré, a lutté et a jeûné par ostentation : il s'est donc interdit les délices de ce bas-monde pour ce bas-monde et en a récolté la fatigue. Néanmoins, s'il avait été sincère, il en aurait mérité la récompense.»<sup>2099</sup>"
})

s613['introduction'] = "«Dis : «Voulez-vous que Nous vous apprenions lesquels sont les plus grands perdants en œuvres? Ceux dont l'effort, dans la vie présente, s'est égaré, alors qu'ils s'imaginent faire le bien.»»<sup>2087</sup>"
# hadiths 1847-1852 are on page 334 (missing) - will be filled later

# ============================================================
# Part 127 (index 128) - Le sermon (page 335)
# L'Humilité (part 126, index 127) hadiths 1847-1852 are on page 334 (missing)
# ============================================================
p127 = 128
s616 = find_subpart(p127, "616")
clear_hadiths(s616)
s616['introduction'] = "«Nous consolidèrent son royaume et lui donnâmes la sagesse et un discours convaincant.»<sup>2108</sup>"
s616['hadiths'].extend([
    {
        "number": "1853",
        "text": "Sa'ad Ibn Ibrāhīm rapporte de son père: Le premier à avoir fait un sermon sur une chaire fut Ibrāhīm (as) lors de l'emprisonnement de Loth par les Romains. Ibrāhīm (as) les combattit jusqu'à ce qu'il sauve des Romains.<sup>2109</sup>"
    },
    {
        "number": "1854",
        "text": "Jābir a dit : Lorsqu'il [le Prophète (s)] faisait un sermon, ses yeux devenaient rouges, sa voix s'élevait et sa colère s'intensifiait, comme s'il était le garde d'une armée qui les avertissait d'une attaque imminente de l'ennemi.<sup>2110</sup>"
    },
    {
        "number": "1855",
        "source": "Al-Mu'jam al-Kabīr",
        "text": "Abū Umāma a dit: En vérité, lorsqu'il nommait un commandant, le Messager d'Allah (as) avait pour habitude de lui dire: «Abrège ton discours, raccourcis tes paroles.»<sup>2111</sup>"
    },
    {
        "number": "1856",
        "source": "Sunan Abī Dāwūd",
        "text": "rapporte de 'Ammār ibn Yāsir : Le Messager d'Allah (s) nous a ordonné d'abréger les discours.<sup>2112</sup>"
    },
    {
        "number": "1857",
        "source": "Sunan Abī Dāwūd",
        "text": "rapporte de Jābir ibn Samura al-Sawā'ī : Le Messager d'Allah (s) ne prolongeait pas son prêche du vendredi ; c'était juste quelques courtes paroles.<sup>2113</sup><br><br><span class=\"hadith-footnote\">(Voir également : 239. La prière (3), section 1147 ; 348. La parole, section 1619)</span>"
    }
])

# ============================================================
# Part 128 (index 129) - L'écriture (page 336)
# ============================================================
p128 = 129
s617 = find_subpart(p128, "617")
clear_hadiths(s617)
s617['introduction'] = "«Avant cela [le Coran], tu ne récitais aucun livre ni n'en écrivais aucun de ta main droite. Sinon, ceux qui nient la vérité auraient eu des doutes.»<sup>2114</sup>"
s617['hadiths'].extend([
    {"number": "1858", "text": "Le Messager d'Allah (s) a dit : La belle écriture renforce la clarté de la vérité.<sup>2115</sup>"},
    {
        "number": "1859",
        "text": "Le Messager d'Allah (s) a dit au sujet de la parole du Très-Haut «ou un vestige d'une science»<sup>2116</sup> : [Cela signifie] l'écriture.<sup>2117</sup>"
    },
    {
        "number": "1860",
        "source": "Al-Durr al-Manthūr",
        "text": "rapporte de 'Aṭā' ibn Yasār : Le Messager d'Allah (s) fut interrogé au sujet de l'écriture. Il (s) dit : «C'est [en premier lieu] un prophète qui l'a enseignée, et ceux qui l'accompagnaient l'ont apprise.»<sup>2118</sup>"
    },
    {"number": "1861", "text": "L'Imām 'Alī (as) a dit : L'écriture est la langue de la main.<sup>2119</sup>"},
    {
        "number": "1862",
        "text": "Parmi les paroles qu'il a adressées à son scribe 'Ubaydullāh ibn Abī Rāfi', l'Imām 'Alī (as) a dit : Mets un flocon de coton dans ton encrier, garde la pointe de ton calame longue, laisse un espace entre les lignes, et joins les lettres, car cela est plus à même de créer une belle écriture.<sup>2120</sup>"
    },
    {
        "number": "1863",
        "text": "L'Imām 'Alī (as) a dit : Fends la pointe de ton calame et épaissis son extrémité, incline-la vers la droite et ton écriture s'embellira.<sup>2121</sup>"
    }
])

# ============================================================
# Part 129 (index 130) - La sincérité (page 337)
# ============================================================
p129 = 130
s618 = find_subpart(p129, "618")
clear_hadiths(s618)
s618['introduction'] = "«Par Ta puissance ! dit [Satan]. Je les séduirai assurément tous, sauf Tes serviteurs élus parmi eux.»<sup>2122</sup><br><br><span class=\"hadith-footnote\">(Voir également : Coran 2:112, 2:139, 2:196, 2:207, 2:238, 2:265, 3:20, 6:52, 6:79, 6:162, 12:24, 18:28, 18:110, 22:31, 30:38, 31:22, 37:40, 39:2-3, 39:11, 39:14, 39:29, 40:14, 72:18, 72:20, 76:9, 92:20, 97:5)</span>"
s618['hadiths'].extend([
    {"number": "1864", "text": "Le Messager d'Allah (s) a dit : Tous les savants seront damnés sauf ceux qui ont œuvré [sur la base de leur savoir], et ceux qui ont œuvré seront damnés sauf les sincères, et les sincères sont [eux-mêmes] en danger.<sup>2123</sup>"},
    {"number": "1865", "text": "L'Imām 'Alī (as) a dit : La sincérité est le plus haut point de la religion.<sup>2124</sup>"},
    {"number": "1866", "text": "L'Imām 'Alī (as) a dit : La sincérité est l'adoration des rapprochés [d'Allah].<sup>2125</sup>"},
    {"number": "1867", "text": "L'Imām 'Alī (as) a dit : La sincérité est le fondement de l'adoration.<sup>2126</sup>"},
    {"number": "1868", "text": "L'Imām 'Alī (as) a dit : La sincérité est le sommet de la foi.<sup>2127</sup>"},
    {"number": "1869", "text": "L'Imām 'Alī (as) a dit : Le salut se trouve dans la sincérité.<sup>2128</sup>"}
])


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1802-1869 (gaps: 1827-1831 p.329, 1847-1852 p.334)")
