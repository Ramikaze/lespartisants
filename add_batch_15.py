import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 55 - LE COMMERCE (Index 56)
    part55 = data[56]
    while len(part55['subparts']) <= 14:
        part55['subparts'].append({"title": "...", "hadiths": []})
        
    part55['subparts'][11]['title'] = "Mise en garde au sujet du recours au serment dans le commerce"
    
    part55['subparts'][12]['title'] = "Le commerce de l'Au-delà"
    part55['subparts'][12]['introduction'] = "«<i>Ô vous qui avez cru ! Vous indiquerai-je un commerce qui vous sauvera d'un châtiment douloureux ? Vous croyez en Allah et en Son Messager, et vous combattez avec vos biens et vos personnes dans le chemin d'Allah, et cela vous est bien meilleur, si vous saviez !</i>»<sup>1088</sup>"
    
    part55['subparts'][13]['title'] = "Le commerce ne distrait pas le croyant [du souvenir d'Allah]"
    part55['subparts'][13]['introduction'] = "«<i>Des hommes que ni le négoce, ni la vente ne distraient de l'invocation d'Allah, de l'accomplissement de la prière (ṣalāt) et de l'acquittement de l'aumône (zakāt), et qui redoutent un Jour où les cœurs seront bouleversés ainsi que les regards.</i>»<sup>1096</sup>"
    
    part55['subparts'][14]['title'] = "Le commerce de la religion"

    # Part 56 - LE REPENTIR (Index 57)
    while len(data) <= 57:
        data.append({"title": "56 - LE REPENTIR", "subparts": []})
    part56 = data[57]
    while len(part56['subparts']) <= 6:
        part56['subparts'].append({"title": "...", "hadiths": []})
        
    part56['subparts'][0]['title'] = "L'incitation au repentir"
    part56['subparts'][0]['introduction'] = "«<i>C'est Lui qui agrée le repentir de Ses serviteurs, pardonne les méfaits et sait ce que vous faites.</i>»<sup>1100</sup>"
    
    part56['subparts'][1]['title'] = "Le statut du repentant"
    part56['subparts'][1]['introduction'] = "«<i>Allah aime ceux qui se repentent, et Il aime ceux qui se purifient.</i>»<sup>1104</sup>"
    
    part56['subparts'][2]['title'] = "Le signe du repentant"
    
    part56['subparts'][3]['title'] = "L'acceptation du repentir"
    part56['subparts'][3]['introduction'] = "«<i>C'est Lui qui agrée le repentir de Ses serviteurs, qui absout les mauvaises actions.</i>»<sup>1111</sup>"
    
    part56['subparts'][4]['title'] = "Quand le repentir est-il accepté?"
    part56['subparts'][4]['introduction'] = "«<i>Mais l'absolution n'est pas destinée à ceux qui font de mauvaises actions jusqu'au moment où la mort se présente à l'un d'eux, et qui s'écrie : «Certes, je me repens maintenant !», ni pour ceux qui meurent mécréants.</i>»<sup>1113</sup>"
    
    part56['subparts'][5]['title'] = "Le regret est un repentir"
    
    part56['subparts'][6]['title'] = "L'aveu sincère [des péchés]"
    part56['subparts'][6]['introduction'] = "«<i>D'autres ont reconnu leurs péchés, ils ont mêlé de bonnes actions à d'autres mauvaises. Il se peut qu'Allah accueille leur repentir.</i>»<sup>1120</sup>"

    updates = [
        # Part 55 - LE COMMERCE (Index 56)
        (56, 11, {"number": "963", "text": "L'Imām 'Alī (as) a dit : Ô négociants! Diminuez vos serments car cela promet la marchandise mais détruit le [vrai] profit.<sup>1086</sup>"}),
        (56, 11, {"number": "964", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut abhorre celui qui promeut sa marchandise en ayant recours aux serments.<sup>1087</sup>"}),
        
        (56, 12, {"number": "965", "text": "Le Messager d'Allah (s) a dit : Tout ce que tu perçois avec ton œil et que ton cœur trouve agréable, consacre-le à Allah, car cela est le commerce de l'Au-delà. En effet, Allah a dit : «<i>Tout ce que vous possédez s'épuisera, tandis que ce qui est auprès d'Allah durera.</i>» <sup>1089 1090</sup>"}),
        (56, 12, {"number": "966", "text": "Le Messager d'Allah (s) a dit : Le commerçant de ce bas-monde met en danger sa personne et son argent. Le commerçant de l'Au-delà est gagnant et retire du profit ; son premier gain est sa propre âme, puis ensuite le Paradis comme refuge.<sup>1091</sup>"}),
        (56, 12, {"number": "967", "text": "L'Imām 'Alī (as) a dit : Il n'y a pas meilleur commerce qu'une œuvre pieuse et il n'y a pas meilleur profit que la récompense [divine].<sup>1092</sup>"}),
        (56, 12, {"number": "968", "text": "L'Imām 'Alī (as) a dit : La personne qui fait le plus de profit est celle qui achète l'Au-delà avec sa vie d'ici-bas.<sup>1093</sup>"}),
        (56, 12, {"number": "969", "text": "L'Imām 'Alī (as) a dit : En vérité, celui qui vend sa personne pour autre chose que le Paradis [se verra exposé] à une grande épreuve.<sup>1094</sup>"}),
        (56, 12, {"number": "970", "text": "L'Imām 'Alī (as) a dit : Celui qui fait de l'obéissance à Allah une marchandise récoltera des profits sans avoir besoin de faire du commerce.<sup>1095</sup>"}),
        
        (56, 13, {"number": "971", "text": "<i>Biḥār al-Anwār</i> cite de <i>Fiqh al-Riḍā</i> (as) [de l'Imām al-Riḍā (as)] : Si tu es occupé par ton commerce à l'heure de la prière, que ton commerce ne te détourne pas de la prière, et ce car Allah a décrit un groupe de gens et a fait leur éloge, en disant : «<i>Des hommes que ni le négoce, ni la vente ne distraient de l'invocation d'Allah, de l'accomplissement de la prière (ṣalāt) et de l'acquittement de l'aumône (zakāt), et qui redoutent un Jour où les cœurs seront bouleversés ainsi que les regards.</i>» Ainsi, ce groupe s'adonnait au commerce mais lorsque l'heure de la prière arrivait, ils délaissaient le commerce pour accomplir leur prière. Leur récompense est plus grande que ceux qui ne sont pas commerçants et qui prient.<sup>1097</sup>"}),
        
        (56, 14, {"number": "972", "text": "L'Imām 'Alī (as) a dit : Celui qui cherche à se nourrir en sacrifiant sa religion aura seulement de sa religion ce qu'il mange.<sup>1098</sup>"}),
        (56, 14, {"number": "973", "text": "L'Imām 'Alī (as) a dit : Celui qui veut gagner ce monde à travers les actes de l'Au-delà [la religion] s'éloignera encore plus de ce qu'il veut.<sup>1099</sup>"}),
        
        # Part 56 - LE REPENTIR (Index 57)
        (57, 0, {"number": "974", "text": "Le Messager d'Allah (s) a dit : Le repentir efface ce qui le précède.<sup>1101</sup>"}),
        (57, 0, {"number": "975", "text": "Le Messager d'Allah (s) a dit : Celui qui se repent d'un péché est comme celui qui n'a pas péché.<sup>1102</sup>"}),
        (57, 0, {"number": "976", "text": "L'Imām 'Alī (as) a dit : Le repentir purifie les cœurs et lave les péchés.<sup>1103</sup>"}),
        
        (57, 1, {"number": "977", "text": "Le Messager d'Allah (s) a dit : Il n'y a pas plus aimé d'Allah que le croyant repentant ou la croyante repentante.<sup>1105</sup>"}),
        (57, 1, {"number": "978", "text": "Le Messager d'Allah (s) a dit : Tous les enfants d'Adam commettent des fautes, mais les meilleurs parmi les fautifs sont les repentants.<sup>1106</sup>"}),
        (57, 1, {"number": "979", "text": "Le Messager d'Allah (s) a dit : Allah se réjouit du repentir de Son serviteur plus qu'une personne stérile qui donne naissance à un enfant, qu'une personne perdue qui trouve son chemin, ou que l'assoiffé qui atteint l'eau.<sup>1107</sup>"}),
        
        (57, 2, {"number": "980", "text": "Le Messager d'Allah (s) a dit : Le repentant se distingue par quatre signes : la sincérité de ses actes pour Allah, l'abstention du faux et de l'erreur, l'astreinte à la vérité, et la vive aspiration au bien.<sup>1108</sup>"}),
        (57, 2, {"number": "981", "text": "L'Imām 'Alī (as) a dit en décrivant les repentants : Ils ont planté les arbres de leurs péchés face à leurs yeux et leurs cœurs, et ils les ont arrosés avec l'eau du regret. Ainsi, les arbres leur ont donné le fruit du salut, et leur ont laissé la satisfaction et la dignité.<sup>1109</sup>"}),
        (57, 2, {"number": "982", "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'un de ses entretiens intimes : Fais en sorte que nous soyons de ceux [...] qui ont éteint le feu des passions en y déversant l'eau du repentir, et ont lavé les réceptacles de l'ignorance par l'eau pure de la vie.<sup>1110</sup>"}),
        
        (57, 3, {"number": "983", "text": "L'Imām 'Alī (as) a dit : Celui à qui le repentir a été accordé ne peut être privé de son acceptation, et celui à qui est accordé le pouvoir de demander pardon ne sera pas privé du pardon.<sup>1112</sup>"}),
        
        (57, 4, {"number": "984", "text": "Le Messager d'Allah (s) a dit : Allah accepte le repentir de celui qui se repent avant de voir [l'ange de la mort].<sup>1114</sup>"}),
        (57, 4, {"number": "985", "text": "L'Imām al-Bāqir (as) a dit : Lorsque l'âme atteint ceci - il désigna de sa main sa gorge -, il n'y a plus moyen de se repentir pour le savant; en revanche, l'ignorant peut toujours se repentir.<sup>1115</sup>"}),
        (57, 4, {"number": "986", "text": "Interrogé au sujet de la raison pour laquelle Allah a noyé Pharaon alors qu'il avait cru en Lui et attesté Son unicité, l'Imām al-Riḍā (as) dit : Car il n'a cru que lorsqu'il a vu le courroux [d'Allah], et la foi à la vue du courroux n'est pas agréée.<sup>1116</sup>"}),
        
        (57, 5, {"number": "987", "text": "Le Messager d'Allah (s) a dit : Le regret est un repentir.<sup>1117</sup>"}),
        (57, 5, {"number": "988", "text": "L'Imām 'Alī (as) a dit : Regretter la faute est une demande de pardon.<sup>1118</sup>"}),
        (57, 5, {"number": "989", "text": "L'Imām 'Alī (as) a dit : Le regret du cœur absout le péché.<sup>1119</sup>"})
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
