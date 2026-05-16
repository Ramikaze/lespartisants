import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 51 - L'ÉPREUVE (Index 52)
    part51 = data[52]
    while len(part51['subparts']) <= 15:
        part51['subparts'].append({"title": "...", "hadiths": []})
    part51['subparts'][15]['title'] = "L'invocation à la vue de personnes éprouvées"

    # Part 52 - LA CALOMNIE (Index 53)
    while len(data) <= 53:
        data.append({"title": "52 - LA CALOMNIE", "subparts": []})
    part52 = data[53]
    while len(part52['subparts']) <= 0:
        part52['subparts'].append({"title": "...", "hadiths": []})
    part52['subparts'][0]['title'] = "Mise en garde contre la calomnie"
    part52['subparts'][0]['introduction'] = "«<i>Et ceux qui offensent les croyants et les croyantes sans qu'ils l'aient mérité se chargent d'une calomnie et d'un péché évident.</i>»<sup>1033</sup><br><br><span class=\"reference-note\">(Voir également : Coran 17:36, 24:12-15, 49:12)</span>"

    # Part 53 - L'EXÉCRATION RÉCIPROQUE (al-mubāhala) (Index 54)
    while len(data) <= 54:
        data.append({"title": "53 - L'EXÉCRATION RÉCIPROQUE (al-mubāhala)", "subparts": []})
    part53 = data[54]
    while len(part53['subparts']) <= 0:
        part53['subparts'].append({"title": "...", "hadiths": []})
    part53['subparts'][0]['title'] = "L'exécration réciproque"
    part53['subparts'][0]['introduction'] = "«<i>A ceux qui te contredisent à son propos [à propos de Jésus], maintenant que tu es bien informé, tu n'as qu'à dire : «Venez, appelons nos fils et les vôtres, nos femmes et les vôtres, nos propres personnes et les vôtres, puis proférons l'exécration réciproque en appelant la malédiction d'Allah sur les menteurs».</i>»<sup>1039</sup>"

    # Part 54 - LE SERMENT D'ALLÉGEANCE (al-bay'a) (Index 55)
    while len(data) <= 55:
        data.append({"title": "54 - LE SERMENT D'ALLÉGEANCE (al-bay'a)", "subparts": []})
    part54 = data[55]
    while len(part54['subparts']) <= 3:
        part54['subparts'].append({"title": "...", "hadiths": []})
    part54['subparts'][0]['title'] = "Le serment d'allégeance au Prophète (s) est une allégeance à Allah"
    part54['subparts'][0]['introduction'] = "«<i>Ceux qui te prêtent serment d'allégeance ne font que prêter serment à Allah : la main d'Allah est au-dessus de leurs mains. Quiconque viole le serment ne le viole qu'à son propre détriment ; et quiconque remplit son engagement auprès d'Allah, Il lui apportera bientôt une énorme récompense.</i>»<sup>1043</sup>"
    
    part54['subparts'][1]['title'] = "Le serment d'allégeance des femmes"
    part54['subparts'][1]['introduction'] = "«<i>Ô Prophète ! Quand les croyantes viennent à toi pour te prêter serment d'allégeance [et s'engagent] qu'elles n'associeront rien à Allah, qu'elles ne voleront pas, qu'elles ne se livreront pas à l'adultère, qu'elles ne tueront pas leurs propres enfants, qu'elles ne commettront aucune infamie ni avec leurs mains ni avec leurs pieds et qu'elles ne désobéiront pas en ce qui est convenable, alors reçois leur serment d'allégeance, et implore d'Allah le pardon pour elle. Allah est certes, Pardonneur et Très Miséricordieux.</i>»<sup>1048</sup>"
    
    part54['subparts'][2]['title'] = "Violer son serment d'allégeance"
    part54['subparts'][2]['introduction'] = "«<i>Soyez fidèles au pacte d'Allah après l'avoir contracté et ne violez pas vos serments après les avoir solennellement prêtés et avoir pris Allah comme garant [de votre sincérité]. Vraiment Allah sait ce que vous faites !</i>»<sup>1050</sup>"
    
    part54['subparts'][3]['title'] = "Le serment d'allégeance des musulmans à l'Imām 'Alī (as)"

    updates = [
        # Part 51 - L'ÉPREUVE (Index 52)
        (52, 15, {"number": "920", "text": "Le Messager d'Allah (s) a dit : Lorsque vous apercevez des personnes éprouvées, rendez grâce à Allah sans qu'elles ne l'entendent, car cela pourrait les attrister.<sup>1031</sup>"}),
        (52, 15, {"number": "921", "text": "L'Imām al-Bāqir (as) a dit : Lorsque vous voyez une personne éprouvée, dites trois fois, sans qu'elle ne l'entende : «Louange à Allah qui m'a épargné ce dont Il t'a éprouvé et s'Il l'avait voulu, Il l'aurait fait». Celui qui récite ces paroles ne sera jamais affecté par cette épreuve.<sup>1032</sup>"}),

        # Part 52 - LA CALOMNIE (Index 53)
        (53, 0, {"number": "922", "text": "Le Messager d'Allah (s) a dit : Le Jour du Jugement, celui qui a calomnié un croyant ou une croyante ou qui a parlé de lui de façon mensongère sera mis par Allah le Très-Haut sur un mont en feu jusqu'à ce qu'il retire ce qu'il a dit.<sup>1034</sup>"}),
        (53, 0, {"number": "923", "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de pire insolence que la calomnie.<sup>1035</sup>"}),
        (53, 0, {"number": "924", "text": "L'Imām 'Alī (as) a dit : La calomnie envers un innocent est aussi immense que le ciel.<sup>1036</sup>"}),
        (53, 0, {"number": "925", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Celui qui accuse les autres au sujet de ce qu'ils ont en eux se verra accuser de ce qu'il n'a pas en lui.<sup>1037</sup>"}),
        (53, 0, {"number": "926", "text": "L'Imām al-Ṣādiq (as) a dit en citant un sage : La calomnie d'un innocent est plus lourde que des montagnes élevées.<sup>1038</sup>"}),

        # Part 53 - L'EXÉCRATION RÉCIPROQUE (Index 54)
        (54, 0, {"number": "927", "text": "L'Imām al-Ṣādiq (as) a dit en s'adressant à Abū al-'Abbās au sujet de l'exécration réciproque: Croise tes doigts dans ses doigts et dit : «Ô Allah ! Si untel a contesté la vérité et qu'il a affirmé une chose fausse, alors frappe-le par un malheur venant du ciel ou par un châtiment venant de Toi.» Puis maudis-le soixante-dix fois.<sup>1040</sup>"}),
        (54, 0, {"number": "928", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, lorsque les chrétiens de Najrān arrivèrent auprès du Messager d'Allah (s), leurs dignitaires étaient Al-Ahtam, Al-'Āqib et al-Sayyid... Ils dirent: «A quoi nous invites-tu ?» Il répondit : «Au témoignage qu'il n'y a point de divinité à part Allah, que je suis le Messager d'Allah, que Jésus était un serviteur, créé, qui mangeait, buvait et faisait ses besoins naturels...». Le Messager (s) leur dit alors : «Venez proférer la malédiction [d'Allah] sur moi. Si je suis sincère, la malédiction s'abattra sur vous et si je mens, elle s'abattra sur moi». Ils dirent : «Ta proposition est juste» puis se donnèrent rendez-vous pour l'exécration réciproque.<br>Lorsqu'ils retournèrent chez eux, leurs dignitaires leur dirent : «S'il vient à l'exécration réciproque en compagnie de son peuple, dans ce cas, nous proférerons l'exécration réciproque car [cela signifie qu'] il n'est pas un prophète. En revanche, s'il vient à l'exécration réciproque avec sa plus proche famille, dans ce cas, nous ne devons pas proférer l'exécration réciproque car n'expose sa famille que celui qui est véridique.» Le lendemain matin, ils arrivèrent auprès du Prophète (s) qui était accompagné du Prince des Croyants, Fāṭima, Ḥasan et Ḥusayn - que les prières d'Allah soient sur eux. Ils prirent peur et dirent au Messager d'Allah (s) : «Nous t'accorderons ce qui te satisfait, mais épargne-nous l'exécration réciproque.» Ainsi, le Messager d'Allah fit une trêve reposant sur la capitation<sup>1041</sup> et ils repartirent chez eux.<sup>1042</sup>"}),

        # Part 54 - LE SERMENT D'ALLÉGEANCE (Index 55)
        (55, 0, {"number": "929", "text": "'Alī ibn Ibrāhīm a dit : Il a été révélé lors du serment d'allégeance de l'Agrément [<i>Riḍwān</i>]: «<i>Allah a très certainement agréé les croyants quand ils t'ont prêté serment d'allégeance sous l'arbre. Il a su ce qu'il y avait dans leurs cœurs, et a fait descendre sur eux la quiétude, et Il les a récompensés par une victoire proche.</i>»<sup>1044</sup> Allah a exigé d'eux de ne plus contester les agissements du Prophète (s) après cela, ni de contrevenir à ce qu'il pourrait leur ordonner. Ainsi, après la révélation du verset nommé al-Riḍwān, Allah le Tout-Puissant a dit : «<i>Ceux qui te prêtent serment d'allégeance ne font que prêter serment à Allah</i>»<sup>1045</sup> <sup>1046</sup>"}),
        (55, 0, {"number": "930", "text": "<i>Ṣaḥīḥ Muslim</i> : Lorsqu'on lui demanda : «Jusqu'à quel terme as-tu prêté serment d'allégeance au Messager d'Allah (s) le jour de Ḥudaybiya ?», Salama ibn al-Akwa' répondit : «Jusqu'à la mort.»<sup>1047</sup>"}),
        (55, 1, {"number": "931", "text": "L'Imām al-Jawād (as) a dit : La façon dont les femmes prêtaient serment d'allégeance au Prophète (s) était la suivante : il immergeait sa main dans un récipient rempli d'eau et la retirait. Ensuite, les femmes immergeaient leurs mains dans ce récipient en signe de leur acceptation et de leur foi en Allah, ainsi que leur reconnaissance de Son messager (s).<sup>1049</sup>"}),
        (55, 2, {"number": "932", "text": "Le Messager d'Allah (s) a dit : Allah ne parlera pas à ces trois personnes : [...] un homme qui prête serment d'allégeance à un Imām uniquement en vue de ce bas-monde, de telle sorte qu'il lui reste fidèle tant qu'il réalise ses désirs, sinon il s'en détourne.<sup>1051</sup>"}),
        (55, 2, {"number": "933", "text": "<i>Biḥār al-Anwār</i> : L'Imām 'Alī (as) a dit : «Il y a en Enfer une ville nommée Ḥaṣīna ; ne me demandez-vous pas ce qu'elle contient ?» Ils demandèrent : «Que contient-elle, ô Prince des croyants ?» Il répondit : «Les mains de ceux qui ont violé leurs engagements.»<sup>1052</sup>"}),
        (55, 2, {"number": "934", "text": "En réponse à une personne qui lui avait demandé «Pour quelle raison as-tu combattu Ṭalḥa et Zubayr ?», l'Imām 'Alī (as) répondit : «Je les ai combattus à cause de la violation du serment d'allégeance qu'ils m'avaient prêté, et de leurs crimes envers mes partisans parmi les croyants.»<sup>1053</sup>"}),
        (55, 2, {"number": "935", "text": "L'Imām al-Riḍā (as) a dit : Celui qui viole un engagement ne sera pas épargné par un destin funeste.<sup>1054</sup>"}),
        (55, 3, {"number": "936", "text": "L'Imām 'Alī (as) a écrit dans sa lettre aux gens de Kūfa lors de son départ de Médine vers Bassora: Les gens m'ont prêté serment d'allégeance sans être contraints ni forcés, mais avec un sens de l'obéissance tout en étant libres.<sup>1055</sup>"})
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
