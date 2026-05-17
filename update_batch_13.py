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
    s['hadiths'] = []
    if 'introduction' in s:
        del s['introduction']


# Part 88 (index 89) - L'argument
p88 = 89
s457 = find_subpart(p88, "457")
s458 = find_subpart(p88, "458")

for s in [s457, s458]:
    clear_hadiths(s)

s457['introduction'] = "«Dis : «L'argument décisif appartient à Allah. Et s'Il l'avait voulu, Il vous aurait certainement tous guidés [sur le droit chemin].»»<sup>1616</sup>"
s457['hadiths'].extend([
    {
        "number": "1406",
        "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut <i>«Dis : «L'argument décisif appartient à Allah»»</i><sup>1617</sup> : En vérité, le Jour de la Résurrection, Allah le Très-Haut demandera à Son serviteur : «Mon serviteur, le savais-tu ?» S'il répond «Oui», Il lui dira : «Pourquoi n'as-tu donc pas agi selon ce que tu savais ?», et s'il répond «J'étais ignorant», Il lui dira : «Pourquoi n'as-tu pas appris pour agir [en fonction de cela] ?!» Ainsi, il sera vaincu, et tel est l'argument décisif.<sup>1618</sup>"
    },
    {
        "number": "1407",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'argument d'Allah existait avant la création, est avec la création et demeurera après la création.<sup>1619</sup>"
    }
])

s458['introduction'] = "«En tant que messagers, annonciateurs et avertisseurs, afin qu'après la venue des messagers il n'y eût pour les gens point d'argument devant Allah. Allah est Puissant et Sage.»<sup>1620</sup>"
s458['hadiths'].extend([
    {
        "number": "1408",
        "text": "L'Imām 'Alī (as) a dit : Ô gens ! Sachez qu'Allah - loué soit-Il - n'a pas sur terre d'argument plus certain que notre prophète Muḥammad (s) ni de sagesse plus décisive que Son Livre, le Grand Coran.<sup>1621</sup>"
    },
    {
        "number": "1409",
        "text": "L'Imām 'Alī (as) a dit : En vérité, Allah le Béni et le Très-Haut n'a pas sur terre d'argument ni de sagesse plus décisives que Son Livre.<sup>1622</sup>"
    }
])


# Part 89 (index 90) - Le hadīth
p89 = 90
s459 = find_subpart(p89, "459")
s460 = find_subpart(p89, "460")
s461 = find_subpart(p89, "461")
s462 = find_subpart(p89, "462")
s463 = find_subpart(p89, "463")
s464 = find_subpart(p89, "464")
s465 = find_subpart(p89, "465")
s466 = find_subpart(p89, "466")
s467 = find_subpart(p89, "467")

for s in [s459, s460, s461, s462, s463, s464, s465, s466, s467]:
    clear_hadiths(s)


s459['hadiths'].extend([
    {
        "number": "1410",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, nos <i>ḥadīth</i> ravivent les cœurs.<sup>1623</sup>"
    },
    {
        "number": "1411",
        "text": "L'Imām al-Bāqir (as) a dit : Un seul <i>ḥadīth</i> que tu recueilles d'une authentique narration est meilleur pour toi que ce monde et tout ce qu'il contient.<sup>1624</sup>"
    }
])

s460['hadiths'].extend([
    {
        "number": "1412",
        "text": "Le Messager d'Allah (s) a dit : Celui qui transmet à ma communauté un <i>ḥadīth</i> par lequel une tradition est établie ou une innovation (<i>bid'a</i>) bloquée entrera au Paradis.<sup>1625</sup>"
    },
    {
        "number": "1413",
        "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) a dit trois fois de suite : «Ô Allah ! Accorde Ta miséricorde à mes successeurs !» On lui demanda alors : «Ô Messager d'Allah, qui sont tes successeurs ?» Il répondit : «Ce sont ceux qui transmettent ma parole (<i>ḥadīth</i>) et mes traditions, et qui les apprennent à ma communauté.»<sup>1626</sup>"
    },
    {
        "number": "1414",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le narrateur d'un <i>ḥadīth</i> qui connait bien la religion est meilleur que mille dévots sans savoir ni connaissance des traditions.<sup>1627</sup>"
    },
    {
        "number": "1415",
        "text": "L'Imām al-Ṣādiq (as) a dit : Connaissez la position des gens à notre égard en fonction de leur narration de nos traditions.<sup>1628</sup>"
    }
])

