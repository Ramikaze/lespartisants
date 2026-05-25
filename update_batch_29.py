import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(part_index, search_str):
    for s in data[part_index].get('subparts', []):
        if search_str in s['title']:
            s.setdefault('hadiths', [])
            return s
    return None

# Part 147 - LE RAPPEL (DHIKR) is at index 148
p147 = 148

# ============================================================
# s750 - La vertu du rappel d'Allah
# ============================================================
s750 = find_subpart(p147, "750")
s750['introduction'] = "«Ô vous qui avez cru ! Que ni vos biens ni vos enfants ne vous distraient du rappel d'Allah. Et quiconque fait cela... alors ceux-là seront les perdants.»<sup>2607</sup>"
s750['hadiths'].extend([
    {
        "number": "2315",
        "text": "Le Messager d'Allah (s) a dit : Ne préférez rien au rappel d'Allah car en vérité, Il a dit : «Le rappel d'Allah est certes ce qu'il y a de plus grand.»<sup>2608,2609</sup>"
    },
    {
        "number": "2316",
        "source": "Kanz al-'Ummāl",
        "text": "Mu'ādh a dit : Le Messager d'Allah (s) a dit : «Il n'y a pas d'acte plus aimé d'Allah le Très-Haut et qui permet autant de sauver le serviteur de tout mal dans ce bas-monde et dans l'Au-delà que le rappel d'Allah.» On demanda : «Même [plus que] le combat dans le sentier d'Allah ?» Il (s) répondit : «Sans le rappel d'Allah, l'ordre du combat n'aurait pas été donné.»<sup>2610</sup>"
    },
    {
        "number": "2317",
        "text": "L'Imām 'Alī (as) a dit : Le rappel [d'Allah] est le plaisir de ceux qui aiment.<sup>2611</sup>"
    },
    {
        "number": "2318",
        "text": "L'Imām 'Alī (as) a dit : Le rappel est la compagnie de l'Aimé.<sup>2612</sup>"
    },
    {
        "number": "2319",
        "text": "L'Imām 'Alī (as) a dit : Le rappel d'Allah est la disposition naturelle de tout bienfaiteur et le trait distinctif de tout croyant.<sup>2613</sup>"
    }
])

# ============================================================
# s751 - L'incitation à multiplier le rappel [d'Allah]
# ============================================================
s751 = find_subpart(p147, "751")
s751['introduction'] = "«Ô vous qui croyez ! Évoquez Allah d'une façon abondante, et glorifiez-Le à la pointe et au déclin du jour.»<sup>2614</sup>"
s751['hadiths'].extend([
    {
        "number": "2320",
        "text": "Le Messager d'Allah (s) a dit : Vous devez réciter le Coran et multiplier le rappel d'Allah car en vérité, cela est un rappel pour vous dans le ciel et une lumière pour vous sur terre.<sup>2615</sup>"
    },
    {
        "number": "2321",
        "text": "L'Imām 'Alī (as) a dit : Celui qui pratique le rappel d'Allah en secret aura certainement abondamment pratiqué le rappel d'Allah.<sup>2616</sup>"
    },
    {
        "number": "2322",
        "text": "L'Imām al-Ṣādiq (as) a dit : Multipliez le rappel d'Allah autant que vous le pouvez à chaque heure de la nuit et du jour, car Allah a ordonné de pratiquer souvent Son rappel.<sup>2617</sup>"
    },
    {
        "number": "2323",
        "text": "L'Imām al-Ṣādiq (as) a dit : Les glorifications de Fāṭima al-Zahrā (as) font partie du rappel abondant à propos duquel Allah le Tout-Puissant a dit : «Évoquez Allah d'une façon abondante.»<sup>2618,2619</sup>"
    }
])

