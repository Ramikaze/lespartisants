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

# Part 77 (index 78) - Le Jihād (2)
p77 = 78
s384 = find_subpart(p77, "384")
s385 = find_subpart(p77, "385")
s386 = find_subpart(p77, "386")

# For 384, we clear and re-add 1212, 1213 from previous batch, plus 1214.
clear_hadiths(s384)
clear_hadiths(s385)
clear_hadiths(s386)

s384['hadiths'].extend([
    {
        "number": "1212",
        "source": "Ma'ānī al-Akhbār",
        "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) envoya des troupes [en mission] et lorsqu'elles revinrent, il dit [à ses membres] : «Bienvenue aux gens qui ont accompli le petit <i>jihād</i> et à qui le grand <i>jihād</i> incombe désormais !» Ils lui demandèrent : «Ô Messager d'Allah, quel est le grand <i>jihād</i> ?» Il répondit : «Le <i>jihād</i> contre sa propre personne.» Puis il rajouta : «Le meilleur des <i>jihād</i> est celui qui permet de lutter contre l'âme qui se trouve entre les deux flancs [de l'homme].»<sup>1385</sup>"
    },
    {
        "number": "1213",
        "text": "L'Imām 'Alī (as) a dit : Le meilleur des <i>jihād</i> est la lutte contre les passions [de l'âme] et de la sevrer des plaisirs de ce monde.<sup>1386</sup>"
    },
    {
        "number": "1214",
        "text": "L'Imām al-Bāqir (as) a dit : Il n'y a pas de meilleure vertu que le <i>jihād</i> et il n'y a pas de [meilleur] <i>jihād</i> que le fait de combattre les passions.<sup>1387</sup>"
    }
])

s385['hadiths'].extend([
    {
        "number": "1215",
        "text": "L'Imām 'Alī (as) a dit : Lutte contre ta personne dans la [voie] de l'obéissance d'Allah de la même façon qu'on lutte contre l'ennemi, vaincs-la comme l'antagoniste vainc son antagoniste, car le plus fort des êtres est celui qui a triomphé sur sa propre personne.<sup>1388</sup>"
    },
    {
        "number": "1216",
        "text": "L'Imām 'Alī (as) a dit : Maîtrisez vos propres personnes par la lutte continuelle contre elles.<sup>1389</sup>"
    }
])

s386['hadiths'].extend([
    {
        "number": "1217",
        "text": "Le Messager d'Allah (s) a dit : Par la lutte constante, les mauvaises habitudes sont vaincues.<sup>1390</sup>"
    },
    {
        "number": "1218",
        "text": "Le Messager d'Allah (s) a dit : Luttez contre vos propres passions, et la sagesse pénétrera dans vos cœurs.<sup>1391</sup>"
    },
    {
        "number": "1219",
        "text": "Le Messager d'Allah (s) a dit : Luttez contre vos propres personnes en mangeant et en buvant modérément; ainsi, les anges vous feront ombrage et Satan vous fuira.<sup>1392</sup>"
    },
    {
        "number": "1220",
        "text": "L'Imām 'Alī (as) a dit : Lutte contre tes basses passions, domine ta colère, oppose-toi à tes mauvaises habitudes, purifie ton âme, perfectionne ton intellect, et cherche à accomplir la récompense de ton Seigneur.<sup>1393</sup>"
    },
    {
        "number": "1221",
        "text": "L'Imām 'Alī (as) a dit : Le contrôle de sa personne et la lutte contre ses basses passions élève les stations [de la personne] et multiplie [les récompenses] des bonnes actions.<sup>1394</sup>"
    },
    {
        "number": "1222",
        "text": "L'Imām 'Alī (as) a dit : Le salut de l'âme s'obtient par la lutte [contre sa propre personne].<sup>1395</sup>"
    }
])

# Part 78 (index 79) - Le Jihād (3)
p78 = 79
s387 = find_subpart(p78, "387")
s388 = find_subpart(p78, "388")

for s in [s387, s388]:
    clear_hadiths(s)

