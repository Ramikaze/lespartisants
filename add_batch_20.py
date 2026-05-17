import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 63 - L'EXPÉRIENCE (Index 64)
    part63 = data[64]
    while len(part63['subparts']) <= 1:
        part63['subparts'].append({"title": "...", "hadiths": []})
        
    part63['subparts'][1]['title'] = "Les dommages issus du manque d'expérience"

    # Part 64 - L'ANXIÉTÉ (Index 65)
    while len(data) <= 65:
        data.append({"title": "64 - L'ANXIÉTÉ", "subparts": []})
    part64 = data[65]
    while len(part64['subparts']) <= 0:
        part64['subparts'].append({"title": "...", "hadiths": []})
        
    part64['subparts'][0]['title'] = "Mise en garde contre l'anxiété"
    part64['subparts'][0]['introduction'] = "«<i>Oui, l'homme a été créé instable ; quand un malheur le touche, il est anxieux ; et quand le bonheur le touche, il est grand refuseur.</i>»<sup>1200</sup>"

    # Part 65 - LA RÉTRIBUTION (Index 66)
    while len(data) <= 66:
        data.append({"title": "65 - LA RÉTRIBUTION", "subparts": []})
    part65 = data[66]
    while len(part65['subparts']) <= 2:
        part65['subparts'].append({"title": "...", "hadiths": []})
        
    part65['subparts'][0]['title'] = "La rétribution [des actes]"
    part65['subparts'][0]['introduction'] = "«<i>À Allah appartient ce qui est dans les cieux et sur la terre, de sorte qu'Il rétribue ceux qui font le mal selon ce qu'ils œuvrent, et récompense ceux qui font le bien par la meilleure [récompense].</i>»<sup>1207</sup>"
    
    part65['subparts'][1]['title'] = "La rétribution des bienfaisants"
    part65['subparts'][1]['introduction'] = "«<i>Et quand il eut atteint sa maturité, Nous lui accordâmes sagesse et savoir. C'est ainsi que Nous récompensons les bienfaisants.</i>»<sup>1209</sup><br><br>«<i>Voilà que Nous l'appelâmes : «Ô Abraham ! Tu as confirmé ta vision. C'est ainsi que Nous récompensons les bienfaisants.»</i>»<sup>1210</sup>"
    
    part65['subparts'][2]['title'] = "La rétribution des malfaiteurs"
    part65['subparts'][2]['introduction'] = "«<i>Et quiconque se détourne de Mon rappel mènera certes une vie pleine de gêne, et le Jour de la Résurrection, Nous l'amènerons aveugle au rassemblement. [...] C'est ainsi que Nous rétribuons l'outrancier qui n'a pas cru aux signes de son Seigneur. Et certes, le châtiment de l'Au-delà est plus sévère et plus durable.</i>»<sup>1211</sup><br><br>«<i>Ceux qui prenaient le veau [comme divinité], bientôt tombera sur eux une colère de la part de leur Seigneur, et un avilissement dans la vie de ce monde. C'est ainsi que Nous rétribuons les inventeurs [d'idoles].</i>»<sup>1212</sup><br><br>«<i>L'Enfer leur servira de lit et, comme couverture, ils auront des voiles de ténèbres. C'est ainsi que Nous rétribuons les injustes.</i>»<sup>1213</sup>"

    # Part 66 - L'ESPIONNAGE (Index 67)
    while len(data) <= 67:
        data.append({"title": "66 - L'ESPIONNAGE", "subparts": []})
    part66 = data[67]
    while len(part66['subparts']) <= 3:
        part66['subparts'].append({"title": "...", "hadiths": []})
        
    part66['subparts'][0]['title'] = "L'interdiction de rechercher les défauts des gens"
    part66['subparts'][0]['introduction'] = "«<i>Ô vous qui avez cru ! Evitez de trop conjecturer [sur autrui] car une partie des conjectures est péché. Et n'espionnez pas ; et ne médisez pas les uns des autres. L'un de vous aimerait-il manger la chair de son frère mort ? [Non !] Vous en auriez horreur. Et craignez Allah. Car Allah est le Grand Accueillant au repentir, Très Miséricordieux.</i>»<sup>1214</sup>"
    
    part66['subparts'][1]['title'] = "Les conséquences de l'espionnage des gens"
    part66['subparts'][2]['title'] = "La licéité de l'espionnage pendant les guerres"
    part66['subparts'][3]['title'] = "Les cas où il faut juger selon ce qui est apparent"

    # Part 67 - L'ASSEMBLÉE (Index 68)
    while len(data) <= 68:
        data.append({"title": "67 - L'ASSEMBLÉE", "subparts": []})
    part67 = data[68]
    while len(part67['subparts']) <= 1:
        part67['subparts'].append({"title": "...", "hadiths": []})
        
    part67['subparts'][0]['title'] = "La plus honorable des assemblées"
    part67['subparts'][1]['title'] = "Ce qu'il faut respecter lors des assemblées"
    part67['subparts'][1]['introduction'] = "«<i>Ô vous qui avez cru ! Lorsqu'on vous dit : «Faites place [aux autres] dans les assemblées !», alors faites place. Allah vous ménagera une place [au Paradis]. Et lorsqu'on vous dit de vous lever, levez-vous.</i>»<sup>1229</sup>"

    updates = [
        # Part 63 - L'EXPÉRIENCE (Index 64)
        (64, 0, {"number": "1052", "text": "L'Imām 'Alī (as) a dit : Les expériences suffisent comme éducateurs.<sup>1193</sup>"}),
        (64, 0, {"number": "1053", "text": "L'Imām 'Alī (as) a dit : [La valeur de] l'opinion de l'homme est proportionnelle à son expérience.<sup>1194</sup>"}),
        (64, 0, {"number": "1054", "text": "L'Imām 'Alī (as) a dit : La raison est un instinct qui s'accroît par la connaissance et l'expérience.<sup>1195</sup>"}),
        (64, 0, {"number": "1055", "text": "L'Imām 'Alī (as) a dit : La raison conserve l'expérience.<sup>1196</sup>"}),
        
        (64, 1, {"number": "1056", "text": "L'Imām 'Alī (as) a dit : Celui qui n'a pas expérimenté les choses sera dupé.<sup>1197</sup>"}),
        (64, 1, {"number": "1057", "text": "L'Imām 'Alī (as) a dit : Celui qui maîtrise ses expériences sera épargné par les préjudices, alors que celui qui se dispense d'expériences restera aveugle face aux conséquences [des actes].<sup>1198</sup>"}),
        (64, 1, {"number": "1058", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est peu expérimenté et imbu de son propre avis ne doit pas aspirer à la direction.<sup>1199</sup>"}),

        # Part 64 - L'ANXIÉTÉ (Index 65)
        (65, 0, {"number": "1059", "text": "Le Messager d'Allah (s) a dit : Deux sons sont abhorrés par Allah : les gémissements et les lamentations lors du malheur, et les chants et la musique lors du bonheur.<sup>1201</sup>"}),
        (65, 0, {"number": "1060", "text": "L'Imām 'Alī (as) a dit : Gare à l'anxiété car elle brise l'espoir, affaiblit l'acte et génère la contrariété. Sache que la solution se trouve dans deux choses : trouver une solution [au problème] s'il en a une, et prendre patience lorsqu'il n'y pas de solution.<sup>1202</sup>"}),
        (65, 0, {"number": "1061", "text": "L'Imām 'Alī (as) a dit : Vainquez l'anxiété par la patience, car l'anxiété détruit la rétribution [d'Allah] et amplifie le malheur.<sup>1203</sup>"}),
        (65, 0, {"number": "1062", "text": "L'Imām 'Alī (as) a dit lorsqu'il entendit les pleurs des femmes sur les défunts de la bataille de Ṣiffīn : Vos femmes vous ont vaincus, d'après ce que j'entends ?! Ne pourriez-vous pas leur interdire de gémir ainsi ?!<sup>1204</sup>"}),
        (65, 0, {"number": "1063", "text": "L'Imām al-Bāqir (as) a dit : Le pire aspect de l'anxiété est de s'adonner aux lamentations et aux gémissements, ainsi que de se frapper le visage et la poitrine et de s'arracher les cheveux. Celui qui se laisse aller aux lamentations a délaissé la patience.<sup>1205</sup>"}),
        (65, 0, {"number": "1064", "text": "L'Imām al-Kāẓim (as) a dit : Le malheur de la personne patiente est unique, alors que celui de la personne anxieuse est double.<sup>1206</sup>"}),

        # Part 65 - LA RÉTRIBUTION (Index 66)
        (66, 0, {"number": "1065", "text": "L'Imām 'Alī (as) a dit : Tout être humain verra ses actes et sera rétribué pour ce qu'il a réalisé.<sup>1208</sup><br><br><span class=\"reference-note\">(Voir également : 57. La récompense)</span>"}),

        # Part 66 - L'ESPIONNAGE (Index 67)
        (67, 0, {"number": "1066", "text": "Le Messager d'Allah (s) a dit : Gare aux conjectures ! En vérité, la conjecture est la plus mensongère des paroles. Ne vous sondez pas les uns les autres [pour obtenir des informations] et ne vous espionnez pas.<sup>1215</sup>"}),
        (67, 0, {"number": "1067", "text": "Le Messager d'Allah (s) a dit : Je n'ai pas reçu l'ordre d'inspecter le cœur des gens, ni de percer leur for intérieur.<sup>1216</sup>"}),
        (67, 0, {"number": "1068", "text": "<i>Kanz al-'Ummāl</i> : 'Umar ibn al-Khaṭṭāb avait pour habitude à Médine de faire des rondes pendant la nuit. [Une nuit], il entendit la voix d'un homme chantant dans une maison. Il sauta par-dessus le mur et lui dit : «Ô ennemi d'Allah ! Crois-tu qu'Allah te protègeras alors que tu Lui désobéis ?» Et l'homme lui répliqua : «Et toi, ô émir des croyants ? Ne te précipite pas [pour me punir], car si j'ai désobéi à Allah une fois, tu Lui as quant à toi désobéi dans trois choses. Allah a dit : «<i>N'espionnez pas</i>»<sup>1217</sup> et tu m'as espionné. Il a dit : «<i>Entrez donc dans les maisons par leurs portes</i>»<sup>1218</sup>, alors que tu es entré chez moi en sautant par-dessus le mur, et sans demander ma permission bien qu'Allah ait dit : «<i>N'entrez pas dans des maisons autres que les vôtres avant de demander la permission [d'une façon délicate] et de saluer leurs habitants.</i>»<sup>1219</sup>» 'Umar dit alors : «Y a-t-il quelque bien en toi, si je décide de te pardonner ?» Il répondit : «Oui.» Ainsi, il lui pardonna, sortit et le laissa [en paix].<sup>1220</sup>"}),
        
        (67, 1, {"number": "1069", "text": "Le Messager d'Allah (s) a dit : Ne guettez pas les faux pas des croyants car Allah guettera les faux pas de celui qui guette ceux de son frère, et celui dont Allah guette les faux pas sera déshonoré, même s'il est dans l'intimité de sa propre maison.<sup>1221</sup>"}),
        (67, 1, {"number": "1070", "text": "Le Messager d'Allah (s) a dit : Ne demandez pas à la dépravée avec qui elle a commis ses actes de dépravation, car elle accusera un musulman innocent aussi facilement qu'elle s'est dépravée.<sup>1222</sup>"}),
        (67, 1, {"number": "1071", "text": "L'Imām al-Ṣādiq (as) a dit : N'espionne pas les gens dans leur religion car tu finiras sans amis.<sup>1223</sup>"}),
        (67, 1, {"number": "1072", "text": "<i>Sunan Abī Dāwūd</i> : L'un des Compagnons a dit : J'ai entendu le Messager d'Allah (s) dire: «En vérité, si tu épies les faiblesses des gens, tu les corrompras ou manqueras de peu de les corrompre.»<sup>1224</sup><br><br><span class=\"reference-note\">(Voir également : 295. Les défauts, section 1406)</span>"}),
        
        (67, 2, {"number": "1073", "text": "L'Imām al-Riḍā (as) a dit : Lorsque le Messager d'Allah (s) envoyait une armée avec un commandant en qui il n'avait pas totalement confiance, il envoyait avec lui une personne en qui il avait confiance afin de l'espionner et d'informer [de sa conduite].<sup>1225</sup>"}),
        
        (67, 3, {"number": "1074", "text": "L'Imām al-Ṣādiq (as) a dit : Cinq choses devraient être jugées par les gens selon ce qui est apparent : les allégeances, les mariages, les héritages, les abattages d'animaux et les témoignages. Ainsi, si la personne apparaît digne de confiance, son témoignage doit être accepté sans s'enquérir de son être profond.<sup>1226</sup>"}),

        # Part 67 - L'ASSEMBLÉE (Index 68)
        (68, 0, {"number": "1075", "text": "Le Messager d'Allah (s) a dit : En vérité, toute chose a un honneur et la plus honorable des assemblées est celle qui se tient face à la Qibla.<sup>1227</sup>"}),
        (68, 0, {"number": "1076", "text": "L'Imām al-Ṣādiq (as) a dit : La plupart du temps, le Messager d'Allah (s) s'asseyait face à la Qibla.<sup>1228</sup>"}),
        
        (68, 1, {"number": "1077", "text": "Le Messager d'Allah (s) a dit : Ne sois pas obscène dans les assemblées afin de ne pas être évité pour ton mauvais caractère, et lorsqu'une"})
    ]

    for p_idx, s_idx, hadith in updates:
        content_list = data[p_idx]['subparts'][s_idx].setdefault('hadiths', [])
        exists = any(h.get('number') == hadith['number'] for h in content_list)
        if not exists:
            content_list.append(hadith)
            print(f"Added {hadith['number']} to Part {p_idx}, Subpart {s_idx}")
        else:
            print(f"Hadith {hadith['number']} already exists.")

    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
