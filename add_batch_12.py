import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 51 - L'ÉPREUVE (Index 52)
    part51 = data[52]
    while len(part51['subparts']) <= 14:
        part51['subparts'].append({"title": "...", "hadiths": []})
        
    part51['subparts'][6]['title'] = "L'épreuve et le rappel"
    part51['subparts'][6]['introduction'] = "«<i>Nous avons éprouvé les gens de Pharaon par des années de disette et par une diminution de fruits afin qu'ils se rappellent.</i>»<sup>1005</sup>"
    
    part51['subparts'][7]['title'] = "Les péchés sont épurés par les épreuves"
    part51['subparts'][8]['title'] = "L'épreuve est un signe de l'amour d'Allah - loué soit-Il"
    part51['subparts'][9]['title'] = "L'épreuve est proportionnelle au degré de la foi"
    part51['subparts'][10]['title'] = "Les degrés auxquels accède le serviteur par les épreuves"
    part51['subparts'][11]['title'] = "L'épreuve du croyant est un bien pour lui"
    part51['subparts'][12]['title'] = "L'épreuve la plus difficile des serviteurs"
    part51['subparts'][13]['title'] = "La délivrance au sommet de l'épreuve"
    part51['subparts'][14]['title'] = "Le rappel d'Allah lors des épreuves"
    part51['subparts'][14]['introduction'] = "«<i>Qui disent, lorsqu'un malheur les touche : «Certes nous sommes à Allah, et c'est à Lui que nous retournerons».</i>»<sup>1028</sup>"

    updates = [
        # Part 51 - L'ÉPREUVE (Index 52)
        (52, 5, {"number": "893", "text": "L'Imām al-Bāqir (as) a dit : En vérité, quand Allah veut du bien à des gens, Il les éprouve.<sup>1001</sup>"}),
        (52, 5, {"number": "894", "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Tout-Puissant a promis l'épreuve au croyant de la même façon que le père de famille promet des cadeaux à sa famille après l'absence [de retour d'un voyage] ; et Il le prive de ce bas-monde de la même façon que le médecin prive son patient de nourriture [le met au régime].<sup>1002</sup>"}),
        (52, 5, {"number": "895", "text": "L'Imām al-Kāẓim (as) a dit : Vous ne serez considérés comme croyants que lorsque vous considérerez les épreuves comme une grâce et l'aisance comme un malheur, car la patience lors de l'épreuve est meilleure que la distraction et la négligence dans l'aisance.<sup>1003</sup>"}),
        (52, 5, {"number": "896", "text": "L'Imām al-'Askarī (as) a dit : Il n'y a pas une épreuve qu'Allah n'entoure d'une grâce.<sup>1004</sup>"}),
        
        (52, 6, {"number": "897", "text": "L'Imām 'Alī (as) a dit alors qu'il sortait pour invoquer la pluie : En vérité, Allah éprouve Ses serviteurs lorsqu'ils commettent de mauvais actes par une pénurie de récoltes, une rétention de bénédictions, et la fermeture de l'accès aux trésors des grâces afin que le repentant se repente, celui qui est susceptible de s'abstenir [des péchés] s'abstienne, celui qui est susceptible de se rappeler se rappelle, et celui qui est susceptible d'être dissuadé soit dissuadé.<sup>1006</sup>"}),
        (52, 6, {"number": "898", "text": "L'Imām al-Ṣādiq (as) a dit : Le croyant ne passe pas quarante nuits sans qu'il ne subisse un évènement qui l'attriste et qui lui serve de rappel.<sup>1007</sup>"}),
        (52, 6, {"number": "899", "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'Allah le Tout-Puissant veut du bien à l'un de Ses serviteurs qui a commis un péché, Il le fait suivre par une punition et lui rappelle de demander pardon. Mais si Allah veut du mal à l'un de Ses serviteurs lorsque ce dernier a commis un péché, Il le fait suivre par une faveur pour lui faire oublier de demander pardon et qu'il continue à pécher. C'est ce que signifie la parole du Tout-Puissant : «<i>Nous les conduirons graduellement vers leur perte par des voies qu'ils ignorent</i>»<sup>1008</sup>, c'est-à-dire par des faveurs lorsqu'ils pèchent.<sup>1009</sup><br><br><span class=\"reference-note\">(Voir également : 6. La politesse, section 54; 362. La maladie, section 1652)</span>"}),
        
        (52, 7, {"number": "900", "text": "L'Imām 'Alī (as) a dit : Louange à Allah qui a épuré les péchés de nos partisans (<i>shī'a</i>) dans ce bas-monde par leurs épreuves, afin que leur obéissance soit préservée par elles et qu'ils méritent une récompensent grâce à cela.<sup>1010</sup>"}),
        (52, 7, {"number": "901", "text": "L'Imām 'Alī (as) a dit : Allah est trop Indulgent, trop Glorieux, trop Généreux et trop Bienveillant pour que le Jour du Jugement, Il châtie de nouveau Son serviteur pieux qu'Il a déjà puni dans le bas-monde.<sup>1011</sup>"}),
        (52, 7, {"number": "902", "text": "L'Imām al-Bāqir (as) a dit : En vérité, lorsqu'Il veut honorer un serviteur alors que ce dernier a commis un péché, Allah le Béni et le Très-Haut l'éprouve par la maladie, et s'Il ne le fait pas, par le besoin, et s'Il ne le fait pas, Il rend sa mort difficile. En revanche, lorsqu'Il veut humilier un serviteur alors que ce dernier a accompli un acte pieux, Il rend son corps sain, et s'Il ne le fait pas, Il rend abondante sa subsistance, et s'Il ne le fait pas, Il lui accorde une mort aisée.<sup>1012</sup><br><br><span class=\"reference-note\">(Voir également : 149. Le péché, section 780)</span>"}),
        
        (52, 8, {"number": "903", "text": "L'Imām al-Ṣādiq (as) a dit alors qu'il était en compagnie de Sadīr : En vérité, quand Allah aime un serviteur, Il l'immerge d'épreuves. Ô Sadīr ! Vous et nous y sommes [immergés] nuit et jour.<sup>1013</sup>"}),
        (52, 8, {"number": "904", "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'Allah aime des gens ou un serviteur, Il déverse sur lui les épreuves de manière abondante, de telle façon qu'il ne sort d'un malheur que pour retomber dans un autre.<sup>1014</sup><br><br><span class=\"reference-note\">(Voir également : 84. L'amour, section 436)</span>"}),
        
        (52, 9, {"number": "905", "text": "L'Imām al-Bāqir (as) a dit : Plus la foi du croyant augmente, plus sa vie devient difficile.<sup>1015</sup>"}),
        (52, 9, {"number": "906", "text": "<i>Al-Kāfī</i> : Jābir ibn Yazīd rapporte que l'Imām al-Bāqir (as) a dit : En vérité, dans ce bas-monde, le croyant est éprouvé proportionnellement au degré de sa foi.<sup>1016</sup>"}),
        (52, 9, {"number": "907", "text": "L'Imām al-Ṣādiq (as) rapporte du Livre de 'Alī (as) : En vérité, le croyant est éprouvé en proportion de ses bonnes actions ; ainsi, celui dont la religion est juste et les actes bons verra s'intensifier ses épreuves, et cela parce qu'Allah le Tout-Puissant n'a pas fait de cette vie une [source de] récompense pour le croyant ni une [source de] punition pour le mécréant. Cependant, celui dont la religion est faible et les actes infimes verra ses épreuves réduites.<sup>1017</sup>"}),
        (52, 9, {"number": "908", "text": "L'Imām al-Kāẓim (as) a dit : Le croyant est comme les deux plateaux de la balance : plus sa foi augmente, plus ses épreuves augmentent ; ainsi, il rencontrera Allah le Tout-Puissant sans avoir aucune faute.<sup>1018</sup>"}),
        
        (52, 10, {"number": "909", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, il y a au Paradis un rang qui n'est atteint que par le serviteur éprouvé dans son corps.<sup>1019</sup>"}),
        (52, 10, {"number": "910", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, il y a pour le serviteur un rang auprès d'Allah auquel il ne peut accéder que par l'une de ces deux choses: soit par la perte de ses biens, soit en ayant été éprouvé dans son corps.<sup>1020</sup><br><br><span class=\"reference-note\">(Voir également : 74. Le Paradis, section 368)</span>"}),
        
        (52, 11, {"number": "911", "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Très-Haut a révélé à Moïse (as) : «Je n'ai créé de créature plus aimée de Moi que Mon serviteur croyant. Dès lors, lorsque Je l'éprouve, c'est pour son bien ; Je le fais réussir pour son bien et Je le protège pour son bien. Je sais mieux ce qui est bénéfique à Mon serviteur ; dès lors, qu'il patiente face à Mon épreuve, qu'il remercie pour Mes bienfaits, et qu'il soit satisfait de Mon décret afin que Je l'inscrive auprès de Moi parmi les véridiques.»<sup>1021</sup><br><br><span class=\"reference-note\">(Voir également : 332. Le décret et la destinée, section 1533)</span>"}),
        
        (52, 12, {"number": "912", "text": "L'Imām 'Alī (as) a dit : Allah n'éprouve pas quelqu'un autant que lorsqu'Il lui accorde un sursis [pour continuer à lui désobéir].<sup>1022</sup>"}),
        (52, 12, {"number": "913", "text": "L'Imām 'Alī (as) a dit : En vérité, la pauvreté fait partie de l'épreuve ; pire que cela est la maladie du corps ; et pire que cela encore, la maladie du cœur.<sup>1023</sup>"}),
        (52, 12, {"number": "914", "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'a pas éprouvé Ses serviteurs d'une chose plus difficile que celle de devoir dépenser de l'argent.<sup>1024</sup>"}),
        (52, 12, {"number": "915", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui est éprouvé par l'une de ses trois épreuves souhaitera la mort : une pauvreté constante, une femme qui déshonore et un ennemi qui domine.<sup>1025</sup><br><br><span class=\"reference-note\">(Voir également : 312. La mise à l'épreuve, section 1464 ; 242. Le malheur, section 1154)</span>"}),
        
        (52, 13, {"number": "916", "text": "L'Imām 'Alī (as) a dit : La délivrance survient au sommet de l'épreuve.<sup>1026</sup>"}),
        (52, 13, {"number": "917", "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'une épreuve se rajoute à une autre épreuve, le soulagement résultera de l'épreuve.<sup>1027</sup>"}),
        
        (52, 14, {"number": "918", "text": "L'Imām 'Alī (as) a dit : Face à toute affliction, il faut dire : «Il n'y a de puissance et de force qu'en Allah, le Très-haut, le Majestueux» (<i>lā ḥawla wa lā quwwata illā billāh al-'alīy al-'aẓīm</i>), et vous la surmonterez.<sup>1029</sup>"}),
        (52, 14, {"number": "919", "text": "L'Imām al-Riḍā (as) a dit : J'ai vu mon père (as) en songe et il m'a dit : «Mon fils ! Lorsque tu traverses une difficulté, répète [l'invocation] : «Ô Clément ! Ô Tout-Miséricordieux !» (<i>yā ra'ūf ! yā raḥīm !</i>) Ce que tu as vu en rêve est comme si tu l'avais vu dans la réalité.»<sup>1030</sup><br><br><span class=\"reference-note\">(Voir également : 140. L'invocation, section 689)</span>"})
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
