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

# Mappings of all 27 contiguous hadiths and Quranic introductions (Batch 47)
hadiths_to_inject = {
    "892": {
        "hadiths": [
            {
                "number": "2853",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, nous avons un sanctuaire nommé Qom où une femme de ma descendance appelée Fāṭima sera enterrée. Celui qui lui rend visite méritera obligatoirement le Paradis.<sup>3208</sup>"
            },
            {
                "number": "2854",
                "text": "L'Imām al-Jawād (as) a dit : Celui qui a visité le tombeau de ma tante à Qom aura le Paradis.<sup>3209</sup>"
            }
        ]
    },
    "893": {
        "hadiths": [
            {
                "number": "2855",
                "text": "Thawāb al-A'māl : Muḥammad ibn Yaḥyā al-'Attār : Un habitant de Rey a dit : Je me rendis auprès de Abū al-Ḥasan al-'Askarī [l'Imām al-Hādī] (as) qui me demanda : «Où étais-tu ?» Je lui répondis : «J'ai rendu visite à Ḥusayn (as).» Il dit : «En vérité, si tu avais visité la tombe de 'Abd al-'Aẓīm chez toi [à Rey], cela aurait été comme si tu avais rendu visite à Ḥusayn ibn 'Alī (as).<sup>3210</sup>"
            }
        ]
    },
    "894": {
        "hadiths": [
            {
                "number": "2856",
                "text": "L'Imām al-Ṣādiq (as) a dit : Que celui qui ne peut pas nous rendre visite rende visite aux gens de bien parmi nos amis, et il lui sera inscrit la récompense de notre visite.<sup>3211</sup>"
            }
        ]
    },
    "895": {
        "hadiths": [
            {
                "number": "2857",
                "text": "L'Imām 'Alī (as) a dit : Rendez visite à vos morts car ils se réjouissent de votre visite. Invoquez vos demandes [à Allah] auprès de la tombe de votre père et de votre mère après avoir prié pour eux.<sup>3212</sup>"
            },
            {
                "number": "2858",
                "text": "Lorsque Dāwūd al-Raqqī demanda : «Si l'homme se rend sur la tombe de son père et de personnes proches ou même non proches, cela leur sera-t-il bénéfique ?» l'Imām al-Ṣādiq (as) répondit : «Oui, en vérité, ils la recevront [cette visite] à la manière dont l'un d'entre vous reçoit un cadeau, et cela les rendra heureux.»<sup>3213</sup>"
            }
        ]
    },
    "896": {
        "hadiths": [
            {
                "number": "2859",
                "text": "Biḥār al-Anwār : Alors qu'il passait à proximité de tombes, l'Imām 'Alī (as) a dit : «Que le salut soit sur vous, ô défunts ! Vous nous avez précédés et nous vous succéderons, et nous vous rejoindrons par la volonté d'Allah. Pour ce qui est de vos maisons, elles ont été habitées ; concernant vos épouses, elles se sont remariées ; quant à votre argent, il a été distribué - ce sont nos nouvelles. Si seulement nous pouvions [vous demander] quelles sont les vôtres !» Et il dit : «S'ils avaient le pouvoir de parler, ils diraient : «Nous avons trouvé que la piété et la crainte révérencielle vis-à-vis d'Allah était la meilleure des provisions [pour la tombe]».»<sup>3214</sup>"
            }
        ]
    },
    "897": {
        "introduction": "«Ô enfants d'Adam, dans chaque lieu de prière (ṣalāt), portez votre parure [vos beaux habits]. Et mangez et buvez ; et ne commettez pas d'excès, car Il [Allah] n'aime pas ceux qui commettent des excès.»<sup>3215</sup><br><br>«Dis : «Qui a interdit la parure d'Allah, qu'Il a produite pour Ses serviteurs, ainsi que les bonnes nourritures ?»»<sup>3216</sup>",
        "hadiths": [
            {
                "number": "2860",
                "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime que son serviteur croyant se prépare et s'apprête lorsqu'il va rendre visite à son frère.<sup>3217</sup>"
            },
            {
                "number": "2861",
                "text": "L'Imām 'Alī (as) a dit : Lorsque l'un de vous s'apprête à rendre visite à son frère musulman, qu'il se pare comme il le ferait s'il rendait visite à un étranger qu'il aimerait rencontrer en ayant la meilleure apparence.<sup>3218</sup><br>(Voir également : 71. La beauté, section 353)"
            }
        ]
    },
    "898": {
        "hadiths": [
            {
                "number": "2862",
                "text": "Le Messager d'Allah (s) a dit : La sérénité alliée à la foi est la meilleure parure de l'homme.<sup>3219</sup>"
            },
            {
                "number": "2863",
                "text": "L'Imām 'Alī (as) a dit : En vérité, la meilleure parure est celle qui te permet de te mêler aux autres tout en te rendant présentable face à eux, et qui ne fournit pas de prétexte à leurs médisances.<sup>3220</sup>"
            },
            {
                "number": "2864",
                "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de meilleure parure que l'obéissance à Allah.<sup>3221</sup>"
            },
            {
                "number": "2865",
                "text": "L'Imām 'Alī (as) a dit : La parure intérieure est plus belle que la parure extérieure.<sup>3222</sup>"
            },
            {
                "number": "2866",
                "text": "L'Imām 'Alī (as) a dit : La parure de la foi se trouve dans la pureté des pensées les plus secrètes, ainsi que dans les bonnes actions extérieures.<sup>3223</sup>"
            }
        ]
    },
    "899": {
        "introduction": "«Par ton Seigneur ! Nous les interrogerons tous sur ce qu'ils œuvraient.»<sup>3224</sup>",
        "hadiths": [
            {
                "number": "2867",
                "text": "L'Imām 'Alī (as) a dit : Craignez Allah concernant Ses serviteurs et Sa terre, car en vérité, vous serez interrogés même au sujet des endroits [que vous fréquentiez] et des bestiaux. Obéissez donc à Allah et ne Lui désobéissez pas.<sup>3225</sup>"
            }
        ]
    },
    "900": {
        "hadiths": [
            {
                "number": "2868",
                "text": "Le Messager d'Allah (s) a dit : En vérité, vous êtes tous des bergers responsables de votre propre troupeau. Le gouverneur est le berger des gens, et il est responsable de ses sujets ; l'homme est le berger de sa famille, et il est responsable d'elle ; la femme est la bergère de la maison de son époux et de ses enfants, et elle est responsable d'eux.<sup>3226</sup>"
            },
            {
                "number": "2869",
                "text": "L'Imām 'Alī (as) a dit : Chaque personne est responsable et doit répondre de ce qu'elle possède, ainsi que de ceux qui dépendent d'elle.<sup>3227</sup>"
            }
        ]
    },
    "901": {
        "hadiths": [
            {
                "number": "2870",
                "text": "Kitāb man lā Yaḥḍuruhu al-Faqīh : Un homme dit à l'Imām al-Ṣādiq (as) : «J'ai des voisins dont les servantes chantent et jouent du luth. Il m'arrive d'aller aux toilettes [à l'extérieur] et d'y prendre mon temps pour les écouter.» L'Imām al-Ṣādiq (as) lui dit alors : «Par Allah, n'as-tu pas entendu la parole du Très-Haut lorsqu'Il dit : «Ne poursuis pas ce dont tu n'as aucune connaissance. L'ouïe, la vue et le cœur : sur tout cela, en vérité, on sera interrogé»<sup>3228</sup> ?!<sup>3229</sup>»"
            }
        ]
    },
    "902": {
        "introduction": "«Nous n'avons envoyé avant toi que des hommes auxquels Nous avons fait des révélations. Demande-donc aux gens du rappel, si vous ne savez pas.»<sup>3230</sup>",
        "hadiths": [
            {
                "number": "2871",
                "text": "Le Messager d'Allah (s) a dit : Le savoir est un trésor et sa clé réside dans la question. Dès lors, questionnez et Allah vous fera miséricorde, car en vérité, quatre types de personnes seront rétribuées [pour une telle question] : celle qui questionne, celle qui parle, celle qui écoute et celle qui les aime.<sup>3231</sup>"
            },
            {
                "number": "2872",
                "text": "Le Messager d'Allah (s) a dit : La question est la moitié du savoir.<sup>3232</sup>"
            }
        ]
    },
    "903": {
        "hadiths": [
            {
                "number": "2873",
                "text": "Le Messager d'Allah (s) a dit : Poser la bonne question est la moitié du savoir.<sup>3233</sup>"
            },
            {
                "number": "2874",
                "text": "L'Imām 'Alī (as) a dit à une personne qui l'interrogea au sujet d'une question problématique : Interroge dans le but de comprendre et non par entêtement [dans le but de créer davantage de confusion] car en vérité, l'ignorant qui s'instruit et souhaite apprendre est comparable au savant, tandis que l'érudit déviant est semblable à l'ignorant entêté.<sup>3234</sup>"
            }
        ]
    },
    "904": {
        "introduction": "«Ô vous qui croyez ! Ne posez pas de questions sur des choses qui, si elles vous étaient divulguées, vous mécontenteraient. Et si vous posez des questions à leur sujet pendant que le Coran est révélé, elles vous seront divulguées. Allah vous a pardonné cela. Et Allah est Pardonneur et Indulgent.»<sup>3235</sup>",
        "hadiths": [
            {
                "number": "2875",
                "text": "Le Messager d'Allah (s) a dit : Laissez-moi lorsque je vous quitte car en vérité, ceux qui vous ont précédés ont été anéantis en raison de leurs questionnements incessants et de leurs divergences vis-à-vis de leurs prophètes. Dès lors, lorsque je vous ordonne une chose, appliquez-la le mieux possible, et lorsque je vous interdis une chose, délaissez-la.<sup>3236</sup>"
            }
        ]
    },
    "905": {
        "hadiths": [
            {
                "number": "2876",
                "text": "Le Messager d'Allah (s) a dit dans son conseil à Abū Dhar : Ô Abū Dhar ! Si tu es interrogé au sujet d'une chose que tu ignores, dis : «Je ne sais pas» et tu seras sauvé de ses répercussions ; et ne donne pas ton avis au sujet de ce que tu ignores afin que tu sois sauvé du châtiment d'Allah le Jour de la Résurrection.<sup>3237</sup>"
            },
            {
                "number": "2877",
                "text": "L'Imām 'Alī (as) a dit : Le savant ne doit pas avoir honte de dire «Je n'ai pas de connaissance à ce sujet» lorsqu'il est interrogé à propos d'une chose qu'il ignore.<sup>3238</sup>"
            },
            {
                "number": "2878",
                "text": "L'Imām 'Alī (as) a dit : En vérité, celui qui abandonne la parole «Je ne sais pas» sera touché là où il est le plus vulnérable.<sup>3239</sup>"
            },
            {
                "number": "2879",
                "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, celui qui répond à toutes les questions qu'on lui pose est un insensé.<sup>3240</sup>"
            },
            {
                "number": "2880",
                "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le savant est questionné sur un sujet qu'il ignore, il doit dire «Allah est plus savant» ; et seul un savant dira cela.<sup>3241</sup><br>(Voir également : 81. La réponse)"
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
    
    # We replace any existing hadiths and introduction to ensure a clean drop-in
    s['hadiths'] = info['hadiths']
    if 'introduction' in info:
        s['introduction'] = info['introduction']
            
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

print("\n✅ Data successfully saved! Hadiths Batch 47 integrated and sorted.")
