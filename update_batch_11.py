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

# Part 80 (index 81) - L'Enfer
p80 = 81
s405 = find_subpart(p80, "405")
s406 = find_subpart(p80, "406")
s407 = find_subpart(p80, "407")

for s in [s405, s406, s407]:
    clear_hadiths(s)

s405['hadiths'].append({
    "number": "1279",
    "text": "L'Imām al-Kāẓim (as) a dit : Allah ne laissera éternellement en Enfer que les mécréants, les négateurs, les égarés et les associationistes. En revanche, ceux parmi les croyants qui ont évité les grands péchés ne seront pas interrogés au sujet des petits péchés.<sup>1461</sup>"
})

s406['hadiths'].extend([
    {
        "number": "1280",
        "text": "Le Messager d'Allah (s) a dit : Sortira de l'Enfer toute personne dont le cœur contiendra le poids d'un atome de foi.<sup>1462</sup>"
    },
    {
        "number": "1281",
        "text": "L'Imām al-Bāqir (as) a dit : En Enfer, des gens seront brûlés dans le Feu et lorsqu'ils seront devenus cendres [et purifiés], ils seront atteints par l'intercession.<sup>1463</sup>"
    }
])

s407['hadiths'].append({
    "number": "1282",
    "text": "L'Imām al-Ṣādiq (as) a dit : «Les gens de l'Enfer y resteront éternellement car leur intention dans le bas-monde était que s'ils venaient à vivre éternellement, ils désobéiraient à Allah éternellement. De même, les gens du Paradis resteront éternellement au Paradis car leur intention dans le bas-monde était que s'ils venaient à vivre éternellement, ils obéiraient à Allah éternellement. C'est par leurs intentions que chacun des deux groupes séjournent éternellement [dans l'un ou l'autre lieu].» Puis il récita la parole: <i>«Dis : «Chacun agit selon sa méthode»»</i><sup>1464</sup> et dit: «C'est-à-dire selon son intention.»<sup>1465</sup>"
})

# Part 81 (index 82) - La réponse
p81 = 82
s408 = find_subpart(p81, "408")
clear_hadiths(s408)

s408['hadiths'].extend([
    {
        "number": "1283",
        "text": "L'Imām 'Alī (as) a dit : Lorsqu'il y a plusieurs réponses, la bonne reste cachée.<sup>1466</sup>"
    },
    {
        "number": "1284",
        "text": "L'Imām 'Alī (as) a dit : Il se peut que l'éloquent ne trouve pas de réponse.<sup>1467</sup>"
    },
    {
        "number": "1285",
        "text": "L'Imām 'Alī (as) a dit : Celui qui se précipite dans ses réponses ne répondra pas justement.<sup>1468</sup>"
    },
    {
        "number": "1286",
        "text": "L'Imām 'Alī (as) a dit : Une preuve de la vertu consiste à donner des réponses justes.<sup>1469</sup>"
    },
    {
        "number": "1287",
        "text": "L'Imām 'Alī (as) a dit : Mets de côté l'intransigeance, réfléchis à l'argumentation, abstiens-toi des paroles futiles, et tu seras ainsi préservé du faux-pas.<sup>1470</sup>"
    },
    {
        "number": "1288",
        "text": "L'Imām 'Alī (as) a dit : Si tu fais preuve d'indulgence envers l'ignorant, tu lui auras certainement offert la réponse adéquate.<sup>1471</sup>"
    },
    {
        "number": "1289",
        "text": "L'Imām 'Alī (as) a dit : Nombreuses sont les paroles dont la réponse est le silence.<sup>1472</sup>"
    },
    {
        "number": "1290",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui répond à toutes les questions qu'on lui pose est certainement fou.<sup>1473</sup><br><br><span class=\"reference-note\">(Voir également : 180. La question (1), section 907)</span>"
    }
])

# Part 82 (index 83) - La générosité
p82 = 83
s409 = find_subpart(p82, "409")
s410 = find_subpart(p82, "410")
s411 = find_subpart(p82, "411")

for s in [s409, s410, s411]:
    clear_hadiths(s)