s387['hadiths'].extend([
    {
        "number": "1223",
        "text": "L'Imām 'Alī (as) a dit : Astreignez-vous au sérieux, à l'effort, à la préparation et à l'apprêtement.<sup>1396</sup>"
    },
    {
        "number": "1224",
        "text": "L'Imām 'Alī (as) a dit : L'obéissance à Allah - loué soit-Il - ne peut être atteinte que par celui qui s'est appliqué avec sérieux et qui a fourni le maximum d'efforts.<sup>1397</sup>"
    },
    {
        "number": "1225",
        "text": "L'Imām al-Ṣādiq (as) a dit : Sachez qu'entre Allah et Ses créatures, il n'y a ni ange rapproché, ni prophète envoyé, ni aucun autre être [susceptible d'intervenir], hormis par leur obéissance [à Allah]. Par conséquent, efforcez-vous d'obéir à Allah.<sup>1398</sup>"
    }
])

s388['hadiths'].extend([
    {
        "number": "1226",
        "text": "Le Messager d'Allah (s) a dit : La personne qui déploie le plus d'efforts est celle qui délaisse les péchés.<sup>1399</sup>"
    },
    {
        "number": "1227",
        "text": "Le Messager d'Allah (s) a dit : Le meilleur des efforts (<i>jihād</i>) est réalisé par celui qui, lorsqu'il se réveille le matin, a l'intention de ne pas être injuste envers quiconque.<sup>1400</sup>"
    },
    {
        "number": "1228",
        "text": "L'Imām al-Bāqir (as), lorsqu'un homme lui dit : «Mes actes sont faibles, mes prières sont peu nombreuses et mon jeûne est minime, même si j'essaie de ne consommer que ce qui est licite et de n'avoir de relation charnelle que de façon licite», rétorqua : «Et quel <i>jihād</i> est meilleur que de réfréner son estomac et ses parties intimes?»<sup>1401</sup>"
    }
])

# Part 79 (index 80) - L'Ignorance
p79 = 80
s389 = find_subpart(p79, "389")
s390 = find_subpart(p79, "390")
s391 = find_subpart(p79, "391")
s392 = find_subpart(p79, "392")
s393 = find_subpart(p79, "393")
s394 = find_subpart(p79, "394")

for s in [s389, s390, s391, s392, s393, s394]:
    clear_hadiths(s)

s389['hadiths'].extend([
    {
        "number": "1229",
        "text": "L'Imām 'Alī (as) a dit : L'ignorance est le pire des maux.<sup>1402</sup>"
    },
    {
        "number": "1230",
        "text": "L'Imām 'Alī (as) a dit : L'ignorance anéantit les vivants et rend le malheur perpétuel.<sup>1403</sup>"
    },
    {
        "number": "1231",
        "text": "L'Imām 'Alī (as) a dit : L'ignorance est [la source de] la corruption de toute chose.<sup>1404</sup>"
    },
    {
        "number": "1232",
        "text": "L'Imām 'Alī (as) a dit : L'ignorance est la racine de tout mal.<sup>1405</sup>"
    },
    {
        "number": "1233",
        "text": "L'Imām 'Alī (as) a dit : La convoitise, la voracité et l'avarice sont les conséquences de l'ignorance.<sup>1406</sup>"
    },
    {
        "number": "1234",
        "text": "L'Imām al-'Askarī (as) a dit : L'ignorance est l'adversaire [de l'homme].<sup>1407</sup>"
    }
])

