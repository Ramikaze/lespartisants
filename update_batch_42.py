import json
import re

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(pi, ss):
    for s in data[pi].get('subparts', []):
        if ss in s['title']:
            return s
    return None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# Part 163 (index 164) - LA SATISFACTION (1)
# ============================================================
p163 = 164

# Subpart 827 - La vertu de la satisfaction
s827 = find_subpart(p163, "827"); eh(s827)
# Keep existing hadiths 2606-2610, and append 2611-2612
s827['hadiths'] = [h for h in s827['hadiths'] if int(h['number']) <= 2610]
s827['hadiths'].extend([
    {
        "number": "2611",
        "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'il parlait d'un fait passé, le Messager d'Allah (s) ne disait jamais : «Si seulement cela s'était passé autrement !»<sup>2957</sup>"
    },
    {
        "number": "2612",
        "text": "L'Imām al-Ṣādiq (as) a dit : La base de l'obéissance à Allah est d'être satisfait vis-à-vis de tout ce qu'Allah a fait, que ce soit concernant ce que le serviteur aime ou concernant ce qu'il déteste.<sup>2958</sup>"
    }
])

# Subpart 828 - Ce qui suscite la satisfaction [vis-à-vis du décret divin]
s828 = find_subpart(p163, "828"); eh(s828)
s828['hadiths'] = [
    {
        "number": "2613",
        "text": "L'Imām 'Alī (as) a dit : L'origine de la satisfaction est la confiance en Allah.<sup>2959</sup>"
    },
    {
        "number": "2614",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, ceux qui connaissent le mieux Allah sont ceux qui sont les plus satisfaits vis-à-vis du décret d'Allah.<sup>2960</sup>"
    }
]

# Subpart 829 - Les fruits de la satisfaction
s829 = find_subpart(p163, "829"); eh(s829)
s829['hadiths'] = [
    {
        "number": "2615",
        "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah aime un serviteur, Il l'éprouve ; s'il patiente, Il le choisit [pour Sa proximité] et s'il est satisfait, Il l'élit et le distingue [par un statut plus élevé].<sup>2961</sup>"
    },
    {
        "number": "2616",
        "text": "Le Messager d'Allah (s) a dit : Sois satisfait de ce qu'Allah t'a destiné et tu seras la plus riche des personnes.<sup>2962</sup>"
    },
    {
        "number": "2617",
        "text": "L'Imām 'Alī (as) a dit : La satisfaction éloigne la tristesse.<sup>2963</sup>"
    },
    {
        "number": "2618",
        "text": "L'Imām 'Alī (as) a dit : En vérité, les gens qui ont la vie la plus agréable sont ceux qui sont satisfaits de ce qu'Allah leur a destiné.<sup>2964</sup>"
    },
    {
        "number": "2619",
        "text": "L'Imām Ḥasan (as) a dit : Je garantis à celui qui ne laisse de place à rien hormis la satisfaction [vis-à-vis d'Allah] dans son cœur que s'il invoque Allah, Il lui répondra.<sup>2965</sup>"
    },
    {
        "number": "2620",
        "text": "L'Imām al-Ṣādiq (as) a dit : La quiétude et le confort se trouvent dans la satisfaction et la certitude, alors que le souci et la tristesse se trouvent dans le doute et le mécontentement.<sup>2966</sup>"
    }
]

# Subpart 830 - Les conséquences de l'insatisfaction
s830 = find_subpart(p163, "830"); eh(s830)
s830['hadiths'] = [
    {
        "number": "2621",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui n'est pas satisfait de ce qu'Allah le Tout-Puissant lui a destiné remet en cause et accuse Allah dans Son décret.<sup>2967</sup>"
    },
    {
        "number": "2622",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est satisfait du décret divin vivra selon ce décret et il sera rétribué [pour sa satisfaction]. En revanche, celui qui n'est pas satisfait du décret divin vivra tout de même selon ce décret, et Allah anéantira sa récompense.<sup>2628</sup><br>(Voir également : 392. Le destin, section 159)"
    }
]

# ============================================================
# Part 164 (index 165) - LA SATISFACTION (2)
# ============================================================
p164 = 165