s409['hadiths'].extend([
    {
        "number": "1291",
        "text": "L'Imām 'Alī (as) a dit : Sois généreux dans tout ce que tu trouves, et tu seras loué.<sup>1474</sup>"
    },
    {
        "number": "1292",
        "text": "L'Imām 'Alī (as) a dit : La générosité de l'homme le rend aimé aux yeux de ses opposants, et son avarice le rend détestable [même] aux yeux de ses enfants.<sup>1475</sup>"
    },
    {
        "number": "1293",
        "text": "L'Imām 'Alī (as) a dit : La générosité fait partie de la noblesse de la nature [humaine].<sup>1476</sup>"
    },
    {
        "number": "1294",
        "text": "L'Imām 'Alī (as) a dit : La générosité est un honneur présent.<sup>1477</sup>"
    },
    {
        "number": "1295",
        "text": "L'Imām Ḥusayn (as) a dit : Celui qui donne règnera.<sup>1478</sup>"
    }
])

s410['hadiths'].extend([
    {
        "number": "1296",
        "text": "Le Messager d'Allah (s) a dit : La personne la plus généreuse est celle qui fait don de sa personne et de ses biens dans la voie d'Allah.<sup>1479</sup>"
    },
    {
        "number": "1297",
        "text": "L'Imām 'Alī (as) a dit : La meilleure générosité est celle qui se manifeste dans la difficulté [malgré son propre besoin].<sup>1480</sup>"
    },
    {
        "number": "1298",
        "text": "L'Imām Ḥusayn (as) a dit : En vérité, la plus généreuse des personnes est celle qui donne sans rien attendre en retour.<sup>1481</sup>"
    }
])

s411['hadiths'].append({
    "number": "1299",
    "text": "L'Imām al-Ṣādiq (as) a dit : La personne n'est généreuse que si elle a ces trois [attributs] : elle est généreuse dans ses biens dans l'opulence comme dans l'indigence, elle les donne à celui qui en a besoin, et elle considère que la gratitude de celui à qui elle a donné est plus grande que ce qu'elle a donné.<sup>1482</sup>"
})

# Part 83 (index 84) - Le voisin
p83 = 84
s412 = find_subpart(p83, "412")
s413 = find_subpart(p83, "413")
s414 = find_subpart(p83, "414")
s415 = find_subpart(p83, "415")
s416 = find_subpart(p83, "416")

for s in [s412, s413, s414, s415, s416]:
    clear_hadiths(s)

s412['introduction'] = "«Adorez Allah, et ne Lui donnez aucun associé. Agissez avec bonté envers [vos] parents, les proches, les orphelins, les pauvres, le proche voisin, le voisin lointain, le collègue.»<sup>1483</sup>"
s412['hadiths'].extend([
    {
        "number": "1300",
        "text": "Le Messager d'Allah (s) a dit : Le caractère sacré du voisin pour l'homme est semblable au caractère sacré de sa mère.<sup>1484</sup>"
    },
    {
        "number": "1301",
        "text": "L'Imām 'Alī (as) a dit lors de sa mort : [Craignez] Allah et souvenez-vous d'[Allah] concernant vos voisins, car votre Prophète vous les a recommandés. Il n'a cessé de recommander la bienséance envers eux, au point où nous avons cru qu'il allait leur accorder une part de l'héritage.<sup>1485</sup>"
    },
    {
        "number": "1302",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le bon voisinage fait prospérer les terres et rallonge la durée de vie.<sup>1486</sup>"
    },
    {
        "number": "1303",
        "text": "L'Imām al-Kāẓim (as) a dit : Le bon voisinage n'est pas de s'abstenir de nuire [à son voisin], mais de patienter face à la nuisance [de son voisin].<sup>1487</sup>"
    }
])

s413['hadiths'].extend([
    {
        "number": "1304",
        "text": "Le Messager d'Allah (s) a dit : Celui qui croit en Allah et au Jour Dernier ne doit pas nuire à son voisin.<sup>1488</sup>"
    },
    {
        "number": "1305",
        "text": "L'Imām al-Riḍā (as) a dit : Ne fait pas partie de nous celui qui n'épargne pas son voisin de ses nuisances.<sup>1489</sup><br><br><span class=\"reference-note\">(Voir également : 8. Le tourment)</span>"
    }
])

s414['hadiths'].extend([
    {
        "number": "1306",
        "text": "L'Imām 'Alī (as) a dit : S'enquérir de son voisin fait partie des bienséances du bon voisinage.<sup>1490</sup>"
    },
    {
        "number": "1307",
        "text": "L'Imām al-Bāqir (as) rapporte du Messager d'Allah (s) : «Ne croit pas en moi celui qui passe la nuit le ventre plein alors que son voisin est affamé.» Il a également dit : «Le Jour de la Résurrection, Allah ne regardera pas les habitants d'un village qui ont dormi alors qu'un affamé était parmi eux.»<sup>1491</sup>"
    }
])

