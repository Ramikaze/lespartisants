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

# Part 91 (index 92) - La guerre
p91 = 92
s487 = find_subpart(p91, "487") # Already cleared in previous script, but appending 1465, 1466
s488 = find_subpart(p91, "488")
s489 = find_subpart(p91, "489")
s490 = find_subpart(p91, "490")
s491 = find_subpart(p91, "491")
s492 = find_subpart(p91, "492")

for s in [s488, s489, s490, s491, s492]:
    clear_hadiths(s)

s487['hadiths'].extend([
    {
        "number": "1465",
        "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) a interdit d'empoisonner les terres des polythéistes.<sup>1680</sup>"
    },
    {
        "number": "1466",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Si vous avez capturé un prisonnier qui ne peut plus marcher et que vous ne possédez aucune monture, alors libérez-le et ne le tuez point, car vous ne savez pas quel serait le jugement de l'Imām à son sujet.<sup>1681</sup>"
    }
])

s488['hadiths'].append({
    "number": "1467",
    "text": "L'Imām al-Bāqir (as) a dit : En vérité, 'Alī (as) avait pour habitude de dire : Je préfèrerais qu'un oiseau de proie me saisisse et m'enlève plutôt que d'attribuer au Messager d'Allah (s) une parole qu'il n'a pas dite. J'ai entendu le Messager d'Allah (s) dire le jour de la Bataille du Fossé (<i>khandaq</i>) : «La guerre est une ruse», et il disait aussi : «Dites ce que vous voulez.»<sup>1682</sup>"
})

s489['introduction'] = "«Quiconque, ce jour-là, leur tourne le dos - à moins que ce soit par tactique de combat, ou pour rallier un autre groupe -, celui-là encourt la colère d'Allah et son refuge sera l'Enfer. Et quelle mauvaise destination !»<sup>1683</sup>"
s489['hadiths'].extend([
    {
        "number": "1468",
        "text": "L'Imām 'Alī (as) a dit en s'adressant à ses compagnons lors de la bataille de Ṣiffīn : Multipliez les attaques, ayez honte de la fuite car c'est un déshonneur qui continue à peser sur les générations suivantes, ainsi qu'un Feu le Jour des comptes. Par conséquent, sacrifiez vos âmes pour d'autres âmes, et allez vers la mort d'un pas léger.<sup>1684</sup>"
    },
    {
        "number": "1469",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui fuit un combat face à deux hommes est considéré comme un déserteur, mais celui qui fuit un combat face à trois hommes n'est pas considéré comme un déserteur.<sup>1685</sup>"
    },
    {
        "number": "1470",
        "text": "L'Imām al-Riḍā (as) a dit : Allah a interdit la fuite lors du combat pour ce qu'elle entraîne comme affaiblissement de la religion et comme mépris envers les messagers et les Imāms justes (as).<sup>1686</sup>"
    }
])

s490['hadiths'].append({
    "number": "1471",
    "text": "Le Messager d'Allah (s) a dit : Combattre un frère musulman est une infidélité, et l'injurier est une immoralité.<sup>1687</sup>"
})

s491['hadiths'].append({
    "number": "1472",
    "text": "L'Imām 'Alī (as) a dit lors d'une confrontation avec l'ennemi : Ô Allah ! Vers Toi les cœurs se sont dirigés et les cous se sont tendus... Ô Allah ! Nous nous plaignons de l'absence de notre Prophète, du grand nombre de nos ennemis et de la dispersion de nos désirs !<sup>1688</sup>"
})

s492['hadiths'].append({
    "number": "1473",
    "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) a dit : En vérité, le Messager d'Allah est parti à la guerre avec les femmes afin qu'elles pansent les plaies des blessés.<sup>1689</sup><br><br><span class=\"hadith-footnote\">(Voir également : 360. La femme, section 1644)</span>"
})

# Part 92 (index 93) - Le belliciste
p92 = 93
s493 = find_subpart(p92, "493")
clear_hadiths(s493)