# Subpart 831 - Ce qui suscite l'agrément d'Allah
s831 = find_subpart(p164, "831"); eh(s831)
s831['introduction'] = (
    "«<i>Est-ce que celui qui se conforme à l'agrément d'Allah ressemble à celui qui encourt "
    "le courroux d'Allah ? Son refuge sera l'Enfer ; et quelle mauvaise destination !</i>»<sup>2969</sup>"
    "<br><br><span class=\"reference-note\">(Voir également : Coran 3:15, 9:21, 9:109, 9:72, 9:100, 5:119, "
    "9:82, 9:16, 48:29, 58:22, 47:28)</span>"
)
s831['hadiths'] = [
    {
        "number": "2623",
        "text": "Biḥār al-Anwār : Il a été rapporté que Moïse (as) a dit : «Ô Seigneur, guide-moi vers un acte dont la réalisation me permettra d'atteindre Ta satisfaction.» Allah lui révéla : «Ô fils de 'Imrān, Ma satisfaction réside dans ce que tu détestes et ce que tu ne pourras supporter.» Moïse tomba alors prosterné en pleurant et dit : «Ô Seigneur ! Tu m'as choisi pour me parler alors que Tu n'avais jamais parlé à un humain avant moi, et Tu ne veux pas me guider vers un acte par lequel j'atteindrai Ta satisfaction ?» Et Allah lui révéla : «En vérité, Ma satisfaction réside dans ta satisfaction vis-à-vis de Mon décret.»<sup>2970</sup>"
    },
    {
        "number": "2624",
        "text": "L'Imām 'Alī (as) a dit : Trois choses permettent au serviteur d'atteindre l'agrément d'Allah : multiplier la demande de pardon, l'affabilité vis-à-vis des gens, et multiplier les actes de charité (ṣadaqa).<sup>2971</sup>"
    },
    {
        "number": "2625",
        "text": "L'Imām 'Alī (as) a dit : Celui qui a mécontenté son corps aura satisfait son Seigneur, et celui qui n'est pas disposé à le faire aura désobéi à son Seigneur.<sup>2972</sup>"
    },
    {
        "number": "2626",
        "text": "L'Imām 'Alī (as) a dit : Il [Allah] vous a conseillé la piété et la crainte révérencielle, et Il a fait en sorte que ce soit le sommet de Sa satisfaction ainsi que Sa demande envers Ses créatures.<sup>2973</sup>"
    },
    {
        "number": "2627",
        "text": "L'Imām 'Alī (as) a dit : La satisfaction d'Allah - loué soit-Il - va de pair avec Son obéissance.<sup>2974</sup>"
    },
    {
        "number": "2628",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, celui parmi vous vis-à-vis duquel Allah est le plus satisfait est celui qui comble le plus sa famille.<sup>2975</sup>"
    }
]

# ============================================================
# Part 165 (index 166) - LA DOUCEUR
# ============================================================
p165 = 166

# Subpart 834 - La vertu de la douceur
s834 = find_subpart(p165, "834"); eh(s834)
s834['hadiths'] = [
    {
        "number": "2634",
        "text": "Le Messager d'Allah (s) a dit : Quand deux personnes se lient d'amitié, la plus rétribuée et la plus aimée d'Allah le Tout-Puissant est celle qui est la plus douce envers son ami.<sup>2976</sup>"
    },
    {
        "number": "2635",
        "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah veut du bien aux membres d'une famille, Il introduit parmi eux la douceur.<sup>2977</sup>"
    },
    {
        "number": "2636",
        "text": "Le Messager d'Allah (s) a dit : La plus intelligente des personnes est celle qui ménage le plus les autres.<sup>2978</sup>"
    },
    {
        "number": "2637",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Tout-Puissant est doux, et Il aime la douceur en toute chose.<sup>2979</sup>"
    },
    {
        "number": "2638",
        "text": "L'Imām 'Alī (as) a dit : La douceur est la clé de la réussite.<sup>2980</sup>"
    },
    {
        "number": "2639",
        "text": "L'Imām al-Bāqir (as) a dit : Chaque chose a une serrure et la serrure de la foi is la douceur.<sup>2981</sup>"
    },
    {
        "number": "2640",
        "text": "L'Imām al-Kāẓim (as) a dit : La douceur est la moitié de la vie.<sup>2982</sup>"
    }
]