s415['hadiths'].append({
    "number": "1308",
    "text": "Le Messager d'Allah (s) a dit au sujet des droits du voisin : S'il implore ton secours, aide-le ; s'il te demande de lui prêter, prête-lui ; s'il devient pauvre, satisfais ses besoins ; s'il lui arrive un malheur, réconforte-le ; si une joie lui arrive, félicite-le ; s'il tombe malade, rends-lui visite ; s'il venait à mourir, assiste à son enterrement. Ne construis pas une maison plus haute que la sienne qui lui barrerait le passage du vent, sauf avec sa permission. Si tu achètes des fruits, offre-lui-en, si tu ne le fais pas, alors amène-les discrètement chez toi. Et ne fait pas sortir tes enfants avec ces fruits [à la main] afin de ne pas contrarier les siens, et ne l'opportune pas par l'odeur [alléchante] de ton repas sans lui en offrir une part.<sup>1492</sup>"
})

s416['hadiths'].append({
    "number": "1309",
    "text": "L'Imām 'Alī (as) a dit : L'enceinte sacrée de la mosquée est de quarante coudées, et le voisinage comprend quarante maisons dans les quatre directions.<sup>1493</sup>"
})

# Part 84 (index 85) - L'Amour
p84 = 85
s417 = find_subpart(p84, "417")
s418 = find_subpart(p84, "418")
s419 = find_subpart(p84, "419")
s420 = find_subpart(p84, "420")
s421 = find_subpart(p84, "421")
s422 = find_subpart(p84, "422")
s423 = find_subpart(p84, "423")
s424 = find_subpart(p84, "424")
s425 = find_subpart(p84, "425")
s426 = find_subpart(p84, "426")
s427 = find_subpart(p84, "427")
s428 = find_subpart(p84, "428")
s429 = find_subpart(p84, "429")
s430 = find_subpart(p84, "430")
s431 = find_subpart(p84, "431")
s432 = find_subpart(p84, "432")
s433 = find_subpart(p84, "433")
s434 = find_subpart(p84, "434")
s435 = find_subpart(p84, "435")
s436 = find_subpart(p84, "436")
s437 = find_subpart(p84, "437")

for s in [s417, s418, s419, s420, s421, s422, s423, s424, s425, s426, s427, s428, s429, s430, s431, s432, s433, s434, s435, s436, s437]:
    clear_hadiths(s)

s417['hadiths'].extend([
    {
        "number": "1310",
        "text": "L'Imām 'Alī (as) a dit : L'affection est une parenté acquise.<sup>1494</sup>"
    },
    {
        "number": "1311",
        "text": "L'Imām 'Alī (as) a dit : La parenté a plus besoin d'affection que l'affection n'a besoin de la parenté.<sup>1495</sup>"
    }
])

s418['hadiths'].extend([
    {
        "number": "1312",
        "text": "L'Imām 'Alī (as) a dit : Trois choses suscitent l'amour : le bon caractère, la gentillesse et l'humilité.<sup>1496</sup>"
    },
    {
        "number": "1313",
        "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses suscitent l'amour : la piété, l'humilité et la générosité.<sup>1497</sup><br><br><span class=\"reference-note\">(Voir également : 42. La gaieté ; 185. La générosité, section 929)</span>"
    }
])

s419['introduction'] = "«Tu n'en trouveras pas, parmi les gens qui croient en Allah et au Jour dernier, qui prennent pour amis ceux qui s'opposent à Allah et au Messager, fussent-ils leurs pères, leurs fils, leurs frères ou les gens de leur tribu. Il a prescrit la foi dans les cœurs.»<sup>1498</sup>"
s419['hadiths'].extend([
    {
        "number": "1314",
        "text": "L'Imām 'Alī (as) a dit : N'offre pas ton affection à celui qui n'est pas fidèle.<sup>1499</sup>"
    },
    {
        "number": "1315",
        "text": "L'Imām 'Alī (as) a dit : L'affection la plus éphémère est l'affection des malfaisants.<sup>1500</sup>"
    },
    {
        "number": "1316",
        "text": "L'Imām 'Alī (as) a dit : Gare au fait d'aimer les ennemis d'Allah ou d'offrir ton affection à des personnes autres que les alliés et amis d'Allah, car celui qui aime des gens sera ressuscité avec eux.<sup>1501</sup><br><br><span class=\"reference-note\">(Voir également : 231. L'ami, section 1103 ; 5. Le frère, section 31 ; 68. La compagnie, section 348)</span>"
    }
])

