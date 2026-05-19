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
# Chapter 140 (index 141) - L'INVOCATION (suite)
# ============================================================
P = 141

# Section 685 (continuation)
s = find_subpart(P, "685"); eh(s)
s['hadiths'].extend([
    {"number": "2088", "text": "L'Imām 'Alī (as) a dit dans une recommandation à son fils Ḥasan (as) : «Sache que Celui qui détient les richesses des royaumes de ce bas-monde et de l'Au-delà t'a autorisé à L'invoquer et Il en a garanti l'acceptation. Il t'a ordonné de Lui demander afin qu'Il te donne, et Il est Très-Miséricordieux et Généreux. Il n'a mis entre toi et Lui aucune barrière et Il ne t'a renvoyé à aucun intercesseur pour intervenir auprès de Lui… Puis Il a mis entre tes mains les clés de Ses trésors qui sont l'autorisation de L'invoquer. Ainsi, dès que tu le souhaites, tu implores l'ouverture des portes de Ses trésors par l'invocation.»<sup>2361</sup>"},
    {"number": "2089", "text": "L'Imām 'Alī (as) a dit : L'invocation est la clé de la miséricorde et la lampe des ténèbres.<sup>2362</sup>"},
    {"number": "2090", "text": "L'Imām 'Alī (as) a dit : Le plus aimé des actes sur terre auprès d'Allah le Tout-Puissant est l'invocation.<sup>2363</sup>"},
    {"number": "2091", "text": "L'Imām 'Alī (as) a dit : L'invocation est le bouclier du croyant.<sup>2364</sup>"},
    {"number": "2092", "text": "L'Imām al-Ṣādiq (as) a dit : Je vous conseille vivement l'invocation, car en vérité c'est un remède à tout mal.<sup>2365</sup>"},
    {"number": "2093", "text": "<em>Al-Kāfī</em> : Muyassar ibn 'Abd al-'Azīz rapporte de Abū 'Abdallah [l'Imām al-Ṣādiq] (as) : L'Imām m'a dit : «Ô Muyassar ! Invoque et ne dis pas «s'en est fini» [c'est-à-dire tout a été déterminé]. En vérité, il existe une station auprès d'Allah le Tout-Puissant n'est atteinte que par la demande.»<sup>2366</sup>"},
    {"number": "2094", "text": "L'Imām al-Ṣādiq (as) a dit : L'invocation est plus percutante que les lances de fer affilées.<sup>2367</sup>"},
    {"number": "2095", "text": "<em>Al-Kāfī</em> : L'Imām al-Riḍā (as) a dit : «Je vous conseille vivement d'utiliser l'arme des prophètes.» Il lui fut alors demandé : «Quelle est donc l'arme des prophètes ?» Il répondit : «L'invocation.»<sup>2368</sup>"}
])

# Section 686
s = find_subpart(P, "686"); eh(s)
s['hadiths'].extend([
    {"number": "2096", "text": "Le Messager d'Allah (s) a dit : Ne repousse le destin que l'invocation.<sup>2369</sup>"},
    {"number": "2097", "text": "L'Imām Zayn al-'Ābidīn (as) a dit : L'invocation repousse le malheur descendu et celui qui n'est pas encore descendu.<sup>2370</sup>"},
    {"number": "2098", "text": "L'Imām al-Kāẓim (as) a dit : Pratiquez l'invocation car l'invocation est pour Allah. Adresser sa requête à Allah repousse le malheur bien qu'il ait été décidé et résolu et qu'il ne lui reste plus qu'à être appliqué. En effet, quand Allah le Tout-Puissant est invoqué et qu'on Lui demande d'éloigner un malheur, il est éloigné.<sup>2371</sup>"}
])

# Section 687
s = find_subpart(P, "687"); eh(s)
s['hadiths'].extend([
    {"number": "2099", "text": "Le Messager d'Allah (s) a dit : Fermez les portes du malheur par l'invocation.<sup>2372</sup>"},
    {"number": "2100", "text": "L'Imām 'Alī (as) a dit : Repoussez les vagues du malheur par l'invocation. Celui qui est entouré de malheurs n'a pas plus besoin de l'invocation que celui qui est exempt et en sécurité face au malheur.<sup>2373</sup>"},
    {"number": "2101", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui craint d'être atteint par un malheur et qui fait des invocations avant qu'il ne lui arrive, Allah le Tout-Puissant lui épargnera ce malheur définitivement.<sup>2374</sup><br><br><span class=\"reference-note\">(Voir également : 51. L'épreuve, section 275)</span>"}
])

# Section 688
s = find_subpart(P, "688"); eh(s)
s['introduction'] = "«Lorsqu'un malheur touche l'homme, il invoque son Seigneur en se tournant vers Lui. Puis lorsqu'Il lui accorde de Sa part un bienfait, il oublie la raison pour laquelle il invoquait, et il assigne à Allah des égaux, afin d'égarer [les gens] de Son chemin. Dis : «Jouis de ta mécréance un court moment. Tu fais partie des gens du Feu.»»<sup>2375</sup><br><br>«N'est-ce pas Lui qui répond à l'angoissé quand il L'invoque, et qui dissipe le mal, et qui vous fait succéder sur la terre, génération après génération, - y a-t-il donc une divinité avec Allah ? Comme il est rare que vous vous rappeliez !»<sup>2376</sup><br><br><span class=\"reference-note\">(Voir également : Coran 39:49, 10:22, 29:65, 30:33, 6:40-41, 6:63 et 17:67)</span>"
s['hadiths'].extend([
    {"number": "2102", "text": "Le Messager d'Allah (s) a dit : Allah le Béni et le Très-Haut a révélé à David (as) : «Rappelle-toi de Moi dans tes bons jours afin que Je te réponde [et t'aide] dans tes mauvais jours.»<sup>2377</sup>"},
    {"number": "2103", "text": "Le Messager d'Allah (s) a dit : Fais-toi connaître à Allah dans ton aisance afin qu'Il te reconnaisse dans [les moments de] malheur.<sup>2378</sup>"},
    {"number": "2104", "text": "L'Imām al-Bāqir (as) a dit : L'invocation du croyant dans l'aisance doit être semblable à son invocation dans [les moments de] malheur.<sup>2379</sup>"}
])