# Subpart 835 - La douceur dans l'adoration
s835 = find_subpart(p165, "835"); eh(s835)
s835['hadiths'] = [
    {
        "number": "2641",
        "text": "Le Messager d'Allah (s) a dit : En vérité, cette religion est solide, alors entrez-y doucement. Ne suscite pas l'aversion des serviteurs d'Allah vis-à-vis de l'adoration d'Allah, sinon vous deviendrez comme des cavaliers dispersés qui n'ont pas voyagé et n'ont pas de monture pour continuer.<sup>2983</sup>"
    },
    {
        "number": "2642",
        "text": "L'Imām 'Alī (as) a dit : Ruse avec ton âme pour [l'inciter à] l'adoration, sois doux vis-à-vis d'elle et ne la contrains pas. Tiens compte de sa fatigue et de son énergie, sauf quand il s'agit des obligations ordonnées car on doit les réaliser et s'en acquitter aux moments prescrits.<sup>2984</sup><br>(Voir également : 261. L'adoration, section 1218)"
    }
]

# Subpart 836 - Les fruits de la douceur
s836 = find_subpart(p165, "836"); eh(s836)
s836['hadiths'] = [
    {
        "number": "2643",
        "text": "Le Messager d'Allah (s) a dit : En vérité, dans la douceur se trouve l'abondance et la bénédiction. Dès lors, celui qui est privé de la douceur est privé du bien.<sup>2985</sup>"
    },
    {
        "number": "2644",
        "text": "L'Imām 'Alī (as) a dit : La douceur rend aisés les obstacles et facilite les situations difficiles.<sup>2986</sup>"
    },
    {
        "number": "2645",
        "text": "L'Imām Husayn (as) a dit : Pour celui qui ne parvient pas à prendre une décision et qui n'a pas de solution, la douceur est la clé [de la résolution du problème].<sup>2987</sup>"
    },
    {
        "number": "2646",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Le dernier conseil que al-Khiḍr donna à Moïse fils de 'Imrān (as) fut : «Nul ne fait preuve de douceur envers autrui dans ce monde sans qu'Allah le Tout-Puissant ne fasse preuve de douceur à son égard le Jour de la Résurrection.»<sup>2988</sup>"
    },
    {
        "number": "2647",
        "text": "L'Imām al-Ṣādiq (as) a dit : Si tu veux être honoré, sois doux et si tu veux être humilié, sois dur.<sup>2989</sup>"
    },
    {
        "number": "2648",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est doux dans ses affaires obtiendra ce qu'il veut des gens.<sup>2990</sup>"
    }
]

# ============================================================
# Part 166 (index 167) - L'OBSERVATION [DES ACTES DE L'HOMME]
# ============================================================
p166 = 167

# Subpart 837 - L'observation [des actes de l'homme] par Allah, les anges et les membres du corps
s837 = find_subpart(p166, "837"); eh(s837)
s837['introduction'] = (
    "«<i>Certes Allah vous observe parfaitement.</i>»<sup>2991</sup><br><br>"
    "«<i>Il ne prononce aucune parole sans avoir auprès de lui un observateur prêt à l'inscrire.</i>»<sup>2992</sup>"
)
s837['hadiths'] = [
    {
        "number": "2649",
        "text": "L'Imām 'Alī (as) a dit : Sachez, ô serviteurs d'Allah, que vous êtes observés par vos propres personnes, et que les membres de votre corps ont un œil sur vous. Et les gardiens probes [les anges] enregistrent vos actes et le nombre de vos respirations. L'obscurité de la nuit noire ne peut vous cacher d'eux, et vous ne pouvez pas non plus vous cacher derrière une porte verrouillée.<sup>2993</sup><br>(Voir également : 366. Les anges, section 1664)"
    }
]

