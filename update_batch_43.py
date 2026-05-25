import json
import re

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
# Part 171 (index 172) - LA ZAKĀT (L'AUMÔNE LÉGALE)
# ============================================================
p171 = 172

# Subpart 851 - Celui qui refuse de s'acquitter de la zakāt
s851 = find_subpart(p171, "851"); eh(s851)
s851['hadiths'] = [
    {
        "number": "2699",
        "text": "L'Imām al-Bāqir (as) a dit : Le Jour du Jugement, Allah transformera les biens de celui qui refusait de s'acquitter de la zakāt en un cobra de feu pourvu de deux glandes venimeuses qui s'enroulera autour de lui, et il lui sera dit : «Accroche-toi à lui comme il s'est accroché à toi dans la vie terrestre.» C'est ce que signifie la parole d'Allah : «Le Jour de la Résurrection, on leur attachera autour du cou ce qu'ils ont gardé avec avarice».<sup>3044, 3045</sup>"
    },
    {
        "number": "2700",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui a refusé de s'acquitter de la zakāt demandera à retourner [sur terre] à l'instant de sa mort, selon la parole d'Allah le Tout-Puissant : «Puis, quand la mort vient à l'un d'eux, il dit : «Mon Seigneur ! Fais-moi revenir [sur terre], afin que je fasse du bien dans ce que je délaissais.»<sup>3046, 3047</sup>"
    },
    {
        "number": "2701",
        "text": "L'Imām al-Ṣādiq (as) a dit : Les voleurs sont de trois sortes : celui qui refuse de s'acquitter de la zakāt, celui qui dépense illicitement la dot de sa femme, et celui qui s'endette sans avoir l'intention de rembourser.<sup>3048</sup>"
    },
    {
        "number": "2702",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui refuse de s'acquitter [même d'une aussi petite somme qu'] un seizième de dirham de la zakāt pourra tout autant mourir en étant juif ou chrétien.<sup>3049</sup>"
    }
]

# Subpart 852 - Les destinataires de la zakāt
s852 = find_subpart(p171, "852"); eh(s852)
s852['introduction'] = (
    "«<i>Les aumônes (ṣadaqāt) sont destinées aux pauvres, aux nécessiteux, à ceux qui y travaillent, "
    "à ceux dont les cœurs sont à gagner [à l'islam], à l'affranchissement des jougs, à ceux qui sont "
    "lourdement endettés, dans le sentier d'Allah et pour le voyageur. C'est un décret d'Allah ! Et "
    "Allah est Omniscient et Sage.</i>»<sup>3050</sup>"
)
s852['hadiths'] = [
    {
        "number": "2703",
        "text": "L'Imām al-Ṣādiq (as) a dit en commentant la parole du Très-Haut : «Les aumônes sont destinées aux pauvres»<sup>3051</sup> : Le pauvre est celui qui ne mendie pas auprès des gens [malgré sa pauvreté] ; le nécessiteux vit dans des conditions plus difficiles ; et le désespéré vit dans les conditions les plus âpres.<sup>3052</sup><br>(Voir également : 232. La charité, section 1116)"
    }
]

# Subpart 853 - Toute chose a une zakāt
s853 = find_subpart(p171, "853"); eh(s853)
s853['hadiths'] = [
    {
        "number": "2704",
        "text": "L'Imām 'Alī (as) a dit : La zakāt de la puissance est l'équité.<sup>3053</sup>"
    },
    {
        "number": "2705",
        "text": "L'Imām 'Alī (as) a dit : La zakāt de la beauté est la chasteté.<sup>3054</sup>"
    },
    {
        "number": "2706",
        "text": "L'Imām 'Alī (as) a dit : La zakāt de l'aisance est la bienfaisance envers les voisins et le maintien des liens familiaux.<sup>3055</sup>"
    },
    {
        "number": "2707",
        "text": "L'Imām 'Alī (as) a dit : La zakāt de la santé est l'effort dans l'obéissance à Allah.<sup>3056</sup>"
    },
    {
        "number": "2708",
        "text": "L'Imām 'Alī (as) a dit : La zakāt du courage est le jihād dans le sentier d'Allah.<sup>3057</sup>"
    },
    {
        "number": "2709",
        "text": "L'Imām 'Alī (as) a dit : Jeûnez, car c'est la zakāt du corps.<sup>3058</sup>"
    },
    {
        "number": "2710",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, toute chose a une zakāt, et la zakāt du savoir est de l'enseigner à ceux qui le méritent.<sup>3059</sup>"
    },
    {
        "number": "2711",
        "text": "L'Imām al-Ṣādiq (as) a dit : La conduite bonne et convenable est la zakāt des bienfaits ; l'intercession est la zakāt d'une haute position ; les maladies sont la zakāt des corps ; l'amnistie est la zakāt de la victoire. Ainsi, toute chose dont tu donnes la zakāt est protégée du fait qu'on te la retire.<sup>3060</sup>"
    }
]

