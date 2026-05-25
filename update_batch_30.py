import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()
start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(part_index, search_str):
    for s in data[part_index].get('subparts', []):
        if search_str in s['title']:
            s.setdefault('hadiths', [])
            return s
    return None

# ============================================================
# Part 147 index 148 - Fix hadith 2365 + add 2366-2371
# ============================================================
p147 = 148
s760 = find_subpart(p147, "760")
for h in s760['hadiths']:
    if h['number'] == '2365':
        h['text'] = "L'Imām 'Alī (as) a dit : Il n'y a rien de pire parmi les transgressions que de suivre ses passions ; dès lors, ne leur obéissez pas car elles vous distrairont [et vous empêcheront de pratiquer le rappel] d'Allah.<sup>2669</sup>"
        break
s760['hadiths'].extend([
    {"number": "2366", "text": "L'Imām 'Alī (as) a dit : Tout ce qui distrait du rappel d'Allah est considéré comme un jeu de hasard (<i>maysir</i>).<sup>2670</sup>"},
    {"number": "2367", "text": "L'Imām 'Alī (as) a dit : Tout ce qui distrait du rappel d'Allah vient d'Iblīs.<sup>2671</sup>"},
    {"number": "2368", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, le fait de se remplir le ventre, la faiblesse de la volonté, l'ivresse de la satiété, et l'illusion du pouvoir font partie des choses qui empêchent et retardent la réalisation des [bonnes] actions, et qui font oublier le rappel [d'Allah].<sup>2672</sup>"}
])

s761 = find_subpart(p147, "761")
s761['introduction'] = "«Et quiconque se détourne de Mon rappel mènera certes une vie pleine de gêne, et le Jour de la Résurrection, Nous l'amènerons aveugle au rassemblement. Il dira : «Ô mon Seigneur, pourquoi m'as-Tu amené aveugle alors qu'auparavant je voyais ?» [Allah lui dira] : «De même que Nos Signes t'étaient venus et que tu les as oubliés, ainsi aujourd'hui tu es oublié.»»<sup>2673</sup><br><br>«Quiconque s'aveugle [et s'écarte] du rappel du Tout-Miséricordieux, Nous lui désignons un diable qui devient son compagnon inséparable.»<sup>2674</sup><br><br>«Ne soyez pas comme ceux qui ont oublié Allah; [Allah] leur a fait alors oublier leurs propres personnes ; ceux-là sont les pervers.»<sup>2675</sup>"
s761['hadiths'].extend([
    {"number": "2369", "text": "L'Imām 'Alī (as) a dit : Celui qui oublie Allah - loué soit-Il -, Allah lui fera oublier sa propre personne et Il aveuglera son cœur.<sup>2676</sup>"}
])

s762 = find_subpart(p147, "762")
s762['introduction'] = "«Invoque ton Seigneur en toi-même, avec humilité et crainte, à mi-voix, le matin et le soir, et ne sois pas du nombre des insouciants.»<sup>2677</sup>"
s762['hadiths'].extend([
    {"number": "2370", "text": "Le Messager d'Allah (s) a dit : Le meilleur rappel est le rappel silencieux.<sup>2678</sup>"},
    {"number": "2371", "text": "L'Imām al-Bāqir ou l'Imām al-Ṣādiq (as) a dit : L'ange n'inscrit que ce qu'il entend. Allah le Tout-Puissant a dit : «Invoque ton Seigneur en toi-même.»<sup>2679</sup> Nul ne connaît la récompense de ce rappel intérieur pratiqué par le serviteur, en dehors d'Allah le Très-Haut.<sup>2680</sup>"}
])

# ============================================================
# Part 148 index 149 - LE DÉSHONNEUR (2372-2381)
# ============================================================
p148 = 149
s763 = find_subpart(p148, "763")
s763['hadiths'].extend([
    {"number": "2372", "text": "L'Imām 'Alī (as) a dit : Satisfaites-vous de peu plutôt que de vous déshonorer [en mendiant].<sup>2681</sup>"},
    {"number": "2373", "text": "L'Imām 'Alī (as) a dit : La mort est préférable à une vie de déshonneur, et une vie frugale est préférable au fait de quémander ici et là.<sup>2682</sup>"},
    {"number": "2374", "text": "L'Imām 'Alī (as) a dit : Une heure de déshonneur ne pourra jamais être compensée par une vie entière d'honneur.<sup>2683</sup>"},
    {"number": "2375", "text": "L'Imām 'Alī (as) a dit dans l'un de ses entretiens intimes [avec Allah] : Ô Allah ! Fais que mon âme soit la première chose chère que Tu m'arracheras, et le premier dépôt que Tu reprendras parmi tous les bienfaits que Tu m'as confiés.<sup>2684</sup>"},
    {"number": "2376", "source": "Al-Manāqib li-Ibn Shahr Āshūb", "text": "L'Imām Ḥusayn (as) a dit : «Une mort digne est meilleure qu'une vie de déshonneur». Il a récité les vers suivants le jour de son martyre : «La mort vaut mieux que de s'embarquer dans [une vie] de déshonneur, Et le déshonneur est préférable à l'entrée dans le Feu, Par Allah, je ne me permettrai ni l'un, ni l'autre.»<sup>2685</sup>"}
])

s764 = find_subpart(p148, "764")
s764['hadiths'].extend([
    {"number": "2377", "text": "Le Messager d'Allah (s) a dit : Celui qui accepte le déshonneur de façon docile et consentie ne fait pas partie de nous, les Gens de la demeure (<i>Ahl al-Bayt</i>).<sup>2686</sup>"},
    {"number": "2378", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut a confié toute chose au croyant, sauf [ce qui cause] son déshonneur.<sup>2687</sup>"},
    {"number": "2379", "source": "Mishkat al-Anwār", "text": "Dāwūd al-Raqqī : J'ai entendu l'Imām al-Ṣādiq (as) dire : «Il ne convient pas à un croyant de se déshonorer.» Il lui fut demandé : «Comment se déshonore-t-il ?» Il dit : «Il entreprend d'obtenir ce qui est au-delà de son contrôle, et il [finit par se] déshonorer.»<sup>2688</sup>"}
])

s765 = find_subpart(p148, "765")
s765['hadiths'].extend([
    {"number": "2380", "text": "Le Messager d'Allah (s) a dit : Quand les gens seront avares de leurs dinars et dirhams, concluront leurs affaires seulement pour obtenir une grande rentabilité, qu'ils seront trop occupés à courir derrière leur bétail, et qu'ils auront délaissé le <i>jihād</i> sur le sentier d'Allah, Allah fera descendre sur eux un déshonneur qui ne sera levé que lorsqu'ils reviendront à leur religion.<sup>2689</sup>"},
    {"number": "2381", "text": "Le Messager d'Allah (s) a dit : La plus déshonorée des personnes est celle qui offense les autres.<sup>2690</sup>"}
])
# NOTE: hadiths 2382-2388 (page 424 manquante) seront ajoutés ultérieurement

# ============================================================
# Part 149 index 150 - LE PÉCHÉ (2389-2448)
# ============================================================
p149 = 150
s766 = find_subpart(p149, "766")
s766['hadiths'].extend([
    {"number": "2389", "text": "L'Imām 'Alī (as) a dit : Je suis étonné de ceux qui s'abstiennent de [certaines] nourritures de peur qu'elles leur soient nuisibles ; comment ne s'abstiennent-ils pas des péchés de peur du Feu ?!<sup>2700</sup>"},
    {"number": "2390", "text": "L'Imām 'Alī (as) a dit : Même si Allah n'avait pas établi de punitions et de menaces pour les actes de désobéissance commis à Son égard, il resterait obligatoire de ne pas Lui désobéir, par gratitude pour Ses grâces.<sup>2701</sup>"},
    {"number": "2391", "text": "L'Imām 'Alī (as) a dit : S'abstenir des mauvaises actions est préférable au fait de réaliser des bonnes actions.<sup>2702</sup>"},
    {"number": "2392", "text": "L'Imām al-Kāẓim (as) a dit : En vérité, les gens raisonnables ont abandonné les excès de la vie de ce monde, mais qu'en est-il des péchés ?! Délaisser [les excès de] la vie terrestre est [simplement] une vertu, alors qu'abandonner les péchés est une obligation.<sup>2703</sup>"},
    {"number": "2393", "source": "Biḥār al-Anwār", "text": "Les Imāms (as) ont dit : Appliquez-vous et déployez vos efforts, et si vous ne parvenez pas à faire de [bonnes] actions, au moins, ne commettez pas de péchés, car en vérité, celui qui construit [continuellement] et qui ne détruit pas [en même temps] verra sa construction s'élever même si elle est simple et sans ornements, alors que celui qui construit et détruit ne verra jamais ce qu'il construit s'élever.<sup>2704</sup>"}
])

s767 = find_subpart(p149, "767")
s767['hadiths'].extend([
    {"number": "2394", "text": "L'Imām 'Alī (as) a dit : Désobéir ouvertement à Allah - loué soit-Il - hâte [S]a colère.<sup>2705</sup>"},
    {"number": "2395", "text": "L'Imām al-Riḍā (as) a dit : Celui qui commet une mauvaise action ouvertement sera déshonoré [par Allah], et celui qui dissimule son péché [en en ayant honte] sera pardonné [par Allah].<sup>2706</sup>"}
])

s768 = find_subpart(p149, "768")
s768['hadiths'].extend([
    {"number": "2396", "text": "L'Imām 'Alī (as) a dit : Le plus grave des péchés est celui qui est pris à la légère par son auteur.<sup>2707</sup>"},
    {"number": "2397", "text": "L'Imām 'Alī (as) a dit : Le plus grand des péchés auprès d'Allah est celui qui est perpétré avec persistance par son auteur.<sup>2708</sup>"},
    {"number": "2398", "text": "L'Imām al-Bāqir (as) a dit : Tous les péchés sont graves, mais les plus graves sont ceux qui entraînent la croissance de la chair et du sang [par des revenus illicites].<sup>2709</sup>"}
])

s769 = find_subpart(p149, "769")
s769['introduction'] = "«Certes Allah ne pardonne pas qu'on Lui donne quelque associé. A part cela, Il pardonne à qui Il veut. Mais quiconque donne à Allah quelque associé commet un énorme péché.»<sup>2710</sup>"
s769['hadiths'].extend([
    {"number": "2399", "text": "Le Messager d'Allah (s) a dit : On peut se repentir de tout péché sauf du mauvais caractère car en vérité, à chaque fois que [la personne ayant mauvais caractère] se délivre d'un péché, elle en commet instantanément un autre.<sup>2711</sup>"},
    {"number": "2400", "text": "Le Messager d'Allah (s) a dit : Prenez garde aux péchés impardonnables [comme le fait de] s'approprier un butin [ou des bénéfices], car celui qui s'approprie un butin sera amené avec lui le Jour du Jugement, et [il en va de même de] la consommation de l'usure, car celui qui consomme l'usure sera ressuscité [de sa tombe] comme celui que le touché de Satan a bouleversé.<sup>2712</sup>"},
    {"number": "2401", "text": "L'Imām 'Alī (as) a dit : Parmi les décrets certains d'Allah dans le Sage Rappel [le Coran]... figure le fait qu'il est vain pour le serviteur de faire des efforts sur lui-même et en agir sincèrement si, lorsqu'il quitte ce monde pour rencontrer son Seigneur, il a commis l'un de ces actes sans s'être repenti : il a associé un autre à Allah dans ses adorations obligatoires ; il a assouvi sa colère en tuant quelqu'un ; il a déshonoré les autres [en révélant] un acte qu'ils ont commis ; il a recherché à satisfaire l'un de ses besoins en introduisant une innovation dans sa religion ; il a rencontré les gens avec un double visage ; ou il les a fréquentés en ayant un double langage.<sup>2713</sup>"},
    {"number": "2402", "text": "L'Imām al-Bāqir (as) a dit : Parmi les péchés impardonnables, figure le fait que l'homme dise : «Si seulement je n'étais puni que pour cela!» (c'est-à-dire considérer le péché comme si petit que l'on s'imagine que l'on pourra aisément en supporter la punition).<sup>2714</sup>"}
])

s770 = find_subpart(p149, "770")
s770['hadiths'].extend([
    {"number": "2403", "text": "L'Imām 'Alī (as) a dit : Prenez garde à [ne pas commettre] d'actes de désobéissance à Allah en secret, car en vérité, le Témoin [de ces actes] est le Juge lui-même.<sup>2715</sup>"},
    {"number": "2404", "text": "L'Imām al-Bāqir (as) a dit : Allah n'accordera aucune attention à celui qui commet des péchés en secret [pensant qu'il peut se cacher de Lui].<sup>2716</sup>"}
])

s771 = find_subpart(p149, "771")
s771['hadiths'].extend([
    {"number": "2405", "text": "Le Messager d'Allah (s) a dit : En vérité, le croyant voit son péché tel un gros rocher au-dessus de lui et il a peur qu'il tombe sur lui. En revanche, le mécréant voit son péché comme un moustique qui lui passe sous le nez.<sup>2717</sup>"},
    {"number": "2406", "text": "Le Messager d'Allah (s) a dit : En vérité, Iblīs est satisfait de vous lorsque vous commettez des petits péchés.<sup>2718</sup>"},
    {"number": "2407", "text": "Le Messager d'Allah (s) a dit : Ne regardez pas la petitesse de vos péchés, regardez plutôt vis-à-vis de qui vous avez fait preuve d'insolence.<sup>2719</sup>"},
    {"number": "2408", "text": "L'Imām 'Alī (as) a dit : Le plus grave des péchés auprès d'Allah – loué soit-Il – est un péché que son auteur considère insignifiant.<sup>2720</sup>"},
    {"number": "2409", "text": "L'Imām al-Bāqir (as) a dit : Il n'y a pas pire malheur que celui de votre indifférence vis-à-vis de vos péchés, et de votre satisfaction vis-à-vis de votre état actuel.<sup>2721</sup>"},
    {"number": "2410", "text": "L'Imām al-Kāẓim (as) a dit : Ne considérez pas vos petits péchés comme insignifiants, car en vérité, les petits péchés s'accumulent et deviennent nombreux [graves].<sup>2722</sup>"},
    {"number": "2411", "text": "L'Imām al-Riḍā (as) a dit : Les petits péchés ouvrent la voie aux grands péchés, et celui qui ne craint pas Allah dans les petites choses ne Le craindra pas dans les grandes.<sup>2723</sup>"}
])

s772 = find_subpart(p149, "772")
s772['introduction'] = "«Si vous évitez les grands péchés qui vous sont interdits, Nous effacerons vos méfaits de votre compte, et Nous vous ferons entrer dans un endroit honorable [le Paradis].»<sup>2724</sup>"
s772['hadiths'].extend([
    {"number": "2412", "text": "Le Messager d'Allah (s) a dit : Les grands péchés sont le fait d'associer une chose à Allah, l'insolence vis-à-vis de ses parents, le crime, et le serment immoral ou licencieux.<sup>2725</sup>"},
    {"number": "2413", "text": "Interrogé au sujet du plus grand des grands péchés, l'Imām 'Alī (as) a dit : Se considérer en sécurité et préservé du stratagème [châtiment] d'Allah, abandonner tout espoir en la magnanimité d'Allah, et perdre espoir en la miséricorde d'Allah.<sup>2726</sup>"},
    {"number": "2414", "text": "L'Imām al-Ṣādiq (as) a dit : Les grands péchés sont au nombre de sept : tuer un croyant intentionnellement, accuser faussement une femme vertueuse [d'adultère], fuir au milieu du combat, revenir à un état de rénégation après la foi, spolier les biens d'un orphelin, consommer l'usure en ayant conscience [de son interdiction], et toute chose pour laquelle Allah a promis le Feu.<sup>2727</sup>"}
])

s773 = find_subpart(p149, "773")
s773['introduction'] = "«Pour ceux qui, s'ils ont commis quelque turpitude ou commis une injustice envers eux-mêmes [en désobéissant à Allah], se souviennent d'Allah et demandent pardon pour leurs péchés – et qui pardonne les péchés sinon Allah ? – et qui ne persistent pas sciemment dans le mal qu'ils ont fait.»<sup>2728</sup>"
s773['hadiths'].extend([
    {"number": "2415", "text": "Le Messager d'Allah (s) a dit : Aucun grand péché ne demeure face à la demande de pardon, et aucun petit péché ne le demeure s'il est commis avec persistance [c'est-à-dire qu'il devient un péché majeur].<sup>2729</sup>"},
    {"number": "2416", "text": "L'Imām al-Bāqir (as) a dit au sujet de la parole d'Allah «qui ne persistent pas sciemment»<sup>2730</sup> : La persistance [dans le péché] est quand le serviteur commet un péché, ne demande pas pardon, et qu'il ne lui vient même pas à l'esprit de se repentir pour cela ; c'est cela la persistance.<sup>2731</sup>"}
])

s774 = find_subpart(p149, "774")
s774['hadiths'].extend([
    {"number": "2417", "text": "L'Imām 'Alī (as) a dit : Allah suscitera le déshonneur de celui qui tire plaisir du fait de commettre des actes de désobéissance vis-à-vis d'Allah.<sup>2732</sup>"},
    {"number": "2418", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Prends garde à ceux qui tirent plaisir de leur péché, car le fait de tirer plaisir d'un péché est plus grave que le fait de le perpétrer.<sup>2733</sup>"}
])

s775 = find_subpart(p149, "775")
s775['hadiths'].extend([
    {"number": "2419", "text": "Le Messager d'Allah (s) a dit : Le péché est [également] une malédiction pour les gens autres que son perpétrateur, [car] s'ils le déshonorent, ils seront affectés [du même péché] ; s'ils le calomnient, ils auront péché et s'ils s'en accommodent, ils deviendront ses associés [dans son péché].<sup>2734</sup>"},
    {"number": "2420", "text": "L'Imām 'Alī (as) a dit : Les larmes ne sont asséchées qu'en raison de la dureté des cœurs, et les cœurs ne sont endurcis qu'en raison de l'abondance des péchés.<sup>2735</sup>"},
    {"number": "2421", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Les péchés qui empêchent la pluie de descendre du ciel sont : les jugements injustes des juges, les faux témoignage, et la dissimulation du témoignage.<sup>2736</sup>"},
    {"number": "2422", "text": "L'Imām al-Bāqir (as) a dit : Lorsque la pluie se raréfie d'année en année, c'est parce qu'Allah la fait descendre où et lorsque qu'Il le veut. Quand des gens Lui désobéissent, Allah le Tout-Puissant éloigne d'eux la pluie qu'Il leur avait destinée.<sup>2737</sup>"},
    {"number": "2423", "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque l'homme commet un péché, un point noir apparaît dans son cœur, et s'il se repent, il s'efface. Par contre, s'il continue [à le commettre], la taille de ce point augmente jusqu'à engloutir tout son cœur. Dès lors, il ne pourra plus jamais réussir.<sup>2738</sup>"},
    {"number": "2424", "text": "L'Imām al-Ṣādiq (as) a dit : Allah n'accorde aucune grâce à un serviteur en la lui reprenant ensuite, à moins qu'il commette un péché par lequel il mérite qu'elle lui soit retirée.<sup>2739</sup>"},
    {"number": "2425", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'homme commet un péché qui le prive de l'accomplissement de la prière de la nuit. Et en vérité, l'acte mauvais s'immisce et affecte son auteur plus rapidement que le couteau affuté [ne pénètre] dans la viande.<sup>2740</sup>"},
    {"number": "2426", "text": "L'Imām al-Ṣādiq (as) a dit : Ceux qui meurent en raison de leurs péchés sont plus nombreux que ceux qui meurent en raison de l'arrivée à échéance de leur vie.<sup>2741</sup>"},
    {"number": "2427", "text": "L'Imām al-Riḍā (as) a dit : Le mensonge des gouverneurs retient l'arrivée de la pluie [à l'endroit où ils gouvernent] ; lorsque le sultan opprime, tout le pays est humilié ; et lorsque l'aumône (<i>zakāt</i>) n'est pas donnée, le bétail meurt.<sup>2742</sup>"}
])

s776 = find_subpart(p149, "776")
s776['hadiths'].extend([
    {"number": "2428", "text": "Le Messager d'Allah (s) a dit : Il y a trois péchés pour lesquels la punition est hâtée [dans ce monde] et n'est pas ajournée à l'Au-delà : l'insolence envers les parents, l'intimidation des gens, et l'ingratitude face à la bonté.<sup>2743</sup>"},
    {"number": "2429", "text": "L'Imām al-Bāqir (as) a dit : [Ceci figure] dans le livre de l'Emir des croyants (as) : L'auteur de ces actes ne mourra qu'après avoir vu leurs conséquences [dans ce monde] : l'intimidation des autres, la rupture des liens familiaux, et le faux serment.<sup>2744</sup>"}
])

s777 = find_subpart(p149, "777")
s777['hadiths'].extend([
    {"number": "2430", "text": "Le Messager d'Allah (s) a dit : Chaque maladie a un remède, et le remède des péchés est la demande de pardon.<sup>2745</sup>"},
    {"number": "2431", "text": "Le Messager d'Allah (s) a dit : Le croyant a soixante-douze voiles. Lorsqu'il commet un péché, un voile se déchire, mais s'il se repent, Allah le lui restitue et lui en donne sept de plus.<sup>2746</sup>"}
])

s778 = find_subpart(p149, "778")
s778['hadiths'].extend([
    {"number": "2432", "text": "<b>1 - La punition dans ce bas-monde :</b> Le Messager d'Allah (s) a dit : Le croyant ou la croyante seront constamment éprouvés par des malheurs dans leurs corps, leur argent et leurs enfants, afin [qu'au moment de leur mort] ils rencontrent Allah sans aucun péché.<sup>2747</sup>"},
    {"number": "2433", "text": "L'Imām 'Alī (as) a dit : Nul serviteur parmi nos partisans (<i>shī'a</i>) ne commet un acte que nous avons interdit sans qu'il soit éprouvé par une affliction dans son argent, ses enfants ou sa propre personne par laquelle il est lavé de ses péchés, et cela afin qu'il rencontre Allah le Tout-Puissant en étant exempt de tout péché. Et s'il lui reste quelque péché après cela, ils seront expiés par la douleur et la difficulté au moment de sa mort.<sup>2748</sup>"},
    {"number": "2434", "text": "L'Imām al-Ṣādiq (as) a dit : Lorsqu'Allah veut du bien à l'un de Ses serviteurs, Il hâte sa punition dans ce bas-monde. En revanche, lorsqu'Allah veut du mal, Il suspend [la punition] de ses péchés pour qu'il s'en acquitte le Jour du Jugement.<sup>2749</sup>"},
    {"number": "2435", "text": "<b>2 - Les maladies :</b> Le Messager d'Allah (s) a dit : La maladie efface les péchés.<sup>2750</sup>"},
    {"number": "2436", "text": "Le Messager d'Allah (s) a dit : La fièvre d'une nuit permet d'expier un an de péchés.<sup>2751</sup>"},
    {"number": "2437", "text": "L'Imām 'Alī (as) a dit : Lorsqu'Allah éprouve un serviteur [par une maladie], ses péchés tombent en proportion de sa maladie.<sup>2752</sup>"},
    {"number": "2438", "text": "L'Imām 'Alī (as) a dit en parlant de la maladie d'un enfant : C'est une expiation pour ses parents.<sup>2753</sup>"},
    {"number": "2439", "text": "<b>3 - Les chagrins :</b> Le Messager d'Allah (s) a dit : Toute fatigue, difficulté ou chagrin qui atteint le croyant, et même les soucis qui le tracassent, sont des moyens par lesquels Allah l'absout de ses péchés.<sup>2754</sup>"},
    {"number": "2440", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, les peines emportent les péchés des musulmans.<sup>2755</sup>"},
    {"number": "2441", "text": "L'Imām al-Riḍā (as) a dit : Aucun des partisans (<i>shī'a</i>) de 'Alī ne perpétue de méfait ou ne commet de péché le matin sans qu'il ne soit atteint par un chagrin qui fait disparaître son méfait de la même façon ; et puisqu'il a commis un péché et que ce chagrin a effacé ce péché, comment le calame [chargé d'inscrire les péchés de cette personne] pourrait-il se mettre en marche ?!<sup>2756</sup>"},
    {"number": "2442", "text": "<b>4 - Les bonnes actions :</b> «Et accomplis la ṣalāt aux deux extrémités du jour et à certaines heures de la nuit. Les bonnes œuvres dissipent les mauvaises. C'est là un rappel pour ceux qui réfléchissent.»<sup>2757</sup> Le Messager d'Allah (s) a dit : Si tu as commis un péché, accomplis une bonne action pour l'effacer.<sup>2758</sup>"},
    {"number": "2443", "text": "<b>5 - Le bon caractère :</b> Le Messager d'Allah (s) a dit : Quatre [qualités], lorsqu'elles sont possédées par une personne, font qu'Allah transformera ses péchés en bonnes actions, même s'il est [noyé] dans le péché de la tête aux pieds : la sincérité [ou l'honnêteté], la pudeur, le bon caractère, et la gratitude.<sup>2759</sup>"},
    {"number": "2444", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le bon caractère fait fondre le péché de la même façon que le soleil fait fondre la glace ; et en vérité, le mauvais caractère gâte les actes de la même façon que le vinaigre gâte le miel.<sup>2760</sup>"},
    {"number": "2445", "text": "<b>6 - Secourir une personne affligée :</b> L'Imām 'Alī (as) a dit : Parmi les choses qui permettent d'expier les péchés majeurs [figure] le fait de secourir l'affligé et d'apporter du réconfort à une personne angoissée.<sup>2761</sup>"},
    {"number": "2446", "text": "<b>7 - La demande de pardon des anges :</b> L'Imām al-Ṣādiq (as) a dit : En vérité, Allah - que Sa gloire soit exaltée - a fait que les anges fassent tomber les péchés de nos partisans (<i>shī'a</i>) de la même façon que le vent fait tomber les feuilles des arbres en automne, et cela [en accord] avec la parole du Tout-Puissant : «[les anges] célèbrent les louanges de leur Seigneur [...] et implorent le pardon pour ceux qui croient.»<sup>2762</sup> Par Allah, ce verset ne désigne que vous [mes partisans].<sup>2763</sup>"},
    {"number": "2447", "text": "<b>8 - Les prosternations fréquentes :</b> L'Imām al-Ṣādiq (as) a dit : Un homme se rendit chez le Messager d'Allah (s) et dit : «Ô Messager d'Allah ! Mes péchés se sont multipliés et [ma réalisation] de [bonnes] actions s'est affaiblie.» Le Messager d'Allah (s) lui dit : «Prosterne-toi de façon fréquente car en vérité, cela fait tomber les péchés de la même façon que le vent fait tomber les feuilles des arbres.»<sup>2764</sup>"},
    {"number": "2448", "text": "<b>9 - Le pèlerinage obligatoire (ḥajj) et le pèlerinage recommandé ('umra) :</b> Le Messager d'Allah (s) a dit : Le pèlerinage recommandé ('umra) permet l'expiation des péchés commis depuis le précédent pèlerinage recommandé effectué. La rétribution du pèlerinage obligatoire (ḥajj) agréé est le Paradis."}
])
# NOTE: hadiths 2449-2453 (page 435 manquante) seront ajoutés ultérieurement

# ============================================================
# Part 150 index 151 - LA DIRECTION (2454-2457)
# ============================================================
p150 = 151
s779 = find_subpart(p150, "779")
s779['hadiths'].extend([
    {"number": "2454", "text": "L'Imām al-Riḍā (as) a dit en parlant d'un homme : «En vérité, il aime le pouvoir.» Puis il (as) dit : «Deux loups avides chassant un mouton séparé de son berger et de son troupeau sont moins dangereux que le fait de rechercher la direction et le pouvoir ne le sont vis-à-vis de la religion du musulman.»<sup>2771</sup>"}
])

s780 = find_subpart(p150, "780")
s780['hadiths'].extend([
    {"number": "2455", "text": "L'Imām 'Alī (as) a dit : Le moyen [nécessaire] pour diriger est la grandeur d'âme.<sup>2772</sup>"},
    {"number": "2456", "text": "L'Imām 'Alī (as) a dit : Celui qui est généreux prévaut et dirige, alors que celui qui a une fortune abondante prend les reines du pouvoir pour lui même.<sup>2773</sup>"},
    {"number": "2457", "text": "L'Imām al-Ṣādiq (as) a dit : J'ai cherché la direction et je l'ai trouvée dans le fait de donner de bons conseils aux serviteurs d'Allah.<sup>2774</sup>"}
])

# ============================================================
# Part 151 index 152 - LE RÊVE (2458-2464)
# ============================================================
p151 = 152
s781 = find_subpart(p151, "781")
s781['hadiths'].extend([
    {"number": "2458", "text": "Le Messager d'Allah (s) a dit au sujet de la parole du Très-Haut : «Il y a pour eux une bonne nouvelle dans la vie d'ici-bas»<sup>2775</sup> : Il s'agit du rêve de bon augure fait par le croyant et par lequel il se voit annoncer une bonne nouvelle dans sa vie de ce monde.<sup>2776</sup>"},
    {"number": "2459", "source": "Biḥār al-Anwār", "text": "Le Messager d'Allah (s) a dit : «Il ne reste de la prophétie [dans la vie des gens] que les bonnes annonces.» Ils lui demandèrent : «Quelles sont les bonnes annonces ?» Il dit : «Le rêve véridique.»<sup>2777</sup>"},
    {"number": "2460", "text": "L'Imām al-Riḍā (as) a dit : En vérité, le Messager d'Allah (s) avait coutume, à son réveil, de demander à ses compagnons : «Y a-t-il des bonnes annonces ?», en voulant dire des rêves.<sup>2778</sup>"}
])

s782 = find_subpart(p151, "782")
s782['hadiths'].extend([
    {"number": "2461", "text": "L'Imām al-Bāqir (as) a dit : En vérité, lorsque les gens dorment, leurs esprits s'envolent vers le ciel. Ainsi, ce que l'esprit voit dans le ciel est vrai, alors que ce qu'il voit dans l'air [entre le ciel et la terre] n'est qu'un amas de rêveries.<sup>2779</sup>"},
    {"number": "2462", "text": "L'Imām al-Ṣādiq (as) a dit : Il existe trois sortes de rêve : une bonne nouvelle d'Allah pour le croyant, un mauvais augure de Satan, et un amas de rêveries.<sup>2780</sup>"}
])

s783 = find_subpart(p151, "783")
s783['hadiths'].extend([
    {"number": "2463", "text": "Le Messager d'Allah (s) a dit : Si l'un de vous fait un bon rêve, qu'il l'interprète et en informe les autres. En revanche, s'il fait un mauvais rêve, il ne doit pas l'interpréter ni en informer les autres.<sup>2781</sup>"},
    {"number": "2464", "text": "Le Messager d'Allah (s) a dit : Le rêve ne doit être raconté qu'à un croyant exempt de jalousie et de méfaits.<sup>2782</sup>"}
])

# ============================================================
# Part 152 index 153 - L'OSTENTATION (2465-2477)
# ============================================================
p152 = 153
s784 = find_subpart(p152, "784")
s784['introduction'] = "«Ne soyez pas comme ceux qui sortirent de leurs demeures pour repousser la vérité et avec ostentation publique, obstruant le chemin d'Allah. Et Allah cerne ce qu'ils font.»<sup>2783</sup>"
s784['hadiths'].extend([
    {"number": "2465", "text": "Le Messager d'Allah (s) a dit : Malheur à ceux qui vendent leur religion pour la vie de ce monde ! Ils revêtent devant les gens une peau de mouton, leur langue est affable et leurs paroles plus douces que le miel, alors que leur cœur est celui du loup. Allah le Très-Haut a dit : «Se font-ils des illusions sur Moi [placent-ils leurs espoirs en Moi en ne faisant rien] ?!»<sup>2784</sup>"},
    {"number": "2466", "text": "Le Messager d'Allah (s) a dit : En vérité, l'ange s'élève avec les actions du serviteur en étant réjoui, mais lorsqu'il se sera élevé avec ses bonnes actions, Allah le Tout-Puissant dira : «Mettez-les dans le Sijjīn<sup>2785</sup>, car ce n'est pas pour Moi qu'il a œuvré.»<sup>2786</sup>"},
    {"number": "2467", "text": "Le Messager d'Allah (s) a dit : Le Jour du Jugement, celui qui a fait preuve d'ostentation sera ainsi appelé : «Ô pervers ! Ô trompeur ! Ô simulateur ! Tes œuvres sont vaines et ta rétribution est nulle. Pars et prends ta rétribution auprès de celui pour qui tu as œuvré.»<sup>2787</sup>"},
    {"number": "2468", "text": "Le Messager d'Allah (s) a dit : Allah - loué soit-Il - a dit : «Je suis le plus riche et auto-suffisant des associés. Ainsi, [que] celui qui a fait une bonne action [pour Moi] puis pour un autre associé que Moi, [sache que] Je n'en ai pas besoin et que Je la laisse à celui à qui il M'a associé.»<sup>2788</sup>"},
    {"number": "2469", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah n'accepte pas un acte qui contient ne serait-ce qu'un atome d'ostentation.<sup>2789</sup>"},
    {"number": "2470", "text": "Lorsqu'un homme demanda au Messager d'Allah (s) : «Ô Messager d'Allah ! En quoi consiste le fait d'être sauvé ?», il (s) répondit : «Dans le fait que le serviteur ne doit pas accomplir un acte d'obéissance à Allah pour les gens.»<sup>2790</sup>"},
    {"number": "2471", "text": "L'Imām 'Alī (as) a dit : Comme est laid l'homme qui a un intérieur malade et une belle apparence !<sup>2791</sup>"},
    {"number": "2472", "text": "L'Imām 'Alī (as) a dit : Ô Allah ! Je me réfugie auprès de Toi afin que mon aspect extérieur n'apparaisse pas beau aux regards des gens alors que l'intérieur de ma personne que je cache soit laid devant Toi, et [je me réfugie auprès de Toi afin de ne pas] me préserver [des péchés] par ostentation des gens alors que tout sur moi, de telle sorte que je me montre aux gens ma bonne apparence et Te laisse les mauvais agissements, en recherchant à me rapprocher de Tes créatures et en m'éloignant de plus en plus de Ta satisfaction.<sup>2792</sup>"},
    {"number": "2473", "text": "L'Imām al-Bāqir (as) a dit : Celui dont l'apparence extérieure est meilleure que son for intérieur verra la balance [et le poids de ses bonnes actions] s'alléger.<sup>2793</sup>"},
    {"number": "2474", "text": "L'Imām al-Ṣādiq (as) a dit : Gare à l'ostentation, car celui qui œuvre pour un autre qu'Allah sera confié par Allah à celui pour qui il a œuvré.<sup>2794</sup>"}
])

s785 = find_subpart(p152, "785")
s785['hadiths'].extend([
    {"number": "2475", "source": "'Uddat al-Dā'ī", "text": "Le Messager d'Allah (s) a dit : «Ce que je crains le plus pour vous est l'associationnisme mineur.» Ils demandèrent : «Quel est l'associationnisme mineur, ô Messager d'Allah ?» Il répondit : «L'ostentation.»<sup>2795</sup>"},
    {"number": "2476", "text": "L'Imām 'Alī (as) a dit : Sachez que même une once d'ostentation est de l'associationnisme.<sup>2796</sup>"},
    {"number": "2477", "text": "L'Imām al-Bāqir (as) a dit : Le Messager d'Allah (s) fut interrogé au sujet de la parole divine «Que celui qui espère donc rencontrer son Seigneur accomplisse de bonnes actions et qu'il n'associe dans son adoration aucun autre à Son Seigneur»<sup>2797</sup> : Il dit alors : «Celui qui accomplit une prière devant les gens par ostentation est un associationniste... et celui qui accomplit tout acte qu'Allah a ordonné devant les gens par ostentation est un associationniste.»<sup>2798</sup>"}
])

# Save
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 30 done: hadiths 2365-2477 added (gaps: 2382-2388 page 424 manquante, 2449-2453 page 435 manquante)")
