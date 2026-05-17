import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Gap 1: 648-659 -> Part 36 (Les Fléaux), Subpart 0
    # Gap 2: 674-687 -> Part 36 (Les Fléaux), Subpart 0
    updates_part36_subpart0 = [
        {"number": "648", "text": "L'Imām 'Alī (as) a dit : Toute chose à un fléau. Le fléau du savoir est l'oubli ; le fléau de l'adoration est la vantardise ; le fléau de la conscience est l'admiration de soi ; le fléau de la noblesse est l'orgueil ; le fléau de l'humour est l'absence de honte ; le fléau de la libéralité est le gaspillage ; le fléau de la pudeur est la faiblesse ; le fléau de l'indulgence est le déshonneur ; et le fléau de l'endurance est la dégénérescence.<sup>722</sup>"},
        {"number": "649", "text": "L'Imām 'Alī (as) a dit : La lâcheté est un fléau.<sup>723</sup>"},
        {"number": "650", "text": "L'Imām 'Alī (as) a dit : La passion est le fléau des intelligences.<sup>724</sup>"},
        {"number": "651", "text": "L'Imām 'Alī (as) a dit : Le fléau de la foi est l'associationnisme.<sup>725</sup>"},
        {"number": "652", "text": "L'Imām 'Alī (as) a dit : Le fléau de la certitude est le doute.<sup>726</sup>"},
        {"number": "653", "text": "L'Imām 'Alī (as) a dit : Le fléau des grâces est l'ingratitude.<sup>727</sup>"},
        {"number": "654", "text": "L'Imām 'Alī (as) a dit : Le fléau de l'obéissance est l'insoumission.<sup>728</sup>"},
        {"number": "655", "text": "L'Imām 'Alī (as) a dit : Le fléau de la noblesse est l'orgueil.<sup>729</sup>"},
        {"number": "656", "text": "L'Imām 'Alī (as) a dit : Le fléau de l'intelligence est la duperie.<sup>730</sup>"},
        {"number": "657", "text": "L'Imām 'Alī (as) a dit : Le fléau de l'adoration est la vantardise.<sup>731</sup>"},
        {"number": "658", "text": "L'Imām 'Alī (as) a dit : Le fléau de la générosité est de mentionner et de faire sentir ses largesses aux autres.<sup>732</sup>"},
        {"number": "659", "text": "L'Imām 'Alī (as) a dit : Le fléau de la religion est la suspicion.<sup>733</sup>"},
        
        {"number": "674", "text": "L'Imām 'Alī (as) a dit : Le fléau du courageux est le manque de détermination.<sup>748</sup>"},
        {"number": "675", "text": "L'Imām 'Alī (as) a dit : Le fléau du fort est de sous-estimer son rival.<sup>749</sup>"},
        {"number": "676", "text": "L'Imām 'Alī (as) a dit : Le fléau de l'indulgence est le déshonneur.<sup>750</sup>"},
        {"number": "677", "text": "L'Imām 'Alī (as) a dit : Le fléau du don est l'ajournement.<sup>751</sup>"},
        {"number": "678", "text": "L'Imām 'Alī (as) a dit : Le fléau de l'économie est l'avarice.<sup>752</sup>"},
        {"number": "679", "text": "L'Imām 'Alī (as) a dit : Le fléau du respect et de la révérence est la plaisanterie.<sup>753</sup>"},
        {"number": "680", "text": "L'Imām 'Alī (as) a dit : Le fléau de la quête est l'échec.<sup>754</sup>"},
        {"number": "681", "text": "L'Imām 'Alī (as) a dit : Le fléau de la souveraineté est le manque de protection.<sup>755</sup>"},
        {"number": "682", "text": "L'Imām 'Alī (as) a dit : Le fléau des pactes est la non-observance.<sup>756</sup>"},
        {"number": "683", "text": "L'Imām 'Alī (as) a dit : Le fléau de la présidence est la fierté.<sup>757</sup>"},
        {"number": "684", "text": "L'Imām 'Alī (as) a dit : Le fléau de la transmission [d'une parole] est le mensonge dans la narration.<sup>758</sup>"},
        {"number": "685", "text": "L'Imām 'Alī (as) a dit : Le fléau du savoir est sa non-application.<sup>759</sup>"},
        {"number": "686", "text": "L'Imām 'Alī (as) a dit : Le fléau de l'acte est l'abandon de la sincérité.<sup>760</sup>"},
        {"number": "687", "text": "L'Imām 'Alī (as) a dit : Le fléau de la générosité est la pauvreté.<sup>761</sup>"}
    ]

    for hadith in updates_part36_subpart0:
        content_list = data[36]['subparts'][0].setdefault('hadiths', [])
        if not any(h.get('number') == hadith['number'] for h in content_list):
            content_list.append(hadith)
            print(f"Added {hadith['number']} to Part 36, Subpart 0")
    
    # Sort hadiths in Part 36, Subpart 0 by number to maintain order
    data[36]['subparts'][0]['hadiths'].sort(key=lambda x: int(x['number']))

    # Gap 3: 709-718 -> Part 37 (L'Avarice)
    # 709-716 go to Subpart 0 (Mise en garde contre l'avarice)
    updates_part37_subpart0 = [
        {"number": "709", "text": "L'Imām 'Alī (as) a dit : L'avarice rassemble les vices de tous les défauts, c'est la bride par laquelle une personne est conduite vers tout mal.<sup>785</sup>"},
        {"number": "710", "text": "L'Imām 'Alī (as) a dit : L'avarice est un déshonneur.<sup>786</sup>"},
        {"number": "711", "text": "L'Imām 'Alī (as) a dit : L'avarice est l'habit de la misère.<sup>787</sup>"},
        {"number": "712", "text": "L'Imām 'Alī (as) a dit : L'avarice vis-à-vis de ce que l'on a est un manque de confiance envers Celui qui est adoré.<sup>788</sup>"},
        {"number": "713", "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve d'avarice dans ce qu'il détient sera humilié, mais celui qui est avare dans sa foi [qui ne l'abandonne pas facilement] sera élevé.<sup>789</sup>"},
        {"number": "714", "text": "L'Imām 'Alī (as) a dit : L'avarice humilie celui qui l'approche et honore celui qui s'en éloigne.<sup>790</sup>"},
        {"number": "715", "text": "L'Imām al-Riḍā (as) a dit : L'avarice brise la réputation.<sup>791</sup>"},
        {"number": "716", "text": "L'Imām al-Hādī (as) a dit : L'avarice est le plus répréhensible des comportements.<sup>792</sup>"}
    ]
    
    for hadith in updates_part37_subpart0:
        content_list = data[37]['subparts'][0].setdefault('hadiths', [])
        if not any(h.get('number') == hadith['number'] for h in content_list):
            content_list.append(hadith)
            print(f"Added {hadith['number']} to Part 37, Subpart 0")
            
    data[37]['subparts'][0]['hadiths'].sort(key=lambda x: int(x['number']))

    # 717-718 go to Subpart 1 (L'explication de l'avarice)
    updates_part37_subpart1 = [
        {"number": "717", "text": "Lorsque son père l'interrogea au sujet de l'avarice empreinte d'avidité, l'Imām Ḥasan (as) répondit : C'est lorsque tu considères ce que tu as entre les mains comme un honneur, et ce que tu as donné comme une perte.<sup>793</sup>"},
        {"number": "718", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, l'avare empreint d'avidité est celui qui nie le droit d'Allah et dépense pour autre chose que ce qui revient à Allah le Tout-Puissant.<sup>794</sup>"}
    ]
    
    for hadith in updates_part37_subpart1:
        content_list = data[37]['subparts'][1].setdefault('hadiths', [])
        if not any(h.get('number') == hadith['number'] for h in content_list):
            content_list.append(hadith)
            print(f"Added {hadith['number']} to Part 37, Subpart 1")
            
    data[37]['subparts'][1]['hadiths'].sort(key=lambda x: int(x['number']))

    # Save
    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