# Create missing Subpart 854 for Id al-Fitr zakāt
has_854 = False
for s in data[p171]['subparts']:
    if "854" in s['title']:
        has_854 = True
        s854 = s
        break

if not has_854:
    s854 = {
        "title": "854 - La zakāt de l' ‘īd al-Fitr (l'aumône légale obligatoire de la fin du Ramadan)",
        "hadiths": []
    }
    data[p171]['subparts'].append(s854)

eh(s854)
s854['hadiths'] = [
    {
        "number": "2712",
        "text": "L'Imām 'Alī (as) a dit : Allah utilise la zakāt de la fin du Ramadan de celui qui s'en acquitte pour compenser tout déficit [éventuel] de zakāt payée sur ses biens.<sup>3061</sup>"
    },
    {
        "number": "2713",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, donner la zakāt [de l' ‘īd al-Fitr] complète et achève le jeûne, tout comme l'envoi de prières sur le Prophète (s) complète et achève la prière ; ceci car en vérité, le jeûne de celui qui jeûne et ne s'est pas acquitté intentionnellement de la zakāt est invalide.<sup>3062</sup>"
    }
]

# ============================================================
# Part 172 (index 173) - LE TEMPS
# ============================================================
p172 = 173

# Subpart 856 - Le blâme du fait de faire confiance au temps
s856 = find_subpart(p172, "856"); eh(s856)
s856['hadiths'] = [
    {
        "number": "2721",
        "text": "L'Imām 'Alī (as) a dit : Celui qui se préoccupe du temps sera [en retour] accaparé par lui.<sup>3070</sup>"
    }
]

# Subpart 857 - Le blâme de l'obstination contre le temps
s857 = find_subpart(p172, "857"); eh(s857)
s857['hadiths'] = [
    {
        "number": "2722",
        "text": "L'Imām 'Alī (as) a dit : Celui qui blâme le temps verra ses reproches durer.<sup>3071</sup>"
    },
    {
        "number": "2723",
        "text": "L'Imām 'Alī (as) a dit : Celui qui s'obstine contre le temps sera mis au pas et contraint par lui, et celui qui se rend et s'abandonne à lui ne sera pas [non plus] préservé.<sup>3072</sup>"
    },
    {
        "number": "2724",
        "text": "L'Imām 'Alī (as) a dit : Celui qui s'obstine contre le temps s'épuisera, et celui qui lui voue du ressentiment finira en colère.<sup>3073</sup>"
    }
]

# Subpart 858 - L'incrimination du temps
s858 = find_subpart(p172, "858"); eh(s858)
s858['hadiths'] = [
    {
        "number": "2725",
        "text": "'Uyūn Akhbār al-Riḍā (as) : Al-Rayyān ibn al-Ṣalt : Al-Riḍā (as) m'a récité ces vers composés par 'Abd al-Muṭṭalib :<br><i>Les gens dans leur ensemble incriminent le temps alors que le défaut du temps n'est que nous-mêmes ;<br>Nous incriminons notre temps, alors que le défaut est en nous ;<br>Si le temps pouvait parler, il nous aurait brocardés.<br>En vérité, le loup délaisse [ne mange pas] la chair du loup, alors que nous nous entredévorons ouvertement.<br>Nous revêtons, pour tromper, de belles pelisses, malheur à l'étranger lorsqu'il vient à nous.</i><sup>3074</sup>"
    }
]

# ============================================================
# Part 173 (index 174) - L'ADULTÈRE
# ============================================================
p173 = 174

# Subpart 859 - L'interdiction de l'adultère
s859 = find_subpart(p173, "859")
if s859:
    s859['introduction'] = (
        "«<i>N'approchez pas l'adultère. En vérité, c'est une turpitude et quel mauvais chemin !</i>»<sup>3075</sup>"
        "<br><br><span class=\"reference-note\">(Voir également : Coran 24:33, 25:68)</span>"
    )

# ============================================================
# Sequential Sorting for all modified subparts
# ============================================================
modified_sections = [
    (p171, "851"), (p171, "852"), (p171, "853"), (p171, "854"),
    (p172, "856"), (p172, "857"), (p172, "858")
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

print("✅ Data successfully saved! Hadiths 2700-2713, 2721-2725, and Adultery Intro injected.")
