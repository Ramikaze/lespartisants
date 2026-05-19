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

def ensure_hadiths(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# Chapter 122 (index 123) - L'ISSUE (suite)
# ============================================================
p122 = 123

s606 = find_subpart(p122, "606")
ensure_hadiths(s606)
s606['hadiths'].extend([
    {
        "number": "1831",
        "text": "L'Imām 'Alī (as) a dit : Si tu veux qu'Allah t'épargne une mauvaise issue, sache que le bien qui t'arrive est dû à la grâce d'Allah et à Sa faveur, et que pour ce qui t'arrive de mal, [sache qu'] Allah t'a donné un sursis et un répit. Crains Sa clémence et Son pardon à ton égard.<sup>2081</sup>"
    },
    {
        "number": "1832",
        "text": "L'Imām al-Ṣādiq (as) a dit en s'adressant à une personne : Si tu veux que tes actions aient une bonne issue et que l'on prenne ton âme alors que tu as accompli les meilleures œuvres, alors honore les droits d'Allah, n'utilise pas Ses grâces pour Lui désobéir, que Sa clémence vis-à-vis de toi ne soit pas source d'illusion [et de négligence], et honore toute personne qui nous évoque en bien et a de l'affection pour nous.<sup>2082</sup>"
    }
])

# ============================================================
# Chapter 123 (index 124) - LE SERVICE
# ============================================================
p123 = 124

s607 = find_subpart(p123, "607")
ensure_hadiths(s607)
s607['hadiths'].extend([
    {
        "number": "1833",
        "text": "Le Messager d'Allah (s) a dit : Dès qu'un musulman rend service à un groupe de musulmans, Allah lui donnera des serviteurs dont le nombre sera équivalent [au groupe à qui il a rendu service] au Paradis.<sup>2083</sup>"
    },
    {
        "number": "1834",
        "text": "Le Messager d'Allah (s) a dit : Le service rendu par un croyant à son frère [mérite l'atteinte d'] une station dont la grandeur ne peut être perçue qu'en rendant le même service.<sup>2084</sup>"
    },
    {
        "number": "1835",
        "text": "<em>Al-Kāfī</em> : Jamīl a dit : l'Imām al-Ṣādiq (as) a dit : «Les croyants sont les serviteurs les uns des autres.» [Jamīl dit :] Je demandai : «Comment sont-ils les serviteurs les uns des autres ?» Il répondit : «En étant bénéfiques les uns aux autres.»<sup>2085</sup>"
    },
    {
        "number": "1836",
        "text": "L'Imām al-Ṣādiq (as) a dit : Rends service à ton frère et s'il abuse de toi, pas de marque d'honneur [ne le sers pas].<sup>2086</sup><br><br><span class=\"reference-note\">(Voir également : 288. Le savoir, section 1353 ; 2. La rémunération)</span>"
    }
])

# ============================================================
# Chapter 124 (index 125) - LES KHARIDJITES
# ============================================================
p124 = 125

s608 = find_subpart(p124, "608")
ensure_hadiths(s608)
s608['introduction'] = "«Dis : «Voulez-vous que Nous vous apprenions lesquels sont les plus grands perdants en œuvres ? Ceux dont l'effort, dans la vie présente, s'est égaré, alors qu'ils s'imaginent faire le bien».»<sup>2087</sup>"
s608['hadiths'].extend([
    {
        "number": "1837",
        "text": "<em>Kanz al-'Ummāl</em> : 'Abdullāh Ibn Amrū a dit : Un homme vint voir le Prophète (s) le jour de [la bataille de] Ḥunayn alors qu'il était occupé à partager le butin. L'homme lui dit : «Ô Muḥammad ! Sois équitable.» Le Prophète (s) lui dit : «Malheur à toi ! Qui peut être équitable si je ne le suis pas ?» - ou bien il (s) dit : - «Auprès de qui aspires-tu trouver l'équité si ce n'est auprès de moi ?» Le Prophète (s) dit ensuite : «Bientôt viendra un groupe semblable à cet homme, [dont les membres] rechercheront le Livre d'Allah alors qu'ils seront ses ennemis, ils liront le Livre d'Allah et pourtant, il ne dépassera pas leur gorge. Ils auront la tête rasée. Ainsi, lorsqu'ils sortiront [pour se révolter], frappez-les au cou.»<sup>2088</sup>"
    },
    {
        "number": "1838",
        "text": "L'Imām 'Alī (as) dit lorsqu'un homme récita ces versets<sup>2089</sup> : Les gens de Ḥarūrā' [les Kharidjites] font partie d'eux.<sup>2090</sup>"
    },
    {
        "number": "1839",
        "text": "L'Imām 'Alī (as) a dit : J'ai entendu le Messager d'Allah (s) dire : «Il viendra, à la fin des temps, un groupe d'hommes jeunes et aux esprits irréfléchis. Leurs paroles seront les meilleures paroles des vertueux, leurs prières sont plus nombreuses que les vôtres, leur récitation [du Coran] sera plus importante que vos récitations ; pourtant, leur foi ne dépassera pas leurs clavicules - ou il (s) dit : leurs gorges - ; ils quitteront la religion aussi rapidement que la flèche quitte l'arc ; aussi, éliminez-les.»<sup>2091</sup>"
    }
])

s609 = find_subpart(p124, "609")
ensure_hadiths(s609)
s609['hadiths'].extend([
    {
        "number": "1840",
        "text": "L'Imām 'Alī (as) a dit alors qu'il passait près des corps des personnes tuées parmi les kharidjites : «Malheur à vous ! Celui qui vous a trompé vous a causé du tort.» On lui demanda : «Qui les a trompés, ô Emir des croyants ?» Il répondit : «Satan qui égare, ainsi que l'âme qui ordonne le mal les a trompés par de faux espoirs, ouvrant ainsi pour eux un vaste espace de désobéissance, et leur promettant la victoire. Ils les ont ainsi poussés dans le Feu.»<sup>2092</sup>"
    },
    {
        "number": "1841",
        "text": "Lorsque l'on demanda à l'Imām 'Alī (as) après que l'on ait tué les Kharidjites : «Ô Emir des croyants ! L'ensemble du groupe a-t-il été éliminé ?» Il répondit : «Pas du tout ! Par Allah, ils continuent à exister dans les lombes des hommes et dans les matrices des femmes. A chaque fois qu'une branche [un chef] émerge, il faut la couper jusqu'à ce que les derniers d'entre eux soient des brigands et des pillards.»<sup>2093</sup>"
    },
    {
        "number": "1842",
        "text": "L'Imām 'Alī (as) a dit : Ô gens ! J'ai percé l'œil de la dissension et nul n'aurait osé le faire à part moi, et ce alors que son obscurité s'était répandue et que sa férocité s'était intensifiée [que le soulèvement avait atteint son sommet].<sup>2094</sup>"
    }
])

s610 = find_subpart(p124, "610")
ensure_hadiths(s610)
s610['hadiths'].append({
    "number": "1843",
    "text": "L'Imām 'Alī (as) a dit : Ne combattez (tuez) pas les Kharidjites après moi, car celui qui aspire à la vérité et qui se trompe en la prenant pour autre chose n'est pas comme celui qui aspire au faux et qui l'a atteint.<sup>2095</sup>"
})

# ============================================================
# Chapter 125 (index 126) - LA PERTE
# ============================================================
p125 = 126

s611 = find_subpart(p125, "611")
ensure_hadiths(s611)
s611['hadiths'].extend([
    {
        "number": "1844",
        "text": "Le Messager d'Allah (s) a dit : Le perdant est celui qui a négligé de réformer [et de préparer] l'Au-delà.<sup>2096</sup>"
    },
    {
        "number": "1845",
        "text": "Le Messager d'Allah (s) a dit : Celui qui passe sa vie dans la quête de la vie d'ici-bas sera perdant dans sa transaction et il sera privé de toute réussite.<sup>2097</sup>"
    }
])

s612 = find_subpart(p125, "612")
ensure_hadiths(s612)
s612['introduction'] = "«Il en est parmi les gens qui adorent Allah d'une manière indécise. S'il leur arrive quelque bien, ils s'en tranquillisent, et s'il leur arrive une épreuve, ils détournent leur visage, perdant ainsi [le bien] de l'ici bas et de l'Au-delà. Telle est la perte évidente !»<sup>2098</sup>"
s612['hadiths'].append({
    "number": "1846",
    "text": "Lorsqu'on lui demanda : «Qui a le [plus] grand malheur ?», l'Imām 'Alī (as) répondit : «C'est l'homme qui a abandonné la vie de ce monde pour la vie de ce monde. Il a ainsi manqué la vie de ce bas-monde et perdu l'Au-delà. C'est aussi un homme qui a adoré, a lutté et a jeûné par ostentation : il s'est donc interdit les délices de ce bas-monde et en a récolté la fatigue. Néanmoins, s'il avait été sincère, il en aurait mérité la récompense.»<sup>2099</sup>"
})

s613 = find_subpart(p125, "613")
ensure_hadiths(s613)
s613['introduction'] = "«Dis : «Voulez-vous que Nous vous apprenions lesquels sont les plus grands perdants en œuvres ? Ceux dont l'effort, dans la vie présente, s'est égaré, alors qu'ils s'imaginent faire le bien.»»<sup>2100</sup>"
s613['hadiths'].append({
    "number": "1847",
    "text": "L'Imām 'Alī (as) a dit : En vérité, le plus grand perdant dans sa transaction et celui dont les efforts sont les plus vains est l'homme qui a usé son corps dans la quête de sa fortune, bien que le destin ne l'ait pas aidé dans son dessein. Il a ainsi quitté ce monde avec regret et fait face à l'Au-delà avec ses [funestes] conséquences.<sup>2101</sup>"
})

# ============================================================
# Chapter 126 (index 127) - L'HUMILITÉ
# ============================================================
p126 = 127

s614 = find_subpart(p126, "614")
ensure_hadiths(s614)
s614['introduction'] = "«Le moment n'est-il pas venu pour ceux qui ont cru, que leurs cœurs s'humilient à l'évocation d'Allah et devant ce qui est descendu de la Vérité ?»<sup>2102</sup>"
s614['hadiths'].extend([
    {
        "number": "1848",
        "text": "<em>Irshād al-Qulūb</em> : Dans le <em>ḥadīth</em> de l'ascension (<em>mi'rāj</em>), [Allah a dit] : Dès qu'un serviteur vient à Me connaître et s'humilie devant Moi, toute chose s'humilie devant lui.<sup>2103</sup>"
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

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 1831-1850 injected (pages 330-334)")
print("Chapters: 122 (+1831-1832), 123 (1833-1836), 124 (1837-1843), 125 (1844-1847), 126 (1848-1850)")
print("Total hadiths added: 20")