s493['introduction'] = "«La récompense de ceux qui font la guerre contre Allah et Son messager, s'efforcent de semer la corruption sur la terre, est qu'ils soient tués, ou crucifiés, ou que soient coupées leur main et leur jambe opposées, ou qu'ils soient expulsés du pays.»<sup>1690</sup>"
s493['hadiths'].extend([
    {
        "number": "1474",
        "text": "Le Messager d'Allah (s) a dit : Le sang de celui qui brandit son épée [contre les gens] doit être versé.<sup>1691</sup>"
    },
    {
        "number": "1475",
        "text": "L'Imām 'Alī (as) a dit : Tuez le voleur armé, et concernant les conséquences d'un tel acte, je serai responsable de son sang.<sup>1692</sup>"
    },
    {
        "number": "1476",
        "text": "L'Imām al-Bāqir (as) a dit : Si un homme entre chez toi et veut attaquer ta famille et tes biens, frappe-le en premier si tu le peux, car le voleur est un belliciste contre Allah et Son Messager, puis tue-le. Je serai votre garant si vous êtes redevable de quelque chose.<sup>1693</sup>"
    },
    {
        "number": "1477",
        "text": "L'Imām al-Bāqir (as) a dit : Celui porte une arme la nuit est un belliciste, sauf s'il s'agit d'une personne au sujet de laquelle il n'y a pas de doute.<sup>1694</sup>"
    },
    {
        "number": "1478",
        "text": "Interrogé au sujet du bannissement du belliciste, l'Imām al-Bāqir (as) répondit : Il doit être banni du pays. En vérité, 'Alī (as) a exilé deux hommes de Kūfa vers une autre contrée.<sup>1695</sup><br><br><span class=\"hadith-footnote\">(Voir également : 154. L'usure, section 800)</span>"
    }
])

# Part 93 (index 94) - La liberté
p93 = 94
s494 = find_subpart(p93, "494")
s495 = find_subpart(p93, "495")
s496 = find_subpart(p93, "496")

for s in [s494, s495, s496]:
    clear_hadiths(s)

s494['hadiths'].append({
    "number": "1479",
    "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a pas grand-chose à admirer dans celui qui ne possède pas [au moins] l'une de ces cinq caractéristiques: la première est la fidélité, la seconde est l'organisation, la troisième est la pudeur, la quatrième est le bon caractère et la cinquième qui regroupe l'ensemble de ces caractéristiques est la liberté.<sup>1696</sup>"
})

s495['hadiths'].extend([
    {
        "number": "1480",
        "text": "L'Imām 'Alī (as) a dit : Ô gens ! En vérité, Adam n'a engendré ni d'esclave ni de servante, tous les êtres humains sont libres.<sup>1697</sup>"
    },
    {
        "number": "1481",
        "text": "L'Imām 'Alī (as) a dit : Ne sois pas esclave d'autrui alors qu'Allah - loué soit-Il - t'a créé libre.<sup>1698</sup>"
    }
])

s496['hadiths'].extend([
    {
        "number": "1482",
        "text": "L'Imām 'Alī (as) a dit : La gaieté est le trait caractéristique de l'homme libre.<sup>1699</sup>"
    },
    {
        "number": "1483",
        "text": "L'Imām 'Alī (as) a dit : En vérité, la pudeur et la chasteté font partie des caractéristiques de la foi, elles sont les attributs des hommes libres et les traits caractéristiques des bienfaisants.<sup>1700</sup>"
    },
    {
        "number": "1484",
        "text": "L'Imām 'Alī (as) a dit : Le serviteur est libre tant qu'il se contente de ce qu'il a, et l'homme libre est un esclave tant qu'il est avide.<sup>1701</sup>"
    },
    {
        "number": "1485",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'homme libre est libre dans tous ses états : lorsqu'il lui arrive un malheur, il patiente ; lorsque les afflictions affluent de tous côtés, il n'est pas abattu même s'il venait à être emprisonné, opprimé et que son aisance se transformait en difficulté. Ceci fut le cas de Joseph le véridique, le probe - que les prières d'Allah soient sur lui - ; ainsi sa liberté n'a pas été atteinte même lorsqu'il fut réduit à l'état d'esclave, vaincu et emprisonné.<sup>1702</sup>"
    }
])

# Part 94 (index 95) - La convoitise
p94 = 95
s497 = find_subpart(p94, "497")
s498 = find_subpart(p94, "498")
s499 = find_subpart(p94, "499")