s420['hadiths'].extend([
    {
        "number": "1317",
        "text": "Le Messager d'Allah (s) a dit : Ton amour pour une chose te rend aveugle et sourd.<sup>1502</sup>"
    },
    {
        "number": "1318",
        "text": "L'Imām 'Alī (as) a dit : L'œil de l'amoureux est aveugle aux défauts de l'être aimé, et son oreille devient sourde à la laideur de ses mauvais agissements.<sup>1503</sup>"
    }
])

s421['hadiths'].extend([
    {
        "number": "1319",
        "text": "L'Imām 'Alī (as) a dit : Celui qui t'aime t'interdit [de commettre des péchés].<sup>1504</sup>"
    },
    {
        "number": "1320",
        "text": "L'Imām 'Alī (as) a dit : Celui qui aime une chose la mentionne constamment.<sup>1505</sup>"
    }
])

s422['introduction'] = "«Dis : «Si vos pères, vos enfants, vos frères, vos conjoints, vos clans, les biens que vous gagnez, le commerce dont vous craignez le déclin et les demeures qui vous sont agréables, vous sont plus chers qu'Allah, Son messager et la lutte (<i>jihād</i>) dans le sentier d'Allah, alors attendez qu'Allah fasse venir Son ordre. Et Allah ne guide pas les gens pervers».»<sup>1506</sup><br><br>«Parmi les hommes, il y en a qui prennent, en dehors d'Allah, des égaux à Lui, en les aimant comme on aime Allah. Or les croyants sont les plus ardents en l'amour d'Allah. Quand les injustes verront le châtiment, ils sauront que la force toute entière est à Allah et qu'Allah est dur en châtiment !»<sup>1507</sup><br><br><span class=\"reference-note\">(Voir également : Coran 3:31 ; 5:51-57 ; 9:25 ; 26:77-82 ; 62:6)</span>"
s422['hadiths'].extend([
    {
        "number": "1321",
        "text": "L'Imām Ḥusayn (as) a dit dans une invocation qui lui est attribuée : C'est Toi qui as fait disparaître les autres du cœur de ceux qui T'aiment jusqu'à ce qu'ils n'aiment nul autre que Toi... Que trouve celui qui T'a perdu ?! Qu'a perdu celui qui T'a trouvé ?! Celui qui s'est satisfait d'un autre que Toi sera indéniablement déçu et perdu.<sup>1508</sup>"
    },
    {
        "number": "1322",
        "text": "L'Imām al-Ṣādiq (as) a dit : La foi de l'homme en Allah ne sera pure que lorsqu'Allah sera plus aimé de lui que sa propre personne et que son père, sa mère, son enfant, sa femme, ses biens et l'ensemble des gens.<sup>1509</sup>"
    },
    {
        "number": "1323",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le cœur est le sanctuaire d'Allah, n'établis donc pas un autre qu'Allah dans le sanctuaire d'Allah.<sup>1510</sup>"
    },
    {
        "number": "1324",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'amour [d'Allah] est préférable à la crainte [d'Allah].<sup>1511</sup>"
    }
])

s423['hadiths'].extend([
    {
        "number": "1325",
        "text": "Irshād al-Qulūb : [Il est rapporté] dans le <i>ḥadīth</i> de l'Ascension [qu'Allah le Très-Haut a dit] : Ô Muḥammad, Mon amour est acquis à ceux qui s'aiment les uns les autres pour Moi; Mon amour est acquis à ceux qui font preuve de gentillesse les uns envers les autres pour Moi; Mon amour est acquis à ceux qui maintiennent leurs liens par amour pour Moi ; Mon amour est acquis à ceux qui remettent leur confiance en Moi. Mon amour n'a pas d'enseigne, ni de sommet, ni de fin. Il ne se manifeste pas sous une enseigne particulière, mais selon des enseignes diverses.<sup>1512</sup>"
    },
    {
        "number": "1326",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Béni et le Très-Haut a dit : «Le moyen le plus aimé par lequel Mon serviteur peut se faire aimer de Moi est [de suivre] ce que Je lui ai rendu obligatoire.»<sup>1513</sup>"
    },
    {
        "number": "1327",
        "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le croyant abandonne la vie d'ici-bas, il s'élève et goûte la douceur de l'amour d'Allah. Il est alors pris pour quelqu'un à l'esprit confus par les gens de ce monde, alors que c'est en réalité eux qui sont confus au sujet de la douceur de l'amour d'Allah de telle façon qu'ils ne s'occupent [en réalité] pas d'un autre que Lui.<sup>1514</sup>"
    }
])

