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
# 1. Fill Gaps in Part 148 (index 149) - LE DÉSHONNEUR
# ============================================================
P_deshonneur = 149
s765 = find_subpart(P_deshonneur, "765")
eh(s765)

# Add hadiths 2382-2386
s765['hadiths'].extend([
    {
        "number": "2382",
        "text": "L'Imām 'Alī (as) a dit : Par peur du déshonneur, les gens le précipitent.<sup>2691</sup>"
    },
    {
        "number": "2383",
        "text": "L'Imām 'Alī (as) a dit : Celui qui dévoile ses malheurs aura consenti au déshonneur.<sup>2692</sup>"
    },
    {
        "number": "2384",
        "text": "L'Imām al-Bāqir (as) a dit : Il n'y a pas pire déshonneur que celui de la cupidité.<sup>2693</sup>"
    },
    {
        "number": "2385",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui aime la vie sera déshonoré.<sup>2694</sup>"
    },
    {
        "number": "2386",
        "text": "Kashf al-Ghumma : Lorsqu'un homme se plaint à l'Imām Ja'far al-Ṣādiq (as) d'un homme ayant commis une injustice envers lui, il lui répondit : «Aie de la patience envers lui.» Il rétorqua : «Les gens me prendront pour quelqu'un qui n'a pas d'honneur [personnel] !» Il répondit : «En vérité, le déshonoré est celui qui commet l'injustice.»<sup>2695</sup>"
    }
])

# Sort hadiths in section 765
s765['hadiths'].sort(key=lambda h: int(h['number']))
print(f"Subpart 765 updated. Hadiths: {[h['number'] for h in s765['hadiths']]}")

# ============================================================
# 2. Fill Gaps in Part 149 (index 150) - LE PÉCHÉ
# ============================================================
P_peche = 150
s766 = find_subpart(P_peche, "766")
eh(s766)

# Set introduction for section 766
s766['introduction'] = (
    "«<i>Évitez le péché apparent ou caché, [car] ceux qui acquièrent le péché seront rétribués "
    "selon ce qu'ils auront commis.</i>»<sup>2696</sup><br>"
    "«<i>Bien au contraire ! Ceux qui font le mal et qui se font cerner par leurs péchés, ceux-là "
    "sont les gens du Feu où ils demeureront éternellement.</i>»<sup>2697</sup>"
)

# Add hadiths 2387-2388
s766['hadiths'].extend([
    {
        "number": "2387",
        "text": "L'Imām 'Alī (as) a dit : Les péchés sont une maladie, le traitement est la demande de pardon et la guérison consiste à ne plus recommencer.<sup>2698</sup>"
    },
    {
        "number": "2388",
        "text": "L'Imām 'Alī (as) a dit : Ô homme ! Comment as-tu osé commettre des péchés, et qu'est-ce qui t'a trompé au sujet de ton Seigneur, et qu'est-ce qui t'a rendu si familier avec ta propre perte ?<sup>2699</sup>"
    }
])

# Sort hadiths in section 766
s766['hadiths'].sort(key=lambda h: int(h['number']))
print(f"Subpart 766 updated. Hadiths: {[h['number'] for h in s766['hadiths']]}")

# Update section 778 - Hadith 2448 continuation and add 2449-2450
s778 = find_subpart(P_peche, "778")
eh(s778)

# Find hadith 2448 to modify its text
h2448 = None
for h in s778['hadiths']:
    if h.get('number') == '2448':
        h2448 = h
        break

if h2448:
    h2448['text'] = (
        "<b>9 - Le pèlerinage obligatoire (ḥajj) et le pèlerinage recommandé ('umra) :</b> "
        "Le Messager d'Allah (s) a dit : Le pèlerinage recommandé ('umra) permet l'expiation des "
        "péchés commis depuis le précédent pèlerinage recommandé effectué. La rétribution du pèlerinage "
        "obligatoire (ḥajj) agréé est le Paradis, et certains péchés ne peuvent être pardonnés qu'à "
        "la station de 'Arafat [endroit situé à proximité de La Mecque où une partie du pèlerinage "
        "obligatoire est effectuée].<sup>2765</sup>"
    )
    print("Hadith 2448 successfully updated with continuation text.")
else:
    print("Warning: Hadith 2448 not found in subpart 778!")

# Add hadiths 2449-2450
s778['hadiths'].extend([
    {
        "number": "2449",
        "text": "<b>10 - La prière sur Muḥammad (s) et sa famille (as) :</b> L'Imām al-Riḍā (as) a dit : Que celui qui ne peut pas faire les actes qui lui permettent d'expier ses péchés, multiplie les prières sur Muḥammad et sur sa famille car en vérité, cela permet d'éradiquer totalement les péchés.<sup>2766</sup><br>(Voir également : 240. La prière (4), section 1148)"
    },
    {
        "number": "2450",
        "text": "<b>11 - La mort :</b> Le Messager d'Allah (s) a dit : La mort est une expiation des péchés commis par les croyants.<sup>2767</sup>"
    }
])

# Sort hadiths in section 778
s778['hadiths'].sort(key=lambda h: int(h['number']))
print(f"Subpart 778 updated. Hadiths: {[h['number'] for h in s778['hadiths']]}")

# ============================================================
# 3. Fill Gaps in Part 150 (index 151) - LA DIRECTION
# ============================================================
P_direction = 151
s779 = find_subpart(P_direction, "779")
eh(s779)

# Add hadiths 2451-2453
s779['hadiths'].extend([
    {
        "number": "2451",
        "text": "L'Imām al-Bāqir (as) a dit : N'aspire pas à être en tête afin que tu ne te retrouves pas en queue.<sup>2768</sup>"
    },
    {
        "number": "2452",
        "text": "L'Imām al-Ṣādiq (as) a dit : Prenez garde aux dirigeants qui prennent les rênes de la direction car par Allah, le bruit des pas [des gens qui le suivent] ne se fait entendre derrière un homme sans que cela ne l'anéantisse et qu'il anéantisse les autres avec lui.<sup>2769</sup>"
    },
    {
        "number": "2453",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui aspire à la direction sera anéanti.<sup>2770</sup>"
    }
])

# Sort hadiths in section 779
s779['hadiths'].sort(key=lambda h: int(h['number']))
print(f"Subpart 779 updated. Hadiths: {[h['number'] for h in s779['hadiths']]}")

# ============================================================
# Save Data
# ============================================================
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Data successfully saved!")