# ============================================================
# s752 - L'incitation à pratiquer continuellement le rappel [d'Allah]
# ============================================================
s752 = find_subpart(p147, "752")
s752['hadiths'].extend([
    {
        "number": "2324",
        "text": "Le Messager d'Allah (s) a dit : Le Jour du Jugement, l'homme regrettera chaque heure de sa vie passée durant laquelle il n'a pas pratiqué le rappel d'Allah.<sup>2620</sup>"
    },
    {
        "number": "2325",
        "text": "L'Imām 'Alī (as) a dit dans l'un de ses entretiens intimes [avec Allah] du mois de Sha'bān : Mon Dieu, inspire-moi la ferveur d'une évocation à une autre, et l'ardeur dans le plaisir d'atteindre Tes Noms et le lieu de Ta Sainteté.<sup>2621</sup>"
    },
    {
        "number": "2326",
        "text": "L'Imām 'Alī (as) a dit : [Mon Dieu], Je T'implore de prier sur Muḥammad et la famille de Muḥammad, fais en sorte que je sois parmi ceux qui se rappellent continuellement de Toi et qui ne brisent pas leur engagement vis-à-vis de Toi.<sup>2622</sup>"
    }
])

# ============================================================
# s753 - Le rappel d'Allah est un bien dans tous les cas
# ============================================================
s753 = find_subpart(p147, "753")
s753['introduction'] = "«En vérité, il y a dans la création des cieux et de la terre, et dans l'alternance de la nuit et du jour, des signes pour les doués d'intelligence qui, debout, assis, couchés sur leurs côtés, invoquent Allah et méditent sur la création des cieux et de la terre [disant] : «Notre Seigneur ! Tu n'as pas créé cela en vain. Gloire à Toi ! Préserve-nous du châtiment du Feu.»<sup>2623</sup>"
s753['hadiths'].extend([
    {
        "number": "2327",
        "text": "L'Imām 'Alī (as) a dit dans l'une de ses recommandations à son fils Ḥasan (as) au moment de sa mort : «Pratique le rappel d'Allah en toute situation.»<sup>2624</sup>"
    },
    {
        "number": "2328",
        "text": "L'Imām al-Ṣādiq (as) a dit : Moïse (as) a dit : «Ô Seigneur, je suis dans une [basse] situation où je considère que Ton rang est trop éminent pour que je pratique Ton rappel [à ce moment précis].» Et Allah lui dit : «Ô Moïse ! Pratique Mon rappel en toute situation.»<sup>2625</sup>"
    }
])

# ============================================================
# s754 - Ceux qui observent le rappel [d'Allah]
# ============================================================
s754 = find_subpart(p147, "754")
s754['hadiths'].extend([
    {
        "number": "2329",
        "text": "Le Messager d'Allah (s) a dit : Celui qui observe le rappel [d'Allah] au milieu des distraits est comme un combattant [dans la voie d'Allah] au milieu de ceux qui fuient.<sup>2626</sup>"
    },
    {
        "number": "2330",
        "text": "Le Messager d'Allah (s) a dit : Tout être mourra assoiffé, sauf celui qui observe le rappel d'Allah.<sup>2627</sup>"
    },
    {
        "number": "2331",
        "text": "Le Messager d'Allah (s) a dit : En vérité, lorsque Moïse ibn 'Imrān (as) s'entretint en secret avec son Seigneur, il dit : «Ô Seigneur ! Es-tu loin de moi pour que je T'appelle, ou bien proche de moi pour que je m'adresse à Toi en chuchotant ?» Et Allah – que Sa gloire soit glorifiée – lui inspira : «Je suis le compagnon [proche] de celui qui observe Mon rappel.»<sup>2628</sup>"
    },
    {
        "number": "2332",
        "text": "L'Imām 'Alī (as) a dit : Allah embellit le rappel [et la réputation] de celui qui est occupé à observer le rappel d'Allah.<sup>2629</sup>"
    },
    {
        "number": "2333",
        "text": "L'Imām 'Alī (as) a dit : Celui qui observe le rappel d'Allah – loué soit-Il – se tient en Sa compagnie.<sup>2630</sup>"
    },
    {
        "number": "2334",
        "text": "L'Imām al-Bāqir (as) a dit : Le croyant est en prière tant qu'il observe le rappel d'Allah, qu'il soit debout, assis ou couché. En vérité, Allah le Très-Haut a dit : «Qui, debout, assis, couchés sur leurs côtés, invoquent Allah.»<sup>2631,2632</sup>"
    },
    {
        "number": "2335",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la foudre ne touche jamais celui qui observe le rappel d'Allah le Tout-Puissant.<sup>2633</sup>"
    }
])