s390['hadiths'].extend([
    {
        "number": "1235",
        "text": "Le Messager d'Allah (s) a dit : En vérité, l'ignorant est celui qui désobéit à Allah, même si son apparence est belle et qu'il est quelqu'un d'important.<sup>1408</sup>"
    },
    {
        "number": "1236",
        "text": "Le Messager d'Allah (s) a dit : La caractéristique de l'ignorant est de faire preuve d'injustice envers toute personne avec qui il s'associe, d'opprimer les personnes qui lui sont inférieures, de flatter ses supérieurs et de parler sans réflexion...<sup>1409</sup>"
    },
    {
        "number": "1237",
        "text": "L'Imām 'Alī (as) a dit : L'ignorant n'est pas conscient de ses lacunes et n'accepte pas les conseils des autres.<sup>1410</sup>"
    },
    {
        "number": "1238",
        "text": "L'Imām 'Alī (as) a dit : L'ignorant est mort bien qu'il soit [en apparence] vivant.<sup>1411</sup>"
    },
    {
        "number": "1239",
        "text": "L'Imām 'Alī (as) a dit : L'ignorant est celui qui s'est autorisé à être leurré par ses passions et caprices.<sup>1412</sup>"
    },
    {
        "number": "1240",
        "text": "L'Imām 'Alī (as) a dit : Vous ne verrez pas un ignorant sans qu'il soit outrancier ou laxiste [dans ses actes].<sup>1413</sup>"
    },
    {
        "number": "1241",
        "text": "L'Imām 'Alī (as) a dit : En vérité, l'ignorant est celui qui est devenu esclave de ses désirs.<sup>1414</sup>"
    },
    {
        "number": "1242",
        "text": "L'Imām 'Alī (as) a dit : L'ignorant est l'esclave de ses bas penchants.<sup>1415</sup>"
    },
    {
        "number": "1243",
        "text": "L'Imām 'Alī (as) a dit : L'acte de l'ignorant est voué à l'échec et son savoir est une source d'égarement.<sup>1416</sup>"
    },
    {
        "number": "1244",
        "text": "L'Imām 'Alī (as) a dit : En vérité, l'ignorant est celui qui se considère savant à propos de ce qu'il ignore, qui se satisfait de son propre avis, qui persiste à rester éloigné des savants et les discrédite. Il considère erroné l'avis de ceux qui s'opposent à lui, et comme fallacieux ce qu'il ne comprend pas. Dès qu'il entend une parole qu'il ignore, il la rejette et la traite de mensongère. Il dit ainsi par ignorance : «Je ne connais pas cela !» ; «Je ne pense pas que cela soit possible !» ; «Comment pourrait-il en être ainsi ?!» ; «D'où vient cela ?!» Ceci est dû à sa confiance en sa propre opinion et à son manque de clairvoyance vis-à-vis de son ignorance. Dès lors, en raison de la confusion de ses opinions, il restera attaché à son ignorance, [continuera de] rejeter la vérité, demeurera perdu dans son ignorance et dédaignera la recherche du savoir.<sup>1417</sup>"
    },
    {
        "number": "1245",
        "text": "L'Imām al-Ṣādiq (as) a dit : Répondre avant d'écouter, s'opposer avant de comprendre et juger ce que l'on ignore font partie des caractéristiques de l'ignorant.<sup>1418</sup>"
    },
    {
        "number": "1246",
        "text": "L'Imām al-Hādī (as) a dit : L'ignorant est prisonnier de sa propre langue.<sup>1419</sup>"
    }
])

s391['hadiths'].extend([
    {
        "number": "1247",
        "text": "L'Imām 'Alī (as) a dit : La plus ignorante des personnes est celle qui se laisse tromper par la parole d'un louangeur flatteur qui embellit pour elle l'infâme et lui rend détestable le convenable.<sup>1420</sup>"
    },
    {
        "number": "1248",
        "text": "L'Imām 'Alī (as) a dit : Le sommet de l'ignorance est qu'une personne se vante de son ignorance.<sup>1421</sup>"
    },
    {
        "number": "1249",
        "text": "L'Imām 'Alī (as) a dit : La plus grande ignorance est l'ignorance qu'a l'homme de la condition de sa propre personne.<sup>1422</sup>"
    }
])

s392['hadiths'].extend([
    {
        "number": "1250",
        "text": "L'Imām 'Alī (as) a dit : Le fait de commettre ce qui est interdit suffit pour être considéré ignorant.<sup>1423</sup>"
    },
    {
        "number": "1251",
        "text": "L'Imām 'Alī (as) a dit : Être en admiration devant son propre savoir suffit pour que cela soit considéré comme de l'ignorance.<sup>1424</sup>"
    },
    {
        "number": "1252",
        "text": "L'Imām 'Alī (as) a dit : Le fait que l'homme ignore son propre statut suffit pour être considéré comme de l'ignorance.<sup>1425</sup>"
    },
    {
        "number": "1253",
        "text": "L'Imām 'Alī (as) a dit : Ne dis pas tout ce que tu sais, car cela suffit pour être considéré comme de l'ignorance.<sup>1426</sup>"
    },
    {
        "number": "1254",
        "text": "L'Imām al-Ṣādiq (as) a dit : [Posséder] la crainte d'Allah suffit comme savoir, et le fait de faire preuve de suffisance et de vanité vis-à-vis d'Allah suffit comme ignorance.<sup>1427</sup>"
    }
])