s461['hadiths'].append({
    "number": "1416",
    "text": "Le Messager d'Allah (s) a dit : La personne de ma communauté qui a mémorisé quarante <i>ḥadīth</i> bénéfiques à ma communauté dans ses affaires religieuses sera ressuscitée le Jour de la Résurrection en tant que savant juriste et érudit [en religion].<sup>1629</sup>"
})

s462['hadiths'].extend([
    {
        "number": "1417",
        "text": "L'Imām 'Alī (as) a dit : Efforcez-vous de comprendre [les <i>ḥadīth</i>], et pas [seulement] de [les] narrer.<sup>1630</sup>"
    },
    {
        "number": "1418",
        "text": "L'Imām 'Alī (as) a dit : L'ambition des sots est dans la narration, alors que l'ambition des savants est dans la compréhension [des <i>ḥadīth</i>].<sup>1631</sup>"
    },
    {
        "number": "1419",
        "text": "L'Imām al-Ṣādiq (as) a dit : Un <i>ḥadīth</i> que tu comprends est meilleur que mille <i>ḥadīth</i> que tu narres [sans les comprendre].<sup>1632</sup>"
    }
])

s463['hadiths'].extend([
    {
        "number": "1420",
        "text": "Le Messager d'Allah (s) a dit : Celui qui m'attribue ce qui est mensonger, laissez-le prendre sa place en Enfer.<sup>1633</sup>"
    },
    {
        "number": "1421",
        "text": "Le Messager d'Allah (s) a dit : M'attribuer ce que je n'ai pas dit compte parmi les plus grands péchés.<sup>1634</sup>"
    }
])

s464['hadiths'].append({
    "number": "1422",
    "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, je serai opposé à celui qui rejette un <i>ḥadīth</i> qui lui est parvenu de moi. Si un <i>ḥadīth</i> que vous ne connaissez pas vous a été transmis, dites : «Allah est plus savant».<sup>1635</sup>"
})

s465['hadiths'].extend([
    {
        "number": "1423",
        "text": "Le Messager d'Allah (s) a dit : Comparez ma parole (<i>ḥadīth</i>) au Livre d'Allah ; s'ils concordent, alors elle est de moi et je l'ai bien dite.<sup>1636</sup>"
    },
    {
        "number": "1424",
        "text": "L'Imām al-Ṣādiq (as) a dit : Tout <i>ḥadīth</i> qui ne concorde pas avec le Coran est faux.<sup>1637</sup>"
    }
])

s466['hadiths'].append({
    "number": "1425",
    "text": "L'Imām al-Bāqir (as) a dit : Parmi les <i>ḥadīth</i> de la famille du Prophète - que les prières d'Allah soient sur eux - qui vous parviennent, acceptez ceux vers lesquels ont penché votre cœur et qui vous semblent familiers. En revanche, renvoyez [et référez-vous] à Allah, à Son Messager et au savant de la descendance Muḥammadienne (s) concernant ceux que votre cœur refuse et que vous rejetez.<sup>1638</sup>"
})

s467['hadiths'].append({
    "number": "1426",
    "text": "Le Messager d'Allah (s) a dit : Le <i>ḥadīth</i> qui vous est transmis de moi et qui correspond à la vérité est bien de moi. En revanche, si on transmet un <i>ḥadīth</i> de moi qui ne correspond pas à la vérité, alors je ne l'ai pas dit, car je ne dis que la vérité.<sup>1639</sup>"
})

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1406-1426")
