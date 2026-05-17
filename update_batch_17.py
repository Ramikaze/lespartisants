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

# Part 95 - La profession
p95 = 96
s500 = find_subpart(p95, "500")
clear_hadiths(s500)

s500['hadiths'].extend([
    {
        "number": "1502",
        "text": "L'Imām 'Alī (as) a dit : La convoitise et l'avarice empreinte d'avidité sont fondées sur le doute et le manque de confiance en Allah.<sup>1719</sup>"
    },
    {
        "number": "1503",
        "text": "L'Imām 'Alī (as) a dit : L'intense convoitise est issue de l'ardeur de la voracité et de la faiblesse de la religion.<sup>1720</sup>"
    },
    {
        "number": "1504",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime le serviteur croyant engagé dans une profession.<sup>1721</sup>"
    },
    {
        "number": "1505",
        "source": "Jāmi' al-Akhbār",
        "text": "rapporte d'Ibn 'Abbās: Lorsqu'il voyait un homme qui lui plaisait, le Messager d'Allah (s) avait pour habitude de demander : «A-t-il une profession ?» S'ils répondaient : «Non», il disait : «Il est descendu dans mon estime.» On demanda alors: «Pourquoi cela, ô Messager d'Allah ?» Il répondit : «Car lorsque le croyant n'exerce pas de profession, il subsiste de par sa religion.»<sup>1722</sup>"
    },
    {
        "number": "1506",
        "text": "L'Imām 'Alī (as) a dit : Initiez-vous au commerce car cela vous rendra indépendant vis-à-vis de ce que détiennent les gens, et en vérité, Allah le Tout-Puissant aime le serviteur probe engagé dans une profession.<sup>1723</sup>"
    },
    {
        "number": "1507",
        "source": "Da'ā'im al-Islām",
        "text": "rapporte de l'Imām al-Ṣādiq (as) qui interrogea l'un de ses compagnons au sujet de ses sources de revenu. Le compagnon lui répondit : «Que je te sois sacrifié, j'ai arrêté le commerce.» L'Imām (as) lui demanda : «Pour quelle raison ?» Il répondit : «Car j'attends l'avènement de cet ordre [de votre gouvernement].» Et l'Imām rétorqua : «Ton comportement est étrange. Tu vas perdre tes biens. N'arrête pas ton commerce, et recherche les bienfaits d'Allah. Ouvre donc ta porte, étale tes marchandises et demande ta subsistance à ton Seigneur.»<sup>1724</sup><br><br><span class=\"hadith-footnote\">(Voir également : 55. Le commerce ; 343. Le gain)</span>"
    }
])


# Part 96 - L'illicite
p96 = 97
s501 = find_subpart(p96, "501")
s502 = find_subpart(p96, "502")
s503 = find_subpart(p96, "503")

for s in [s501, s502, s503]:
    clear_hadiths(s)

s501['hadiths'].extend([
    {
        "number": "1508",
        "text": "L'Imām 'Alī (as) a dit : Si tu aspires aux vertus, évite l'illicite.<sup>1725</sup>"
    },
    {
        "number": "1509",
        "text": "L'Imām 'Alī (as) a dit : La meilleure des vertus est d'éviter l'illicite.<sup>1726</sup>"
    },
    {
        "number": "1510",
        "text": "L'Imām 'Alī (as) a dit : Même si Allah - loué soit-Il - n'avait pas interdit l'illicite, il aurait [au moins] été obligatoire à la personne intelligente de l'éviter.<sup>1727</sup>"
    }
])

s502['hadiths'].extend([
    {
        "number": "1511",
        "text": "Le Messager d'Allah (s) a dit : L'adoration associée à la consommation de l'illicite est semblable à une construction sur du sable - ou sur de l'eau [selon une autre narration].<sup>1728</sup>"
    },
    {
        "number": "1512",
        "text": "Le Messager d'Allah (s) a dit : S'abstenir de consommer [même] une bouchée illicite est plus aimé par Allah que deux mille <i>raka'āt</i> de prières surérogatoires.<sup>1729</sup>"
    },
    {
        "number": "1513",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, quand un homme accumule de l'argent illicite, ne seront acceptés ni son pèlerinage obligatoire (<i>ḥajj</i>), ni son pèlerinage recommandé (<i>'umra</i>), ni le maintien de ses liens familiaux, et cela pourra même gâcher son mariage.<sup>1730</sup>"
    },
    {
        "number": "1514",
        "text": "L'Imām al-Ṣādiq (as) a dit en commentant la parole du Très-Haut <i>«Nous avons considéré l'œuvre qu'ils ont accomplie et Nous l'avons réduite en poussière éparpillée»</i><sup>1731</sup> : Par Allah, bien que leurs œuvres étaient plus blanches que le coton égyptien, ils ne s'éloignaient pas de l'illicite si on le leur présentait.<sup>1732</sup>"
    }
])