s424['introduction'] = "«Allah aime les bienfaisants.»<sup>1515</sup><br><br>«Allah aime ceux qui se repentent, et Il aime ceux qui se purifient.»<sup>1516</sup><br><br>«Au contraire, celui qui reste fidèle à son engagement et craint Allah... Allah aime les pieux.»<sup>1517</sup><br><br>«Allah aime les endurants.»<sup>1518</sup><br><br>«Allah aime ceux qui remettent en Lui leur confiance.»<sup>1519</sup><br><br>«Allah aime ceux qui jugent équitablement.»<sup>1520</sup><br><br>«Allah aime ceux qui combattent dans Son chemin en rang serré, pareils à un édifice renforcé.»<sup>1521</sup>"
s424['hadiths'].extend([
    {
        "number": "1328",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime le pudique, l'indulgent, le chaste et le vertueux.<sup>1522</sup>"
    },
    {
        "number": "1329",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, Allah aime tout cœur triste et Il aime tout serviteur reconnaissant.<sup>1523</sup>"
    },
    {
        "number": "1330",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah aime celui qui est jovial parmi les gens sans être obscène, qui a une pensée fondée sur le monothéisme, qui s'arme de patience et qui est fier de prier.<sup>1524</sup>"
    }
])

s425['introduction'] = "«Combattez dans le sentier d'Allah ceux qui vous combattent, et ne transgressez pas. Certes, Allah n'aime pas les transgresseurs.»<sup>1525</sup><br><br>«Allah n'aime pas les corrupteurs.»<sup>1526</sup><br><br>«Il n'aime pas les gaspilleurs.»<sup>1527</sup><br><br>«Et assurément Il n'aime pas les orgueilleux.»<sup>1528</sup>"

s426['hadiths'].extend([
    {
        "number": "1331",
        "text": "Le Messager d'Allah (s) a dit : Les serviteurs les plus aimés par Allah sont les plus bénéfiques à Ses serviteurs et les plus zélés dans l'établissement de Son droit ; ce sont ceux qui aiment le convenable et son application.<sup>1529</sup>"
    },
    {
        "number": "1332",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le serviteur le plus aimé par Allah le Tout-Puissant est l'homme véridique dans ses paroles qui observe strictement ses prières ainsi que ce qu'Allah lui a rendu obligatoire, et qui restitue les dépôts confiés.<sup>1530</sup>"
    }
])

s427['introduction'] = "«Dis : «Si vous aimez vraiment Allah, suivez-moi, Allah vous aimera alors et vous pardonnera vos péchés. Allah est Pardonneur et Miséricordieux».»<sup>1531</sup>"
s427['hadiths'].extend([
    {
        "number": "1333",
        "text": "L'Imām 'Alī (as) a dit : Quand Allah aime un serviteur, Il lui inspire de bons actes de dévotion.<sup>1532</sup>"
    },
    {
        "number": "1334",
        "text": "L'Imām al-Ṣādiq (as) a dit : Que celui qui se réjouirait d'apprendre qu'Allah l'aime œuvre dans l'obéissance à Allah et nous suive. N'a-t-il pas entendu la parole d'Allah le Tout-Puissant à Son Prophète (s) : <i>«Dis : «Si vous aimez vraiment Allah, suivez-moi, Allah vous aimera alors et vous pardonnera vos péchés. Allah est Pardonneur et Miséricordieux.»»</i><sup>1533</sup> ?<sup>1534</sup>"
    }
])

s428['hadiths'].append({
    "number": "1335",
    "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui veut savoir l'état de sa considération auprès d'Allah, qu'il observe la considération qu'il donne à Allah en lui-même, car Allah donne à Son serviteur la même considération que le serviteur Lui donne en lui-même.<sup>1535</sup>"
})