# Subpart 838 - Incitation à observer et surveiller sa propre personne
s838 = find_subpart(p166, "838"); eh(s838)
s838['hadiths'] = [
    {
        "number": "2650",
        "text": "Le Messager d'Allah (s) a dit : Il était inscrit sur eux [c'est-à-dire les feuillets d'Abraham (as)] : Tant qu'elle est saine d'esprit, la personne raisonnable doit réserver plusieurs heures [dans la journée] : une heure pour s'entretenir avec son Seigneur, une heure durant laquelle elle juge et demande des comptes à sa propre personne, une heure où elle médite au sujet de ce qu'Allah le Tout-Puissant a fait pour elle, et une heure de plaisir licite. Cette heure l'aidera à bien effectuer les autres heures, et sera un moment pour récupérer et reposer son cœur.<sup>2994</sup>"
    },
    {
        "number": "2651",
        "text": "L'Imām 'Alī (as) a dit : Fais de ta personne un observateur de ta propre personne, et utilise ta vie présente pour obtenir ta part dans l'Au-delà.<sup>2995</sup>"
    },
    {
        "number": "2652",
        "text": "L'Imām 'Alī (as) a dit : L'homme doit dominer et contrôler sa personne, observer son cœur et garder sa langue.<sup>2996</sup>"
    },
    {
        "number": "2653",
        "text": "L'Imām 'Alī (as) a dit : Allah est miséricordieux envers le serviteur qui a accueilli un précepte ou a pris ses précautions, qui a été invité à la droiture et s'en est rapproché, qui a été saisi par un guide et a été sauvé, et qui traite son Seigneur avec égards par crainte de ses fautes.<sup>2997</sup>"
    },
    {
        "number": "2654",
        "text": "L'Imām 'Alī (as) a dit : La personne raisonnable doit comptabiliser les méfaits de son âme commis dans le domaine de la religion, de l'opinion, des vertus éthiques et de la bonne conduite. Elle doit rassembler cela en elle-même ou dans un livre, et travailler à les faire disparaître.<sup>2998</sup>"
    },
    {
        "number": "2655",
        "text": "L'Imām al-Ṣādiq (as) a dit : Parmi les exhortations d'Allah - le Béni et le Très-Haut - à Jésus fils de Marie (as) figure : «Ô Jésus, où que tu sois, observe ta propre personne pour Moi.»<sup>2999</sup>"
    },
    {
        "number": "2656",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui dont les jours se ressemblent [sans aucun changement dans son comportement et ses actes] est perdant ; celui dont le lendemain est pire que le jour présent est maudit ; celui qui n'observe pas ses propres manques et défauts [pour s'améliorer] verra ses manques persister ; et pour celui dont les manques et défauts persistent, la mort est préférable.<br>(Voir également : 304. La négligence, section 1434)"
    }
]

# Subpart 839 - L'observation et le jugement de sa propre personne
s839 = find_subpart(p166, "839"); eh(s839)
s839['hadiths'] = [
    {
        "number": "2657",
        "text": "L'Imām al-Kāẓim (as) a dit : Celui qui ne juge et ne demande pas de comptes à sa propre personne chaque jour ne fait pas partie des nôtres : lorsqu'il accomplit une bonne action, il doit demander à Allah de lui permettre d'en réaliser davantage, et lorsqu'il accomplit une mauvaise action, il doit demander pardon à Allah et se repentir.<sup>3001</sup>"
    }
]

# ============================================================
# Part 167 (index 168) - LE RAMADAN
# ============================================================
p167 = 168

