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


# Part 104 (index 105) - La bienfaisance
p104 = 105
s538 = find_subpart(p104, "538")
s539 = find_subpart(p104, "539")
s540 = find_subpart(p104, "540")

for s in [s538, s539, s540]:
    clear_hadiths(s)

s538['introduction'] = "«Certes, Allah commande l'équité, la bienfaisance et l'assistance aux proches. Et Il interdit la turpitude, l'acte répréhensible et la rébellion. Il vous exhorte afin que vous vous souveniez.»<sup>1855</sup>"
s538['hadiths'].extend([
    {
        "number": "1618",
        "text": "Le Messager d'Allah (s) a dit : Les cœurs ont été prédisposés à l'amour de celui qui est bienfaisant envers eux et à la haine de celui qui est malfaisant envers eux.<sup>1856</sup>"
    },
    {
        "number": "1619",
        "text": "L'Imām 'Alī (as) a dit : La bienfaisance t'incombe, car c'est la meilleure des cultures et la plus profitable des marchandises.<sup>1857</sup>"
    },
    {
        "number": "1620",
        "text": "L'Imām 'Alī (as) a dit : Quelle bonne provision pour la Résurrection est la bienfaisance envers les serviteurs !<sup>1858</sup>"
    },
    {
        "number": "1621",
        "text": "L'Imām 'Alī (as) a dit : L'aumône (<i>zakāt</i>) de la victoire est la bienfaisance.<sup>1859</sup>"
    },
    {
        "number": "1622",
        "text": "L'Imām 'Alī (as) a dit : Celui dont la bienfaisance est profuse sera aimé de ses frères.<sup>1860</sup>"
    },
    {
        "number": "1623",
        "text": "L'Imām 'Alī (as) a dit : Par la bienfaisance, on gagne les cœurs.<sup>1861</sup>"
    }
])

s539['hadiths'].extend([
    {
        "number": "1624",
        "text": "Le Messager d'Allah (s) a dit : Sois bienfaisant envers celui qui a été malfaisant à ton égard.<sup>1862</sup>"
    },
    {
        "number": "1625",
        "text": "L'Imām 'Alī (as) a dit : En vérité, ta bienfaisance envers les ennemis et les jaloux les irritera plus que le fait que tu les offenses, et c'est aussi une invitation à leur réforme.<sup>1863</sup><br><br><span class=\"hadith-footnote\">(Voir également : 375. L'équité, section 1728 ; 159. Les liens familiaux, section 813)</span>"
    }
])

s540['hadiths'].append({
    "number": "1626",
    "source": "Kanz al-'Ummāl",
    "text": "rapporte de Salmān ibn 'Āmir al-Ḍabbī : «Ô Messager d'Allah ! Mon père avait coutume de faire preuve d'hospitalité vis-à-vis de l'invité, d'honorer le voisin, d'être fidèle à sa parole et de donner dans l'adversité. En quoi cela lui sera utile ?» Il répondit : «Est-il mort en étant associationiste ?» Je lui répondis : «Oui.» Il me dit : «En vérité, cela ne lui sera pas utile. En revanche, cela restera pour ses descendants dans le sens où ils ne seront jamais déshonorés, ni humiliés, ni ne souffriront de pauvreté.»<sup>1864</sup>"
})


# Part 105 (index 106) - La mémoire
p105 = 106
s541 = find_subpart(p105, "541")
s542 = find_subpart(p105, "542")
s543 = find_subpart(p105, "543")

for s in [s541, s542, s543]:
    clear_hadiths(s)

s541['hadiths'].append({
    "number": "1627",
    "text": "L'Imām al-Ṣādiq (as) a dit – selon un hadith rapporté par Mufaḍḍal : As-tu déjà pensé à ce qu'aurait été l'état de l'homme s'il était dépourvu de cette faculté qu'est la mémoire? Combien de difficultés vivrait-il au quotidien, dans sa vie et ses expériences, s'il ne pouvait pas se rappeler de ce qui lui est bénéfique et de ce qui lui est nuisible, de ce qu'il a donné et de ce qu'il a reçu, de ce qu'il a vu et de ce qu'il a entendu ? ... Il ne retrouverait plus son chemin, même après l'avoir emprunté maintes fois, et il ne mémoriserait aucun savoir, même s'il en avait fait l'apprentissage durant toute une vie. Il ne professerait aucune religion, aucune expérience ne lui serait profitable, et il ne pourrait tirer aucune leçon d'une chose s'étant passée. En vérité, il aurait perdu la base même de son humanité.<sup>1865</sup>"
})

s542['hadiths'].append({
    "number": "1628",
    "text": "Le Messager d'Allah (s) a dit : Celui qui apprend dans son enfance est semblable à [celui qui] sculpte dans la pierre, alors que celui qui apprend en étant adulte est semblable à celui qui écrit sur l'eau.<sup>1866</sup>"
})

s543['hadiths'].append({
    "number": "1629",
    "text": "Le Messager d'Allah (s) a dit : Trois choses éloignent l'oubli et ravivent la mémoire: la lecture du Coran, se brosser les dents, et le jeûne.<sup>1867</sup>"
})