s503['hadiths'].extend([
    {
        "number": "1515",
        "text": "Le Messager d'Allah (s) a dit : Celui qui peut entretenir une relation illicite avec une femme ou une servante et qui s'en abstient par crainte d'Allah, Allah le Tout-Puissant lui interdira le Feu, le préservera de la Grande frayeur, et le fera entrer au Paradis.<sup>1733</sup>"
    },
    {
        "number": "1516",
        "text": "Le Messager d'Allah (s) a dit : Allah donnera à l'homme qui peut commettre un acte illicite et qui s'en abstient uniquement par crainte d'Allah, ce qui est meilleur que cela pour lui dans cette vie avant l'Au-delà.<sup>1734</sup>"
    },
    {
        "number": "1517",
        "text": "L'Imām al-Kāẓim (as) a dit : Le Messager d'Allah (s) avait l'habitude de rendre visite aux gens des Abords (<i>Ahl al-Ṣuffa</i>) [de la Mosquée], qui étaient ses invités et avaient quitté leurs familles et leurs biens pour émigrer à Médine. Le Prophète (s) les avait installés aux abords de la Mosquée. Ils étaient quatre cent hommes, et il (s) venait les saluer matin et soir. Un jour, il (s) vint les voir alors que certains étaient occupés à raccommoder leurs sandales, d'autres à rapiécer leurs vêtements ou encore à s'épouiller. Le Prophète (s) avait pour habitude de leur donner chaque jour un demi-boisseau de dattes.<br>Un jour, l'un des hommes se leva et dit : «Ô Messager d'Allah ! Les dattes que tu nous donnes ont brûlé nos estomacs !» Le Messager d'Allah (s) lui dit : «Si j'avais pu vous nourrir avec l'ensemble de ce monde, je l'aurais fait. Cependant, [sachez que] ceux d'entre vous qui me survivront se verront servir des bols [de nourriture] matin et soir, et chacun d'entre vous revêtira une chemise le matin et une autre le soir, et vous ornerez vos maisons [de rideaux et de tapis] comme l'est la Ka'ba.» Un homme se leva et dit : «Ô Messager d'Allah, nous sommes impatients que ce moment vienne, quand cela aura-t-il lieu ?» Il (s) répondit: «L'époque à laquelle vous vivez actuellement est meilleure que celle-là. En vérité, lorsque vous vous remplissez le ventre de ce qui est licite, il est fort possible que vous le remplissiez également de ce qui est illicite.»<sup>1735</sup>"
    }
])


# Part 97 - Le parti
p97 = 98
s504 = find_subpart(p97, "504")
s505 = find_subpart(p97, "505")

for s in [s504, s505]:
    clear_hadiths(s)

s504['introduction'] = "«Et quiconque prend pour alliés Allah, Son messager et les croyants [réussira], car c'est le parti d'Allah qui sera victorieux.»<sup>1736</sup>"
s504['hadiths'].extend([
    {
        "number": "1518",
        "text": "L'Imām 'Alī (as) a dit : Te réjouirais-tu d'être dans le parti vainqueur d'Allah ? Alors crains Allah - loué soit-Il -, et sois bienfaisant dans tous tes actes, car Allah est avec ceux qui Le craignent et qui sont bienfaisants.<sup>1737</sup>"
    },
    {
        "number": "1519",
        "text": "L'Imām al-Ṣādiq (as) a dit : Nous sommes, ainsi que nos partisans (<i>shī'a</i>), le parti d'Allah, et [les membres du] parti d'Allah sont les vainqueurs.<sup>1738</sup>"
    }
])

