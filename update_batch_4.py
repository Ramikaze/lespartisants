import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Update Part 16 - L'IMĀMAT (1) (Index 17) - Modify ONLY Subparts 100 to 110
    part16 = data[17]
    subparts_before = part16["subparts"][:11] # 89 to 99
    subparts_after = part16["subparts"][22:]  # 111 to 114
    
    new_subparts = [
        {
            "title": "100 - Vos Imāms sont vos délégués",
            "hadiths": [
                {"number": "318", "text": "Le Messager d'Allah (s) a dit : Vos Imāms sont vos délégués auprès d'Allah ; dès lors, considérez [attentivement] qui vous déléguez [et suivez] pour votre foi et votre prière.<sup>353</sup>"},
                {"number": "319", "text": "Le Messager d'Allah (s) a dit : En vérité, vos Imāms sont vos guides vers Allah ; dès lors, considérez [attentivement] qui vous suivez dans votre religion et vos prières.<sup>354</sup>"}
            ]
        },
        {
            "title": "101 - Celui qui accepte la gouvernance d'un Imam illégitime",
            "hadiths": [
                {"number": "320", "text": "L'Imām al-Bāqir (as) a dit : Allah le Béni et le Très-Haut a dit : Je châtierai tout groupe musulman qui accepte la gouvernance d'un Imām injuste qui n'est pas d'Allah.<sup>355</sup>"},
                {"number": "321", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui associe l'Imām dont l'Imāmat provient d'Allah à un autre Imām dont l'Imāmat ne provient pas d'Allah aura commis le péché de l'associationnisme.<sup>356</sup>"},
                {"number": "322", "text": "L'Imām al-Ṣādiq (as) a dit : Les bonnes actions des fidèles qui se sont alliés à un Imām illégitime non désigné par Allah le Très-Haut ne seront pas acceptées.<sup>357</sup>"}
            ]
        },
        {
            "title": "102 - Les dirigeants de l'Enfer",
            "introduction": "«<i>Nous fîmes d'eux des dirigeants [a'imma] qui appellent les gens au Feu.</i>»<sup>358</sup>",
            "hadiths": [
                {"number": "323", "text": "L'Imām 'Alī (as) a dit : En vérité, la pire personne auprès d'Allah est un dirigeant (<i>imām</i>) injuste qui est égaré et qui égare, car il abroge la tradition (<i>sunna</i>) appliquée et ravive l'hérésie abandonnée. J'ai entendu le Messager d'Allah (s) dire : «Le Jour de la Résurrection, l'Imām injuste sera amené seul, sans allié et sans excuse. Il sera jeté dans le feu de l'Enfer, y tournera tel un moulin, puis demeurera en son fond.»<sup>359</sup>"}
            ]
        },
        {
            "title": "103 - Les faux prétendants à l'Imāmat",
            "hadiths": [
                {"number": "324", "text": "L'Imām al-Bāqir (as) a dit en commentant la parole d'Allah «<i>Au Jour de la Résurrection, tu verras les visages de ceux qui mentaient sur Allah, assombris</i>»<sup>360</sup> : Ce sont ceux qui ont dit : «Je suis Imām» alors qu'ils n'étaient pas Imām.<sup>361</sup>"},
                {"number": "325", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui a prétendu à l'Imāmat sans en avoir la légitimité est un mécréant.<sup>362</sup>"}
            ]
        },
        {
            "title": "104 - Nulle obéissance à celui qui n'obéit pas à Allah",
            "introduction": "«<i>Et ils dirent : «Seigneur ! Nous avons obéi à nos chefs et à nos grands. Ce sont eux qui nous ont égarés du Sentier».</i>»<sup>363</sup>",
            "hadiths": [
                {"number": "326", "text": "Le Messager d'Allah (s) a dit : Pas d'obéissance à celui qui n'obéit pas à Allah.<sup>364</sup>"},
                {"number": "327", "text": "Le Messager d'Allah (s) a dit : ô 'Alī ! Parmi les quatre choses qui brisent le dos figurent un Imām qui désobéit à Allah et dont les ordres sont obéis...<sup>365</sup>"},
                {"number": "328", "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) a un jour levé une armée en mettant à sa tête un homme. Il ordonna aux soldats de l'écouter et de lui obéir. Ce dernier alluma un feu et demanda à ses subordonnés de se précipiter dedans. Une partie d'entre eux refusa et dit : «Nous voulions justement éviter le feu.» Un autre groupe accepta d'y aller. Quand ce récit parvint au Prophète (s), il dit [au sujet de ceux qui avaient refusé de se jeter dans le feu] : «S'ils y étaient allés, ils y seraient restés définitivement.» Il ajouta : «Il ne faut pas obéir [à celui qui appelle à] la désobéissance à Allah ; en vérité, l'obéissance doit être [lorsque l'on appelle] au bien.»<sup>366</sup>"}
            ]
        },
        {
            "title": "105 - L'obligation de se révolter contre les dirigeants tyranniques",
            "hadiths": [
                {"number": "329", "text": "<i>Al-Durr al-Manthūr</i> : Le Messager d'Allah (s) a dit : La meule de l'islam viendra bientôt à tourner ; là où ira le Coran suivez-le, car viendra une époque où le gouverneur et le Coran se combattront et se sépareront. Vous serez gouvernés par des rois qui vous dirigeront d'une certaine manière et appliqueront d'autres lois pour eux-mêmes. Si vous leur obéissez, ils vous égareront et si vous leur désobéissez, ils vous tueront. Quelqu'un demanda : «Ô Messager d'Allah ! Comment devrons-nous agir si nous assistons à cela ?» Il (s) répondit : «[Agissez] comme les apôtres de Jésus, qui furent découpés avec la scie et portés sur des croix. La mort en état d'obéissance [à Allah] est meilleure que la vie dans la désobéissance.»<sup>367</sup>"}
            ]
        },
        {
            "title": "106 - Ce qui autorise à ne pas se révolter",
            "hadiths": [
                {"number": "330", "text": "L'Imām al-Bāqir (as) a dit : Si se rallie à l'Imām (as) un nombre équivalent au nombre des hommes présents lors de la bataille de Badr, soit trois-cent treize, il sera obligé de se soulever [contre le dirigeant illégitime] et de changer la situation.<sup>368</sup>"},
                {"number": "331", "text": "<i>Al-Kāfī</i> : L'Imām al-Ṣādiq (as) a dit à Sadīr : «Par Allah, ô Sadīr, si j'avais des partisans au nombre de ces chevreaux, j'aurais été incapable de rester assis [de ne pas me révolter].» [Sadīr rapporte :] Nous avons mis pied à terre et prié. Après notre prière, je me suis dirigé vers les chevreaux et je les ai comptés : il y en avait [seulement] dix-sept.<sup>369</sup>"}
            ]
        },
        {
            "title": "107 - L'élection de l'Imām",
            "hadiths": [
                {"number": "332", "text": "<i>Kamāl al-Dīn</i> : Sa'ad ibn 'Abdillāh al-Qummī rapporte que lorsqu'il interrogea l'Imām al-Mahdī ('aj) sur la raison qui empêchait la communauté d'élire elle-même son Imām, il ('aj) répondit : «L'Imām est-il un réformateur ou un corrupteur ?» Je [al-Qummī] répondis : «C'est un réformateur.» Il (as) dit : «Est-il possible qu'un homme corrupteur soit élu par eux, étant donné qu'aucune [des personnes qui l'élisent] ne sait ce qui passe de bon et de mauvais dans son esprit ?» Je répondis : «Oui.» Il dit : «C'est la raison.»<sup>370</sup>"}
            ]
        },
        {
            "title": "108 - Le ḥadīth des deux trésors (thaqalayn)",
            "hadiths": [
                {"number": "333", "text": "Le Messager d'Allah (s) a dit : Je laisse deux trésors (<i>thaqalayn</i>)<sup>371</sup> parmi vous ; si vous vous agrippez à eux, vous ne vous égarerez jamais après moi. L'un est plus grand et élevé que l'autre. [L'un est] le Livre d'Allah, qui est une corde tendue du ciel vers la terre ; [l'autre est] ma descendance, les gens de ma famille. Sachez qu'ils [le Coran et ma descendance] ne se sépareront que lorsqu'ils me rejoindront au bord des eaux du Paradis.<sup>372</sup>"}
            ]
        },
        {
            "title": "109 - L'obligation de rester aux côtés des Gens de la demeure prophétique (as)",
            "hadiths": [
                {"number": "334", "text": "Le Messager d'Allah (s) a dit : En vérité, l'exemple des Gens de ma demeure est pour vous comme celui de l'arche de Noé : celui qui y embarqua fut sauvé, et celui qui resta dernière fut noyé.<sup>373</sup>"},
                {"number": "335", "text": "L'Imām 'Alī (as) a dit : Observez les gens de la demeure de votre Prophète, engagez-vous dans leur direction et suivez leurs pas, car ils ne vous feront jamais quitter la guidance, ils ne vous mèneront jamais à la destruction. S'ils sont assis [ne se révoltent pas], asseyez-vous et s'ils se lèvent, levez-vous.<sup>374</sup>"},
                {"number": "336", "text": "L'Imām 'Alī (as) a dit : En effet, l'exemple de la famille de Muḥammad (s) est comme celui des étoiles dans le ciel : lorsqu'une étoile s'éteint, une autre naît. Ainsi, les bienfaits d'Allah ont été parachevés pour vous, et Il vous a montré ce à quoi vous aspiriez.<sup>375</sup>"},
                {"number": "337", "text": "L'Imām 'Alī (as) a dit : Nous sommes l'arbre de la Prophétie, le lieu où s'établit la Révélation, le lieu de la venue des Anges, les mines du savoir et les sources de la sagesse.<sup>376</sup>"},
                {"number": "338", "text": "L'Imām 'Alī (as) a dit : En vérité, les Imāms sont les administrateurs d'Allah sur Sa création, ils font connaître Allah aux créatures ; n'entrera au Paradis que celui qui les reconnaît et qu'ils reconnaissent, et n'entrera en Enfer que celui qui les renie et qu'ils renient.<sup>377</sup>"},
                {"number": "339", "text": "L'Imām 'Alī (as) a dit : Nous [la famille du Prophète (s)] sommes comme la place du milieu sur une selle : celui assis en arrière qui glisse doit revenir vers l'avant [la place du milieu], et celui assis en avant qui glisse doit revenir vers l'arrière.<sup>378</sup>"},
                {"number": "340", "text": "L'Imām al-Ṣādiq (as) a dit en décrivant l'état des Imāms et leurs caractéristiques : Allah a fait d'eux [la source de] vie des morts, les lampes des ténèbres, les clés de l'éloquence et les fondations de l'islam.<sup>379</sup><br><br><span class=\"reference-note\">(Voir également : 288. Le savoir, section 1367)</span>"}
            ]
        },
        {
            "title": "110 - La raison de l'oppression contre les Gens de la demeure prophétique (as)",
            "hadiths": [
                {"number": "341", "text": "L'Imām 'Alī (as) a dit : La raison de l'oppression contre nous concernant ce rang [du califat] - alors que nous sommes supérieurs de par notre filiation et avons les liens les plus proches avec le Messager d'Allah (s) - est l'attraction [pour le pouvoir]. Les âmes de certains ont été avides et d'autres âmes [les Gens de la demeure] sont restées indifférentes à cela - le Juge en sera Allah.<sup>380</sup>"}
            ]
        }
    ]
    
    part16["subparts"] = subparts_before + new_subparts + subparts_after
    data[17] = part16

    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
