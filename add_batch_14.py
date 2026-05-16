import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 55 - LE COMMERCE (Index 56)
    while len(data) <= 56:
        data.append({"title": "55 - LE COMMERCE", "subparts": []})
    part55 = data[56]
    while len(part55['subparts']) <= 10:
        part55['subparts'].append({"title": "...", "hadiths": []})
        
    part55['subparts'][0]['title'] = "La vertu du commerce"
    part55['subparts'][0]['introduction'] = "«<i>Ô vous qui croyez ! Que certains d'entre vous ne mangent pas les biens des autres illégalement. Mais qu'il y ait du commerce [légal] entre vous, par consentement mutuel. Et ne vous tuez pas vous-mêmes.</i><sup>1057</sup> <i>Allah, en vérité, est Miséricordieux envers vous.</i>»<sup>1058</sup>"
    
    part55['subparts'][1]['title'] = "Délaisser le commerce"
    part55['subparts'][2]['title'] = "Le bon comportement dans le commerce"
    
    part55['subparts'][3]['title'] = "L'interdiction de la fraude"
    part55['subparts'][3]['introduction'] = "«<i>Malheur aux fraudeurs qui, lorsqu'ils font mesurer pour eux-mêmes exigent la pleine mesure, et qui lorsqu'eux-mêmes mesurent ou pèsent pour les autres, [leur] causent perte.</i>»<sup>1070</sup><br><br><span class=\"reference-note\">(Voir également : Coran 6:152, 11:84-85, 26:181-183, 55:7-9)</span>"
    
    part55['subparts'][4]['title'] = "L'incitation du commerçant à la charité"
    part55['subparts'][5]['title'] = "L'indulgence dans la vente et l'achat"
    part55['subparts'][6]['title'] = "Le marchandage"
    part55['subparts'][7]['title'] = "L'égalité entre la personne qui marchande et celle qui ne marchande pas"
    part55['subparts'][8]['title'] = "Le profit du croyant vis-à-vis d'un autre croyant"
    part55['subparts'][9]['title'] = "Les commerçants immoraux"
    part55['subparts'][10]['title'] = "Inciter les commerçants à être honnête"

    updates = [
        # Part 54 - LE SERMENT D'ALLÉGEANCE (Index 55)
        (55, 3, {"number": "937", "text": "L'Imām 'Alī (as) a dit : Vous vous êtes précipités autour de moi tels des chameaux assoiffés qui se précipitent vers l'abreuvoir, avides de me prêter serment d'allégeance.<sup>1056</sup>"}),

        # Part 55 - LE COMMERCE (Index 56)
        (56, 0, {"number": "938", "text": "L'Imām 'Alī (as) a dit : Pratiquez divers commerces, car il y a en cela pour vous une absence de besoin de ce qui est possédé par les gens. Et en vérité, Allah le Tout-Puissant aime celui qui est engagé dans une profession de façon honnête.<sup>1059</sup>"}),
        (56, 0, {"number": "939", "text": "L'Imām al-Ṣādiq (as) a dit : Le commerce renforce l'intelligence.<sup>1060</sup>"}),
        
        (56, 1, {"number": "940", "text": "L'Imām al-Ṣādiq (as) a dit : Délaisser le commerce affaiblit l'intelligence.<sup>1061</sup>"}),
        (56, 1, {"number": "941", "text": "Lorsque le vendeur de tissus Mu'ādh ibn Kathīr lui dit : «Je m'apprête à abandonner le marché car j'ai de l'argent en main», l'Imām al-Ṣādiq (as) répondit : «Dans ce cas, on ne t'accordera plus d'estime, et on ne fera plus appel à ton aide pour aucune chose.»<sup>1062</sup>"}),
        
        (56, 2, {"number": "942", "text": "Le Messager d'Allah (s) a dit : Que celui qui vend et achète s'abstienne de cinq choses, sans quoi il ne devrait pas vendre ni acheter : l'usure, le [faux] serment, cacher les défauts [des marchandises], faire l'éloge de ce qu'il vend, et montrer de la désapprobation lorsqu'il achète.<sup>1063</sup>"}),
        (56, 2, {"number": "943", "text": "L'Imām 'Alī (as) a dit : Le commerçant peureux sera privé [de subsistance], alors que le commerçant audacieux sera pourvu de subsistance.<sup>1064</sup>"}),
        (56, 2, {"number": "944", "text": "L'Imām 'Alī (as) a dit : Ô commerçants ! La connaissance [des lois et principes] du commerce d'abord, puis le commerce ensuite ! La connaissance d'abord, puis le commerce ! La connaissance d'abord, puis le commerce !<sup>1065</sup>"}),
        (56, 2, {"number": "945", "text": "L'Imām 'Alī (as) a dit : Ô commerçants ! Commencez en demandant à Allah une bonne issue, recherchez les grâces en étant accommodant, rapprochez-vous des acheteurs, parez-vous d'indulgence, abstenez-vous des serments, éloignez-vous du mensonge, répugnez l'injustice, soyez juste vis-à-vis des opprimés, n'approchez pas l'usure, et «<i>donnez donc la pleine mesure et le poids, et ne donnez pas aux gens moins que ce qui leur est dû. Et ne commettez pas de la corruption sur la terre</i>»<sup>1066</sup> <sup>1067</sup>"}),
        (56, 2, {"number": "946", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui veut faire du commerce doit avant tout s'instruire dans sa religion de manière approfondie afin qu'il sache ce qui lui est autorisé et ce qui lui est interdit. Celui qui ne s'est pas instruit dans sa religion et qui a pratiqué le commerce s'enlisera dans les doutes et les ambiguïtés.<sup>1068</sup>"}),
        (56, 2, {"number": "947", "text": "L'Imām al-Ṣādiq (as) a dit : Tout musulman qui épargne à un autre musulman une vente regrettable, Allah le Tout-Puissant lui pardonna son faux-pas le Jour de la Résurrection.<sup>1069</sup>"}),
        
        (56, 3, {"number": "948", "text": "Le Messager d'Allah (s) a dit : Lorsque vous pesez, rajoutez un peu plus [en faveur du client].<sup>1071</sup>"}),
        (56, 3, {"number": "949", "text": "L'Imām al-Ṣādiq (as) a dit : La transaction n'est accomplie que lorsque la balance penche d'un côté [en faveur du client].<sup>1072</sup>"}),
        
        (56, 4, {"number": "950", "text": "Le Messager d'Allah (s) a dit : Ô commerçants ! En vérité, le Diable et le péché sont présents lors de la vente, imprégnez-la donc de charité (<i>ṣadaqa</i>).<sup>1073</sup>"}),
        
        (56, 5, {"number": "951", "text": "Le Messager d'Allah (s) a dit : Qu'Allah soit Miséricordieux envers un serviteur indulgent lorsqu'il vend, indulgent lorsqu'il achète, indulgent lorsqu'il juge et indulgent lorsqu'il est jugé.<sup>1074</sup>"}),
        (56, 5, {"number": "952", "text": "L'Imām 'Alī (as) a dit en conseillant un homme qui vendait une marchandise : J'ai entendu le Messager d'Allah (s) dire : «L'indulgence est l'un des aspects du gain.»<sup>1075</sup>"}),
        
        (56, 6, {"number": "953", "text": "Le Messager d'Allah (s) a dit : Ô 'Alī ! Ne marchande pas pour quatre choses : l'achat de l'animal à sacrifier, le linceul, l'esclave et le transport vers La Mecque.<sup>1076</sup>"}),
        (56, 6, {"number": "954", "text": "L'Imām 'Alī (as) a dit : Marchande même pour deux dirhams, car celui qui est escroqué n'est ni louable, ni rétribué.<sup>1077</sup>"}),
        
        (56, 7, {"number": "955", "text": "L'Imām al-Ṣādiq (as) a dit au sujet d'un homme qui avait une marchandise qu'il a mise en vente à un prix donné et la vendait à ce prix aux personnes qui ne disaient rien, tandis qu'il proposait une meilleure offre à celle qui marchandait ou qui refusait d'acheter à ce prix : Il n'y aurait eu aucun mal s'il faisait une meilleure offre à deux ou trois personnes, mais s'il le fait juste avec celle qui refuse d'acheter à ce prix et marchande et pas avec celle qui ne marchande pas, cela ne me plaît pas, à moins qu'il vende toute sa marchandise en une seule fois.<sup>1078</sup>"}),
        
        (56, 8, {"number": "956", "text": "L'Imām al-Ṣādiq (as) a dit : Le profit du croyant vis-à-vis d'un autre croyant est de l'usure sauf s'il achète pour plus de cent dirhams. Dans ce cas, il est légitime de réaliser un profit qui permet de se nourrir pour la journée. Ou encore si ce dernier achète pour faire du commerce, vous pouvez réaliser un profit, mais faites preuve de modération vis-à-vis d'eux.<sup>1079</sup>"}),
        (56, 8, {"number": "957", "text": "Interrogé au sujet de l'affirmation selon laquelle «Le profit du croyant vis-à-vis d'un autre croyant est de l'usure», l'Imām al-Ṣādiq (as) répondit : Cela sera ainsi quand la vérité se sera manifestée et que notre Qā'im des Gens de la demeure prophétique [Ahl al-Bayt] sera établi. En revanche, maintenant, il n'y a aucun mal.<sup>1080</sup>"}),
        
        (56, 9, {"number": "958", "text": "<i>Kanz al-'Ummāl</i> : Le Messager d'Allah (s) a dit : «En vérité, les commerçants sont les immoraux.» Ils dirent : «Ô Messager d'Allah, Allah n'a-t-Il pas autorisé le commerce ?» Il répondit : «Oui, mais ils mentent lorsqu'ils parlent, ils font de [faux] serments et commettent des péchés.»<sup>1081</sup>"}),
        (56, 9, {"number": "959", "text": "<i>Kanz al-'Ummāl</i> : 'Alī (as) avait l'habitude d'aller au marché, se tenait à sa place [habituelle] et disait : Que la paix soit sur vous, ô gens du marché ! Craignez Allah dans vos serments, car le serment dégrade la marchandise et détruit les bénédictions. Le marchand est un immoral sauf celui qui ne prend et ne donne que ce qui est juste.<sup>1082</sup>"}),
        
        (56, 10, {"number": "960", "text": "Le Messager d'Allah (s) a dit : Le Jour du Jugement, le commerçant musulman digne de confiance et honnête sera avec les martyrs.<sup>1083</sup>"}),
        (56, 10, {"number": "961", "text": "Le Messager d'Allah (s) a dit : Le Jour du Jugement, le commerçant honnête sera sous l'ombre du Trône.<sup>1084</sup>"}),
        (56, 10, {"number": "962", "text": "Le Messager d'Allah (s) a dit : Parmi les trois personnes qui ne seront pas regardées par Allah [avec miséricorde] [...] et celle qui fait l'éloge de sa marchandise de façon mensongère.<sup>1085</sup>"})
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