# Subpart 840 - Le mois de Ramadan
s840 = find_subpart(p167, "840"); eh(s840)
s840['introduction'] = (
    "«<i>[Ces jours sont] le mois de Ramadan au cours duquel le Coran a été descendu comme guide "
    "pour les gens, et preuves claires de la bonne direction et du discernement. Ainsi, quiconque "
    "d'entre vous est présent en ce mois, qu'il jeûne ! Et quiconque est malade ou en voyage, "
    "alors qu'il jeûne un nombre égal d'autres jours. - Allah veut pour vous la facilité, Il ne veut "
    "pas la difficulté pour vous, afin que vous en complétiez le nombre et que vous proclamiez la "
    "grandeur d'Allah pour vous avoir guidés, et afin que vous soyez reconnaissants !</i>»<sup>3002</sup>"
)
s840['hadiths'] = [
    {
        "number": "2658",
        "text": "Le Messager d'Allah (s) a dit : En vérité, le mois de Ramadan est appelé ainsi car il brûle les péchés.<sup>3002a</sup>"
    },
    {
        "number": "2659",
        "text": "Le Messager d'Allah (s) a dit : En vérité, les portes du ciel s'ouvrent la première nuit du mois de Ramadan et elles ne se referment que la dernière nuit.<sup>3002b</sup>"
    },
    {
        "number": "2660",
        "text": "Le Messager d'Allah (s) a dit : Si le serviteur savait la valeur du [mois de] Ramadan, il souhaiterait que le Ramadan dure toute l'année.<sup>3002c</sup>"
    },
    {
        "number": "2661",
        "text": "Le Messager d'Allah (s) a dit : Lorsque la lune du [mois de] Ramadan apparaît, les portes de l'Enfer sont fermées, les portes du Paradis sont ouvertes, et les démons sont enchaînés.<sup>3002d</sup>"
    },
    {
        "number": "2662",
        "text": "L'Imām 'Alī (as) a dit : En vérité, un jour, le Messager d'Allah (s) s'est adressé à nous en disant : «Ô gens, en vérité, le mois d'Allah est venu à vous avec la bénédiction, la miséricorde et le pardon ; un mois qui est auprès d'Allah le meilleur des mois, dont les journées sont les meilleures des journées, dont les nuits sont les meilleures des nuits, et dont les heures sont les meilleures des heures. C’est un mois où vous êtes conviés à être les hôtes d'Allah et durant lequel vous avez été rendus dignes de la générosité d'Allah. [Durant ce mois,] vos respirations sont des glorifications [d'Allah], votre sommeil est une adoration, vos actes sont agréés et vos invocations exaucées…» Je me levai alors et demandai : «Ô Messager d'Allah, quel est le meilleur des actes durant ce mois ?» Il répondit : «Ô Abū al-Ḥasan ! Le meilleur des actes durant ce mois est l'abstention vis-à-vis de ce qu'Allah le Tout-Puissant a interdit.»<sup>3003</sup>"
    },
    {
        "number": "2663",
        "text": "L'Imām al-Bāqir (as) a dit : À l'approche du mois de Ramadan, alors qu'il ne restait que trois jours du mois de Sha'bān, le Messager d'Allah (s) dit à Bilāl : «Appelle les gens.» Lorsqu'ils furent rassemblés, il monta sur le minbar, loua Allah et fit Sa louange, puis dit : «Ô gens, en vérité, le mois qui vient à vous est le maître de tous les mois ; il comporte une nuit qui est meilleure que mille mois. Durant ce mois, les portes de l'Enfer sont fermées et les portes du Paradis sont ouvertes. Dès lors, celui qui atteint ce mois et n'est pas pardonné aura été tenu à l'écart par Allah.»<sup>3004</sup>"
    },
    {
        "number": "2664",
        "text": "L'Imām al-Ṣādiq (as) a dit dans l'un de ses conseils à ses enfants lors de l'avènement du mois de Ramadan : Déployez tous vos efforts [pour y faire le bien] car en vérité, durant ce mois, les subsistances sont assignées, les échéances [de vie] sont déterminées, les noms des proches serviteurs d'Allah qui souhaitent s'efforcer vers Lui sont enregistrés, et il y a dans ce mois une nuit durant laquelle les actes qui y sont réalisés sont meilleurs que les actes de mille mois.<sup>3005</sup>"
    }
]

# Subpart 841 - Le pardon d'Allah durant le mois de Ramadan
s841 = find_subpart(p167, "841"); eh(s841)
s841['hadiths'] = [
    {
        "number": "2665",
        "text": "Le Messager d'Allah (s) a dit : Celui qui atteint le mois de Ramadan et n'est pas pardonné aura été tenu à l'écart par Allah.<sup>3006</sup>"
    },
    {
        "number": "2666",
        "text": "Dans son sermon à l'occasion de l'arrivée du mois de Ramadan, le Messager d'Allah (s) a dit : En vérité, le plus malheureux est celui qui est privé du pardon d'Allah durant ce grand mois.<sup>3007</sup>"
    },
    {
        "number": "2667",
        "text": "Le Messager d'Allah (s) a dit : Si une personne n'a pas été pardonnée durant le mois de Ramadan, durant quel autre mois pourra-t-elle être pardonnée ?<sup>3008</sup>"
    },
    {
        "number": "2668",
        "text": "L'Imām al-Ṣādiq (as) a dit : Si une personne n'a pas été pardonnée durant le mois de Ramadan, elle ne sera pardonnée durant aucun autre mois après lui, sauf si elle se rend à ‘Arafāt [durant le pèlerinage obligatoire].<sup>3009</sup>"
    }
]