# ============================================================
# s755 - Rappelez-vous d'Allah et Il se rappellera de vous
# ============================================================
s755 = find_subpart(p147, "755")
s755['introduction'] = "«Souvenez-vous de Moi, Je me souviendrai de vous ! Remerciez-Moi et ne soyez pas ingrats envers Moi !»<sup>2634</sup>"
s755['hadiths'].extend([
    {
        "number": "2336",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah le Très Haut a dit : «Fils d'Adam ! Souviens-toi de Moi en toi-même et Je Me souviendrai de toi en Moi-même. Fils d'Adam ! Souviens-toi de Moi dans ta solitude [en secret] et Je Me souviendrai de toi dans ta solitude [en secret]. Fils d'Adam ! Souviens-toi de Moi en public et Je Me souviendrai de toi devant un public meilleur que le tien.»<sup>2635</sup>"
    }
])

# ============================================================
# s756 - Les fruits du rappel [d'Allah]
# ============================================================
s756 = find_subpart(p147, "756")
s756['introduction'] = "«Ceux qui ont cru et dont les cœurs se tranquillisent au rappel d'Allah. N'est-ce pas par le rappel d'Allah que se tranquillisent les cœurs ?»<sup>2636</sup>"
s756['hadiths'].extend([
    {
        "number": "2337",
        "text": "Le Messager d'Allah (s) a dit : Le rappel d'Allah est un remède pour les cœurs.<sup>2637</sup>"
    },
    {
        "number": "2338",
        "text": "Le Messager d'Allah (s) a dit : Celui qui multiplie le rappel d'Allah sera affranchi de l'hypocrisie.<sup>2638</sup>"
    },
    {
        "number": "2339",
        "text": "Le Messager d'Allah (s) a dit : Allah aimera celui qui multiplie Son rappel.<sup>2639</sup>"
    },
    {
        "number": "2340",
        "text": "L'Imām 'Alī (as) a dit : Celui qui fait prospérer son cœur en pratiquant constamment le rappel d'Allah verra ses actes s'améliorer, qu'ils soient faits en secret ou en public.<sup>2640</sup>"
    },
    {
        "number": "2341",
        "text": "L'Imām 'Alī (as) a dit : L'origine de la réforme du cœur se trouve dans le fait de l'occuper avec le rappel d'Allah.<sup>2641</sup>"
    },
    {
        "number": "2342",
        "text": "L'Imām 'Alī (as) a dit : Allah – loué soit-Il – ravive le cœur et illumine la raison ainsi que les tréfonds du cœur de celui qui pratique le rappel d'Allah.<sup>2642</sup>"
    },
    {
        "number": "2343",
        "text": "L'Imām 'Alī (as) a dit : Pratiquer le rappel d'Allah est une nourriture pour l'esprit et consiste à tenir compagnie à l'Aimé.<sup>2643</sup>"
    },
    {
        "number": "2344",
        "text": "L'Imām 'Alī (as) a dit : Pratiquez souvent le rappel d'Allah, car en vérité, cela illumine les cœurs.<sup>2644</sup>"
    },
    {
        "number": "2345",
        "text": "L'Imām 'Alī (as) a dit : La pratique continuelle du rappel [d'Allah] illumine le cœur et l'esprit.<sup>2645</sup>"
    },
    {
        "number": "2346",
        "text": "L'Imām 'Alī (as) a dit : En vérité, Allah – loué soit-Il – a fait en sorte que la pratique de [Son] rappel polisse les cœurs ; par cela, ils entendront après avoir été sourds, ils verront après avoir été malvoyants, et ils seront guidés après avoir été indociles.<sup>2646</sup>"
    },
    {
        "number": "2347",
        "text": "L'Imām 'Alī (as) a dit dans une invocation : Ô Celui dont le Nom est un remède et le rappel une guérison.<sup>2647</sup>"
    },
    {
        "number": "2348",
        "text": "L'Imām 'Alī (as) a dit : Le rappel [d'Allah] est la clé de la familiarité et de la proximité [avec Lui].<sup>2648</sup>"
    },
    {
        "number": "2349",
        "text": "L'Imām 'Alī (as) a dit : Si tu vois qu'Allah – loué soit-Il – te rend familier de Son rappel, alors Il t'aime ; et si tu vois qu'Allah te rend familier de Sa création et qu'Il t'éloigne de Son rappel, alors Il te déteste.<sup>2649</sup>"
    },
    {
        "number": "2350",
        "text": "L'Imām 'Alī (as) a dit : Le rappel d'Allah permet de repousser Satan.<sup>2650</sup>"
    },
    {
        "number": "2351",
        "text": "L'Imām 'Alī (as) a dit : Le rappel d'Allah polit les poitrines et apaise les cœurs.<sup>2651</sup>"
    },
    {
        "number": "2352",
        "text": "L'Imām 'Alī (as) a dit : Le rappel [d'Allah] élargit la poitrine.<sup>2652</sup>"
    }
])

