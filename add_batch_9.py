import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 46 - L'AGRESSION (Index 47)
    part46 = data[47]
    part46['subparts'][0]['introduction'] = "«<i>Lorsqu'Il les a sauvés, les voilà qui, sur terre, agressent injustement. Ô gens ! Votre agression ne retombera que sur vous-mêmes. C'est une jouissance temporaire de la vie présente. Ensuite, c'est vers Nous que sera votre retour, et Nous vous rappellerons alors ce que vous faisiez.</i>»<sup>913</sup><br><br>«<i>Certes, Allah commande l'équité, la bienfaisance et l'assistance aux proches. Et Il interdit la turpitude, l'acte répréhensible et l'agression. Il vous exhorte ainsi afin que vous vous souveniez.</i>»<sup>914</sup>"
    
    part46['subparts'][2]['introduction'] = "«<i>Et si deux groupes de croyants se combattent, établissez la conciliation entre eux. Si l'un d'eux agresse l'autre, combattez le groupe qui se rebelle, jusqu'à ce qu'il se conforme à l'ordre d'Allah. Puis, s'il s'y conforme, réconciliez-les avec justice et soyez équitables, car Allah aime les justes.</i>»<sup>924</sup>"

    # Part 47 - LES PLEURS (Index 48)
    part47 = data[48]
    while len(part47['subparts']) <= 1:
        part47['subparts'].append({"title": "...", "hadiths": []})
        
    part47['subparts'][0]['title'] = "Pleurer par crainte d'Allah"
    part47['subparts'][0]['introduction'] = "«<i>Lorsque les versets du Tout Miséricordieux leur étaient récités, ils tombaient prosternés en pleurant.</i>»<sup>929</sup><br><br>«<i>Et ils tombent sur leur menton, pleurant, et cela augmente leur humilité.</i>»<sup>930</sup>"
    
    part47['subparts'][1]['title'] = "La sécheresse de l'œil"

    updates = [
        # Part 45 - L'AVERSION (Index 46)
        (46, 3, {"number": "822", "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses apportent la malveillance : l'hypocrisie, l'oppression et l'admiration de soi.<sup>912</sup><br><br><span class=\"reference-note\">(Voir également : 267. L'animosité)</span>"}),

        # Part 46 - L'AGRESSION (Index 47)
        (47, 0, {"number": "823", "text": "Le Messager d'Allah (s) a dit : En vérité, le mal qui est le plus vite puni est l'agression.<sup>915</sup>"}),
        (47, 0, {"number": "824", "text": "L'Imām 'Alī (as) a dit : Celui qui dégaine le sabre de l'agression sera tué par celui-ci.<sup>916</sup>"}),
        (47, 0, {"number": "825", "text": "L'Imām 'Alī (as) a dit : L'agression détruit les grâces [divines].<sup>917</sup>"}),
        (47, 0, {"number": "826", "text": "L'Imām 'Alī (as) a dit : L'agression provoque la destruction.<sup>918</sup>"}),
        (47, 0, {"number": "827", "text": "L'Imām 'Alī (as) a dit : Gare à l'agression, car elle hâte l'anéantissement et son auteur devient un moyen d'édifier les autres.<sup>919</sup>"}),
        (47, 0, {"number": "828", "text": "L'Imām 'Alī (as) a dit : En vérité, l'agression mène ses auteurs au Feu.<sup>920</sup>"}),
        (47, 0, {"number": "829", "text": "L'Imām al-Ṣādiq (as) a dit : Fais attention à ne jamais prononcer une parole agressive, même si tu admires [la force] de ta propre personne et des tiens.<sup>921</sup>"}),
        
        (47, 1, {"number": "830", "text": "L'Imām al-Ṣādiq (as) a dit en commentant la parole Divine «<i>Celui qui est contraint sans toutefois être agresseur ni transgresseur</i>»<sup>922</sup> : L'agresseur est celui qui se dresse contre l'Imām.<sup>923</sup>"}),
        
        (47, 2, {"number": "831", "text": "Ḥafṣ ibn Ghiyāth a dit : J'ai interrogé l'Imām al-Ṣādiq (as) au sujet de deux groupes de croyants, l'un d'eux étant agresseur et l'autre juste ; le groupe des justes ayant vaincu les agresseurs. Il répondit : «Le groupe des justes n'a pas de droit de poursuivre un fuyard, de tuer un prisonnier ou d'achever un blessé - cela est valable lorsqu'il ne reste plus aucun agresseur ni aucune de leur formation vers laquelle ils puissent se réfugier.»<sup>925</sup>"}),
        (47, 2, {"number": "832", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, [l'Imām] 'Alī (as) a écrit à Mālik alors qui était en première ligne du front le jour de [la bataille de] Baṣra, de ne pas attaquer ceux qui n'avancent pas, ni de tuer celui qui bat en retraite, ni d'achever un blessé ; quant à celui qui ferme la porte de chez lui [qui ne s'engage pas au combat], il est en sécurité.<sup>926</sup>"}),
        (47, 2, {"number": "833", "text": "'Abdullāh ibn Sharīk rapporte de son père : Lorsque l'ennemi fut vaincu le jour de la bataille du chameau, l'Emir des croyants (as) dit : «Ne poursuivez pas le fuyard, n'achevez pas le blessé, et celui qui ferme sa porte doit être en sécurité.» Or, le jour de la bataille de Ṣiffīn, il tua les combattants et les fuyards, et acheva les blessés. Abān ibn Taghlib dit à 'Abdullāh ibn Sharīk : «Ces deux agissements sont différents.» 'Abdullāh ibn Sharīk dit alors : «En vérité, les auteurs [de la bataille] du chameau ont assassiné Ṭalḥa et Zubair, mais dans cette [seconde] bataille, Mu'āwiya était encore présent parmi eux et les dirigeait.»<sup>927</sup><br><br><span class=\"reference-note\">(Voir également : 126. L'humilité)</span>"}),
        
        (47, 3, {"number": "834", "text": "L'Imām al-Ṣādiq (as) a dit : Le combat de 'Alī (as) face aux gens de la Qibla recelait une bénédiction ; s'il ne les avait pas combattus, personne après lui n'aurait su comment se comporter envers eux.<sup>928</sup>"}),

        # Part 47 - LES PLEURS (Index 48)
        (48, 0, {"number": "835", "text": "Le Messager d'Allah (s) a dit : Bienheureux est le visage qu'Allah regarde alors qu'il pleure pour un péché par crainte d'Allah le Tout-Puissant, alors que ce péché n'est connu que par Lui.<sup>931</sup>"}),
        (48, 0, {"number": "836", "text": "Lors de son sermon d'adieu, le Messager d'Allah (s) a dit : Celui dont les yeux ont versé des larmes par crainte d'Allah aura pour chaque larme l'équivalent d'une rétribution [de la taille de] la montagne d'Uḥud dans la balance de ses actes.<sup>932</sup>"}),
        (48, 0, {"number": "837", "text": "Le Messager d'Allah (s) a dit : Sept personnes seront sous l'ombre du Trône d'Allah le Tout-Puissant le Jour où il n'y aura aucune ombre hormis la Sienne : [....] et un homme qui s'est rappelé d'Allah le Tout-Puissant dans sa solitude et dont les yeux ont été inondés de larmes par crainte d'Allah.<sup>933</sup>"}),
        (48, 0, {"number": "838", "text": "Le Messager d'Allah (s) a dit : Celui dont les yeux ont, par crainte d'Allah, versés une larme ne serait-ce que de la traille d'une mouche, Allah lui accordera la sécurité le jour de la grande frayeur.<sup>934</sup>"}),
        (48, 0, {"number": "839", "text": "L'Imām 'Alī (as) a dit : Les larmes des yeux et la crainte des cœurs font partie de la miséricorde d'Allah - que Son rappel soit exalté. Ainsi, quand vous les trouvez en vous, profitez-en pour faire des invocations.<sup>935</sup>"}),
        (48, 0, {"number": "840", "text": "L'Imām 'Alī (as) a dit : Pleurer par crainte d'Allah est la clé de [Sa] miséricorde.<sup>936</sup>"}),
        (48, 0, {"number": "841", "text": "L'Imām 'Alī (as) a dit : Pleurer par crainte d'Allah illumine le cœur et immunise de l'accoutumance au péché.<sup>937</sup>"}),
        (48, 0, {"number": "842", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Deux gouttes sont les plus aimées par Allah le Tout-Puissant : la goutte de sang [versée] dans le sentier d'Allah, et la larme versée durant l'obscurité de la nuit par un serviteur uniquement pour Allah le Tout-Puissant.<sup>938</sup>"}),
        (48, 0, {"number": "843", "text": "L'Imām al-Bāqir (as) a dit : Le Jour de la Résurrection, tout œil pleurera hormis trois : un œil qui a veillé [la nuit en adoration] pour Allah, un œil qui s'est rempli [de larmes] par crainte d'Allah, et un œil qui s'est détourné des interdits d'Allah.<sup>939</sup>"}),
        (48, 0, {"number": "844", "text": "L'Imām al-Ṣādiq (as) a dit : Si tu n'arrives pas à pleurer, force-toi à pleurer, car même s'il sort de ton œil l'équivalent d'une tête de mouche, alors quelle heureuse fortune !<sup>940</sup>"}),
        (48, 0, {"number": "845", "text": "L'Imām al-Ṣādiq (as) a dit : Toute chose a un poids et une mesure sauf les larmes, car une larme peut éteindre des océans de Feu. Si les yeux sont noyés de larmes, le visage de son auteur ne sera jamais marqué par la pauvreté ou l'humiliation, et lorsque les yeux débordent de larmes, Allah lui interdira le Feu. Si une personne pleurait pour une nation, elle serait l'objet de miséricorde.<sup>941</sup>"}),
        
        (48, 1, {"number": "846", "text": "Le Messager d'Allah (s) a dit : Parmi les signes du malheur est la sécheresse de l'œil.<sup>942</sup>"}),
        (48, 1, {"number": "847", "text": "L'Imām 'Alī (as) a dit : La sécheresse de l'œil est le résultat de la dureté des cœurs, et les cœurs ne durcissent que par l'abondance des péchés.<sup>943</sup>"})
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