# Section 689
s = find_subpart(P, "689"); eh(s)
s['hadiths'].extend([
    {"number": "2105", "text": "<em>Biḥār al-Anwār</em> : Parmi Ses révélations à Moïse (as), Allah a dit : Ô Moïse ! Demande-Moi toute chose dont tu as besoin, même le fourrage de tes brebis et le sel de ta pâte.<sup>2380</sup>"},
    {"number": "2106", "text": "Le Messager d'Allah (s) a dit : Demandez à Allah tout vos besoins, même le lacet de votre sandale, car en vérité, si Allah ne vous le facilite pas, cela ne vous sera pas facilité [ni acquis].<sup>2381</sup>"},
    {"number": "2107", "text": "L'Imām al-Bāqir (as) a dit : Ne considérez pas comme insignifiants vos petits besoins, car en vérité, le croyant le plus aimé par Allah le Très-Haut est celui qui Lui demande le plus.<sup>2382</sup>"}
])

# Section 690
s = find_subpart(P, "690"); eh(s)
s['introduction'] = "«Quand Mes serviteurs t'interrogent sur Moi… alors Je suis tout proche. Je réponds à l'appel de celui qui M'invoque lorsqu'il M'invoque. Qu'ils répondent à Mon appel et qu'ils croient en Moi, afin qu'ils soient bien guidés.»<sup>2383</sup>"
s['hadiths'].extend([
    {"number": "2108", "text": "Le Messager d'Allah (s) a dit : Lorsqu'Allah veut exaucer un serviteur, Il lui permet de L'invoquer.<sup>2384</sup>"},
    {"number": "2109", "text": "L'Imām 'Alī (as) a dit : Celui qui frappe à la porte d'Allah - loué soit-Il -, elle lui sera ouverte.<sup>2385</sup>"},
    {"number": "2110", "text": "L'Imām Ḥasan (as) a dit : Allah le Tout-Puissant n'a nullement ouvert la porte de la demande à l'être pour lui fermer ensuite la porte de l'exaucement.<sup>2386</sup>"}
])

# Section 691 - Les conditions de l'exaucement
s = find_subpart(P, "691"); eh(s)
s['hadiths'].extend([
    {"number": "2111", "text": "<strong>1 - La connaissance</strong><br><br>L'Imām al-Ṣādiq (as) a répondu à un groupe qui lui demanda : «[Pourquoi] invoquons-nous et ne sommes-nous pas exaucés ?» : «Parce que vous invoquez Celui que vous ne connaissez pas.»<sup>2387</sup>"},
    {"number": "2112", "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut : «<em>Qu'ils répondent à Mon appel et qu'ils croient en Moi</em>»<sup>2388</sup> : Cela signifie : «Ils doivent savoir que Je suis capable de leur donner ce qu'ils Me demandent.»<sup>2389</sup>"},
    {"number": "2113", "text": "<strong>2 - Agir en fonction de ce que la connaissance nécessite</strong><br><br>Lorsqu'il fut interrogé au sujet de la parole du Très-Haut : «<em>Invoquez-Moi, Je vous répondrai</em>»<sup>2390</sup> et qu'il lui fut demandé : «Pourquoi [arrive-t-il que] nous invoquions sans être exaucés ?», l'Imām 'Alī (as) répondit : «En vérité, vos cœurs ont trahi de huit manières : la première est que vous connaissez Allah mais vous ne vous acquittez pas de ce dont vous Lui êtes redevables ainsi qu'Il vous l'a ordonné. Dès lors, votre connaissance ne vous a été d'aucun bénéfice… Quelle invocation voulez-vous qu'Il exauce dans ces conditions, alors que vous avez fermé ses portes et ses voies ?»<sup>2391</sup>"},
    {"number": "2114", "text": "<strong>3 - La licéité des revenus</strong><br><br>Le Messager d'Allah (s) a dit : En vérité, lorsque le serviteur lève les mains vers Allah [pour L'invoquer] alors que sa nourriture est illicite, comment sera-t-il exaucé alors qu'il est dans cet état ?<sup>2392</sup>"},
    {"number": "2115", "text": "Le Messager d'Allah (s) a dit : Rends licite tes revenus et ton invocation sera exaucée car en vérité, si l'homme consomme une bouchée (illicite), aucune de ses invocations ne sera exaucée pendant quarante jours.<sup>2393</sup>"},
    {"number": "2116", "text": "L'Imām al-Ṣādiq (as) a dit : Si l'un de vous veut être exaucé, que ses revenus soient licites et qu'il répare les injustices qu'il a perpétrées envers les autres. En vérité, l'invocation d'un serviteur qui a dans son ventre de l'illicite ou qui a perpétré une injustice à l'encontre de l'une de Ses créatures ne sera pas élevée vers Allah.<sup>2394</sup>"},
    {"number": "2117", "text": "<strong>4 - La présence du cœur et sa sensibilité durant l'invocation</strong><br><br>Le Messager d'Allah (s) a dit : Sachez qu'Allah n'exauce pas l'invocation qui provient d'un cœur distrait et inattentif.<sup>2395</sup>"}
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 2088-2117 injected (pages 374-378)")
print("Chapter 140 - L'Invocation: sections 685-691")
print(f"Total hadiths added: 30")