s393['hadiths'].extend([
    {
        "number": "1255",
        "text": "Le Messager d'Allah (s) a dit : Exposer tout ce que l'on sait fait partie de l'ignorance.<sup>1428</sup>"
    },
    {
        "number": "1256",
        "text": "L'Imām 'Alī (as) a dit : Se fier à la vie de ce bas-monde malgré tout ce que tu y constates est une ignorance.<sup>1429</sup>"
    },
    {
        "number": "1257",
        "text": "L'Imām 'Alī (as) a dit : Ton désir pour l'impossible est une ignorance.<sup>1430</sup>"
    },
    {
        "number": "1258",
        "text": "L'Imām Ḥasan (as) a dit lorsque son père lui demanda d'expliquer le sens de l'ignorance : C'est de se précipiter sur une occasion avant de se rendre capable [de l'accomplir], et c'est de s'abstenir de répondre.<sup>1431</sup>"
    },
    {
        "number": "1259",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'ignorance réside dans trois choses : changer constamment d'amis, déclarer la guerre sans raison, et espionner des affaires qui ne nous concernent pas.<sup>1432</sup>"
    },
    {
        "number": "1260",
        "text": "L'Imām al-'Askarī (as) a dit : Rire sans raison fait partie de l'ignorance.<sup>1433</sup>"
    }
])

s394['hadiths'].extend([
    {
        "number": "1261",
        "text": "L'Imām 'Alī (as) a dit : Les gens sont les ennemis de ce qu'ils ignoreent.<sup>1434</sup>"
    },
    {
        "number": "1262",
        "text": "L'Imām 'Alī (as) a dit : Celui qui ignore une chose essaie de lui trouver un défaut.<sup>1435</sup>"
    },
    {
        "number": "1263",
        "text": "L'Imām 'Alī (as) a dit : J'ai dit quatre choses qu'Allah le Très-Haut a validées en révélant [des versets à ce sujet] dans Son Livre: [...] J'ai dit : «Celui qui ignore une chose s'y opposera», et Allah a révélé : <i>«Ils ont traité de mensonge ce qu'ils ne peuvent embrasser de leur savoir.»</i><sup>1436</sup> <sup>1437</sup>"
    },
    {
        "number": "1264",
        "text": "L'Imām 'Alī (as) a dit : Ne vous opposez pas à ce que vous ignorez, car la majorité du savoir se trouve dans ce que vous ne connaissez pas.<sup>1438</sup><br><br><span class=\"reference-note\">(Voir également : 295. Les défauts, section 1408)</span>"
    }
])

# Part 80 (index 81) - L'Enfer
p80 = 81
s395 = find_subpart(p80, "395")
s396 = find_subpart(p80, "396")
s397 = find_subpart(p80, "397")
s398 = find_subpart(p80, "398")
s399 = find_subpart(p80, "399")
s400 = find_subpart(p80, "400")
s401 = find_subpart(p80, "401")
s402 = find_subpart(p80, "402")
s403 = find_subpart(p80, "403")
s404 = find_subpart(p80, "404")

for s in [s395, s396, s397, s398, s399, s400, s401, s402, s403, s404]:
    clear_hadiths(s)

s395['introduction'] = "«L'Enfer demeure aux aguets, refuge pour les transgresseurs.»<sup>1439</sup>"
s395['hadiths'].extend([
    {
        "number": "1265",
        "text": "L'Imām 'Alī (as) a dit : Prenez garde au Feu dont le crépitement est prêt, dont les flammes sont ardentes, et dont la douleur est perpétuellement renouvelée.<sup>1440</sup>"
    },
    {
        "number": "1266",
        "text": "L'Imām 'Alī (as) a dit : Le Feu dont la rage est ardente, les flammes sont hautes, l'embrasement est flamboyant, le souffle est déchaîné, et l'extinction est éloignée ; son combustible est embrasé et sa menace est effrayante.<sup>1441</sup>"
    }
])

s396['introduction'] = "«Et si vous n'y parvenez pas – et assurément vous n'y parviendrez jamais –, parez-vous donc contre le Feu qu'alimenteront les hommes et les pierres, lequel est réservé aux infidèles.»<sup>1442</sup><br><br>«Et quant aux injustes, ils formeront le combustible de l'Enfer.»<sup>1443</sup>"

s397['introduction'] = "««Saisissez-le ! Puis, mettez-lui un carcan ; ensuite brûlez-le dans la Fournaise ; puis liez-le avec une chaîne de soixante-dix coudées».»<sup>1444</sup>"
s397['hadiths'].append({
    "number": "1267",
    "text": "L'Imām al-Ṣādiq (as) a dit en rapportant l'une des paroles de Gabriel (as) au Messager d'Allah (s) : Si un seul chaînon de la chaîne dont la longueur est de soixante-dix bras était placé sur ce monde, ce dernier fonderait en raison de sa chaleur.<sup>1445</sup>"
})