s505['introduction'] = "«Le Diable les a dominés et leur a fait oublier le rappel d'Allah. Ceux-là sont le parti du Diable, et c'est le parti du Diable qui sont assurément les perdants.»<sup>1739</sup>"
s505['hadiths'].extend([
    {
        "number": "1520",
        "text": "L'Imām 'Alī (as) a dit : Ô gens ! En vérité, les dissensions ne commencent que lorsque l'on suit ses passions... Si la vérité était dans son état pur, il n'y aurait pas eu de discorde, Cependant, les gens prennent une portion de ceci [la vérité] et une portion de cela [le faux], les mélangent, et [le vrai et le faux] apparaissent ainsi ensemble. C'est là que Satan domine ses alliés, cependant, ceux qui ont été auparavant l'objet de la grâce d'Allah seront sauvés.<sup>1740</sup>"
    },
    {
        "number": "1521",
        "text": "L'Imām 'Alī (as) a dit dans l'un de ses sermons où il décrit les hypocrites : Ils sont les compagnons de Satan, la chaleur ardente du Feu. Ceux-là sont le parti de Satan ; en vérité, [les membres du] parti de Satan sont les perdants.<sup>1741</sup><br><br><span class=\"hadith-footnote\">(Voir également : 216. Satan, section 1029)</span>"
    }
])


# Part 98 - La prudence
p98 = 99
s506 = find_subpart(p98, "506")
s507 = find_subpart(p98, "507")
s508 = find_subpart(p98, "508")
s509 = find_subpart(p98, "509")
s510 = find_subpart(p98, "510")
s511 = find_subpart(p98, "511")

for s in [s506, s507, s508, s509, s510, s511]:
    clear_hadiths(s)

s506['hadiths'].extend([
    {
        "number": "1522",
        "text": "L'Imām 'Alī (as) a dit : La prudence est de la perspicacité.<sup>1742</sup>"
    },
    {
        "number": "1523",
        "text": "L'Imām 'Alī (as) a dit : Celui qui est prudent triomphera, et celui qui manque de prudence sera vaincu.<sup>1743</sup>"
    },
    {
        "number": "1524",
        "text": "L'Imām 'Alī (as) a dit : La prudence avant la mise en application te protège du regret.<sup>1744</sup>"
    },
    {
        "number": "1525",
        "text": "L'Imām 'Alī (as) a dit : Les personnes les plus intelligentes sont celles qui prévoient les conséquences.<sup>1745</sup>"
    },
    {
        "number": "1526",
        "text": "L'Imām al-Ṣādiq (as) a dit : La prudence permet d'éclairer le doute.<sup>1746</sup>"
    }
])

s507['hadiths'].append({
    "number": "1527",
    "text": "L'Imām 'Alī (as) a dit : Celui qui s'enlise dans des choses sans avoir réfléchi aux conséquences s'expose aux difficultés.<sup>1747</sup>"
})

s508['hadiths'].extend([
    {
        "number": "1528",
        "text": "L'Imām 'Alī (as) a dit : La victoire vient de la prudence et de la détermination.<sup>1748</sup>"
    },
    {
        "number": "1529",
        "text": "L'Imām 'Alī (as) a dit : Il n y a rien de bon dans une décision [prise avec détermination] sans prudence.<sup>1749</sup>"
    }
])

s509['hadiths'].extend([
    {
        "number": "1530",
        "text": "L'Imām 'Alī (as) a dit : La prudence est de prendre en compte les conséquences et de demander conseil aux gens réfléchis.<sup>1750</sup>"
    },
    {
        "number": "1531",
        "text": "L'Imām 'Alī (as) a dit : La base de la prudence est de s'abstenir dans le doute.<sup>1751</sup>"
    },
    {
        "number": "1532",
        "text": "L'Imām 'Alī (as) a dit : Avoir un sentiment de certitude et de quiétude avant de connaître est contraire à la prudence.<sup>1752</sup>"
    }
])

s510['hadiths'].extend([
    {
        "number": "1533",
        "text": "L'Imām 'Alī (as) a dit : La personne prudente est celle que l'illusion de ce bas-monde ne préoccupe pas aux dépens de l'action pour l'Au-delà.<sup>1753</sup>"
    },
    {
        "number": "1534",
        "text": "L'Imām 'Alī (as) a dit : La personne prudente est celle qui a bien choisi ses amis, car l'être est jugé d'après ses amis.<sup>1754</sup>"
    },
    {
        "number": "1535",
        "text": "L'Imām 'Alī (as) a dit : La personne prudente est celle que la prospérité [de ce bas-monde] ne distrait pas des actes en vue de l'Au-delà.<sup>1755</sup>"
    },
    {
        "number": "1536",
        "text": "L'Imām 'Alī (as) a dit : La personne prudente est celle qui retarde la punition lorsqu'elle est submergée par la colère et qui hâte la récompense de la bienfaisance à la première occasion possible.<sup>1756</sup>"
    }
])

