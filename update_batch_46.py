import json
import os

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# Helper function to find a subpart globally by its number in the title
def find_subpart_globally(num_str):
    for p_idx, part in enumerate(data):
        for s in part.get('subparts', []):
            if s['title'].startswith(num_str + " ") or f"- {num_str} " in s['title'] or f" {num_str} -" in s['title']:
                return p_idx, s
    return None, None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# Mappings of all 59 contiguous hadiths (Batch 46)
hadiths_to_inject = {
    # -------------------------------------------------------------
    # Part 175 (Index 176) - LE MARIAGE (Continuation & End)
    # -------------------------------------------------------------
    "876": {
        "hadiths": [
            {
                "number": "2795",
                "text": "Le Messager d'Allah (s) a dit : L'Archange Gabriel m'a continuellement apporté tant de conseils au sujet de la femme que j'ai cru que l'on ne pourrait pas divorcer d'elle, sauf pour une perversité manifeste.<sup>3150</sup>"
            },
            {
                "number": "2796",
                "text": "Le Messager d'Allah (s) a dit : Le mari se doit de nourrir sa femme, de la vêtir, et de ne pas se renfrogner face à elle.<sup>3151</sup>"
            },
            {
                "number": "2797",
                "text": "Le Messager d'Allah (s) a dit : La parole de l'homme qui dit à sa femme «je t'aime» ne quittera jamais son cœur.<sup>3152</sup>"
            }
        ]
    },
    "877": {
        "hadiths": [
            {
                "number": "2798",
                "text": "Irshād al-Qulūb : Le Messager d'Allah (s) a dit : Allah ferme sept portes de l'Enfer et ouvre sept portes du Paradis à toute femme qui rend service à son mari pendant sept jours. Elle pourra ainsi y entrer par celle qu'elle souhaitera. Et il (s) a dit : Aucune femme n'apaise la soif de son mari en lui offrant un verre d'eau sans que cela ne soit meilleur pour elle qu'une année de jeûne durant la journée et de prière durant la nuit.<sup>3153</sup>"
            },
            {
                "number": "2799",
                "text": "L'Imām al-Ṣādiq (as) a dit : Umm Salama interrogea le Messager d'Allah (s) au sujet du mérite des femmes lorsqu'elles servent leurs maris. Il répondit : Toute femme qui déplace un objet d'un endroit à un autre dans la maison de son mari dans le but de l'améliorer sera regardée [avec miséricorde] par Allah, et toute personne regardée [avec miséricorde] par Allah ne sera pas châtiée par Lui.<sup>3154</sup>"
            },
            {
                "number": "2800",
                "text": "L'Imām al-Kāẓim (as) a dit : Le jihād de la femme réside dans le fait d'être une bonne épouse pour son mari.<sup>3155</sup>"
            }
        ]
    },
    "878": {
        "hadiths": [
            {
                "number": "2801",
                "text": "Le Messager d'Allah (s) a dit : Si un homme apaise la soif de sa femme, il est rétribué pour cela.<sup>3156</sup>"
            },
            {
                "number": "2802",
                "text": "Le Messager d'Allah (s) a dit : Le fait que l'homme s'asseye en compagnie de sa famille est plus aimé d'Allah le Très-Haut que sa retraite ('i'tikāf) dans ma mosquée.<sup>3157</sup>"
            },
            {
                "number": "2803",
                "text": "Le Messager d'Allah (s) a dit : En vérité, l'homme qui porte une bouchée de nourriture vers la bouche de sa femme is rétribué.<sup>3158</sup>"
            }
        ]
    },
    "879": {
        "hadiths": [
            {
                "number": "2804",
                "text": "Le Messager d'Allah (s) a dit : Si un homme a une femme qui le maltraite, Allah n'accepte pas la prière ni aucune bonne œuvre de cette dernière, même si elle jeûne toute sa vie, jusqu'à ce qu'elle l'aide et le satisfasse... Et le mari subira le même opprobre et châtiment s'il la maltraite et est injuste envers elle.<sup>3159</sup>"
            },
            {
                "number": "2805",
                "text": "L'Imām al-Ṣādiq (as) a dit : Maudite, maudite soit la femme qui maltraite son mari et le met dans un état de détresse ; et heureuse, heureuse soit la femme qui honore son mari, ne le maltraite pas, et lui obéit en tout !<sup>3160</sup>"
            }
        ]
    },
    "880": {
        "hadiths": [
            {
                "number": "2806",
                "text": "Le Messager d'Allah (s) a dit : En vérité, je suis étonné de l'homme qui frappe sa femme alors que c'est lui qui mérite davantage d'être frappé !<sup>3161</sup>"
            },
            {
                "number": "2807",
                "text": "Le Messager d'Allah (s) a dit : Prenez garde au fait qu'Allah le Tout-Puissant et Son Messager désavouent celui qui fait du mal à sa femme jusqu'à ce qu'elle demande le divorce sans compensation.<sup>3162</sup>"
            },
            {
                "number": "2808",
                "text": "L'Imām 'Alī (as) a dit dans son conseil à son fils Ḥasan (as) : Que ta famille ne se sente pas la plus malheureuse à cause de toi.<sup>3163</sup>"
            }
        ]
    },
    "881": {
        "hadiths": [
            {
                "number": "2809",
                "text": "Le Messager d'Allah (s) a dit : Allah accorde à celui qui a patienté face au mauvais caractère de sa femme [pour Allah], une rétribution équivalente à celle accordée à Job (as) pour son malheur pour chaque jour et chaque nuit endurée ; et elle [la femme] aura un fardeau de péchés aussi lourd que des collines de sable pour chaque jour et chaque nuit.<sup>3164</sup>"
            },
            {
                "number": "2810",
                "text": "Le Messager d'Allah (s) a dit : Allah accordera à celle qui patiente face au mauvais caractère de son mari l'équivalent [de la rétribution] d'Āsiya fille de Muzāḥim [l'épouse de Pharaon].<sup>3165</sup>"
            }
        ]
    },
    "882": {
        "hadiths": [
            {
                "number": "2811",
                "text": "Le Messager d'Allah (s) a dit : Il n'y a pas de chose plus bénéfique au croyant après la piété et la crainte révérencielle vis-à-vis d'Allah le Tout-Puissant qu'une épouse vertueuse.<sup>3166</sup>"
            },
            {
                "number": "2812",
                "text": "Le Messager d'Allah (s) a dit : Le meilleur plaisir de ce monde est une épouse vertueuse.<sup>3167</sup>"
            },
            {
                "number": "2813",
                "text": "Le Messager d'Allah (s) a dit : Avoir une épouse vertueuse fait partie du bonheur de l'homme.<sup>3168</sup><br>(Voir également : 137. Le bien, section 672)"
            }
        ]
    },
    "883": {
        "hadiths": [
            {
                "number": "2814",
                "text": "Le Messager d'Allah (s) a dit : Le pire de tout est une mauvaise épouse.<sup>3169</sup>"
            },
            {
                "number": "2815",
                "text": "L'Imām al-Ṣādiq (as) a dit : Le pire ennemi du croyant est une mauvaise épouse.<sup>3170</sup>"
            },
            {
                "number": "2816",
                "text": "L'Imām al-Ṣādiq (as) a dit : L'une des invocations du Messager d'Allah (s) était : «Je cherche refuge auprès de Toi d'une épouse qui ferait blanchir mes cheveux avant terme.»<sup>3171</sup>"
            }
        ]
    },
    "884": {
        "hadiths": [
            {
                "number": "2817",
                "text": "Le Messager d'Allah (s) a dit : Celui qui entre dans un marché et achète un cadeau pour l'apporter à sa famille est comme celui qui apporte des aumônes (ṣadaqa) à un groupe de nécessiteux. Qu'il commence par donner [les cadeaux] aux filles avant les garçons.<sup>3172</sup>"
            },
            {
                "number": "2818",
                "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, celui dont Allah est le plus satisfait est celui qui comble le plus sa famille.<sup>3173</sup>"
            }
        ]
    },
    "885": {
        "hadiths": [
            {
                "number": "2819",
                "text": "Le Messager d'Allah (s) a dit : Si vous êtes conviés à un mariage, ne vous pressez pas à y aller car cela rappelle les plaisirs de ce monde, mais si vous êtes conviés à un convoi funèbre, accourrez-y car cela rappelle l'Au-delà.<sup>3174</sup>"
            },
            {
                "number": "2820",
                "text": "Le Messager d'Allah (s) a dit : Si l'un de vous est convié à un repas de mariage, qu'il y réponde favorablement.<sup>3175</sup>"
            }
        ]
    },
    "886": {
        "hadiths": [
            {
                "number": "2821",
                "text": "Le Messager d'Allah (s) a dit : Annoncez ce mariage et célébrez-le à la mosquée.<sup>3176</sup>"
            },
            {
                "number": "2822",
                "text": "Le Messager d'Allah (s) a dit : Annoncez le mariage et tenez secrètes les fiançailles.<sup>3177</sup>"
            }
        ]
    },
    # -------------------------------------------------------------
    # Part 176 (Index 177) - LA VISITE
    # -------------------------------------------------------------
    "887": {
        "hadiths": [
            {
                "number": "2823",
                "text": "Le Messager d'Allah (s) a dit : Celui qui rend visite à son frère croyant sans qu'il ait besoin de lui sera inscrit parmi ceux qui auront rendu visite à Allah, et Allah honore ceux qui Lui rendent visite.<sup>3178</sup>"
            },
            {
                "number": "2824",
                "text": "L'Imām 'Alī (as) a dit : Rendez visite pour Allah, tenez compagnie pour Allah, donnez pour Allah, refusez pour Allah, séparez-vous des ennemis d'Allah, et liez-vous avec les amis d'Allah.<sup>3179</sup>"
            },
            {
                "number": "2825",
                "text": "L'Imām al-Bāqir (as) a dit : Rendez-vous mutuellement visite dans vos maisons car en vérité, cela permet de vivifier nos enseignements, et Allah accorde Sa miséricorde à un serviteur qui vivifie nos enseignements.<sup>3180</sup>"
            },
            {
                "number": "2826",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui rend visite à son frère dans la voie d'Allah et pour Allah viendra le Jour du Jugement habillé d'un vêtement de lumière, et il illuminera toute chose sur son passage.<sup>3181</sup>"
            },
            {
                "number": "2827",
                "text": "L'Imām al-Ṣādiq (as) a dit : Rendez-vous mutuellement visite, car vos visites revivifient vos cœurs et rappellent nos traditions, et nos traditions suscitent à leur tour de l'affection mutuelle entre vous. Ainsi, si vous les adoptez, vous serez guidés et sauvés [alors que] si vous les délaissez, vous vous égarerez et vous périrez. Par conséquent, adoptez-les et je vous garantirai votre salut.<sup>3182</sup>"
            }
        ]
    },
    "888": {
        "hadiths": [
            {
                "number": "2828",
                "text": "L'Imām al-Kāẓim (as) a dit : Rien n'offense autant Iblīs et ses soldats que la visite des frères les uns aux autres pour Allah.<sup>3183</sup>"
            },
            {
                "number": "2829",
                "text": "Le Messager d'Allah (s) a dit : La visite fait grandir l'affection.<sup>3184</sup>"
            },
            {
                "number": "2830",
                "text": "L'Imām al-Jawād (as) a dit : La rencontre des frères [en religion], même brève, suscite l'épanouissement et la fécondité de l'esprit.<sup>3185</sup>"
            }
        ]
    },
    "889": {
        "hadiths": [
            {
                "number": "2831",
                "text": "Le Messager d'Allah (s) a dit : Espace tes visites, et on t'aimera ainsi davantage.<sup>3186</sup>"
            },
            {
                "number": "2832",
                "text": "L'Imām 'Alī (as) a dit dans son testament à son fils Ḥusayn (as) : L'affluence des visites génère la lassitude.<sup>3187</sup>"
            },
            {
                "number": "2833",
                "text": "L'Imām 'Alī (as) a dit : Si tu es certain de l'affection de ton frère à ton égard, ne t'inquiète plus de savoir quand tu lui rends visite et quand lui te rend visite.<sup>3188</sup>"
            }
        ]
    },
    # -------------------------------------------------------------
    # Part 177 (Index 178) - LA VISITE DES TOMBES
    # -------------------------------------------------------------
    "890": {
        "hadiths": [
            {
                "number": "2834",
                "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, j'intercèderai pour celui qui m'a rendu visite.<sup>3189</sup>"
            },
            {
                "number": "2835",
                "text": "Le Messager d'Allah (s) a dit : Je suis informé des salutations de celui qui m'a salué d'une partie de la terre, alors que j'entends [personnellement] les salutations de celui qui me salue à proximité de ma tombe.<sup>3190</sup>"
            }
        ]
    },
    "891": {
        "hadiths": [
            {
                "number": "2836",
                "text": "Lorsque Ḥasan ibn 'Alī (as) lui demanda : «Ô père, quelle est la récompense de celui qui te rend visite ?», le Messager d'Allah (s) lui répondit : «Ô fils, celui qui me rend visite durant ma vie ou après ma mort, qui rend visite à ton père, ton frère ou bien qui te rend visite à toi, il m'incombe de lui rendre visite le Jour de la Résurrection, où je le délivrerai de ses péchés.»<sup>3191</sup>"
            },
            {
                "number": "2837",
                "text": "Le Messager d'Allah (s) a dit : Les pieds de celui qui rend visite à Ḥasan dans son lieu de repos seront affermis [lors de la traversée du] ṣirāṭ, le jour où les pieds trébucheront.<sup>3192</sup>"
            },
            {
                "number": "2838",
                "text": "Le Messager d'Allah (s) a dit : Une partie de mi [de ma descendance] sera bientôt enterrée dans la terre du Khurāsān ; nul croyant ne lui rendra visite sans qu'Allah lui accorde obligatoirement le Paradis et interdise son corps au Feu.<sup>3193</sup>"
            },
            {
                "number": "2839",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui nous rend visite après notre mort est comme s'il nous avait rendu visite durant notre vie.<sup>3194</sup>"
            },
            {
                "number": "2840",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, il y a à sa proximité [de Kūfa] un tombeau que nulle personne attristée ne visite et ne prie à sa proximité quatre raka'āt de prière sans qu'Allah ne la rende heureuse en exauçant sa demande.<sup>3195</sup>"
            },
            {
                "number": "2841",
                "text": "Le Messager d'Allah (s) a dit : «Entre ma tombe et mon minbar se trouve l'un des jardins du Paradis, et mon minbar se trouve sur l'une des rivières du Paradis», car la tombe de Fāṭima - que les prières d'Allah soient sur elle - se situe entre sa tombe et son minbar, et sa tombe est l'un des jardins du Paradis irrigué par l'une des rivières du Paradis.<sup>3196</sup>"
            },
            {
                "number": "2842",
                "text": "L'Imām al-Ṣādiq (as) a dit : Allah inscrira au compte de celui qui rend visite à Ḥusayn (as) en reconnaissant son droit, l'équivalent de la récompense de mille pèlerinages obligatoires (hajj) agréés et de mille pèlerinages recommandés ('umra) agréés, et Il lui pardonnera ses péchés antérieurs et futurs.<sup>3197</sup>"
            },
            {
                "number": "2843",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Ḥusayn ibn 'Alī (as) regardait vers son Seigneur... et disait : «Si celui qui me rend visite savait ce qu'Allah a préparé pour lui, sa joie serait supérieure à sa peine [à mon sujet].» En vérité, celui qui lui rend visite le quittera en étant absous de tout péché.<sup>3198</sup>"
            },
            {
                "number": "2844",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque tu rends visite à Abū 'Abdillāh [l'Imām Ḥusayn (as)], accomplis ton pèlerinage en étant triste, malheureux, décoiffé, poussiéreux, affamé et assoiffé, car Ḥusayn (as) a été tué alors qu'il était triste, malheureux, décoiffé, poussiéreux, affamé et assoiffé ; puis demande-lui ce dont tu as besoin et quitte-le, et ne t'établis pas à proximité de sa tombe.<sup>3199</sup>"
            },
            {
                "number": "2845",
                "text": "L'Imām al-Ṣādiq (as) a dit : Les péchés de celui qui me rend visite seront pardonnés et il ne mourra pas dans la pauvreté.<sup>3200</sup>"
            },
            {
                "number": "2846",
                "text": "Lorsqu'on lui demanda : «Quelle est la position de celui qui a rendu visite à l'un de vous [les Imāms] ?» l'Imām al-Ṣādiq (as) répondit : [Elle est comme celle] de celui qui a rendu visite au Messager d'Allah (s).<sup>3201</sup>"
            },
            {
                "number": "2847",
                "text": "La vertu éminente de la visite de la tombe de l'Émir des croyants par rapport à celle de la tombe de Ḥusayn est semblable à l'éminence de l'Émir des croyants par rapport à Ḥusayn.<sup>3202</sup>"
            },
            {
                "number": "2848",
                "text": "Lorsqu'Ibn Sinān demanda à l'Imām al-Riḍā (as) : «Quelle est la récompense de celui qui rend visite à ton père ?», il répondit : Il aura le Paradis, alors rends-lui donc visite.<sup>3203</sup>"
            },
            {
                "number": "2849",
                "text": "L'Imām al-Riḍā (as) a dit : Aucun de mes amis et partisans ne me rend visite en reconnaissant mon droit sans que j'intercède pour lui le Jour de la Résurrection.<sup>3204</sup>"
            },
            {
                "number": "2850",
                "text": "L'Imām al-Riḍā (as) a dit : Le Jour de la Résurrection, je me rendrai auprès de celui qui m'a rendu visite dans mon lieu d'exil en trois endroits afin de le sauver de leurs affres : lorsque les recueils [des actes] seront distribués à droite et à gauche, au ṣirāṭ [pont au-dessus de l'Enfer], et devant la balance [qui pèse les actes].<sup>3205</sup>"
            },
            {
                "number": "2851",
                "text": "Interrogé au sujet de la visite des tombes de Abū 'Abdillāh Ḥusayn, de Abū al-Ḥasan al-Kāẓim et de Abū Ja'far al-Jawād (as), l'Imām al-Hādī (as) répondit : [La visite de celle de] Abū 'Abdillāh Ḥusayn (as) est prioritaire, mais [rendre visite aux trois Imāms] a la récompense la plus grande et complète.<sup>3206</sup>"
            },
            {
                "number": "2852",
                "text": "L'Imām al-'Askarī (as) a dit à Abū Hāshim al-Ja'farī : Ma tombe à Surra man ra'ā [Samarra] sera un endroit de sécurité et de salut pour les gens des deux rives [de l'Euphrate].<sup>3207</sup>"
            }
        ]
    },
    "892": {
        "hadiths": [
            {
                "number": "2853",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, nous avons un sanctuaire nommé Qom où une femme de ma descendance appelée Fāṭima sera enterrée. Celui qui lui rend visite méritera obligatoirement le Paradis.<sup>3208</sup>"
            }
        ]
    }
}

# Perform the injections
modified_subparts_info = []

for sub_num, info in hadiths_to_inject.items():
    p_idx, s = find_subpart_globally(sub_num)
    if p_idx is None or s is None:
        print(f"❌ ERROR: Subpart {sub_num} could not be found globally in database!")
        continue
    
    eh(s)
    
    # We replace any existing hadiths to ensure a clean drop-in
    s['hadiths'] = info['hadiths']
            
    print(f"Injected {len(s['hadiths'])} hadiths to Subpart {sub_num} (Part index {p_idx}, Title: {s['title']})")
    modified_subparts_info.append((p_idx, sub_num))

# ============================================================
# Sequential Sorting for all modified subparts (programmatic)
# ============================================================
print("\nSorting modified subparts...")
for p_idx, sub_num in modified_subparts_info:
    p_idx_new, s = find_subpart_globally(sub_num)
    if s and 'hadiths' in s:
        s['hadiths'].sort(key=lambda h: int(h['number']))
        print(f"Sorted Subpart {sub_num} (Part index {p_idx_new}). Hadiths: {[h['number'] for h in s['hadiths']]}")

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\n✅ Data successfully saved! Hadiths Batch 46 integrated and sorted.")