# ============================================================
# s757 - L'incitation à pratiquer le rappel d'Allah dans certaines situations
# ============================================================
s757 = find_subpart(p147, "757")
s757['hadiths'].extend([
    {
        "number": "2353",
        "text": "<b>a - Lors de la rencontre de l'ennemi :</b> «Ô vous qui croyez ! Lorsque vous rencontrez une troupe [ennemie], soyez fermes, et invoquez beaucoup Allah afin de réussir.»<sup>2653</sup><br>L'Imām 'Alī (as) a dit : Lorsque vous êtes confrontés à votre ennemi durant le combat, diminuez vos paroles et multipliez le rappel d'Allah le Tout-Puissant.<sup>2654</sup>"
    },
    {
        "number": "2354",
        "text": "<b>b - Lorsque l'on entre dans les marchés :</b> L'Imām 'Alī (as) a dit : Multipliez le rappel d'Allah le Tout-Puissant lorsque vous entrez dans les marchés quand les gens sont occupés, car en vérité, cela permet d'effacer les péchés et d'augmenter les bonnes actions. Ainsi, vous ne serez pas inscrits parmi les distraits.<sup>2655</sup>"
    },
    {
        "number": "2355",
        "text": "<b>c - Lors de malheurs, lorsque l'on rend un jugement ou que l'on partage :</b> Le Messager d'Allah (s) a dit : Pratique le rappel d'Allah dans ta tristesse quand tu es triste, avec ta langue quand tu juges, et avec ta main quand tu dois effectuer un partage.<sup>2656</sup>"
    },
    {
        "number": "2356",
        "text": "<b>d - Lors de colère :</b> Le Messager d'Allah (s) a dit : Allah a révélé à l'un de Ses prophètes : «Ô fils d'Adam ! Rappelle-toi de Moi dans ta colère et Je me rappellerai de toi dans Ma colère. Et ainsi, Je ne t'annihilerai pas avec ceux que J'annihilerai.»<sup>2657</sup>"
    },
    {
        "number": "2357",
        "text": "<b>e - Dans la solitude et lors de plaisirs :</b> L'Imām al-Bāqir (as) a dit : Il est écrit dans la Thora : «[...] Ô Moïse ! [...] Rappelle-toi de Moi dans la solitude de la joie des plaisirs, et Je me rappellerai de toi lors de tes moments de négligence.»<sup>2658</sup>"
    }
])

