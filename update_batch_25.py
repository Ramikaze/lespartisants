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
# Part 116 (index 117) - Le bain - suite (page 320)
# ============================================================
p116 = 117
s587 = find_subpart(p116, "587")
clear_hadiths(s587)
s587['hadiths'].extend([
    {
        "number": "1769",
        "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses détruisent le corps et peuvent provoquer la mort : manger des restes de viande de la veille, prendre un bain en ayant le ventre plein, et avoir des relations intimes avec des personnes âgées.<sup>2017</sup>"
    },
    {
        "number": "1770",
        "text": "L'Imām al-Ṣādiq (as) a dit : Ne prends un bain que si tu as quelque chose dans le ventre qui va refroidir la température de ton estomac, car cela renforce la santé du corps. Mais ne prends pas de bain lorsque tu as l'estomac trop plein.<sup>2018</sup>"
    }
])

# ============================================================
# Part 117 (index 118) - Le besoin (pages 320-322)
# ============================================================
p117 = 118
s588 = find_subpart(p117, "588")
s589 = find_subpart(p117, "589")
s590 = find_subpart(p117, "590")
s591 = find_subpart(p117, "591")

for s in [s588, s589, s590, s591]:
    clear_hadiths(s)

s588['hadiths'].extend([
    {
        "number": "1771",
        "text": "L'Imām 'Alī (as) a dit : Prodigue à qui tu veux et tu seras son maître ; sollicite ce dont tu as besoin auprès de qui tu veux et tu seras son prisonnier ; ne dépends de qui tu veux [pour un besoin] et tu seras son égal.<sup>2019</sup>"
    },
    {
        "number": "1772",
        "text": "L'Imām 'Alī (as) a dit : Tu te seras rabaissé aux yeux de celui auprès de qui tu as sollicité un besoin.<sup>2020</sup>"
    }
])

s589['hadiths'].extend([
    {
        "number": "1773",
        "text": "L'Imām al-Ṣādiq (s) a dit : Allah le Tout-Puissant a dit : «Les créatures sont Mes enfants, celles que J'aime le plus sont celles qui sont les plus douces les unes avec les autres et s'efforcent le plus de satisfaire les besoins des autres.»<sup>2021</sup>"
    },
    {
        "number": "1774",
        "text": "Le Messager d'Allah (s) a dit : Celui qui s'efforce d'aider son frère et de lui être bénéfique aura la rétribution d'un combattant dans la voie d'Allah.<sup>2022</sup>"
    },
    {
        "number": "1775",
        "text": "Le Messager d'Allah (s) a dit : Celui qui s'efforce de satisfaire le besoin de son frère croyant est comme celui qui a adoré Allah neuf mille ans en jeûnant le jour et en priant la nuit.<sup>2023</sup>"
    },
    {
        "number": "1776",
        "text": "Le Messager d'Allah (s) a dit : Celui qui a satisfait le besoin de son frère croyant est comme celui qui a adoré Allah sa vie entière.<sup>2024</sup>"
    },
    {
        "number": "1777",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Tout-Puissant inscrit un million de bonnes actions à celui qui s'est efforce de satisfaire le besoin de son frère musulman pour Allah.<sup>2025</sup>"
    },
    {
        "number": "1778",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah satisfera le besoin de celui qui s'engage à satisfaire le besoin de son frère croyant et musulman tant qu'il reste engagé à satisfaire le besoin de son frère.<sup>2026</sup>"
    },
    {
        "number": "1779",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui s'efforce de satisfaire le besoin de son frère est comme celui qui court entre Ṣafā et Marwā.<sup>2027</sup>"
    },
    {
        "number": "1780",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour de la Résurrection, Allah le Tout-Puissant satisfera cent mille des besoins de celui qui a satisfait le besoin de son frère croyant, le premier étant le Paradis.<sup>2028</sup>"
    },
    {
        "number": "1781",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, satisfaire le besoin d'un croyant est plus aimé d'Allah que l'accomplissement de vingt pèlerinages obligatoires (<i>ḥajj</i>) en dépensant cent mille [dinars ou dirhams] lors de chaque pèlerinage.<sup>2029</sup><br><br><span class=\"hadith-footnote\">(Voir également : 272. La bienseance (1) ; 104. La bienfaisance ; 5. Le frère, section 41)</span>"
    }
])