# Part 106 (index 107) - La rancune
p106 = 107
s544 = find_subpart(p106, "544")
s545 = find_subpart(p106, "545")

for s in [s544, s545]:
    clear_hadiths(s)

s544['hadiths'].extend([
    {
        "number": "1630",
        "text": "L'Imām 'Alī (as) a dit : La rancune est le plus bas des défauts.<sup>1868</sup>"
    },
    {
        "number": "1631",
        "text": "L'Imām 'Alī (as) a dit : La rancune est source de colère.<sup>1869</sup>"
    },
    {
        "number": "1632",
        "text": "L'Imām 'Alī (as) a dit : La rancune est le trait caractéristique des jaloux.<sup>1870</sup>"
    },
    {
        "number": "1633",
        "text": "L'Imām 'Alī (as) a dit : La rancune est un feu qui n'est éteint que par la victoire [contre son opposant].<sup>1871</sup>"
    },
    {
        "number": "1634",
        "text": "L'Imām 'Alī (as) a dit : La rancune est la cause des dissensions.<sup>1872</sup>"
    },
    {
        "number": "1635",
        "text": "L'Imām 'Alī (as) a dit : Le rancunier a l'âme torturée, et son anxiété est multipliée.<sup>1873</sup>"
    },
    {
        "number": "1636",
        "text": "L'Imām 'Alī (as) a dit : Le rancunier n'a pas d'affection.<sup>1874</sup>"
    },
    {
        "number": "1637",
        "text": "L'Imām al-Hādī (as) a dit : Le reproche [exprimé] est préférable à la rancune [nourrie intérieurement].<sup>1875</sup>"
    },
    {
        "number": "1638",
        "text": "L'Imām al-'Askarī (as) a dit: Les personnes les moins apaisées sont les rancuniers.<sup>1876</sup>"
    }
])

s545['hadiths'].append({
    "number": "1639",
    "text": "L'Imām Ṣādiq (as) a dit : Le croyant a de la rancune tant qu'il est avec la personne, mais dès qu'il l'a quitte, sa rancune disparaît.<sup>1877</sup>"
})


# Part 107 (index 108) - Le dénigrement
p107 = 108
s546 = find_subpart(p107, "546")
s547 = find_subpart(p107, "547")

for s in [s546, s547]:
    clear_hadiths(s)

s546['hadiths'].extend([
    {
        "number": "1640",
        "text": "Luqmān (as) a dit en s'adressant à son fils : Ô mon fils ! Ne dénigre jamais un être pour ses vêtements usés car ton Dieu et son Dieu est le même [Dieu] unique.<sup>1878</sup>"
    },
    {
        "number": "1641",
        "text": "Le Messager d'Allah (s) a dit : Que l'un de vous ne fasse pas preuve de mépris envers l'une des créatures d'Allah, car nul ne sait laquelle d'entre elles est l'ami d'Allah.<sup>1879</sup>"
    },
    {
        "number": "1642",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah continuera à dénigrer et à détester celui qui aura dénigré un pauvre croyant jusqu'à ce qu'il cesse son dénigrement.<sup>1880</sup>"
    }
])

s547['hadiths'].extend([
    {
        "number": "1643",
        "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, Allah le Très-Haut fera connaître celui qui a humilié ou a dénigré un croyant ou une croyante à cause de sa pauvreté ou de son peu de moyens, et Il le déshonorera.<sup>1881</sup>"
    },
    {
        "number": "1644",
        "text": "Le Messager d'Allah (s) a dit : Ne dénigre aucune personne parmi les musulmans car en vérité, le plus petit d'entre eux est grand auprès d'Allah.<sup>1882</sup>"
    },
    {
        "number": "1645",
        "text": "Le Messager d'Allah (s) a dit : Il suffit au fils d'Adam pour faire preuve de méchanceté de dénigrer son frère musulman.<sup>1883</sup>"
    },
    {
        "number": "1646",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut a dit : «Que celui qui a offensé l'un de Mes amis s'apprête à Me combattre, et Je suis très rapide lorsqu'il s'agit de secourir Mes amis.»<sup>1884</sup>"
    }
])


# Part 108 (index 109) - La vérité
p108 = 109
s548 = find_subpart(p108, "548")
clear_hadiths(s548)

s548['introduction'] = "«Bien au contraire, Nous lançons la Vérité contre le faux qui le subjugue, et le voilà qui disparaît. Et malheur à vous pour ce que vous attribuez [injustement à Allah] !»<sup>1885</sup>"
s548['hadiths'].extend([
    {
        "number": "1647",
        "text": "L'Imām 'Alī (as) a dit : La vérité est le plus fort des appuis.<sup>1886</sup>"
    },
    {
        "number": "1648",
        "text": "L'Imām 'Alī (as) a dit : Sachez que la ..." # Incomplete sentence, wait let me check the image. It is cut off. "Sachez que la ..." is on the bottom of page 301.
    }
])


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1618-1648")