for s in [s497, s498, s499]:
    clear_hadiths(s)

s497['hadiths'].extend([
    {
        "number": "1486",
        "text": "Interrogé au sujet de la convoitise, l'Imām 'Alī (as) répondit : C'est le désir de ce qui est petit au travers de la perte de beaucoup.<sup>1703</sup>"
    },
    {
        "number": "1487",
        "text": "L'Imām 'Alī (as) a dit : La convoitise est une [source de] détresse perpétuelle.<sup>1704</sup>"
    },
    {
        "number": "1488",
        "text": "L'Imām 'Alī (as) a dit : La convoitise entâche la noblesse.<sup>1705</sup>"
    },
    {
        "number": "1489",
        "text": "L'Imām 'Alī (as) a dit : La convoitise est la monture de l'épuisement.<sup>1706</sup>"
    },
    {
        "number": "1490",
        "text": "L'Imām 'Alī (as) a dit : La convoitise n'augmente pas la subsistance mais dégrade la valeur de la personne.<sup>1707</sup><br><br><span class=\"hadith-footnote\">(Voir également : 253. L'ambition)</span>"
    }
])

s498['hadiths'].extend([
    {
        "number": "1491",
        "text": "L'Imām 'Alī (as) a dit : La personne qui convoite est prisonnière d'une bassesse dont la captivité est perpétuelle.<sup>1708</sup>"
    },
    {
        "number": "1492",
        "text": "Lorsqu'on lui demanda : «Quelle est la pire des humiliations ?», l'Imām 'Alī (as) répondit : «La convoitise vis-à-vis de ce monde.»<sup>1709</sup>"
    },
    {
        "number": "1493",
        "text": "L'Imām 'Alī (as) a dit : La subsistance est partagée et la personne qui convoite en est privée.<sup>1710</sup>"
    },
    {
        "number": "1494",
        "text": "L'Imām 'Alī (as) a dit : Celui qui convoite est indigent, même s'il venait à détenir ce monde et tout ce qu'il contient.<sup>1711</sup>"
    },
    {
        "number": "1495",
        "text": "L'Imām 'Alī (as) a dit : Celui qui convoite est malheureux et misérable.<sup>1712</sup>"
    },
    {
        "number": "1496",
        "text": "L'Imām 'Alī (as) a dit : La personne qui convoite n'arrive jamais à satiété.<sup>1713</sup>"
    },
    {
        "number": "1497",
        "text": "L'Imām Ḥusayn (as) a dit : La pudeur n'entrave pas [l'arrivée de] la subsistance, tout comme la convoitise ne permet pas son augmentation car en vérité, la subsistance est partagée, l'échéance [de la vie] est certaine et la convoitise ne recherche que le péché.<sup>1714</sup>"
    },
    {
        "number": "1498",
        "text": "L'Imām al-Bāqir (as) a dit : Celui qui convoite ce monde est comme le ver à soie : plus il s'entoure de soie, plus il rend difficile sa sortie, jusqu'à ce qu'il meure de chagrin.<sup>1715</sup>"
    },
    {
        "number": "1499",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'Emir des croyants - que les prières d'Allah soient sur lui - avait pour habitude de dire : Ô fils d'Adam ! Si tu recherches de ce monde ce qui suffit [à tes besoins], alors le peu qui s'y trouve te suffira. En revanche, si tu aspires à plus [que ce dont tu as besoin], alors tout ce qu'il contient ne te suffira pas.<sup>1716</sup><br><br><span class=\"hadith-footnote\">(Voir également : 337. La frugalité, section 1567)</span>"
    }
])

s499['hadiths'].extend([
    {
        "number": "1500",
        "text": "Le Messager d'Allah (s) a dit : Ô 'Alī ! Sache que la lâcheté, l'avarice et la convoitise sont un même instinct dont la racine est la mauvaise conjecture et la basse opinion [vis-à-vis d'Allah].<sup>1717</sup>"
    },
    {
        "number": "1501",
        "text": "Le Messager d'Allah (s) a dit : En vérité, l'homme convoite ce qu'on lui interdit.<sup>1718</sup>"
    }
])

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1465-1501")