s511['hadiths'].extend([
    {
        "number": "1537",
        "text": "Le Messager d'Allah (s) a dit : La plus prudente des personnes est celle qui maîtrise le mieux sa colère.<sup>1757</sup>"
    },
    {
        "number": "1538",
        "text": "Le Messager d'Allah (s) a dit : Les plus perspicaces parmi vous sont ceux qui se souviennent le plus de la mort, et les plus prudents sont ceux qui sont le mieux préparés à cela.<sup>1758</sup>"
    },
    {
        "number": "1539",
        "text": "L'Imām 'Alī (as) a dit : Les plus prudents parmi vous sont ceux qui renoncent le plus et qui sont les plus sobres.<sup>1759</sup>"
    }
])


# Part 99 - Le chagrin
p99 = 100
s512 = find_subpart(p99, "512")
s513 = find_subpart(p99, "513")
s514 = find_subpart(p99, "514")
s515 = find_subpart(p99, "515")
s516 = find_subpart(p99, "516")

for s in [s512, s513, s514, s515, s516]:
    clear_hadiths(s)

s512['hadiths'].extend([
    {
        "number": "1540",
        "text": "Jésus (as) a dit : Le corps de celui qui est très soucieux deviendra souffrant.<sup>1760</sup>"
    },
    {
        "number": "1541",
        "text": "L'Imām 'Alī (as) a dit : Le souci est la moitié de la vieillesse.<sup>1761</sup>"
    },
    {
        "number": "1542",
        "text": "L'Imām 'Alī (as) a dit : Le souci dissout le corps.<sup>1762</sup>"
    },
    {
        "number": "1543",
        "text": "L'Imām al-Ṣādiq (as) a dit : Les chagrins sont l'affection du cœur tout comme les maladies sont l'affection du corps.<sup>1763</sup><br><br><span class=\"hadith-footnote\">(Voir également : 141. Le monde d'ici-bas, section 712)</span>"
    }
])

s513['hadiths'].extend([
    {
        "number": "1544",
        "text": "Le Messager d'Allah (s) a dit : Celui qui regarde ce que les autres possèdent verra son chagrin être permanent et son regret continuel.<sup>1764</sup>"
    },
    {
        "number": "1545",
        "text": "Le Messager d'Allah (s) a dit : Combien de plaisirs d'une heure suscitent un chagrin de longue durée !<sup>1765</sup>"
    },
    {
        "number": "1546",
        "text": "L'Imām 'Alī (as) a dit : Celui qui est en colère contre une personne qu'il ne peut atteindre verra son chagrin se prolonger et sera tourmenté.<sup>1766</sup>"
    },
    {
        "number": "1547",
        "text": "L'Imām 'Alī (as) a dit : Je n'ai vu de personne injuste qui soit aussi semblable à la personne victime d'injustice que le jaloux : il a une âme fatiguée, un cœur affligé et un chagrin perpétuel.<sup>1767</sup>"
    },
    {
        "number": "1548",
        "text": "L'Imām 'Alī (as) a dit : Celui qui néglige ses actes sera éprouvé par le souci.<sup>1768</sup>"
    },
    {
        "number": "1549",
        "text": "L'Imām 'Alī (as) a dit : Gare à l'anxiété car elle brise l'espoir, affaiblit les actes et rend soucieux.<sup>1769</sup>"
    }
])