# ============================================================
# Part 168 (index 169) - L'ÂME
# ============================================================
p168 = 169

# Subpart 842 - La connaissance de l'âme
s842 = find_subpart(p168, "842"); eh(s842)
s842['introduction'] = (
    "«<i>Et ils t'interrogent sur l'âme. Dis : «L'âme relève de l'Ordre de mon Seigneur». "
    "Et on ne vous a donné que peu de connaissance.</i>»<sup>3010</sup>"
    "<br><br><span class=\"reference-note\">(Voir également : Coran 39:42)</span>"
)
s842['hadiths'] = [
    {
        "number": "2669",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, les âmes ne se mélangent pas aux corps ni ne dépendent d'eux. Ce sont plutôt des halos pour les corps qu'elles encerclent.<sup>3011</sup>"
    },
    {
        "number": "2670",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'âme is un corps subtil enveloppé d'un réceptacle dense [le corps].<sup>3012</sup>"
    }
]

# Subpart 843 - Les âmes sont des troupes mobilisées
s843 = find_subpart(p168, "843"); eh(s843)
s843['hadiths'] = [
    {
        "number": "2671",
        "text": "Le Messager d'Allah (s) a dit : Les âmes sont des troupes mobilisées ; elles sont mutuellement attirées par celles avec qui elles sont en harmonie, et repoussent mutuellement celles de qui elles diffèrent.<sup>3013</sup>"
    },
    {
        "number": "2672",
        "text": "L'Imām 'Alī (as) a dit : L'amour est lorsque les cœurs entretiennent une affection mutuelle du fait de l'harmonie existant entre les âmes.<sup>3014</sup>"
    }
]

# ============================================================
# Part 169 (index 170) - LE REPOS
# ============================================================
p169 = 170

# Subpart 846 - Ce qui suscite le repos
s846 = find_subpart(p169, "846"); eh(s846)
s846['hadiths'] = [
    {
        "number": "2677",
        "text": "L'Imām 'Alī (as) a dit : Celui qui est convaincu que ce qu'Allah lui a destiné lui parviendra aura le cœur apaisé.<sup>3019</sup>"
    },
    {
        "number": "2678",
        "text": "L'Imām 'Alī (as) a dit : Une épouse avec qui on est compatible est l'un des deux [principaux] repos.<sup>3020</sup>"
    },
    {
        "number": "2679",
        "text": "L'Imām 'Alī (as) a dit : Celui qui se limite à ce qui lui suffit pour vivre se garantira le repos et mènera une vie sans souci.<sup>3021</sup>"
    },
    {
        "number": "2680",
        "text": "L'Imām 'Alī (as) a dit : La sobriété et l'indifférence à la vie terrestre est ce qui procure le plus grand repos.<sup>3022</sup>"
    },
    {
        "number": "2681",
        "text": "L'Imām al-Ṣādiq (as) a dit : La sérénité et le repos résident dans la satisfaction et la certitude, alors que le souci et le chagrin résident dans le doute et le mécontentement.<sup>3023</sup>"
    },
    {
        "number": "2682",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le plus grand des repos est de ne pas fonder ses espoirs [en les faveurs] des gens.<sup>3024</sup>"
    }
]

# Subpart 847 - La recherche du repos dans ce monde
s847 = find_subpart(p169, "847"); eh(s847)
s847['hadiths'] = [
    {
        "number": "2683",
        "text": "Biḥār al-Anwār : L'Imām al-Ṣādiq (as) a dit à ses compagnons : «N'espérez pas l'impossible.» Ils demandèrent : «Mais qui donc espère l'impossible ?» Il répondit : «Vous-mêmes. N'espérez-vous pas le repos dans ce monde ?» Ils répondirent : «Oui.» Il dit alors : «Pour le croyant, le repos est impossible dans ce monde.»<sup>3025</sup>"
    }
]

