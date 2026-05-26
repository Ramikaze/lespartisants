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
            # We match the number followed by a space or hyphen to be precise
            if s['title'].startswith(num_str + " ") or f"- {num_str} " in s['title'] or f" {num_str} -" in s['title']:
                return p_idx, s
    return None, None

def eh(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# Mappings of all 29 gap-filling hadiths
gaps_to_inject = {
    # -------------------------------------------------------------
    # Gap 1: Page 465 (Hadiths 2629-2633)
    # -------------------------------------------------------------
    "832": {
        "hadiths": [
            {
                "number": "2629",
                "text": "A‘lām al-Dīn : Parmi les entretiens intimes de Moïse (as) avec Allah, il dit : «Ô mon Seigneur, quel est le signe de Ta satisfaction vis-à-vis de Ton serviteur ?» Allah lui révéla : «Si tu Me vois préparer Mon serviteur pour Mon obéissance et l'éloigner de Ma désobéissance, [sache que] cela est le signe de Ma satisfaction.»<sup>2966</sup>"
            },
            {
                "number": "2630",
                "text": "L'Imām 'Alī (as) a dit : Le signe de la satisfaction d'Allah - loué soit-Il - vis-à-vis du serviteur est la satisfaction de ce dernier vis-à-vis de ce qu'Allah - loué soit-Il - a décrété, que ce soit en sa faveur ou en sa défaveur.<sup>2967</sup>"
            }
        ]
    },
    "833": {
        "hadiths": [
            {
                "number": "2631",
                "text": "L'Imām 'Alī (as) a écrit à Muḥammad fils d'Abū Bakr : Si tu peux satisfaire l'une des créatures de ton Seigneur sans entraîner Son insatisfaction, fais-le car en vérité, Allah le Tout-Puissant peut facilement remplacer un serviteur par un autre, alors que le serviteur ne peut remplacer Allah par aucune chose.<sup>2968</sup>"
            },
            {
                "number": "2632",
                "text": "L'Imām Ḥusayn (as) a dit : Allah affranchira de tout besoin vis-à-vis des gens celui qui aspire à satisfaire Allah au prix de l'insatisfaction des gens ; et Il abandonnera à ces mêmes gens celui qui aspire à satisfaire les gens au prix de l'insatisfaction d'Allah.<sup>2969</sup>"
            }
        ]
    },
    "834": {
        "hadiths": [
            {
                "number": "2633",
                "text": "Le Messager d'Allah (s) a dit : En vérité, la douceur n'a été déposée sur aucune chose sans qu'elle ne l'embellisse, et elle n'a été enlevée d'aucune chose sans qu'elle ne l'enlaidisse.<sup>2970</sup>"
            }
        ]
    },
    # -------------------------------------------------------------
    # Gap 2: Page 473 (Hadiths 2673-2676)
    # -------------------------------------------------------------
    "843": {
        "hadiths": [
            {
                "number": "2673",
                "text": "Kanz al-'Ummāl : Shaqīq ibn Salama : Un homme vint chez 'Alī et s'entretint with lui. Lors de leur discussion, il lui dit : «En vérité, je t'aime.» 'Alī lui répondit : «Tu mens.» L'homme demanda : «Pourquoi donc, ô Émir des croyants ?» Il dit : «Car mon cœur ne ressent pas d'amour pour toi, [alors que] le Prophète (s) a dit : «En vérité, les âmes se rencontrent dans le ciel et se sentent ; celles qui sont en harmonie s'attirent mutuellement, et celles qui diffèrent se repoussent mutuellement.» Ainsi, lorsqu'arriva ce qui arriva à 'Alī [et que les Kharijites se rebellèrent contre lui], cet homme fit partie de ceux-là.»<sup>3015</sup><br>(Voir également : 231. L'ami, section 1101)"
            }
        ]
    },
    "844": {
        "hadiths": [
            {
                "number": "2674",
                "text": "L'Imām 'Alī (as) a dit : Le corps a six états : la santé, la maladie, la mort, la vie, le sommeil et l'éveil. Il en va de même pour l'âme : sa vie est dans son savoir, sa mort est dans son ignorance, sa maladie est dans son doute, sa bonne santé est dans sa certitude, son sommeil est dans sa distraction, et son éveil est dans sa pleine conscience.<sup>3016</sup>"
            }
        ]
    },
    "845": {
        "hadiths": [
            {
                "number": "2675",
                "text": "Lorsqu'Abū Baṣīr demanda à l'Imām al-Ṣādiq (as) au sujet de l'âme durant le sommeil : «Sort-elle du corps ?», il répondit : Non, ô Abū Baṣīr ; en vérité, si l'âme quittait le corps, elle n'y reviendrait plus. Elle est plutôt comme le soleil fixé à sa place au centre du ciel, et dont le rayonnement s'étend néanmoins à la terre.<sup>3017</sup>"
            },
            {
                "number": "2676",
                "text": "L'Imām al-Kāẓim (as) a dit : En vérité, lorsque l'homme dort, son âme animale reste dans son corps, et ce qui quitte le corps est l'âme rationnelle.<sup>3018</sup><br>(Voir également : 387. Le sommeil, section 1778)"
            }
        ]
    },
    # -------------------------------------------------------------
    # Gap 3: Page 480 (Hadiths 2714-2720)
    # -------------------------------------------------------------
    "855": {
        "hadiths": [
            {
                "number": "2714",
                "text": "L'Imām 'Alī (as) a dit : La valeur de l'homme concernant son savoir sur les choses is la connaissance de son temps.<sup>3063</sup>"
            },
            {
                "number": "2715",
                "text": "L'Imām 'Alī (as) a dit : La personne qui connaît le mieux le temps est celle qui n'est pas surprise par les événements.<sup>3064</sup>"
            },
            {
                "number": "2716",
                "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui connaît son temps n'est jamais accablé par ses incertitudes et obscurités.<sup>3065</sup>"
            }
        ]
    },
    "856": {
        "hadiths": [
            {
                "number": "2717",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait confiance au temps sera abattu.<sup>3066</sup>"
            },
            {
                "number": "2718",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait confiance au temps sera trahi par lui, et celui qui le tient en estime sera rabaissé par lui.<sup>3067</sup>"
            },
            {
                "number": "2719",
                "text": "L'Imām 'Alī (as) a dit : Celui qui fait confiance au temps sera trahi par lui ; celui qui lui accorde une grande importance sera rabaissé par lui ; celui qui le contraint sera contraint par lui ; et celui qui se réfugie auprès de lui sera livré par lui. Tout tireur n'atteint pas toujours sa cible. Lorsque le souverain change, de même change le temps.<sup>3068</sup>"
            },
            {
                "number": "2720",
                "text": "L'Imām 'Alī (as) a dit : Le temps trahit celui qui [pense le] posséder, et il ne cherche pas à plaire à ceux qui le blâment.<sup>3069</sup>"
            }
        ]
    },
    # -------------------------------------------------------------
    # Gap 4: Page 483 (Hadiths 2733-2738)
    # -------------------------------------------------------------
    "860": {
        "hadiths": [
            {
                "number": "2733",
                "text": "L'Imām al-Ṣādiq (as) a dit : Quand l'adultère se répand, les tremblements de terre surviennent [en conséquence].<sup>3083</sup>"
            }
        ]
    },
    "861": {
        "hadiths": [
            {
                "number": "2734",
                "text": "Le Christ (as) a dit : Toute femme qui se parfume et sort de chez elle afin que son parfum soit senti par les autres est une femme adultère, et tout œil [qui la regarde avec désir] commet l'adultère.<sup>3084</sup>"
            },
            {
                "number": "2735",
                "text": "Le Christ (as) a dit : Ne fixe pas ce qui ne t'appartient pas car en vérité, tes parties intimes ne commettront pas d'adultère si tu préserves ton regard. Si tu peux [même] éviter de regarder le vêtement d'une femme qui ne t'est pas autorisée, fais-le.<sup>3085</sup>"
            },
            {
                "number": "2736",
                "text": "Le Messager d'Allah (s) a dit : Chaque respiration de l'homme a une part d'adultère dont il est inévitablement conscient au moment donné. Ainsi, l'adultère de l'œil est de regarder [ce qui est interdit], l'adultère du pied est de marcher [en direction du péché], et l'adultère de l'oreille est d'écouter [ce qui est prohibé].<sup>3086</sup><br>(Voir également : 376. Le regard, section 1734)"
            }
        ]
    },
    "862": {
        "hadiths": [
            {
                "number": "2737",
                "text": "Le Messager d'Allah (s) a dit : Les gens ne peuvent adorer Allah par une chose meilleure que le renoncement aux plaisirs de ce monde.<sup>3088</sup>"
            },
            {
                "number": "2738",
                "text": "L'Imām 'Alī (as) a dit : Le renoncement est le trait distinctif des pieux et de ceux qui craignent Allah, ainsi que la disposition naturelle de ceux qui se tournent [vers Lui].<sup>3089</sup>"
            }
        ]
    },
    # -------------------------------------------------------------
    # Gap 5: Page 486 (Hadiths 2749-2755)
    # -------------------------------------------------------------
    "865": {
        "hadiths": [
            {
                "number": "2750",
                "text": "L'Imām 'Alī (as) a dit : La personne la plus à même de pratiquer le renoncement est celle qui comprend les défauts et insuffisances de ce bas-monde.<sup>3103</sup>"
            },
            {
                "number": "2751",
                "text": "L'Imām 'Alī (as) a dit : Comment celui qui n'a pas saisi la valeur de l'Au-delà pourrait-il renoncer aux plaisirs de ce monde ?!<sup>3104</sup>"
            },
            {
                "number": "2752",
                "text": "L'Imām al-Bāqir (as) a dit : Rappelez-vous fréquemment de la mort, car dès qu'un être se rappelle fréquemment de la mort, il renonce aux plaisirs de ce monde.<sup>3105</sup>"
            },
            {
                "number": "2753",
                "text": "L'Imām al-Kāẓim (as) a dit alors qu'il se tenait à proximité d'une tombe : En vérité, ce qui s'achève avec ceci [la mort] mérite d'être commencé dans le renoncement. Et ce qui est commencé avec ceci mérite que sa fin soit crainte.<sup>3106</sup>"
            },
            {
                "number": "2754",
                "text": "L'Imām al-'Askarī (as) a dit : Si tous les habitants de ce monde faisaient usage de leur intellect, ce dernier serait détruit [en ce qu'il cesserait d'avoir la moindre importance].<sup>3107</sup><br>(Voir également : 367. La mort, section 1671)"
            }
        ]
    },
    "866": {
        "hadiths": [
            {
                "number": "2749",
                "text": "Interrogé au sujet des caractéristiques de celui qui renonce [aux plaisirs de ce monde], l'Imām al-Riḍā (as) a dit : C'est celui qui arrive à calmer sa faim sans rechercher de nourriture, qui s'est préparé pour le jour de sa mort, et qui est lassé de sa vie [du fait qu'il désire ardemment l'Au-delà et la rencontre avec Allah].<sup>3102</sup>"
            },
            {
                "number": "2755",
                "text": "Le Messager d'Allah (s) a dit : Le renoncement aux plaisirs de ce monde repose le cœur et le corps, tandis que leur désir les épuise.<sup>3108</sup>"
            }
        ]
    }
}

# Perform the injections
modified_subparts_info = []

for sub_num, info in gaps_to_inject.items():
    p_idx, s = find_subpart_globally(sub_num)
    if p_idx is None or s is None:
        print(f"❌ ERROR: Subpart {sub_num} could not be found globally in database!")
        continue
    
    eh(s)
    
    # We append the new hadiths to any existing ones in the subpart
    # (Checking for duplicates first, just in case)
    existing_nums = {h['number'] for h in s['hadiths']}
    added_count = 0
    for h in info['hadiths']:
        if h['number'] not in existing_nums:
            s['hadiths'].append(h)
            added_count += 1
            
    print(f"Added {added_count} hadiths to Subpart {sub_num} (Part index {p_idx}, Title: {s['title']})")
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

print("\n✅ Data successfully saved! Missing gaps in Mizan Al-Hikmah filled and sorted.")