s514['introduction'] = "«En vérité, les bien-aimés d'Allah seront à l'abri de toute crainte, et ils ne seront point affligés.»<sup>1770</sup>"
s514['hadiths'].extend([
    {
        "number": "1550",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah, par Sa sagesse et Sa grâce, a fait en sorte que la sérénité et la joie soient dans la certitude et la satisfaction, tandis que le souci et le chagrin soient dans le doute et le mécontentement [par rapport à Allah].<sup>1771</sup>"
    },
    {
        "number": "1551",
        "text": "Le Messager d'Allah (s) a dit : Ô gens ! Cette vie est la demeure du chagrin, non celle de la joie ; c'est la demeure des difficultés, non celle du repos. Celui qui la connait ne se réjouira pas d'une espérance et ne sera pas chagriné par une peine.<sup>1772</sup>"
    },
    {
        "number": "1552",
        "text": "Le Messager d'Allah (s) a dit : La parole <i>«Il n'y a de force et de puissance qu'en Allah» (lā ḥawla wa lā quwwata illā billāh al-'alīy al-'aẓīm)</i> guérit quatre-vingt-dix-neuf douleurs, la plus simple étant le souci.<sup>1773</sup>"
    },
    {
        "number": "1553",
        "source": "Maṭālib al-Sa'ūl",
        "text": "Ibn 'Abbās a dit : Après celles du Messager d'Allah (s), nulle parole ne m'a été plus bénéfique que la lettre que m'a écrite 'Alī ibn Abī Ṭālib (as). En effet, il m'a écrit : «Maintenant, l'être humain ressent de la peine pour avoir raté une chose qu'il n'aurait pu atteindre, et il est heureux d'atteindre une chose qu'il n'aurait pas pu manquer. Dès lors, que ta joie soit pour ce que tu atteins en vue de ta vie future, et que ton regret ne soit que pour ce que tu as manqué dans cette voie. Ce que tu as obtenu dans ce monde ne doit pas te réjouir et ce que tu as manqué ne doit pas te chagriner. Que ton souci soit pour ce qui vient après la mort, et que la Paix soit avec toi.»<sup>1774</sup>"
    },
    {
        "number": "1554",
        "text": "L'Imām 'Alī (as) a dit : Quel bon remède aux soucis que la certitude !<sup>1775</sup>"
    },
    {
        "number": "1555",
        "text": "L'Imām 'Alī (as) a dit : Laver les vêtements chasse le souci et le chagrin.<sup>1776</sup>"
    },
    {
        "number": "1556",
        "text": "L'Imām al-Ṣādiq (as) a dit : Si toute chose est déterminée par le destin et le décret [divin], alors pourquoi avoir du chagrin ?<sup>1777</sup>"
    },
    {
        "number": "1557",
        "text": "L'Imām al-Ṣādiq (as) a dit : Un prophète se plaint à Allah d'une peine. Il lui ordonna alors de manger du raisin.<sup>1778</sup>"
    },
    {
        "number": "1558",
        "text": "L'Imām al-Ṣādiq (as) a dit : Que celui qui est soucieux sans en savoir sa cause se lave la tête.<sup>1779</sup><br><br><span class=\"hadith-footnote\">(Voir également : 187. La joie, section 935)</span>"
    }
])

s515['hadiths'].extend([
    {
        "number": "1559",
        "source": "'Ilal al-Sharā'i'",
        "text": "Abū Baṣīr a dit : Je suis entré chez l'Imām al-Ṣādiq (as) accompagné de l'un de nos compagnons. Je lui dis : «Que je vous sois sacrifié, ô fils du Messager d'Allah. En vérité, je suis peiné et attristé sans en savoir la cause.» L'Imām (as) me répondit : «En vérité, ce chagrin et cette joie vous vient de nous. Ainsi, s'il nous arrive un chagrin ou une joie, cela vous atteindra, car vous et nous sommes de la lumière d'Allah le Tout-Puissant.»<sup>1780</sup>"
    },
    {
        "number": "1560",
        "source": "Biḥār al-Anwār",
        "text": "L'érudit [l'Imām al-Ṣādiq] (as) fut interrogé au sujet d'un homme qui se réveillait attristé sans en savoir la raison. Il répondit : «Si cela lui arrive, qu'il sache que son frère est attristé ; de même s'il se réveille en étant heureux sans raison apparente qui suscite la joie. Nous demandons à Allah Son aide pour [accomplir] nos devoirs envers nos frères.»<sup>1781</sup>"
    }
])

s516['hadiths'].extend([
    {
        "number": "1561",
        "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant ne peut être mieux adoré qu'avec un chagrin continuel.<sup>1782</sup>"
    },
    {
        "number": "1562",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, Allah aime tout cœur triste.<sup>1783</sup>"
    }
])

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1502-1562")