s398['hadiths'].append({
    "number": "1268",
    "text": "L'Imām al-Ṣādiq (as) a dit en rapportant l'une des paroles de Gabriel (as) au Messager d'Allah (s) : Si seulement l'un des vêtements des gens de l'Enfer était suspendu entre le ciel et la terre, les gens de ce bas-monde mourraient en raison de son odeur.<sup>1446</sup>"
})

s399['introduction'] = "«Il n'y aura pour eux d'autre nourriture que des plantes épineuses qui n'engraissent, ni n'apaisent la faim.»<sup>1447</sup><br><br>«Il n'a pour lui ici, aujourd'hui, point d'ami chaleureux [pour le protéger], ni d'autre nourriture que du pus.»<sup>1448</sup>"
s399['hadiths'].extend([
    {
        "number": "1269",
        "text": "Le Messager d'Allah (s) a dit : Si un seau d'eau purulente [de l'Enfer] était versé lorsque le soleil se lève [sur ce monde], les crânes des gens habitant au lieu de son coucher se mettraient à bouillir.<sup>1449</sup>"
    },
    {
        "number": "1270",
        "text": "L'Imām al-Ṣādiq (as) a dit en rapportant l'une des paroles de Gabriel (as) au Messager d'Allah (s) : Si un fragment d'épine [de l'Enfer] venait à tomber dans la boisson des gens de ce monde, ils mourraient de par son odeur nauséabonde.<sup>1450</sup>"
    }
])

s400['introduction'] = "«Et vous boirez par-dessus cela de l'eau bouillante, vous en boirez comme boivent les chameaux assoiffés.»<sup>1451</sup>"
s400['hadiths'].append({
    "number": "1271",
    "text": "L'Imām 'Alī (as) a dit : En vérité, lorsque le <i>Zaqqūm</i><sup>1452</sup> et les épines sèches bouilliront dans le ventre des gens de l'Enfer comme de l'eau bouillante, ils imploreront une boisson et il leur sera donné un breuvage de pus suintant qu'ils avaleront avec grande difficulté, et la mort les assaillira de tous côtés sans qu'ils puissent mourir.<sup>1453</sup>"
})

s401['hadiths'].append({
    "number": "1272",
    "text": "Le Messager d'Allah (s) a dit : Les premières personnes à entrer en Enfer seront un gouverneur dominateur et injuste, un riche qui ne s'est pas acquitté des devoirs inhérents à ses biens, et un pauvre arrogant.<sup>1454</sup>"
})

s402['hadiths'].append({
    "number": "1273",
    "text": "Le Messager d'Allah (s) a dit : La personne la moins châtiée en Enfer sera chaussée de sandales de feu qui feront bouillir son cerveau du fait de leur chaleur.<sup>1455</sup>"
})

s403['hadiths'].extend([
    {
        "number": "1274",
        "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, la personne la plus châtiée sera un savant dont le savoir n'aura été pour lui d'aucune utilité.<sup>1456</sup>"
    },
    {
        "number": "1275",
        "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, les personnes les plus châtiées seront un homme qui a tué un prophète ou qui a été tué par un prophète, et un dirigeant qui a égaré et trompé.<sup>1457</sup>"
    },
    {
        "number": "1276",
        "text": "L'Imām 'Alī (as) a dit : La plus punie des personnes sera celle qui a rendu le bien par le mal.<sup>1458</sup>"
    },
    {
        "number": "1277",
        "text": "L'Imām 'Alī (as) a dit : Le Jour de la Résurrection, la plus châtiée des personnes sera celle que le décret d'Allah a mis en colère.<sup>1459</sup><br><br><span class=\"reference-note\">(Voir également : 288. Le savoir, section 1360)</span>"
    }
])

s404['hadiths'].append({
    "number": "1278",
    "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, en Enfer se trouve une vallée pour les arrogants, appelée <i>Saqar</i>. Elle s'est plainte à Allah le Très-Haut de l'intensité de sa chaleur et lui a demandé la permission de respirer un coup, et lorsqu'elle l'a fait, elle a brûlé l'Enfer.<sup>1460</sup>"
})

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1214-1278")
