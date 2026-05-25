import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(pi, ss):
    for s in data[pi].get('subparts', []):
        if ss in s['title']:
            return s
    return None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# Part 152 (index 153) - L'OSTENTATION (cont.)
# ============================================================
p152 = 153

s786 = find_subpart(p152, "786"); eh(s786)
s786['hadiths'].extend([
    {
        "number": "2478",
        "text": "Mustadrak al-Wasā'il : Le Messager d'Allah (s) a dit : «En vérité, le Feu et ses occupants enragent contre les personnes ayant fait preuve d'ostentation.» On lui demanda : «Ô Messager d'Allah ! Pour quelle raison le Feu se maint-il ?!» Il répondit : «En raison de la chaleur du feu par lequel ils sont châtiés.»<sup>2799</sup>"
    },
    {
        "number": "2479",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour du Jugement, un serviteur qui avait l'habitude de prier sera amené et il dira : «Ô Seigneur ! J'ai prié pour Toi et pour obtenir Ton agrément !» Et il lui sera dit : «Tu as plutôt prié pour que l'on dise que ta prière était belle. Emmenez-le donc au Feu.»<sup>2800</sup>"
    }
])

s787 = find_subpart(p152, "787"); eh(s787)
s787['hadiths'].extend([
    {
        "number": "2480",
        "text": "L'Imām 'Alī (as) a dit : La personne qui fait preuve d'ostentation a trois traits caractéristiques : elle s'active quand elle voit les gens, elle devient paresseuse lorsqu'elle est seule, et elle aime être congratulée pour tous ses actes.<sup>2801</sup>"
    }
])

s788 = find_subpart(p152, "788"); eh(s788)
s788['hadiths'].extend([
    {
        "number": "2481",
        "text": "Le Messager d'Allah (s) a dit : Réaliser [des actes d'adoration et des bonnes actions] en secret est meilleur que de le faire en public, [excepté] si on le fait pour donner l'exemple.<sup>2802</sup>"
    },
    {
        "number": "2482",
        "text": "Lorsqu'il fut interrogé par Zurāra au sujet d'un homme qui accomplit une bonne action, est vu par autrui et s'en réjouit, l'Imām al-Bāqir (as) dit : Il n'y a aucun mal à cela ; toute personne aime apparaître aux autres comme une bonne personne, à condition qu'à la base elle n'ait pas accompli cette action dans ce but.<sup>2803</sup>"
    },
    {
        "number": "2483",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui accomplit une bonne action en secret, elle lui sera inscrite en tant que «secrète». S'il déclare l'avoir faite, elle sera effacée et inscrite comme «publique». Et s'il la déclare une seconde fois, elle sera effacée et inscrite comme «ostentatoire».<sup>2804</sup>"
    }
])

# ============================================================
# Part 153 (index 154) - L'OPINION (2484-2497)
# ============================================================
p153 = 154

s789 = find_subpart(p153, "789"); eh(s789)
s789['hadiths'].extend([
    {
        "number": "2484",
        "text": "L'Imām 'Alī (as) a dit : L'opinion [juste] vient d'un jugement équilibré, alors que l'opinion irréfléchie et hâtive est véritablement un mauvais appui.<sup>2805</sup>"
    },
    {
        "number": "2485",
        "text": "L'Imām 'Alī (as) a dit : Échangez vos opinions les uns avec les autres, et celle qui est juste en émergera.<sup>2806</sup>"
    },
    {
        "number": "2486",
        "text": "L'Imām 'Alī (as) a dit : Celui qui fait bon accueil aux divers aspects d'une opinion [aux différentes opinions] saura où résident les erreurs.<sup>2807</sup>"
    },
    {
        "number": "2487",
        "text": "L'Imām 'Alī (as) a dit : La personne qui a la meilleure opinion est celle qui ne rejette pas l'avis d'un conseiller.<sup>2808</sup>"
    }
])