# ============================================================
# Part 170 (index 171) - L'AGRICULTURE
# ============================================================
p170 = 171

# Subpart 848 - La culture et la plantation sont recommandées [par Dieu]
s848 = find_subpart(p170, "848"); eh(s848)
s848['hadiths'] = [
    {
        "number": "2684",
        "text": "Le Messager d'Allah (s) a dit : Si un oiseau, un être humain, ou un animal mange [le produit] d'une plantation ou d'une culture d'un musulman, cela sera considéré comme une aumône (ṣadaqa) de lui pour eux.<sup>3026</sup>"
    },
    {
        "number": "2685",
        "text": "L'Imām al-Bāqir (as) a dit : Mon père avait l'habitude de dire : Le meilleur des actes est le labour [de la terre], dont le produit sera consommé par le bon comme le dépravé. Le bon en mangera en demandant pardon pour toi, alors que ce que le dépravé mange le maudira. Les bestiaux et les oiseaux en mangeront aussi.<sup>3027</sup>"
    },
    {
        "number": "2686",
        "text": "L'Imām al-Bāqir (as) a dit : L'Émir des croyants (as) avait l'habitude de dire : Celui qui dispose d'eau et de terre et qui continue à être nécessiteux malgré cela est tenu à l'écart par Allah [de Sa miséricorde].<sup>3028</sup>"
    },
    {
        "number": "2687",
        "text": "L'Imām al-Ṣādiq (as) a dit : Les cultivateurs sont les trésors de l'humanité, car ils plantent les bonnes choses qu'Allah le Tout-Puissant a fait pousser. Le Jour de la Résurrection, ils occuperont le meilleur rang et la station la plus proche [d'Allah], et ils seront appelés «les bénis».<sup>3029</sup>"
    },
    {
        "number": "2688",
        "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole d'Allah le Tout-Puissant «C'est à Allah que les croyants doivent faire confiance»<sup>3030</sup> : [Ce sont] les cultivateurs.<sup>3031</sup>"
    },
    {
        "number": "2689",
        "text": "Lorsque Yazīd ibn Hārūn al-Wāsiṭī l'interrogea au sujet des cultivateurs, l'Imām al-Ṣādiq (as) répondit : Ce sont les agriculteurs, qui sont les trésors d'Allah sur Sa terre. Il n'y a pas d'activité plus aimée aux yeux d'Allah que l'agriculture, et Allah n'a jamais envoyé un prophète sans que celui-ci ne soit cultivateur, sauf Idrīs [Enoch] (as) qui était tailleur.<sup>3032</sup>"
    }
]

# ============================================================
# Part 171 (index 172) - LA ZAKĀT (L'AUMÔNE LÉGALE)
# ============================================================
p171 = 172

# Subpart 849 - Le caractère obligatoire de la zakāt
s849 = find_subpart(p171, "849"); eh(s849)
s849['introduction'] = (
    "«<i>Prélève de leurs biens une aumône par laquelle tu les purifies et les bénis, "
    "et prie pour eux. Ta prière est une quiétude pour eux. Et Allah est Audient et "
    "Omniscient.</i>»<sup>3033</sup><br><br>"
    "«<i>Et accomplissez la ṣalāt et acquittez la zakāt. Et tout ce que vous avancez de "
    "bien pour vous-mêmes, vous le retrouverez auprès d'Allah, car Allah voit parfaitement "
    "ce que vous faites.</i>»<sup>3034</sup>"
)
s849['hadiths'] = [
    {
        "number": "2690",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah - que Son rappel soit glorifié - n'a pas rendu une chose obligatoire plus difficile à cette communauté que la zakāt. La majorité sera damnée [pour ne pas l'avoir payée].<sup>3035</sup>"
    },
    {
        "number": "2691",
        "text": "L'Imām al-Ṣādiq (as) a dit : La prière de celui qui ne donne pas la zakāt est nulle, et la zakāt de celui qui n'est pas pieux est nulle.<sup>3036</sup>"
    },
    {
        "number": "2692",
        "text": "L'Imām al-Ṣādiq (as) a dit : La zakāt a été prescrite pour être un examen pour les riches et une aide pour les pauvres. Si les gens s'acquittaient de la zakāt liée à leur fortune, il ne resterait aucun musulman pauvre et nécessiteux, et ils se suffiraient à eux-mêmes grâce à ce qu'Allah le Tout-Puissant a rendu obligatoire. En vérité, les gens ne sont pauvres, dans le besoin, affamés et dévêtus qu'à cause des péchés des riches.<sup>3037</sup>"
    }
]