s429['hadiths'].extend([
    {
        "number": "1336",
        "text": "Le Messager d'Allah (s) a dit : Le signe de l'amour de [l'homme pour] Allah le Très-Haut est l'amour du rappel d'Allah, et le signe de la haine envers Allah le Très-Haut est la haine du rappel d'Allah le Tout-Puissant.<sup>1536</sup>"
    },
    {
        "number": "1337",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Très-Haut a révélé à Moïse (as) : «A menti celui qui prétend M'aimer alors qu'il dort [et M'oublie] à la tombée de la nuit : tout amoureux n'aime-t-il pas être seul avec son bien aimé ?!»<sup>1537</sup>"
    }
])

s430['hadiths'].append({
    "number": "1338",
    "text": "Le Messager d'Allah (s) a dit : Allah a dit: «Mon serviteur n'a pas de moyen plus aimé pour se faire aimer de Moi que de suivre les obligations auxquelles Je l'ai astreint. En vérité, il cherche à se faire aimer de Moi par les prières surérogatoires jusqu'à ce que Je l'aime. Et lorsque Je l'aime, Je deviens l'oreille avec laquelle il entend, l'œil avec lequel il voit, la langue avec laquelle il parle, la main avec laquelle il saisit, le pied avec lequel il marche. S'il M'appelle, Je lui réponds et s'il Me demande, Je lui donne.»<sup>1538</sup>"
})

s431['hadiths'].extend([
    {
        "number": "1339",
        "text": "Le Messager d'Allah (s) a dit : L'amour de ce monde et l'amour d'Allah ne peuvent jamais coexister dans un même cœur.<sup>1539</sup>"
    },
    {
        "number": "1340",
        "text": "L'Imām al-Ṣādiq (as) a dit : Par Allah, n'aime pas Allah celui qui aime ce monde et qui s'est lié d'amitié avec un autre que nous.<sup>1540</sup><br><br><span class=\"reference-note\">(Voir également : 141. Le monde d'ici-bas, section 721)</span>"
    }
])

s432['hadiths'].append({
    "number": "1341",
    "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit en s'adressant à David (as) : «Aime-Moi, et encourage Mes créatures à M'aimer.» Il dit : «Ô Seigneur ! Je t'aime, mais comment pourrais-je encourager Tes créatures à T'aimer ?» Il dit : «Rappelle-leur Mes grâces, car si tu les leur rappelles, elles M'aimeront.»<sup>1541</sup>"
})

s433['hadiths'].extend([
    {
        "number": "1342",
        "text": "Le Messager d'Allah (s) a dit : La meilleure des actions est d'aimer pour Allah et de détester pour Allah le Très-Haut.<sup>1542</sup>"
    },
    {
        "number": "1343",
        "text": "Le Messager d'Allah (s) a dit en s'adressant à l'un de ses compagnons : Ô serviteur d'Allah ! Aime pour Allah et déteste pour Allah, lie-toi d'amitié pour Allah et fais preuve d'inimitié pour Allah car la proche amitié (<i>wilāya</i>) avec Allah n'est atteinte que grâce à cela. L'homme ne trouvera le goût de la foi - même si ses prières et son jeûne sont nombreux - que lorsqu'il agira ainsi. Cependant, [actuellement] la fraternité entre les hommes est surtout pour ce bas-monde ; ils s'aiment pour lui et se détestent pour lui.<sup>1543</sup>"
    },
    {
        "number": "1344",
        "text": "L'Imām al-Ṣādiq (as) a dit : Deux croyants ne se rencontrent pas sans que le meilleur soit celui qui aime davantage l'autre.<sup>1544</sup>"
    },
    {
        "number": "1345",
        "text": "L'Imām al-Ṣādiq (as) a dit : Toute personne qui n'aime pas pour la religion et ne déteste pas pour la religion est sans religion.<sup>1545</sup>"
    },
    {
        "number": "1346",
        "text": "L'Imām al-Jawād (as) a dit : Allah a révélé à un prophète : «Ton renoncement aux plaisirs de ce monde hâte ton repos, et ta dévotion pour Moi te rend cher auprès de Moi. En revanche, as-tu voué de l'animosité à [l']un [de Mes] ennemis pour Moi, ou t'es-tu lié d'amitié à un être pour Moi ?»<sup>1546</sup>"
    }
])

s434['hadiths'].extend([
    {
        "number": "1347",
        "text": "Le Messager d'Allah (s) a dit : Le serviteur ne devient vraiment croyant que s'il m'aime plus que sa propre personne, qu'il aime plus mes descendants que ses propres descendants, qu'il aime plus ma famille que sa propre famille, et qu'il aime plus mon être que son propre être.<sup>1547</sup>"
    },
    {
        "number": "1348",
        "text": "Le Messager d'Allah (s) a dit : Aimez Allah pour les bienfaits dont Il vous comble chaque matin, aimez-moi par amour d'Allah, et aimez ma famille par amour pour moi.<sup>1548</sup>"
    },
    {
        "number": "1349",
        "text": "<i>Al-Maḥāsin</i> : L'Imām al-Ṣādiq (as) rapporte de ses pères (as) : Le Messager d'Allah (s) a dit : «Celui qui nous aime, nous les Gens de la demeure, qu'il rende grâce à Allah pour la première des grâces.» On lui demanda : «Quelle est la première grâce ?» Il répondit : «Une naissance pure [une conception légitime], car ne nous aime que celui qui est de naissance pure.»<sup>1549</sup>"
    },
    {
        "number": "1350",
        "text": "<i>Al-Da'awāt</i> : Ḥārith al-Hamadānī a dit: Un jour, je suis allé voir l'Emir des croyants (as) à midi. Il me dit : «Quelle est la raison de ta venue ?» Je lui répondis : «Mon amour pour toi, par Allah.» Il (as) me dit : «Si tu es sincère, tu me verras en trois lieux : quand ton âme parviendra à cet endroit - et il désigna sa gorge -, sur le pont <i>ṣirāṭ</i> [étendu au-dessus de l'Enfer], et auprès des eaux paradisiaques.»<sup>1550</sup>"
    },
    {
        "number": "1351",
        "text": "L'Imām al-Bāqir (as) a dit en commentant la parole du Très-Haut : <i>«il a saisi l'anse la plus solide»</i><sup>1551</sup> : C'est l'affection pour nous, les Gens de la demeure prophétique (Ahl al-Bayt).<sup>1552</sup>"
    }
])

s435['hadiths'].append({
    "number": "1352",
    "text": "L'Imām al-Bāqir (as) a dit : Par Allah, nous n'avons pas d'immunité face à Allah, il n'y a entre nous et Allah aucune parenté, nous ne possédons aucun argument contre Allah, et nous ne nous rapprochons de Lui que par Son obéissance. Dès lors, celui parmi vous qui obéit à Allah bénéficiera de notre proche amitié (<i>wilāya</i>), tandis que notre proche amitié ne sera d'aucune utilité à celui qui désobéit à Allah. Malheur à vous, ne vous laissez pas tromper ! Malheur à vous, ne vous laissez pas tromper!<sup>1553</sup>"
})

s436['hadiths'].extend([
    {
        "number": "1353",
        "text": "L'Imām 'Alī (as) a dit : La fraternité pour Allah rend l'amour sincère.<sup>1554</sup>"
    },
    {
        "number": "1354",
        "text": "L'Imām 'Alī (as) a dit : Celui dont l'amitié est pour Allah sera de bonne compagnie et son amour authentique.<sup>1555</sup>"
    }
])

s437['hadiths'].extend([
    {
        "number": "1355",
        "text": "Le Messager d'Allah (s) a dit : L'homme est avec ceux qu'il aime.<sup>1556</sup>"
    },
    {
        "number": "1356",
        "text": "<i>Kanz al-'Ummāl</i> : Un homme interrogea le Messager d'Allah (s) au sujet de l'Heure [finale]. Il lui répondit : «Comment t'es-tu préparé pour cela ?» L'homme répondit : «Je n'ai pas préparé grand-chose [d'autre que les actes obligatoires], sauf mon amour pour Allah et Son Messager.» Et le Prophète lui dit : «Alors tu seras avec ceux que tu aimes.»<sup>1557</sup>"
    }
])

# Part 85 (index 86) - L'emprisonnement
p85 = 86
s438 = find_subpart(p85, "438")
clear_hadiths(s438)

s438['hadiths'].extend([
    {
        "number": "1357",
        "text": "L'Imām 'Alī (as) a dit : L'Imām est dans l'obligation d'emprisonner les savants immoraux, les médecins ignorants, et les locataires ruinés.<sup>1558</sup>"
    },
    {
        "number": "1358",
        "text": "L'Imām 'Alī (as) a dit : Si une femme abjure l'islam, elle ne sera pas tuée mais emprisonnée à perpétuité.<sup>1559</sup>"
    }
])

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1279-1358")