# ============================================================
# s758 - La vérité profonde du rappel [d'Allah]
# ============================================================
s758 = find_subpart(p147, "758")
s758['hadiths'].extend([
    {
        "number": "2358",
        "text": "Le Messager d'Allah (s) a dit : Celui qui obéit à Allah le Tout-Puissant aura pratiqué le rappel d'Allah même si sa prière, son jeûne et sa psalmodie du Coran sont modestes.<sup>2659</sup>"
    },
    {
        "number": "2359",
        "text": "L'Imām al-Ṣādiq (as) a dit en commentant la parole du Très-Haut «Et le rappel d'Allah est certes ce qu'il y a de plus grand» : [Cela signifie] se rappeler d'Allah concernant ce qu'Il a rendu licite et illicite.<sup>2661</sup>"
    },
    {
        "number": "2360",
        "text": "L'Imām al-Ṣādiq (as) a dit : Il y a deux types de rappel [d'Allah] : un rappel sincère en accord avec le cœur, et un rappel exclusif qui fait disparaître le rappel de tout autre qu'Allah.<sup>2662</sup>"
    },
    {
        "number": "2361",
        "text": "L'Imām al-Ṣādiq (as) a dit : Pratique le rappel d'Allah pour qu'Il se rappelle de toi, car en vérité, Il se rappelle de toi alors qu'Il n'a nul besoin de toi. Ainsi, Son rappel de toi est plus noble, plus désirable, et plus complet que ton rappel de Lui, et il le précède... Dès lors, que celui qui veut pratiquer le rappel d'Allah le Très-Haut sache que tant qu'Allah ne se rappelle pas du serviteur en lui donnant ainsi la réussite [et la grâce] de se rappeler de Lui, le serviteur ne sera pas capable de se souvenir de Lui [et de pratiquer Son rappel].<sup>2663</sup>"
    },
    {
        "number": "2362",
        "text": "L'Imām al-Riḍā (as) a dit : Celui qui pratique le rappel d'Allah et qui n'anticipe pas Sa rencontre se sera moqué de sa propre personne.<sup>2664</sup>"
    }
])

# ============================================================
# s759 - Ce qui suscite la permanence du rappel [d'Allah]
# ============================================================
s759 = find_subpart(p147, "759")
s759['hadiths'].extend([
    {
        "number": "2363",
        "source": "Biḥār al-Anwār",
        "text": "Dans le ḥadīth de l'ascension [du Prophète (s), Allah le Très-Haut a dit] : «Ô Ahmad... Pratique Mon rappel de façon continue.» Il demanda : «Ô Seigneur, comment puis-je pratiquer Ton rappel de façon continue ?» Il répondit : «En t'isolant des gens, en méprisant le monde et la vie, et en vidant ton ventre et ta maison [des délices] de ce monde.»<sup>2665</sup>"
    },
    {
        "number": "2364",
        "text": "L'Imām 'Alī (as) a dit : Celui qui aime une chose est attaché à en pratiquer le rappel.<sup>2666</sup>"
    }
])

# ============================================================
# s760 - Ce qui empêche le rappel [d'Allah]
# ============================================================
s760 = find_subpart(p147, "760")
s760['introduction'] = "«Ô vous qui avez cru ! Que ni vos biens ni vos enfants ne vous distraient du rappel d'Allah. Et quiconque fait cela... alors ceux-là seront les perdants.»<sup>2667</sup><br><br>«Le Diable ne veut que jeter parmi vous, à travers le vin et le jeu de hasard, l'inimitié et la haine, et vous détourner de votre rappel d'Allah et de la ṣalāt. Allez-vous donc y mettre fin ?»<sup>2668</sup>"
s760['hadiths'].extend([
    {
        "number": "2365",
        "text": "L'Imām 'Alī (as) a dit : Il n'y a rien de pire parmi les transgressions que de suivre ses [mauvais] désirs et de persévérer dans ses péchés."
    }
])

# Save
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Batch 29 done: hadiths 2315-2365 added to Part 147 (Le rappel dhikr)")
