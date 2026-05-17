import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part Index 31, Subpart Index 6 (179 - Les degrés de la foi)
    updates = [
        (31, 6, {"number": "549", "text": "Le Messager d'Allah (s) a dit : Le meilleur de la foi est que tu saches qu'Allah est avec toi où que tu sois.<sup>614</sup>"}),
        (31, 6, {"number": "550", "text": "Le Messager d'Allah (s) a dit : Le meilleur de la foi est la patience et la bonté.<sup>615</sup>"}),
        (31, 6, {"number": "551", "text": "Le Messager d'Allah (s) a dit : La foi a plus de soixante-dix branches. La meilleure d'entre elle est la parole «Point de divinité à part Dieu», et la plus basse est d'enlever ce qui est nocif sur le chemin [emprunté par les gens]. La pudeur est [aussi] l'une des branches de la foi.<sup>616</sup>"}),
        (31, 6, {"number": "552", "text": "L'Imām 'Alī (as) a dit : La bonne conviction [en Allah] est le meilleur de la foi.<sup>617</sup>"}),
        (31, 6, {"number": "553", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la foi comporte dix degrés semblables à une échelle sur laquelle on peut s'élever échelon après échelon. Que celui qui est au deuxième échelon ne dise pas à celui qui est encore au premier : «Tu n'es rien» avant qu'il n'atteigne lui-même le dixième échelon. Ne rabaisse pas celui qui est en-dessous de toi, car tu risques à ton tour d'être rabaissé par celui qui au-dessus de toi. Et quand tu vois quelqu'un qui est [un échelon] plus bas que toi, élève-le vers toi avec douceur et bonté. Ne lui impose pas ce qu'il ne peut supporter car tu le briseras. En vérité, celui qui brise un croyant aura comme obligation de le rétablir.<sup>618</sup>"}),
        (31, 6, {"number": "554", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Tout-Puissant a partagé la foi en sept parties : la bonté pieuse, la véracité, la certitude, le contentement, la fidélité, le savoir et l'indulgence.<sup>619</sup>"}),
    ]

    for p_idx, s_idx, hadith in updates:
        content_list = data[p_idx]['subparts'][s_idx].setdefault('hadiths', [])
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
