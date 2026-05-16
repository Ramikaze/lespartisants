import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    part30 = data[30]
    
    # Ensure enough subparts exist
    required_titles = [
        "La foi et l'islam",
        "La réalité de la foi",
        "La relation entre la foi et les actes",
        "La foi et les péchés",
        "Ce qui permet d'accomplir la foi",
        "L'augmentation de la foi"
    ]
    
    for i, title in enumerate(required_titles):
        if len(part30['subparts']) <= i:
            part30['subparts'].append({"title": title, "content": []})
        else:
            part30['subparts'][i]['title'] = title
            
    part30['subparts'][5]['introduction'] = "«<i>Et quand Ses versets leur sont récités, cela fait augmenter leur foi.</i>»<sup>612</sup>"
    part30['subparts'][5]['note'] = "(Voir également : Coran 2:260, 18:13-14, 33:22, 48:4, 58:22)"
    part30['subparts'][2]['note'] = "(Voir également : 290. Les actes)"

    # Overwrite 521 completely
    # First remove 521 if it exists in subpart 0
    part30['subparts'][0]['content'] = [h for h in part30['subparts'][0]['content'] if h.get('number') != "521"]

    updates = [
        (30, 0, {
            "number": "521",
            "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la foi est ce qui s'enracine dans les cœurs, tandis que l'islam est le moyen par lequel se réalisent les mariages, les héritages et [la préservation] de la vie des gens.<sup>583</sup>"
        }),
        (30, 1, {
            "number": "522",
            "text": "Le Messager d'Allah (s) a dit : La foi n'est pas dans l'embellissement et les souhaits que l'on formule ; la foi est plutôt ce qui est pur [et sincère] dans le cœur, et est attesté par les actes.<sup>584</sup>"
        }),
        (30, 1, {
            "number": "523",
            "text": "Le Messager d'Allah (s) a dit : La foi est la connaissance par le cœur, l'affirmation par la parole, et l'application de ses fondements.<sup>585</sup>"
        }),
        (30, 1, {
            "number": "524",
            "text": "Le Messager d'Allah (s) a dit : La foi est la patience et la bonté.<sup>586</sup>"
        }),
        (30, 1, {
            "number": "525",
            "text": "Le Messager d'Allah (s) a dit : En vérité, toute chose a une vérité, et le serviteur ne parvient à la vérité de la foi que lorsqu'il sait que ce qui l'a atteint ne pouvait pas ne pas l'atteindre, et que ce qui ne l'a pas atteint n'aurait pas pu l'atteindre.<sup>587</sup>"
        }),
        (30, 1, {
            "number": "526",
            "text": "Le Messager d'Allah (s) a dit : Le serviteur n'atteint la vérité de la foi que lorsqu'il ne se met en colère que pour Allah et qu'il n'est satisfait que pour Allah. Lorsqu'il agit ainsi, il mérite alors [d'atteindre] la vérité de la foi.<sup>588</sup>"
        }),
        (30, 1, {
            "number": "527",
            "text": "Le Messager d'Allah (s) a dit : Le serviteur ne devient réellement croyant que lorsqu'il souhaite le bien pour les autres autant qu'il le souhaite pour lui-même.<sup>589</sup>"
        }),
        (30, 1, {
            "number": "528",
            "text": "L'Imām 'Alī (as) a dit : La foi est la sincérité des actes [pour Allah].<sup>590</sup>"
        }),
        (30, 1, {
            "number": "529",
            "text": "L'Imām 'Alī (as) a dit : La foi est la patience dans le malheur et la gratitude dans l'aisance.<sup>591</sup>"
        }),
        (30, 1, {
            "number": "530",
            "text": "L'Imām 'Alī (as) a dit : La sincérité est à la source de la foi.<sup>592</sup>"
        }),
        (30, 1, {
            "number": "531",
            "text": "L'Imām 'Alī (as) a dit : La foi d'un serviteur n'est véritable que lorsque sa confiance en ce qui est détenu entre les mains d'Allah - loué soit-Il - est plus importante qu'en ce qu'il détient entre ses propres mains.<sup>593</sup>"
        }),
        (30, 1, {
            "number": "532",
            "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'une des vérités de la foi est de préférer la vérité vis-à-vis du faux, même si ce dernier est à votre avantage.<sup>594</sup>"
        }),
        (30, 2, {
            "number": "533",
            "text": "Le Messager d'Allah (s) a dit : La foi et les actes sont deux frères associés par un seul lien. Allah n'agrée pas l'un sans l'autre.<sup>595</sup>"
        }),
        (30, 2, {
            "number": "534",
            "text": "Le Messager d'Allah (s) a dit : Les Murji'ites<sup>596</sup> ont été maudits par soixante-dix prophètes. Ce sont ceux qui disent que la foi est l'attestation sans les actes.<sup>597</sup>"
        }),
        (30, 2, {
            "number": "535",
            "text": "L'Imām 'Alī (as) a dit : Si la foi se limitait à une simple parole, rien n'aurait été révélé pour cela à propos du jeûne, de la prière, ainsi que du licite et de l'illicite.<sup>598</sup>"
        }),
        (30, 2, {
            "number": "536",
            "text": "L'Imām al-Kāẓim (as) a dit : Toute la foi est basée sur les actes<sup>599</sup> tandis que la parole est une partie de ces actes qu'Allah a rendus obligatoires, comme Il l'a exprimé dans Son Livre.<sup>600</sup>"
        }),
        (30, 3, {
            "number": "537",
            "text": "Le Messager d'Allah (s) a dit : Aucun péché ne peut faire sortir le croyant de sa foi, tout comme aucun acte de bienfaisance ne peut faire sortir l'incroyant de sa mécréance.<sup>601</sup>"
        }),
        (30, 3, {
            "source": "Kanz al-'Ummāl :",
            "number": "538",
            "text": "Le Messager d'Allah (s) a dit : «Celui qui dit : «Point de divinité à part Dieu» (<i>lā ilāha illā Allāh</i>) avec sincérité entrera au Paradis.» On dit : «Que signifie cette sincérité ?» Il répondit : «C'est ce qui retient de s'approcher des interdits d'Allah.»<sup>602</sup>"
        }),
        (30, 3, {
            "number": "539",
            "text": "Le Messager d'Allah (s) a dit : [La parole] «Point de divinité à part Dieu» sera bénéfique à celui qui la prononce sauf lorsqu'il la dépréciera. Et la dépréciation à son égard apparaîtra lorsque les péchés seront ouvertement commis et que personne ne les rejettera ni ne cherchera à les corriger.<sup>603</sup>"
        }),
        (30, 3, {
            "number": "540",
            "text": "L'Imām al-Kāẓim (as), à qui il fut demandé si les grands péchés faisaient sortir de la foi, répondit : Oui, et les péchés moins graves également. Le Messager d'Allah (s) a dit : «Celui qui commet l'adultère ne le ferait pas s'il était encore un croyant, et le voleur ne volerait pas s'il était encore un croyant.»<sup>604</sup>"
        }),
        (30, 4, {
            "number": "541",
            "text": "Le Messager d'Allah (s) a dit : Trois qualités, lorsqu'elles sont présentes dans un individu, permettent l'accomplissement de sa foi : un homme qui, pour Allah, ne craint pas le reproche d'une personne qui lui en adresse, celui qui ne tire pas vanité de ses actes, et celui qui, lorsqu'il a le choix entre deux choses dont l'une est pour ce monde et l'autre pour l'Au-delà, choisit celle pour l'Au-delà au détriment de ce monde.<sup>605</sup>"
        }),
        (30, 4, {
            "number": "542",
            "text": "Le Messager d'Allah (s) a dit : Le serviteur n'a une foi accomplie que lorsqu'il aime pour son frère ce qu'il aime pour lui-même, et lorsqu'il craint Allah à la fois dans ses moments de plaisanterie et de sérieux.<sup>606</sup>"
        }),
        (30, 4, {
            "number": "543",
            "text": "Le Messager d'Allah (s) a dit : La foi du serviteur en Allah n'est accomplie que lorsqu'il acquiert cinq de ces caractéristiques : remettre sa confiance en Allah, confier ses affaires à Allah, se soumettre aux ordres d'Allah, être satisfait du destin décidé par Allah, et patienter face aux épreuves d'Allah. En vérité, celui qui aime pour Allah, déteste pour Allah, donne pour Allah, et s'abstient pour Allah aura ainsi accompli sa foi.<sup>607</sup>"
        }),
        (30, 4, {
            "number": "544",
            "text": "L'Imām 'Alī (as) a dit : Le plus parfait dans sa foi parmi vous est celui qui a le meilleur caractère.<sup>608</sup>"
        }),
        (30, 4, {
            "number": "545",
            "text": "L'Imām 'Alī (as) a dit : Celui qui possède ces trois qualités aura une foi accomplie : la raison, l'indulgence et le savoir.<sup>609</sup>"
        }),
        (30, 4, {
            "number": "546",
            "text": "L'Imām 'Alī (as) a dit : La foi d'un serviteur n'est complète que lorsqu'il aime celui qu'Allah - gloire à Lui - aime et lorsqu'il hait celui qu'Allah - gloire à Lui - hait.<sup>610</sup>"
        }),
        (30, 4, {
            "number": "547",
            "text": "L'Imām al-Ṣādiq (as) a dit : Le serviteur n'accomplit la vérité de la foi que lorsqu'il acquiert ces trois qualités : la compréhension de la religion, une juste planification de ses moyens de subsistance, et la patience face aux souffrances.<sup>611</sup>"
        }),
        (30, 5, {
            "number": "548",
            "text": "L'Imām 'Alī (as) a dit : En vérité, la foi apparaît comme un point blanc dans le cœur. Au fur et à mesure que la foi augmente, le blanc s'étend et lorsque la foi est accomplie, tout le cœur devient blanc.<sup>613</sup>"
        })
    ]

    for p_idx, s_idx, hadith in updates:
        content_list = data[p_idx]['subparts'][s_idx].setdefault('content', [])
        exists = any(h.get('number') == hadith['number'] for h in content_list)
        if not exists:
            content_list.append(hadith)
            print(f"Added {hadith['number']} to Part {p_idx}, Subpart {s_idx}")
        else:
            print(f"Hadith {hadith['number']} already exists.")

    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    # Replace the JSON array in the JS file content
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
