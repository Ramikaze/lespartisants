import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 58 - LA RÉVOLUTION (Index 59)
    while len(data) <= 59:
        data.append({"title": "58 - LA RÉVOLUTION", "subparts": []})
    part58 = data[59]
    while len(part58['subparts']) <= 2:
        part58['subparts'].append({"title": "...", "hadiths": []})
        
    part58['subparts'][0]['title'] = "La révolution islamique en Orient avant la venue du Douzième Imām (Al-Qā'im) ('aj)"
    part58['subparts'][1]['title'] = "Le rôle des non-arabes dans la révolution"
    part58['subparts'][2]['title'] = "La révolution provenant de la ville de Qom"

    # Part 59 - LE DÉTERMINISME (Index 60)
    while len(data) <= 60:
        data.append({"title": "59 - LE DÉTERMINISME", "subparts": []})
    part59 = data[60]
    while len(part59['subparts']) <= 3:
        part59['subparts'].append({"title": "...", "hadiths": []})
        
    part59['subparts'][0]['title'] = "La fausseté du déterminisme"
    part59['subparts'][1]['title'] = "Ni déterminisme ni liberté totale"
    part59['subparts'][2]['title'] = "A Allah revient en premier lieu le mérite des bonnes actions"
    part59['subparts'][3]['title'] = "La façon dont il faut se comporter envers les partisans du déterminisme"

    updates = [
        # Part 58 - LA RÉVOLUTION (Index 59)
        (59, 0, {"number": "1015", "text": "Le Messager d'Allah (s) a dit : Des hommes émergeront d'Orient et ils prépareront le terrain pour le gouvernement du Mahdī ('aj).<sup>1150</sup>"}),
        (59, 0, {"number": "1016", "text": "<i>Al-Malāḥim wa al-Fitan</i> : 'Abdullāh [ibn 'Abbās] a dit : Alors que nous étions assis auprès du Messager d'Allah (s), un groupe de jeunes qurayshites passa devant nous et son visage pâlit. Nous lui dîmes : «Ô Messager d'Allah (s), nous voyons sur ton visage que quelque chose te déplaît.» Il dit : «En vérité, nous sommes les gens d'une demeure pour qui Allah a choisi l'Au-delà aux dépens de la vie d'ici-bas. Après moi, les gens de ma demeure subiront l'affliction, le bannissement et l'exil jusqu'à ce qu'un groupe de gens sorte de ce lieu (et il fit signe en direction de l'Orient) avec des étendards noirs. Ils réclameront la vérité et elle ne leur sera pas accordée, ils la solliciteront encore et ils ne seront pas exaucés. Alors, ils combattront avec patience, et ce qu'ils ont demandé leur sera accordé. Mais ils refuseront de l'accepter pour eux-mêmes, jusqu'à ce qu'ils le donnent à un homme de ma famille qui remplira la terre d'équité et de justice tout comme elle fut auparavant remplie d'injustice et d'oppression. Que celui qui les atteint se joigne à eux, même s'il faut pour cela ramper sur la neige.»<sup>1151</sup>"}),
        
        (59, 1, {"number": "1017", "text": "L'Imām al-Bāqir (as) a dit : Les compagnons du Qā'im seront au nombre de trois cent treize hommes d'origine non-arabe. Certains parmi eux seront transportés par les nuages durant la journée et seront connus par leur nom, le nom de leur père, leur lignée et décorations, tandis que d'autres seront endormis dans leurs lits et le rencontreront [le Douzième Imām, al-Qā'im] à La Mecque sans rendez-vous spécifique.<sup>1152</sup>"}),
        (59, 1, {"number": "1018", "text": "<i>Sunan al-Tirmidhī</i> : Ṣāliḥ ibn Abī Ṣāliḥ, le serviteur de 'Amrū ibn al Ḥarith, a dit : J'ai entendu Abū Hurayra dire : «J'ai évoqué les non-arabes (<i>a'ājim</i>) en présence du Messager d'Allah (s) et le Messager d'Allah (s) a dit : «La confiance que j'ai en eux ou en certains d'entre eux est plus forte que celle que j'ai en vous ou en certains d'entre vous».»<sup>1153</sup>"}),
        (59, 1, {"number": "1019", "text": "L'Imām 'Alī (s) a dit : Je peux presque voir les non-arabes (<i>a'ājim</i>) établir demeure dans la mosquée de Kūfa, et enseigner le Coran aux gens tel qu'il a été révélé.<sup>1154</sup>"}),
        
        (59, 2, {"number": "1020", "text": "L'Imām al-Ṣādiq (as) a dit : Arrivera un temps où la ville de Qom et ses habitants seront une autorité (<i>ḥujja</i>) pour le reste des gens. Cela se réalisera à partir de l'époque de l'occultation de notre Qā'im (as) jusqu'à sa réapparition. S'il n'en était pas ainsi, la terre engloutirait ses habitants. En vérité, les anges éloignent les malheurs de la ville de Qom et de ses habitants, et aucun tyran ne se dirige vers elle avec une mauvaise intention sans qu'il ne soit anéanti par Celui qui anéantit les tyrans.<sup>1155</sup>"}),
        (59, 2, {"number": "1021", "text": "<i>Biḥār al-Anwār</i> : 'Affān al-Baṣrī a dit: [L'Imām al-Ṣādiq (as)] me demanda : «Sais-tu pourquoi elle s'appelle Qom ?» Je répondis : «Allah, Son Messager et vous, êtes plus savants.» Il (as) dit : «En vérité, elle a été nommée Qom car ses habitants se rassembleront autour du Qā'im, descendant de la famille de Muḥammad - que les prières d'Allah soient sur lui. Ils se dresseront en sa compagnie, resteront avec lui et l'assisteront.»<sup>1156</sup>"}),
        (59, 2, {"number": "1022", "text": "L'Imām al-Kāẓim a dit : Un homme de Qom invitera les gens à la vérité, il sera rejoint par des gens aussi fermes que le fer forgé, que les vents des tempêtes ne feront pas trébucher. Ils ne se fatigueront pas de la guerre et ne feront pas preuve de lâcheté. Ils placeront leur confiance en Allah, et la fin [heureuse] sera pour les pieux.<sup>1157</sup>"}),
        (59, 2, {"number": "1023", "text": "<i>Biḥār al-Anwār</i> : L'un de nos partisans a dit : J'étais assis auprès de l'Imām al-Ṣādiq (as), lorsqu'il récita ce verset : «<i>Lorsque vint l'accomplissement de la première de ces deux [prédictions], Nous envoyâmes contre vous certains de Nos serviteurs doués d'une force terrible, qui pénétrèrent à l'intérieur des demeures. Et la prédiction fut accomplie.</i>»<sup>1158</sup> On lui demanda : «Que nous te soyons sacrifiés, qui sont-ils ?» Et il répondit trois fois : «Par Allah, ce sont les gens de Qom.»<sup>1159</sup>"}),

        # Part 59 - LE DÉTERMINISME (Index 60)
        (60, 0, {"number": "1024", "text": "L'Imām 'Alī (as) a dit au sujet de la fausseté du déterminisme : S'il en était ainsi, la récompense et le châtiment seraient non fondés et erronés, de même que l'ordre, l'interdiction, et le fait de proscrire les mauvais actes ; [de même] la promesse [du Paradis] et la menace [de l'Enfer] seraient dénuées de sens. Le pécheur ne pourrait être réprimandé ni le bienfaiteur loué ; mais [au contraire], le bienfaiteur mériterait davantage de réprimandes que le malfaiteur, et le malfaiteur mériterait plus de gratifications que le bienfaiteur. [Les croyances au déterminisme] sont les paroles des adorateurs d'idoles et des ennemis du Miséricordieux.<sup>1160</sup>"}),
        (60, 0, {"number": "1025", "text": "L'Imām al-Ṣādiq (as) a dit : Les actes pour lesquels tu peux réprimander un serviteur sont de son ressort, et les choses pour lesquelles tu ne peux réprimander un serviteur sont du ressort d'Allah. Allah demandera à Son serviteur: «Pourquoi [M']as-tu désobéi ? Pourquoi as-tu péché ? Pourquoi as-tu bu du vin ? Pourquoi as-tu commis l'adultère ?» Car cela est du ressort du serviteur, mais Il ne lui demandera pas : «Pourquoi es-tu tombé malade ? Pourquoi es-tu petit de taille ? Pourquoi es-tu blanc de peau ? Pourquoi es-tu noir de peau ? Car cela est du ressort d'Allah le Tout-Puissant.»<sup>1161</sup>"}),
        (60, 0, {"number": "1026", "text": "L'Imām al-Kāẓim (as) a dit : Les péchés ne peuvent provenir que de l'un de ces trois cas: soit ils viennent d'Allah - ce qui n'est pas le cas-, car il ne sied pas au Seigneur de châtier un serviteur pour un acte qu'il n'a pas commis ; soit ils viennent d'Allah et du serviteur ensemble - ce n'est pas ainsi -, car il ne sied pas à un associé fort d'opprimer un associé faible ; soit ils viennent du serviteur, - ce qui est le cas - ; par conséquent, si Allah pardonne, c'est en raison de Sa bonté et de Sa magnanimité, et s'Il punit, c'est en raison du péché du serviteur et de ses crimes.<sup>1162</sup>"}),
        
        (60, 1, {"number": "1027", "text": "<i>Al-Tawḥīd</i> : L'Imām al-Bāqir (as) et l'Imām al-Ṣādiq (as) ont dit : «En vérité, Allah le Tout-Puissant est trop Miséricordieux envers Ses créatures pour les contraindre à commettre un péché et les punir ensuite pour cela, et Allah est trop puissant pour vouloir une chose sans qu'elle ne se réalise.» On lui demanda alors : «Est-ce qu'entre le déterminisme et la liberté totale, il existe une troisième situation ?» Il répondit : «Oui, [une situation] plus vaste que la distance entre le ciel et la terre.»<sup>1163</sup>"}),
        (60, 1, {"number": "1028", "text": "<i>Biḥār al-Anwār</i> : Al-Mufaḍḍal rapporte que l'Imām al-Ṣādiq (as) a dit : «Ni déterminisme, ni liberté totale, mais une situation entre les deux.» Il [al-Mufaḍḍal] demanda : «Quelle est donc la situation entre les deux ?» Il répondit : «Cela est semblable à un homme que tu vois en train de commettre un péché et que tu dissuades. Cependant, il ne t'écoute pas ; par conséquent, tu le laisses à son péché. Le laisser à son péché après qu'il ait rejeté ton conseil ne signifie pas que c'est toi qui lui a ordonné de pécher.»<sup>1164</sup>"}),
        
        (60, 2, {"number": "1029", "text": "L'Imām al-Riḍā (as) a dit : Allah le Très-Haut a dit : «Ô fils d'Adam ! Par Ma volonté, tu as été doté de volonté, par Ma grâce, tu as pu t'acquitter des obligations envers Moi, par Ma puissance, tu as été doté de puissance et a pu Me désobéir. Je t'ai créé voyant et entendant, Je suis donc plus méritant et digne de tes bonnes actions que tu ne l'es toi-même, et tu mérites plus tes mauvaises actions que Moi-même.»<sup>1165</sup>"}),
        
        (60, 3, {"number": "1030", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui prétend qu'Allah contraint Ses serviteurs à la désobéissance ou bien qu'Il leur impose ce qu'ils ne peuvent supporter, ne mangez pas les bêtes qu'il a sacrifiées, n'acceptez pas son témoignage, ne faites pas la prière derrière lui et ne lui donnez pas une part de l'aumône (<i>zakāt</i>).<sup>1166</sup>"})
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
