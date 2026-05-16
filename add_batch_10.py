import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 48 - LA CONTRÉE (Index 49)
    while len(data) <= 49:
        data.append({"title": "48 - LA CONTRÉE", "subparts": []})
    part48 = data[49]
    while len(part48['subparts']) <= 3:
        part48['subparts'].append({"title": "...", "hadiths": []})
        
    part48['subparts'][0]['title'] = "La bonne contrée"
    part48['subparts'][0]['introduction'] = "«<i>Une bonne contrée et un Seigneur Pardonneur.</i>»<sup>944</sup><br><br>«<i>Et Nous avions placé entre eux et les cités que Nous avions bénies, d'autres cités proéminentes, et Nous avions évalué les étapes de voyage entre elle. «Voyagez entre elles, de nuit et de jour, en toute sécurité».</i>»<sup>945</sup><br><br><span class=\"reference-note\">(Voir également : Coran 21:71, 21:81, 23:50, 28:29-30, 79:16, 90:1-2, 95:1-3)</span>"
    part48['subparts'][1]['title'] = "Choisissez les grandes villes"
    part48['subparts'][2]['title'] = "La meilleure des contrées"
    part48['subparts'][3]['title'] = "Ce dont ne peuvent se passer les habitants de toute contrée"

    # Part 49 - L'ÉLOQUENCE (Index 50)
    while len(data) <= 50:
        data.append({"title": "49 - L'ÉLOQUENCE", "subparts": []})
    part49 = data[50]
    while len(part49['subparts']) <= 2:
        part49['subparts'].append({"title": "...", "hadiths": []})

    part49['subparts'][0]['title'] = "La signification de l'éloquence"
    part49['subparts'][1]['title'] = "La plus éloquente des paroles"
    part49['subparts'][2]['title'] = "La manipulation par la parole"

    # Part 50 - LA DIFFUSION [DE L'ISLAM] (Index 51)
    while len(data) <= 51:
        data.append({"title": "50 - LA DIFFUSION [DE L'ISLAM]", "subparts": []})
    part50 = data[51]
    while len(part50['subparts']) <= 1:
        part50['subparts'].append({"title": "...", "hadiths": []})

    part50['subparts'][0]['title'] = "L'importance de la diffusion [de l'islam]"
    part50['subparts'][0]['introduction'] = "«<i>Les croyants n'ont pas à quitter tous leurs foyers. Pourquoi de chaque clan quelques hommes ne viendraient-ils pas s'instruire dans la religion pour pouvoir à leur retour avertir leur peuple afin qu'ils soient sur leur garde ?</i>»<sup>957</sup>"
    
    part50['subparts'][1]['title'] = "Ce qui incombe au diffuseur [de l'islam]"

    updates = [
        # Part 48 - LA CONTRÉE (Index 49)
        (49, 1, {"number": "848", "text": "L'Imām 'Alī (as) a écrit à al-Ḥārith al-Hamadānī : Habite les grandes villes, car c'est le lieu de rassemblement des musulmans ; évite les lieux d'ignorance et de dureté.<sup>946</sup>"}),
        (49, 2, {"number": "849", "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de contrée qui te réclame plus qu'une autre ; la meilleure des contrées est celle qui te soutient [dans laquelle tu as trouvé sérénité et repos].<sup>947</sup>"}),
        (49, 3, {"number": "850", "text": "L'Imām al-Ṣādiq (as) a dit : Les habitants de toute contrée ne peuvent se passer de trois [types de personnes] vers lesquelles elles peuvent se réfugier pour tout ce qui touche à leur vie d'ici-bas ou à leur vie dans l'Au-delà - et s'ils en sont dépourvus, ils deviennent ignorants et barbares : un savant instruit et pieux, un souverain droit et obéi, et un médecin expérimenté et digne de confiance.<sup>948</sup>"}),

        # Part 49 - L'ÉLOQUENCE (Index 50)
        (50, 0, {"number": "851", "text": "L'Imām 'Alī (as) a dit : L'éloquence est ce qui est exprimé de façon facile [par l'orateur] et est léger [et facile] à comprendre [pour l'auditeur].<sup>949</sup>"}),
        (50, 0, {"number": "852", "text": "L'Imām 'Alī (as) a dit : L'éloquence est de répondre sans attendre et d'atteindre son but [faire comprendre son message] sans se tromper.<sup>950</sup>"}),
        (50, 0, {"number": "853", "text": "L'Imām 'Alī (as) a dit : La concision suffit parfois [pour atteindre] l'éloquence.<sup>951</sup>"}),
        (50, 0, {"number": "854", "text": "L'Imām al-Ṣādiq (as) a dit : L'éloquence ne réside pas dans la finesse de la langue ni dans d'abondants radotages, mais dans le fait de saisir le sens [que l'on veut transmettre] et de viser à en apporter la preuve.<sup>952</sup>"}),
        (50, 0, {"number": "855", "text": "L'Imām al-Ṣādiq (as) a dit : L'éloquence réside dans trois choses : se rapprocher du sens visé, s'éloigner du discours prolixe, et dire beaucoup avec peu de mots.<sup>953</sup>"}),
        (50, 1, {"number": "856", "text": "L'Imām 'Alī (as) a dit : L'éloquence la plus expressive réside dans ce qui véhicule simplement le message, et ce qui est agréablement concis.<sup>954</sup>"}),
        (50, 1, {"number": "857", "text": "L'Imām 'Alī (as) a dit : La meilleure des paroles est celle qui est embellie par une structure plaisante, et est comprise à la fois par l'élite et le profane.<sup>955</sup>"}),
        (50, 2, {"number": "858", "text": "Le Messager d'Allah (s) a dit : Les mauvais de ma communauté sont les bavards, les beaux parleurs, et les hautains ; les meilleurs de ma communauté sont ceux qui ont la meilleure morale.<sup>956</sup>"}),

        # Part 50 - LA DIFFUSION [DE L'ISLAM] (Index 51)
        (51, 0, {"number": "859", "text": "Le Messager d'Allah (s) a dit : Je réitère ici cette parole : établissez la prière, acquittez-vous de l'aumône, ordonnez le convenable, interdisez le blâmable. En vérité, le sommet de l'ordonnance du convenable et de l'interdiction du blâmable est de vous fier à ma parole, de la diffuser aux absents, d'ordonner son acceptation et d'interdire sa transgression, car c'est un ordre provenant d'Allah le Tout-Puissant et de moi-même.<sup>958</sup>"}),
        (51, 0, {"number": "860", "text": "Le Messager d'Allah (s) a dit en s'adressant à 'Alī (as) : Ô 'Alī, lorsqu'Allah guide un homme par tes mains [par toi], cela vaut mieux pour toi que [de posséder] tout ce que le soleil éclaire.<sup>959</sup>"}),
        (51, 0, {"number": "861", "text": "Le Messager d'Allah (s) a dit : Faites aimer Allah à Ses serviteurs, et Allah vous aimera.<sup>960</sup>"}),
        (51, 0, {"number": "862", "text": "Le Messager d'Allah (s) a dit : Celui qui convertit une personne à l'islam entre obligatoirement au Paradis.<sup>961</sup>"}),
        (51, 0, {"number": "863", "text": "Le Messager d'Allah (s) a dit : Toute personne qui appelle à la bonne voie aura la même rétribution que celle qui l'a suivie sans que cela ne diminue leur propre rétribution.<sup>962</sup>"}),
        (51, 0, {"number": "864", "text": "Le Messager d'Allah (s) a dit : Les élus de ma communauté sont ceux qui invitent à Allah le Très-Haut et qui Le font aimer de Ses serviteurs.<sup>963</sup>"}),
        (51, 0, {"number": "865", "text": "Sharīf ibn Sābiq al-Taflīsī rapporte de Ḥammād al-Samdarī : J'ai dit à l'Imām al-Ṣādiq (as) : «Je me rends souvent dans des pays d'associationnisme ; à ce propos, certains m'ont dit : «Si tu meurs en ces lieux, tu seras ressuscité en leur compagnie.» [En est-il ainsi ?»] Il (as) me dit : «Ô Ḥammād ! Quand tu es là-bas, évoques-tu notre cause [l'Imāmat] et appelles-tu [les gens] à cela ?» Je lui dis : «Oui.» Il (as) me dit : «Quand tu es dans ces contrées [en terre d'islam], parles-tu de notre cause et appelles-tu les gens à elle ?» Je dis : «Non.» Il me dit : «Alors si tu venais à mourir dans ces lieux [les contrées associationnistes], tu seras ressuscité en tant que communauté à toi tout seul, et ta lumière courra devant toi.»<sup>964</sup><br><br><span class=\"reference-note\">(Voir également : 273. La bienséance (2), section 1286)</span>"}),
        
        (51, 1, {"number": "866", "text": "<b>1 - La connaissance de la religion</b><br><br>Le Messager d'Allah (s) a dit : En vérité, la religion d'Allah le Tout-Puissant ne sera secourue que par le biais d'une personne qui en maîtrise l'ensemble des aspects.<sup>965</sup>"}),
        (51, 1, {"number": "867", "text": "<b>2 - Se référer aux paroles des Gens de la demeure prophétique (as)</b><br><br>'Abd al-Salām ibn Ṣāliḥ al-Harawī a dit : J'ai entendu Abū al-Ḥasan al-Riḍā (as) dire : «Que la miséricorde d'Allah soit sur un serviteur qui a ravivé notre cause.» Je demandai : «Comment ravive-t-il votre cause ?» Il répondit : «En apprenant nos sciences et en l'enseignant aux gens, car si les gens venaient à connaître les vertus de nos paroles, ils nous suivraient.»<sup>966</sup>"}),
        (51, 1, {"number": "868", "text": "<b>3 - La sincérité</b><br><br>«<i>Je ne vous demande aucune rétribution pour cela, ma rétribution n'incombe qu'au Seigneur de l'univers.</i>»<sup>967</sup><br><br>Le Messager d'Allah (s) a dit : Nul serviteur ne prononce un discours sans qu'Allah le Tout-Puissant ne l'interroge sur son intention.<sup>968</sup>"}),
        (51, 1, {"number": "869", "text": "<b>4 - Le courage</b><br><br>«<i>Ceux qui diffusaient les messages d'Allah, Le craignaient et ne redoutaient nul autre qu'Allah. Et Allah suffit pour tenir le compte de tout.</i>»<sup>969</sup><br><br>Le Messager d'Allah (s) a dit : Dis la vérité sans redouter, dans la voie d'Allah, le blâme des réprobateurs.<sup>970</sup>"})
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
