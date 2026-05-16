import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Part 51 - L'ÉPREUVE (Index 52)
    while len(data) <= 52:
        data.append({"title": "51 - L'ÉPREUVE", "subparts": []})
    part51 = data[52]
    while len(part51['subparts']) <= 5:
        part51['subparts'].append({"title": "...", "hadiths": []})
        
    part51['subparts'][0]['title'] = "Être éprouvé par le mal et le bien"
    part51['subparts'][0]['introduction'] = "«<i>Nous vous éprouvons par le mal et par le bien [à titre] de tentation.</i>»<sup>982</sup>"
    
    part51['subparts'][1]['title'] = "La philosophie de l'épreuve"
    part51['subparts'][1]['introduction'] = "«<i>Ceci afin qu'Allah éprouve ce que vous avez dans vos poitrines, et qu'Il purifie ce que vous avez dans vos cœurs. Et Allah connaît ce qu'il y a dans les cœurs.</i>»<sup>985</sup><br><br>«<i>Certes Nous vous éprouverons afin de distinguer ceux d'entre vous qui luttent [pour la cause d'Allah] et qui endurent, afin d'éprouver [de faire apparaître] vos nouvelles.</i>»<sup>986</sup><br><br>«<i>Celui qui a créé la mort et la vie pour vous éprouver [et savoir] qui de vous est le meilleur en œuvre, et c'est Lui le Puissant, le Pardonneur.</i>»<sup>987</sup>"
    
    part51['subparts'][2]['title'] = "La dureté des épreuves du croyant"
    part51['subparts'][2]['introduction'] = "«<i>Pensez-vous entrer au Paradis alors que vous n'avez pas encore subi des épreuves semblables à celles que subirent ceux qui vécurent avant vous ? Misère et maladie les avaient touchés ; et ils furent secoués jusqu'à ce que le Messager, et avec lui ceux qui avaient crus, se fussent écriés : «A quand donc le secours d'Allah ?» Certes, le secours d'Allah est sûrement proche.</i>»<sup>992</sup>"
    
    part51['subparts'][3]['title'] = "Le rôle des mauvais actes dans l'apparition des épreuves"
    part51['subparts'][3]['introduction'] = "«<i>Tout malheur qui vous frappe est dû à ce que vos mains ont acquis. Et Il pardonne beaucoup.</i>»<sup>996</sup>"
    
    part51['subparts'][4]['title'] = "Celui qui n'est pas éprouvé est méprisé par Allah"
    part51['subparts'][5]['title'] = "La grâce de l'épreuve"

    updates = [
        # Part 50 - LA DIFFUSION [DE L'ISLAM] (Index 51)
        (51, 1, {"number": "870", "text": "Le Messager d'Allah (s) a dit : La peur des gens ne doit pas empêcher l'un de vous de dire la vérité quand il la voit ou quand il en est témoin, car dire la vérité et faire le rappel d'un grand événement [l'Au-delà] ne rapproche pas le terme de la vie et n'éloigne pas la subsistance.<sup>971</sup>"}),
        (51, 1, {"number": "871", "text": "<b>5 - L'honnêteté</b><br><br>L'Imām al-Ṣādiq (as) a dit selon ce qui lui est attribué dans <i>Miṣbāḥ al-Sharī'a</i> : La meilleure des exhortations est la parole qui n'outrepasse pas les limites de l'honnêteté, ni l'acte les limites de la sincérité.<sup>972</sup>"}),
        (51, 1, {"number": "872", "text": "'Amrū ibn Abī al-Miqdām a dit : Lors de ma première rencontre avec lui, Abū Ja'far [l'Imām Bāqir] (as) m'a dit : Apprenez l'honnêteté avant la parole.<sup>973</sup>"}),
        (51, 1, {"number": "873", "text": "<b>6 - La bonté</b><br><br>Le Messager d'Allah (s) a dit : Facilitez et ne causez pas de difficultés [lorsque vous propagez la religion], suscitez l'apaisement et non le dégoût.<sup>974</sup>"}),
        (51, 1, {"number": "874", "text": "Le Messager d'Allah (s) a dit : J'ai reçu l'ordre de ménager les gens tout comme j'ai reçu l'ordre de transmettre le Message.<sup>975</sup>"}),
        (51, 1, {"number": "875", "text": "L'Imām al-Ṣādiq (as) a dit en s'adressant à 'Umar ibn Ḥanẓalah : Ô 'Umar ! Ne surchargez pas nos partisans (shī'a), soyez bons avec eux, car ils ne peuvent supporter ce que vous supportez.<sup>976</sup>"}),
        (51, 1, {"number": "876", "text": "<b>7 - Le bon conseil</b><br><br>«<i>Je vous transmets les messages de mon Seigneur, et je suis pour vous un conseiller digne de confiance.</i>»<sup>977</sup><br><br>L'Imām 'Alī (as) a dit en énonçant les vertus du vénérable Messager : [Allah] l'a envoyé alors que les gens étaient dans l'égarement et le doute, et plongés dans les dissensions. [...] Il (s) a prodigué de nombreux conseils, a suivi la [bonne] voie et a appelé [les gens] à la sagesse et à la bonne exhortation.<sup>978</sup>"}),
        (51, 1, {"number": "877", "text": "<b>8 - La correspondance du cœur et de la langue</b><br><br>L'Imām 'Alī (as) a dit dans les paroles qui lui sont attribuées : Quand il vient du cœur, le mot touche le cœur, mais s'il ne provient que de la langue, il n'ira pas au-delà de l'oreille.<sup>979</sup>"}),
        (51, 1, {"number": "880_placeholder", "text": "<b>9 - La diffusion par l'acte</b><br><br>L'Imām al-Ṣādiq (as) a dit : Invitez les gens au bien par autre chose que vos langues afin qu'ils voient en vous l'assiduité, l'honnêteté et la piété.<sup>980</sup>", "number": "878"}),
        (51, 1, {"number": "879", "text": "L'Imām al-Ṣādiq (as) a dit : Qu'Allah répande Sa miséricorde sur les gens qui sont une lumière et un phare [une guidance] ; ils appellent les autres à notre cause au travers de leurs actes et par le meilleur de leurs efforts.<sup>981</sup><br><br><span class=\"reference-note\">(Voir également : 273. La bienséance (2), section 1289)</span>"}),

        # Part 51 - L'ÉPREUVE (Index 52)
        (52, 0, {"number": "880", "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a pas de tension ou d'aisance qui ne soit de la part d'Allah une faveur ou une épreuve.<sup>983</sup>"}),
        (52, 0, {"number": "881", "text": "L'Imām al-Ṣādiq (as) a dit : Toute chose ayant une tension ou une aisance issue de ce qu'Allah a ordonné ou interdit implique une épreuve et un jugement d'Allah.<sup>984</sup>"}),
        
        (52, 1, {"number": "882", "text": "L'Imām 'Alī (as) a dit : En vérité, Allah le Très-Haut a révélé le for intérieur des gens - non pas qu'Il ignorait les secrets bien gardés qu'ils cachent au fond de leur conscience, mais pour les éprouver et [voir] qui est le meilleur en œuvre, afin que la rétribution soit une récompense [des bonnes actions] et le châtiment, une punition [des mauvaises].<sup>988</sup>"}),
        (52, 1, {"number": "883", "text": "L'Imām 'Alī (as) a dit : Plus l'épreuve et l'examen sont importants, plus la récompense et la rétribution sont conséquentes. Ne voyez-vous pas qu'Allah - loué soit-Il - a mis à l'épreuve les premiers hommes depuis Adam - que la paix d'Allah soit sur lui - jusqu'aux derniers de ce monde par des pierres qui ne sont ni maléfiques ni bénéfiques, et de surcroît aveugles et sourdes ? [et qu'] Il a fait construire avec ces pierres Sa maison sacrée qu'Il a érigée pour les gens en tant que lieu de droiture... ?!<br>Toutefois, Allah éprouve Ses serviteurs par différentes afflictions, les astreint à de nombreux efforts, et les éprouve par toutes sortes de malheurs pour faire sortir l'orgueil de leurs cœurs et installer l'humilité dans leurs âmes, afin de faire de cela des portes ouvertes vers Sa grâce et des moyens de soumission pour [se préparer à recevoir] Son pardon.<sup>989</sup>"}),
        (52, 1, {"number": "884", "text": "L'Imām 'Alī (as) a dit : En vérité, vous serez secoués et tamisés jusqu'à ce que ceux parmi vous qui sont en bas se retrouvent en haut et ceux parmi vous qui sont en haut se retrouvent en bas, ainsi que ceux qui étaient à l'arrière devancent les autres, et ceux qui étaient devant soient devancés.<sup>990</sup>"}),
        (52, 1, {"number": "885", "text": "L'Imām 'Alī (as) a dit : Ne te réjouis point de la richesse et de l'aisance et ne t'attriste pas de la pauvreté et du malheur car en vérité, l'or est testé par le feu et le croyant est testé par l'épreuve.<sup>991</sup>"}),
        
        (52, 2, {"number": "886", "text": "L'Imām 'Alī (as) a dit : En vérité, l'épreuve [atteint] plus vite le croyant pieux que la pluie [n'atteint] la terre.<sup>993</sup>"}),
        (52, 2, {"number": "887", "text": "L'Imām al-Ṣādiq (as) a dit : Les personnes les plus éprouvées sont les prophètes, ensuite leurs successeurs et leurs disciples, et ainsi de suite [en fonction de la piété des gens].<sup>994</sup>"}),
        (52, 2, {"number": "888", "text": "L'Imām al-Bāqir (as) a dit : En vérité, le croyant est éprouvé par toutes sortes d'épreuves et il peut mourir de toutes sortes de morts, hormis le suicide.<sup>995</sup>"}),
        
        (52, 3, {"number": "889", "text": "Le Messager d'Allah (s) a dit : Allah le Très-Haut a révélé à Job : «Sais-tu quel était ton péché vis-à-vis de Moi qui a fait que Je t'éprouve par ces épreuves ?» Il répondit : «Non.» Le Seigneur lui dit : «Tu es entré dans la cour du pharaon et tu l'as flatté par deux mots.»<sup>997</sup><br><br><span class=\"reference-note\">(Voir également : 149. Le péché, section 777)</span>"}),
        
        (52, 4, {"number": "890", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah déteste le renfermé malfaisant qui ne supporte jamais le moindre dommage dans son corps ou son argent.<sup>998</sup>"}),
        (52, 4, {"number": "891", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, je déteste qu'un homme soit préservé [des épreuves] dans cette vie et ne soit touché par aucun malheur.<sup>999</sup><br><br><span class=\"reference-note\">(Voir également : 362. La maladie, section 1652 ; 285. La santé, section 1326)</span>"}),
        
        (52, 5, {"number": "892", "text": "Le Messager d'Allah (s) a dit : En vérité, Allah nourrit Son serviteur croyant par des épreuves de la même façon que la mère nourrit son enfant de lait.<sup>1000</sup>"})
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