# Subpart 850 - Le rôle de la zakāt dans la croissance des biens
s850 = find_subpart(p171, "850"); eh(s850)
s850['hadiths'] = [
    {
        "number": "2693",
        "text": "Le Messager d'Allah (s) a dit : Si tu veux qu'Allah fasse fructifier tes biens, acquitte-toi de leur zakāt.<sup>3038</sup>"
    },
    {
        "number": "2694",
        "text": "L'Imām 'Alī (as) a dit : Immunisez vos biens en vous acquittant de la zakāt.<sup>3039</sup>"
    },
    {
        "number": "2695",
        "text": "L'Imām Ḥasan (as) a dit : Le fait de donner la zakāt ne diminue en rien la fortune.<sup>3040</sup>"
    },
    {
        "number": "2696",
        "text": "L'Imām al-Bāqir (as) a dit : Nous avons trouvé inscrit ceci dans le livre du Messager d'Allah (s) : «...Lorsque les gens refusent de s'acquitter de la zakāt, la terre refuse de donner ses bénédictions dans les cultures, les fruits et les mines.»<sup>3041</sup>"
    },
    {
        "number": "2697",
        "text": "L'Imām al-Kāẓim (as) a dit : En vérité, Allah le Tout-Puissant a institué la zakāt comme une provision pour les nécessiteux et comme un moyen de faire augmenter vos biens.<sup>3042</sup>"
    },
    {
        "number": "2698",
        "text": "L'Imām al-Riḍā (as) a dit : Lorsque la zakāt n'est pas payée, le bétail meurt.<sup>3043</sup><br>(Voir également : 382. La dépense, section 1759)"
    }
]

# Subpart 851 - Celui qui refuse de s'acquitter de la zakāt
s851 = find_subpart(p171, "851"); eh(s851)
s851['hadiths'] = [
    {
        "number": "2699",
        "text": "L'Imām al-Bāqir (as) a dit : Le Jour du Jugement, Allah transformera les biens de celui qui refusait de s'acquitter de la zakāt en un cobra de feu pourvu de deux glandes venimeuses qui s'enroulera autour de lui, et il lui sera dit : «Accroche-toi à lui comme il s'est accroché à toi dans la vie terrestre.» C'est ce que signifie la parole d'Allah : «Le Jour de la Résurrection, on leur attachera autour du cou ce qu'ils ont gardé avec avarice».<sup>3044, 3045</sup>"
    }
]


# ============================================================
# Sequential Sorting for all modified subparts
# ============================================================
modified_sections = [
    (p163, "827"), (p163, "828"), (p163, "829"), (p163, "830"),
    (p164, "831"),
    (p165, "834"), (p165, "835"), (p165, "836"),
    (p166, "837"), (p166, "838"), (p166, "839"),
    (p167, "840"), (p167, "841"),
    (p168, "842"), (p168, "843"),
    (p169, "846"), (p169, "847"),
    (p170, "848"),
    (p171, "849"), (p171, "850"), (p171, "851")
]

for p_idx, s_title in modified_sections:
    s = find_subpart(p_idx, s_title)
    if s and 'hadiths' in s:
        s['hadiths'].sort(key=lambda h: int(h['number']))
        print(f"Sorted Subpart {s_title} (Part index {p_idx}). Hadiths: {[h['number'] for h in s['hadiths']]}")

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Data successfully saved! Hadiths 2611-2628, 2634-2689, 2690-2699 injected.")