s790 = find_subpart(p153, "790"); eh(s790)
s790['hadiths'].extend([
    {
        "number": "2488",
        "text": "L'Imām 'Alī (as) a dit : Celui qui s'obstine à suivre sa propre opinion sera anéanti. En revanche, celui qui consulte les autres aura une part de leur compréhension.<sup>2809</sup>"
    },
    {
        "number": "2489",
        "text": "L'Imām 'Alī (as) a dit : Seul l'ignorant est fier de sa propre opinion.<sup>2810</sup>"
    },
    {
        "number": "2490",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui s'obstine à suivre sa propre opinion l'a basée sur un argument peu solide et erroné.<sup>2811</sup>"
    }
])

s791 = find_subpart(p153, "791"); eh(s791)
s791['hadiths'].extend([
    {
        "number": "2491",
        "text": "L'Imām 'Alī (as) a dit : Insister obstinément sur son opinion la détruit.<sup>2812</sup>"
    },
    {
        "number": "2492",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le reclus n'a pas d'opinion.<sup>2813</sup><br>(Voir également : 352. L'entêtement)"
    }
])

s792 = find_subpart(p153, "792"); eh(s792)
s792['hadiths'].extend([
    {
        "number": "2493",
        "text": "L'Imām 'Alī (as) a dit : La justesse des opinions change avec les gouvernements. Lorsqu'un nouveau gouvernement entre en scène, il en va de même de son opinion [qui est acceptée comme valide] et quand il part, elle part avec lui.<sup>2814</sup>"
    }
])

s793 = find_subpart(p153, "793"); eh(s793)
s793['hadiths'].extend([
    {
        "number": "2494",
        "text": "Le Messager d'Allah (s) a dit : Cette communauté agira pendant un moment en s'appuyant sur le Livre d'Allah. Par la suite, elle agira selon la pratique (sunna) du Messager d'Allah et après, elle agira selon sa propre opinion. Et lorsque les gens agiront selon leur propre opinion, ils s'égareront et égareront les autres.<sup>2815</sup>"
    },
    {
        "number": "2495",
        "text": "Kanz al-'Ummāl : L'Imām 'Alī (as) a dit : «Un acte n'est pas accepté s'il est accompagné de l'une de ces trois choses : l'associationnisme, la mécréance et l'opinion.» Ils demandèrent : «Ô Emir des croyants, que signifie l'opinion ?» Il répondit : «Abandonner le Livre d'Allah ainsi que la pratique (sunna) de Son Messager, et agir selon sa propre opinion.»<sup>2816</sup>"
    }
])

s794 = find_subpart(p153, "794"); eh(s794)
s794['hadiths'].extend([
    {
        "number": "2496",
        "text": "Le Messager d'Allah (s) a dit : Si le dirigeant s'efforce avec sincérité d'atteindre une bonne opinion et qu'il juge de façon juste, il sera récompensé par deux rétributions. En revanche, s'il s'est efforcé avec sincérité dans cette voie et s'est trompé, il aura tout de même une rétribution [pour son effort].<sup>2817</sup>"
    },
    {
        "number": "2497",
        "text": "L'Imām 'Alī (as) a dit : Celui qui s'est efforcé avec sincérité en vue de conseiller les gens sera récompensé selon son intention et il aura rempli son devoir.<sup>2818</sup>"
    }
])

# ============================================================
# Part 154 (index 155) - L'USURE (2498-2507)
# ============================================================
p154 = 155

s795 = find_subpart(p154, "795"); eh(s795)
s795['hadiths'].extend([
    {
        "number": "2498",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah le Tout-Puissant maudit le bénéficiaire de l'usure, celui qui la donne, celui qui la consigne par écrit et ceux qui en sont les témoins.<sup>2819</sup>"
    },
    {
        "number": "2499",
        "text": "Le Messager d'Allah (s) a dit : Lors de mon ascension céleste (mi'rāj), j'ai été amené auprès d'hommes dont le ventre était aussi gros qu'une maison et rempli de serpents visibles de l'extérieur. Je demandai alors : «Qui sont ces gens, ô Gabriel ?» Il répondit : «Ce sont les usuriers.»<sup>2820</sup>"
    },
    {
        "number": "2500",
        "text": "L'Imām al-Bāqir (as) a dit : Le plus vil des gains est celui issu de l'usure.<sup>2821</sup>"
    },
    {
        "number": "2501",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'usurier ne quittera pas ce monde avant d'avoir été rendu fou par Satan.<sup>2822</sup>"
    },
    {
        "number": "2502",
        "text": "L'Imām al-Ṣādiq (as) a dit : Un dirham gagné par l'usure est plus grave aux yeux d'Allah le Tout-Puissant que soixante-dix incestes commis au sein de la Demeure sacrée d'Allah.<sup>2823</sup>"
    }
])

s796 = find_subpart(p154, "796"); eh(s796)
s796['hadiths'].extend([
    {
        "number": "2503",
        "text": "Lorsque Hishām ibn al-Ḥakam l'interrogea sur la raison de l'interdiction de l'usure, l'Imām al-Ṣādiq (as) répondit : Si l'usure était licite, les gens délaisseraient le commerce et tout ce dont ils ont besoin. Allah a donc interdit l'usure afin que les hommes s'éloignent des [moyens de subsistance] illicites et qu'ils aient recours au commerce, à l'achat et à la vente, et que cela facilite à son tour les prêts entre eux.<sup>2824</sup>"
    },
    {
        "number": "2504",
        "text": "Lorsqu'il fut interrogé sur la raison de l'interdiction de l'usure, l'Imām al-Ṣādiq (as) répondit : Afin que les hommes ne soient pas réticents à faire preuve de courtoisie les uns vis-à-vis des autres.<sup>2825</sup>"
    }
])

s797 = find_subpart(p154, "797"); eh(s797)
s797['hadiths'].extend([
    {
        "number": "2505",
        "text": "L'Imām 'Alī (as) a dit : Engagez-vous d'abord dans des relations communes avec les gens, puis [apprenez] la loi, et ensuite [seulement] faites du commerce, car par Allah, l'usure se glisse plus discrètement au sein de cette communauté que la fourmi qui se faufile sur la roche noire.<sup>2826</sup>"
    },
    {
        "number": "2506",
        "text": "L'Imām 'Alī (as) a dit : Celui qui commerce sans connaître les lois à ce sujet sera impliqué dans l'usure.<sup>2827</sup><br>(Voir également : 55. Le commerce, section 285)"
    }
])

s798 = find_subpart(p154, "798"); eh(s798)
s798['introduction'] = (
    "«<i>Ô vous qui croyez ! Craignez Allah et renoncez au reliquat de l'intérêt usuraire, si vous "
    "êtes croyants. Et si vous ne le faites pas, alors recevez l'annonce d'une guerre de la part "
    "d'Allah et de Son messager. Et si vous vous repentez, vous aurez vos capitaux. Vous ne "
    "lèserez personne, et vous ne serez point lésés.</i>»<sup>2828</sup>"
)
s798['hadiths'].extend([
    {
        "number": "2507",
        "text": "Lorsqu'il apprit qu'un homme consommait de l'usure et qu'il appelait cela liba<sup>2829</sup> [pour s'en justifier], l'Imām al-Ṣādiq (as) a dit : Si Allah le Tout-Puissant m'en donnait le pouvoir, je lui ferais couper le cou.<sup>2830</sup>"
    }
])

# ============================================================
# Part 155 (index 156) - L'ESPOIR (2508-2511)
# ============================================================
p155 = 156

s799 = find_subpart(p155, "799"); eh(s799)
s799['introduction'] = (
    "«<i>Certes, ceux qui ont cru, émigré et lutté dans le sentier d'Allah, ceux-là espèrent la "
    "miséricorde d'Allah. Et Allah est Pardonneur et Miséricordieux.</i>»<sup>2831</sup>"
)
s799['hadiths'].extend([
    {
        "number": "2508",
        "text": "L'Imām 'Alī (as) a dit : L'homme qui espère est en quête, et l'homme apeuré est en fuite.<sup>2832</sup>"
    },
    {
        "number": "2509",
        "text": "L'Imām 'Alī (as) a dit en s'adressant à un homme qui lui avait demandé conseil : Ne sois pas de celui qui espère l'Au-delà sans actes, qui remet à plus tard son repentir à cause de hauts espoirs, et qui parle comme les ascètes de la vie de ce monde, alors qu'il se comporte en pratique comme ceux qui la convoitent.<sup>2833</sup>"
    },
    {
        "number": "2510",
        "text": "Interrogé au sujet de gens qui désobéissent [à Allah] tout en disant : «Nous espérons [en la miséricorde divine]», puis restent dans cet état jusqu'à ce que la mort leur vienne, l'Imām al-Ṣādiq (as) répondit : «Ceux-là sont balancés et oscillent entre leurs désirs. Ils mentent et ne sont pas réellement de ceux qui espèrent, car celui qui espère une chose la cherche, tandis que celui qui a peur d'une chose la fuit.»<sup>2834</sup>"
    }
])

s800 = find_subpart(p155, "800"); eh(s800)
s800['hadiths'].extend([
    {
        "number": "2511",
        "text": "L'Imām 'Alī (as) a dit : Placez tous vos espoirs en Allah - loué soit-Il -, et ne les placez pas en un autre que Lui, car toute personne plaçant ses espoirs en un autre qu'Allah échouera.<sup>2835</sup><br>(Voir également : 181. La demande (2), section 908 ; 417. Le désespoir, section 1907)"
    }
])

# ============================================================
# Part 156 (index 157) - LE RETOUR (2512-2515)
# ============================================================
p156 = 157

s801 = find_subpart(p156, "801"); eh(s801)
s801['hadiths'].extend([
    {
        "number": "2512",
        "text": "L'Imām al-Ṣādiq (as) a dit : Par Allah, les jours et les nuits ne prendront pas fin avant qu'Allah fasse revenir les morts, qu'Il donne la mort aux vivants, qu'Il rende les droits aux ayant-droits et qu'Il établisse la religion qu'Il a choisie pour Lui-même.<sup>2837</sup>"
    }
])

s802 = find_subpart(p156, "802"); eh(s802)
s802['hadiths'].extend([
    {
        "number": "2513",
        "text": "L'Imām Ḥusayn (as) a dit : Je serai le premier à émerger au moment où la terre se fendra. Je sortirai au même moment que l'Emir des croyants et la manifestation de notre Qa'im.<sup>2838</sup>"
    },
    {
        "number": "2514",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le premier à revenir dans ce monde sera Ḥusayn ibn 'Alī (as), et il lui sera donné de régner jusqu'à ce que ses sourcils, de vieillesse, tombent sur ses yeux.<sup>2839</sup>"
    }
])

s803 = find_subpart(p156, "803"); eh(s803)
s803['hadiths'].extend([
    {
        "number": "2515",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, le Retour ne sera pas général mais spécifique. Ne seront ressuscités que ceux ayant une foi absolument pure ou faisant preuve d'un associationnisme pur.<sup>2840</sup>"
    }
])

# ============================================================
# Part 157 (index 158) - LA COMPASSION (2516-2522)
# ============================================================
p157 = 158

s804 = find_subpart(p157, "804"); eh(s804)
s804['introduction'] = (
    "«<i>Muhammad est le Messager d'Allah. Et ceux qui sont avec lui sont durs envers les "
    "mécréants, miséricordieux entre eux.</i>»<sup>2842</sup><br>"
    "«<i>Et c'est être, en outre, de ceux qui croient et s'enjoignent mutuellement la patience "
    "et s'enjoignent mutuellement la miséricorde. Ceux-là sont les gens de la droite.</i>»<sup>2843</sup>"
)
s804['hadiths'].extend([
    {
        "number": "2516",
        "text": "Le Messager d'Allah (s) a dit : Le Très-Miséricordieux et le Très-Haut fait preuve de miséricorde envers ceux qui sont compatissants et miséricordieux [vis-à-vis des autres]. Faites preuve de compassion sur terre, et Celui qui est dans le ciel fera preuve de compassion envers vous.<sup>2844</sup>"
    },
    {
        "number": "2517",
        "text": "Le Messager d'Allah (s) a dit : Dans le Feu, un appel sera lancé par l'un de ses résidents : «Ô Tendre, ô Donateur, Sauve-moi du Feu!» Allah ordonnera alors à un ange de le faire sortir et de l'amener devant Lui. Allah le Tout-Puissant dira alors : «As-tu un jour fait preuve de compassion envers un oiseau ?»<sup>2845</sup>"
    },
    {
        "number": "2518",
        "text": "L'Imām 'Alī (as) a dit : Sois compatissant, et on fera preuve de compassion envers toi.<sup>2846</sup>"
    },
    {
        "number": "2519",
        "text": "L'Imām 'Alī (as) a dit : Je suis étonné de celui qui espère la compassion de Celui qui est au-dessus de lui et qui ne fait pas lui-même preuve de compassion vis-à-vis de celui qui est en dessous de lui.<sup>2847</sup>"
    }
])

s805 = find_subpart(p157, "805"); eh(s805)
s805['hadiths'].extend([
    {
        "number": "2520",
        "text": "Le Messager d'Allah (s) a dit : Soyez compatissants envers une personne puissante qui a été déshonorée, un riche devenu pauvre, et un savant oublié au milieu d'une génération d'ignorants.<sup>2848</sup>"
    },
    {
        "number": "2521",
        "text": "Le Messager d'Allah (s) a dit : Soyez compatissants envers les pauvres.<sup>2849</sup>"
    },
    {
        "number": "2522",
        "text": "L'Imām 'Alī (as) a dit : Sois compatissant envers le plus jeune de ta famille et respectueux envers le plus âgé.<sup>2850</sup>"
    }
])

# ============================================================
# Part 158 (index 159) - LA MISÉRICORDE (2523)
# ============================================================
p158 = 159

s806 = find_subpart(p158, "806"); eh(s806)
s806['hadiths'].extend([
    {
        "number": "2523",
        "text": "Le Messager d'Allah (s) a dit : En vérité, le jour où Il a créé les cieux et la terre, Allah le Très-Haut a créé cent miséricordes. Chaque miséricorde correspond à tout ce qui est entre le ciel et la terre. Parmi elles, Il a fait descendre une miséricorde sur terre et c'est elle qui fait que les créatures sont compatissantes et miséricordieuses entre elles, c'est par elle que la mère a de la tendresse envers son enfant, par elle que les oiseaux et les fauves peuvent s'abreuver d'eau, et par elle que toutes les créatures vivent.<sup>2851</sup>"
    }
])

# ============================================================
# Sequential Sorting for all modified subparts
# ============================================================
modified_sections = [
    (p152, "786"), (p152, "787"), (p152, "788"),
    (p153, "789"), (p153, "790"), (p153, "791"), (p153, "792"), (p153, "793"), (p153, "794"),
    (p154, "795"), (p154, "796"), (p154, "797"), (p154, "798"),
    (p155, "799"), (p155, "800"),
    (p156, "801"), (p156, "802"), (p156, "803"),
    (p157, "804"), (p157, "805"),
    (p158, "806")
]

for p_idx, s_title in modified_sections:
    s = find_subpart(p_idx, s_title)
    if s and 'hadiths' in s:
        s['hadiths'].sort(key=lambda h: int(h['number']))
        print(f"Sorted Subpart {s_title} (Part index {p_idx}). Hadiths: {[h['number'] for h in s['hadiths']]}")

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Data successfully saved! Hadiths 2478-2523 injected.")