s590['hadiths'].extend([
    {
        "number": "1782",
        "text": "L'Imām al-Bāqir (as) a dit : La malédiction d'Allah le Tout-Puissant s'abattra sur tout musulman qui n'accueille pas son frère qui se rend chez lui pour lui rendre visite ou pour demander son accord ou qui n'a besoin de demander la permission d'entrer, et cela jusqu'à ce qu'ils se voient.<sup>2030</sup>"
    },
    {
        "number": "1783",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui a demandé à son frère croyant une chose dont il a besoin alors qu'il est en situation de difficulté, et qui l'a renvoyé les mains vides alors qu'il pouvait exaucer sa requête directement ou par le biais de quelqu'un d'autre, Allah le ressuscitera le Jour de la Résurrection alors qu'il sera enchaîné des mains jusqu'au cou, et ce jusqu'à ce qu'Allah ait terminé les comptes de l'ensemble des créatures.<sup>2031</sup>"
    },
    {
        "number": "1784",
        "text": "L'Imām al-Ṣādiq (as) a dit : Toute personne parmi nos partisans (<i>shī'a</i>) auprès de laquelle un de nos frères est venu implorer une aide concernant un besoin et qui n'a pas répondu alors qu'elle pouvait le faire, sera accablée par Allah le Tout-Puissant pour avoir satisfait les besoins de l'un de nos ennemis et châtiée pour cela le Jour de la Résurrection.<sup>2032</sup>"
    },
    {
        "number": "1785",
        "text": "L'Imām al-Ṣādiq (as) a dit : Par Allah, tout croyant qui refuse ses biens à un croyant [en vue de l'aider] alors qu'il en a besoin, ne goûtera pas les nourritures du Paradis et il ne boira pas la liqueur cachetée [du Paradis].<sup>2033</sup>"
    }
])

s591['hadiths'].append({
    "number": "1786",
    "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, dès qu'un homme me sollicite pour un besoin, j'entreprends de le satisfaire de peur que son besoin ne soit satisfait [entre temps] et qu'il n'ait plus besoin de mon aide lorsqu'elle lui parviendra.<sup>2034</sup>"
})

# ============================================================
# Part 117 (index 118) - Le besoin - s592 "La façon d'exprimer"
# The images only show up to p322 with hadith 1786 ending s591
# and p323 is missing from this batch - will handle s592 next time
# But check if there's content on page 323 visible...
# Page 323 is NOT in this batch, so skip s592 for now

# ============================================================
# Part 118 (index 119) - La précaution (page 323 missing - only 1792 shown on page 324)
# ============================================================
# Page 323 not provided - but 1792 visible at top of page 324
p118 = 119
s593 = find_subpart(p118, "593")
clear_hadiths(s593)
s593['hadiths'].append({
    "number": "1792",
    "text": "L'Imām al-Ṣādiq (as) a dit : Fais preuve de précaution en toute chose que tu as la possibilité de réaliser.<sup>2040</sup>"
})

# ============================================================
# Part 119 (index 120) - La vie (page 324)
# ============================================================
p119 = 120
s594 = find_subpart(p119, "594")
s595 = find_subpart(p119, "595")
s596 = find_subpart(p119, "596")
s597 = find_subpart(p119, "597")

for s in [s594, s595, s596, s597]:
    clear_hadiths(s)

s594['hadiths'].append({
    "number": "1793",
    "text": "L'Imām 'Alī (as) a dit : Sachez que l'homme peut se rassasier et se lasser de toute chose sauf de la vie, car il ne trouve aucun confort dans la mort.<sup>2041</sup>"
})

s595['introduction'] = "«Nous avons fait de l'eau toute chose vivante.»<sup>2042</sup>"
s595['hadiths'].append({
    "number": "1794",
    "text": "L'Imām al-Ṣādiq (as) a dit : Le goût de l'eau est la vie.<sup>2043</sup>"
})

s596['hadiths'].append({
    "number": "1795",
    "text": "L'Imām al-'Askarī (as) a dit : Ce qui est meilleur que la vie est la chose qui te dégoûterait de la vie si tu venais à la perdre, et ce qui est pire que la mort est la chose qui te ferait aimer la mort si elle venait à te toucher.<sup>2044</sup>"
})

s597['hadiths'].append({
    "number": "1796",
    "text": "L'Imām 'Alī (as) a dit : Il n'y a de vie qu'avec la religion, et il n'y a de mort qu'avec la négation de la vérité certaine.<sup>2045</sup>"
})


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1769-1796 (skipping 1787-1791 - page 323 needed)")
