import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Ensure Part 30 (La foi) has subpart 0
    part30 = data[30]
    if len(part30['subparts']) == 0:
        part30['subparts'].append({
            "title": "La foi et l'islam",
            "introduction": "«Les bédouins ont dit : «Nous avons la foi.» Dis: «Vous n'avez pas encore la foi. Dites plutôt: «Nous nous sommes seulement soumis», car la foi n'a pas encore pénétré dans vos cœurs.»<span class=\"footnote-ref\">580</span>",
            "content": []
        })

    updates = [
        (29, 13, {
            "number": "517",
            "text": "Le Messager d'Allah (s) a dit : Le Mahdī ('aj) réapparaîtra parmi les derniers de ma communauté. Allah l'abreuvera de pluie, de la terre sortiront des végétaux, la richesse sera donnée de façon abondante, le bétail augmentera et la communauté s'agrandira.<span class=\"footnote-ref\">577</span>"
        }),
        (29, 13, {
            "number": "518",
            "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Lorsque notre Qā'im se dressera, Allah fera disparaître tout défaut de nos partisans (shī'a). Il rendra leurs cœurs aussi solides que le fer et fera en sorte que la force d'un homme équivaille à celle de quarante. Ils seront les dirigeants de la terre et ses chefs.<span class=\"footnote-ref\">578</span>"
        }),
        (29, 13, {
            "number": "519",
            "text": "L'Imām al-Bāqir (as) a dit : Lorsque al-Qā'im se dressera, il proposera la foi à chaque personne vouant de l'inimitié aux Gens de la Demeure prophétique. Si elle y adhère réellement [cela sera pour son bien], sinon, il l'éliminera à moins qu'elle ne paie la capitation comme le font les Gens du livre [vivant en terre d'islam] actuellement. Il attachera à la taille de ces personnes une ceinture [zonnār, ceinture portée par les chrétiens de l'époque] et les fera sortir des villes [pour les exiler] dans ses environs.<span class=\"footnote-ref\">579</span>"
        }),
        (30, 0, {
            "number": "520",
            "text": "L'Imām al-Bāqir (as) a dit : La foi est le fait d'attester<span class=\"footnote-ref\">581</span> et d'agir, alors que l'islam est le fait d'attester sans acte.<span class=\"footnote-ref\">582</span>"
        }),
        (30, 0, {
            "number": "521",
            "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la"
        })
    ]

    for p_idx, s_idx, hadith in updates:
        content_list = data[p_idx]['subparts'][s_idx].setdefault('content', [])
        # Check if already exists
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
