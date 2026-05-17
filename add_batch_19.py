import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 60 - LE TYRAN (Index 61)
    while len(data) <= 61:
        data.append({"title": "60 - LE TYRAN", "subparts": []})
    part60 = data[61]
    while len(part60['subparts']) <= 1:
        part60['subparts'].append({"title": "...", "hadiths": []})
        
    part60['subparts'][0]['title'] = "Le blâme de la tyrannie et du caractère tyrannique"
    part60['subparts'][0]['introduction'] = "«<i>Et ils demandèrent la victoire. Et tout tyran insolent fut déçu.</i>»<sup>1167</sup><br><br>«<i>Voilà les 'Ād. Ils avaient nié les signes de leur Seigneur, désobéi à Ses messagers et suivi le commandement de tout tyran entêté.</i>»<sup>1168</sup>"
    
    part60['subparts'][1]['title'] = "La mauvaise fin des tyrans"

    # Part 61 - LA LÂCHETÉ (Index 62)
    while len(data) <= 62:
        data.append({"title": "61 - LA LÂCHETÉ", "subparts": []})
    part61 = data[62]
    while len(part61['subparts']) <= 1:
        part61['subparts'].append({"title": "...", "hadiths": []})
        
    part61['subparts'][0]['title'] = "Le blâme de la lâcheté"
    part61['subparts'][1]['title'] = "Le lâche et la guerre"

    # Part 62 - LA DISCUSSION (Index 63)
    while len(data) <= 63:
        data.append({"title": "62 - LA DISCUSSION", "subparts": []})
    part62 = data[63]
    while len(part62['subparts']) <= 1:
        part62['subparts'].append({"title": "...", "hadiths": []})
        
    part62['subparts'][0]['title'] = "La discussion blâmée"
    part62['subparts'][0]['introduction'] = "«<i>Et il y a des gens qui discutent au sujet d'Allah sans aucune science, et qui suivent tout diable rebelle.</i>»<sup>1184</sup><br><br>«<i>Seuls ceux qui ont mécru discutent les versets d'Allah. Que leurs activités dans le pays de te trompent pas.</i>»<sup>1185</sup><br><br><span class=\"reference-note\">(Voir également : Coran 3:66, 7:71, 8:6, 18:54, 18:56, 19:97, 22:8-9, 22:68, 25:50, 42:35, 43:57)</span>"
    
    part62['subparts'][1]['title'] = "La bonne discussion"
    part62['subparts'][1]['introduction'] = "«<i>Appelle au sentier de ton Seigneur par la sagesse et la bonne exhortation. Et discute avec eux de la meilleure façon. Car c'est ton Seigneur qui connait le mieux celui qui s'écarte de Son sentier et c'est Lui qui connaît le mieux ceux qui sont bien guidés.</i>»<sup>1188</sup>"

    # Part 63 - L'EXPÉRIENCE (Index 64)
    while len(data) <= 64:
        data.append({"title": "63 - L'EXPÉRIENCE", "subparts": []})
    part63 = data[64]
    while len(part63['subparts']) <= 0:
        part63['subparts'].append({"title": "...", "hadiths": []})
        
    part63['subparts'][0]['title'] = "Les bénédictions de l'expérience"

    updates = [
        # Part 60 - LE TYRAN (Index 61)
        (61, 0, {"number": "1031", "text": "Le Messager d'Allah (s) a dit : Le tyran entêté est celui qui refuse de dire : «Point de divinité à part Dieu.»<sup>1169</sup>"}),
        (61, 0, {"number": "1032", "text": "L'Imām 'Alī (as) a dit : L'acte du tyran ne peut se purifier.<sup>1170</sup>"}),
        (61, 0, {"number": "1033", "text": "L'Imām 'Alī (as) a dit : Ne vous adressez pas à moi comme on s'adresse aux tyrans, ne soyez pas circonspects face à moi comme face aux oppresseurs, et ne vous associez pas avec moi avec hypocrisie.<sup>1171</sup>"}),
        
        (61, 1, {"number": "1034", "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, les tyrans et les insolents seront rassemblés sous la forme de petites fourmis, et ils seront foulés par les pieds des autres en raison de leur petitesse devant Allah.<sup>1172</sup>"}),
        (61, 1, {"number": "1035", "text": "L'Imām 'Alī (as) a dit : Celui qui agit de façon tyrannique sera brisé.<sup>1173</sup>"}),
        (61, 1, {"number": "1036", "text": "L'Imām 'Alī (as) a dit : Celui qui agit de façon tyrannique sera humilié et rabaissé par Allah.<sup>1174</sup>"}),
        (61, 1, {"number": "1037", "text": "L'Imām 'Alī (as) a dit : Prends garde au comportement tyrannique vis-à-vis des serviteurs d'Allah, car tout tyran sera annihilé par Allah.<sup>1175</sup>"}),
        (61, 1, {"number": "1038", "text": "L'Imām al-Ṣādiq (as) a dit : Les tyrans seront les personnes les plus éloignées d'Allah le Tout-Puissant le Jour de la résurrection.<sup>1176</sup>"}),

        # Part 61 - LA LÂCHETÉ (Index 62)
        (62, 0, {"number": "1039", "text": "L'Imām 'Alī (as) a dit : La lâcheté est un défaut.<sup>1177</sup>"}),
        (62, 0, {"number": "1040", "text": "L'Imām 'Alī (as) a dit : La lâcheté, la cupidité et l'avarice sont de mauvais instincts qui sont suscités par une mauvaise opinion d'Allah - loué soit-Il.<sup>1178</sup>"}),
        (62, 0, {"number": "1041", "text": "L'Imām 'Alī (as) a dit : Méfiez-vous de la lâcheté car c'est [une source de] déshonneur et un défaut.<sup>1179</sup>"}),
        (62, 0, {"number": "1042", "text": "L'Imām 'Alī (as) a dit : La pure lâcheté est issue de l'impuissance de l'âme et de la faiblesse de la conviction.<sup>1180</sup>"}),
        (62, 0, {"number": "1043", "text": "Interrogé au sujet de la lâcheté, l'Imām Ḥasan (as) a dit : C'est l'agressivité envers l'ami et la fuite face à l'ennemi.<sup>1181</sup>"}),
        
        (62, 1, {"number": "1044", "text": "Le Messager d'Allah (s) a dit : Celui qui ressent en lui de la lâcheté ne devrait pas partir en guerre.<sup>1182</sup>"}),
        (62, 1, {"number": "1045", "text": "L'Imām 'Alī (as) a dit : Il n'est pas autorisé au lâche de participer à la guerre car il sera rapidement mis en fuite. En revanche, il doit prendre ce avec quoi il souhaitait faire la guerre [réunir le matériel de guerre] et en équiper un autre que lui. De cette façon, il aura l'équivalent de la rétribution du combattant, sans diminuer en rien la rétribution de ce dernier.<sup>1183</sup>"}),

        # Part 62 - LA DISCUSSION (Index 63)
        (63, 0, {"number": "1046", "text": "Le Messager d'Allah (s) a dit : Tout groupe qui discute longuement s'égare.<sup>1186</sup>"}),
        (63, 0, {"number": "1047", "text": "L'Imām 'Alī (as) a dit : Gare à la discussion car elle génère le doute.<sup>1187</sup><br><br><span class=\"reference-note\">(Voir également : 363. La dispute ; 377. Le débat)</span>"}),
        
        (63, 1, {"number": "1048", "text": "L'Imām 'Alī (as) a dit dans les sagesses qui lui sont attribuées : Ordonnez aux jeunes de discuter et de polémiquer, aux adultes de réfléchir et aux personnes âgées de garder le silence.<sup>1189</sup>"}),
        (63, 1, {"number": "1049", "text": "L'Imām al-'Askarī (as) a dit : En présence de l'Imām al-Ṣādiq (as), la question de la discussion au sujet de la religion et le fait que le Messager d'Allah (s) et les Imāms infaillibles (as) ont interdit cela furent évoqués. L'Imām al-Ṣādiq (as) dit : «Ils ne l'ont pas complètement interdite, mais ils n'ont interdit que la discussion qui n'est pas menée de la meilleure façon.»<sup>1190</sup>"}),

        # Part 63 - L'EXPÉRIENCE (Index 64)
        (64, 0, {"number": "1050", "text": "L'Imām 'Alī (as) a dit : Les expériences sont un savoir bénéfique.<sup>1191</sup>"}),
        (64, 0, {"number": "1051", "text": "L'Imām 'Alī (as) a dit en s'adressant à son fils (as) : Je t'ai inculqué une bonne éducation avant que ton cœur ne durcisse et que ton esprit ne soit occupé ; cela afin que tu comprennes avec ton esprit ce que les gens expérimentés t'ont épargné d'expérimenter toi-même. Ainsi, tu seras ménagé de la difficulté de la recherche et de la douleur de l'expérience.<sup>1192</sup>"})
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
