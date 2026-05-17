import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # Update Part 14 - L'ESPOIR (Index 15)
    data[15] = {
        "title": "14 - L'ESPOIR",
        "subparts": [
            {
                "title": "75 - L'espoir est une miséricorde",
                "hadiths": [
                    {"number": "233", "text": "Le Messager d'Allah (s) a dit : L'espoir est une miséricorde pour ma communauté. Sans l'espoir, la mère n'allaiterait pas le nouveau-né et le planteur ne planterait pas d'arbre.<sup>255</sup>"},
                    {"number": "234", "text": "L'Imām 'Alī (as) a dit : L'espoir est un aimable compagnon.<sup>256</sup>"},
                    {"number": "235", "text": "<i>Tanbīh al-Khawāṭir</i> : Alors que Jésus fils de Marie (as) était assis, [il vit] un vieillard qui retournait la terre avec une pelle. Jésus (as) dit : «Ô Allah, enlève-lui l'espoir.» L'homme posa sa pelle et s'allongea. Une heure passa, et Jésus dit : «Ô Allah, rends-lui l'espoir.» L'homme se leva et se remit au travail.<sup>257</sup>"}
                ]
            },
            {
                "title": "76 - L'espoir ne cesse jamais",
                "hadiths": [
                    {"number": "236", "text": "Le Messager d'Allah (s) a dit : Celui qui espère vivre jusqu'au lendemain espère vivre pour l'éternité.<sup>258</sup>"},
                    {"number": "237", "text": "L'Imām 'Alī (as) a dit : Il n'y a pas de fin à l'espoir.<sup>259</sup>"},
                    {"number": "238", "text": "L'Imām 'Alī (as) a dit : L'espoir ne cesse jamais.<sup>260</sup>"}
                ]
            },
            {
                "title": "77 - Mise en garde contre les faux espoirs",
                "introduction": "«<i>Laisse-les manger, jouir [un temps], et être distraits par l'espoir ; car bientôt ils sauront !</i>»<sup>261</sup>",
                "hadiths": [
                    {"number": "239", "text": "L'Imām 'Alī (as) a dit : Protégez-vous des faux espoirs, car une personne peut commencer le jour sans en voir la fin, et elle peut être enviée au début de la nuit et pleurée [pour sa mort] à la fin.<sup>262</sup>"},
                    {"number": "240", "text": "L'Imām 'Alī (as) a dit : Le [faux] espoir est comme un mirage, il séduit celui qui le voit et déçoit celui qui a placé en lui son espoir.<sup>263</sup>"},
                    {"number": "241", "text": "L'Imām 'Alī (as) a dit : Les espérances aveuglent les yeux de la clairvoyance.<sup>264</sup>"},
                    {"number": "242", "text": "L'Imām 'Alī (as) a dit : L'espérance est le pouvoir des démons sur le cœur des insouciants.<sup>265</sup>"},
                    {"number": "243", "text": "L'Imām 'Alī (as) a dit : Le résultat de l'espérance est la détérioration des actes.<sup>266</sup>"},
                    {"number": "244", "text": "L'Imām 'Alī (as) a dit : Le [faux] espoir distrait le cœur, fait de fausses promesses, augmente l'inattention et occasionne le regret.<sup>267</sup>"},
                    {"number": "245", "text": "L'Imām 'Alī (as) a dit : En vérité, l'espoir annihile la raison, fait de fausses promesses, incite à l'inattention et suscite le regret. Considérez l'espoir comme un mensonge car il est trompeur, tandis que la personne qui s'y adonne est en état de péché.<sup>268</sup>"},
                    {"number": "246", "text": "L'Imām al-Ṣādiq (as) a dit : Combien de grâces d'Allah sont répandues sur Son serviteur alors qu'il ne les espérait pas, et combien de personnes espèrent une chose alors que le choix [d'Allah] est autre.<sup>269</sup>"}
                ]
            },
            {
                "title": "78 - L'espoir et l'échéance de la vie",
                "hadiths": [
                    {"number": "247", "text": "<i>Tanbīh al-Khawāṭir</i> : Il est rapporté que le Messager d'Allah (s) prit trois bâtonnets. Il en planta un dans le sol, mit le deuxième à côté, et éloigna le troisième. Puis il demanda : «Savez-vous ce que c'est ?» Les compagnons répondirent: «Allah et Son Messager sont plus savants.» Il dit: «Ceci est l'être humain, ceci [le bâtonnet se trouvant à côté] est l'échéance [c'est-à-dire la mort], et ceci [le bâtonnet éloigné] est l'espoir auquel s'adonne le fils d'Adam : l'échéance arrive sans que l'espoir se soit concrétisé.»<sup>270</sup>"},
                    {"number": "248", "text": "L'Imām 'Alī (as) a dit : Si l'homme voyait l'échéance [de sa vie] et la vitesse à laquelle elle se rapproche de lui, il détesterait l'espoir.<sup>271</sup>"},
                    {"number": "249", "text": "L'Imām 'Alī (as) a dit : L'espoir fait oublier l'échéance.<sup>272</sup>"},
                    {"number": "250", "text": "L'Imām 'Alī (as) a dit : La chose la plus proche [de l'homme] est l'échéance [de sa vie] et la plus lointaine est l'espoir.<sup>273</sup>"},
                    {"number": "251", "text": "L'Imām 'Alī (as) a dit : L'âme ne cesse d'espérer que lorsqu'elle atteint son échéance.<sup>274</sup>"},
                    {"number": "252", "text": "L'Imām 'Alī (as) a dit : Sachez que vous vivez des jours d'espoir tandis que derrière tout cela se trouve l'échéance [de la vie]. Toute personne qui, dans ses jours d'espérance et avant l'arrivée de son échéance, œuvre, le fruit de son travail lui sera bénéfique et l'arrivée de son échéance ne lui causera pas de dommages.<sup>275</sup>"},
                    {"number": "253", "text": "L'Imām al-Kāẓim (as) a dit : Si les dates les échéances [c'est-à-dire les durées des vies] étaient connues, les espoirs seraient discrédités.<sup>276</sup>"}
                ]
            },
            {
                "title": "79 - Les résultats des grands espoirs",
                "hadiths": [
                    {"number": "254", "text": "<i>Al-Kāfī</i> : Parmi ce qu'Allah le Tout-Puissant a dit à Moïse (as) [figure] : Ô Moïse ! Ne fonde pas de grands espoirs dans ce bas-monde, car ton cœur s'endurcira et celui dont le cœur est endurci est éloigné de Moi.<sup>277</sup>"},
                    {"number": "255", "text": "L'Imām 'Alī (as) a dit : Celui qui entretient de grands espoirs raccourcit la portée de ses actes.<sup>278</sup>"},
                    {"number": "256", "text": "L'Imām 'Alī (as) a dit : En ce qui concerne les grands espoirs, ils font oublier l'Au-delà.<sup>279</sup>"}
                ]
            },
            {
                "title": "80 - Les espoirs réduits",
                "hadiths": [
                    {"number": "257", "text": "Le Messager d'Allah (s) a dit en s'adressant à Ibn Mas'ūd : Réduis tes espoirs de telle façon que le matin, à ton réveil, dis : «Je n'atteindrai pas le soir» et lorsque tu vas te coucher le soir, dis : «Je ne verrai pas le matin». Et sois préparé à quitter la vie de ce monde, et aspire à la rencontre d'Allah.<sup>280</sup>"},
                    {"number": "258", "text": "L'Imām 'Alī (as) a dit : Il serait plus judicieux que celui qui a la certitude qu'il se séparera de ceux qu'il aime, qu'il ira sous terre, qu'il sera confronté au Jugement, qu'il n'aura pas besoin des choses qu'il a laissées derrière lui et qu'il aura besoin des choses qu'il a réalisées [pour l'Au-delà], réduise ses espoirs et œuvre longuement.<sup>281</sup>"},
                    {"number": "259", "text": "L'Imām al-Bāqir (as) a dit : Equipe-toi pour la vie de ce monde en réduisant tes espoirs.<sup>282</sup>"}
                ]
            },
            {
                "title": "81 - L'interdiction de fonder ses espoirs sur un autre qu'Allah",
                "hadiths": [
                    {"number": "260", "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : Je mettrai un terme à l'espoir de tout croyant qui a fondé ses espérances sur un autre que Moi [en le remplaçant] par le désespoir.<sup>283</sup>"},
                    {"number": "261", "text": "L'Imām 'Alī (as) a dit : Celui qui fonde ses espoirs sur un être humain le craindra.<sup>284</sup><br><br><span class=\"reference-note\">(Voir également : 413. La confiance en Allah, section 1878)</span>"}
                ]
            }
        ]
    }

    # Update Part 15 - LA COMMUNAUTÉ [MUSULMANE] (Index 16)
    data[16] = {
        "title": "15 - LA COMMUNAUTÉ [MUSULMANE]",
        "subparts": [
            {
                "title": "82 - Le statut de la communauté musulmane",
                "introduction": "«<i>Vous êtes la meilleure communauté qu'on ait fait surgir pour les hommes. Vous recommandez le convenable, interdisez le blâmable et croyez à Allah. Si les gens du Livre croyaient, ce serait meilleur pour eux. Il y en a qui croient, mais la plupart d'entre eux sont des pervers.</i>»<sup>285</sup>",
                "hadiths": [
                    {"number": "262", "text": "Le Messager d'Allah (s) a dit : Ma communauté est une communauté bénie, mais nul ne sait si ses débuts [les premiers musulmans] seront meilleurs, ou sa fin [les musulmans de la fin des temps].<sup>286</sup>"},
                    {"number": "263", "text": "Le Messager d'Allah (s) a dit : Ma communauté est une communauté qui est l'objet de la miséricorde divine.<sup>287</sup>"},
                    {"number": "264", "text": "Le Messager d'Allah (s) a dit : Vous parachevez soixante-dix communautés, parmi lesquelles vous êtes les meilleurs et les plus honorés auprès d'Allah.<sup>288</sup>"},
                    {"number": "265", "text": "Le Messager d'Allah (s) a dit : Annonce à cette communauté la bonne nouvelle de l'honneur, la religion, l'éminence, la victoire et le pouvoir sur terre.<sup>289</sup>"}
                ]
            },
            {
                "title": "83 - Les meilleurs de la communauté musulmane",
                "hadiths": [
                    {"number": "266", "text": "Le Messager d'Allah (s) a dit : Les meilleures personnes de ma communauté sont celles qui se détournent le plus de ce bas-monde et qui aspirent le plus à l'Au-delà.<sup>290</sup>"},
                    {"number": "267", "text": "Le Messager d'Allah (s) a dit : La meilleure personne de ma communauté est celle qui a consacré sa jeunesse à obéir à Allah, qui a sevré son âme des plaisirs de la vie et qui s'est éprise de l'Au-delà. Certes, sa rétribution auprès d'Allah est l'un des plus hauts rangs au Paradis.<sup>291</sup>"},
                    {"number": "268", "text": "Le Messager d'Allah (s) a dit : Les meilleures personnes de ma communauté sont celles qui, lorsqu'elles subissent une impudence, supportent ; lorsqu'on leur fait du mal, pardonnent; et lorsqu'elles sont offensées, patientent.<sup>292</sup>"}
                ]
            },
            {
                "title": "84 - La communauté du juste milieu",
                "introduction": "«<i>C'est ainsi que Nous avons fait de vous une communauté du juste milieu afin que vous soyez témoins aux gens et que le Messager vous soit témoin.</i>»<sup>293</sup>",
                "hadiths": [
                    {"number": "269", "text": "L'Imām 'Alī (as) a dit : Nous sommes les témoins d'Allah face à Ses créatures, Sa preuve sur Sa terre ; nous sommes ceux à propos de qui Allah dit : «<i>C'est ainsi que Nous avons fait de vous une communauté du juste milieu.</i>».<sup>294</sup>"}
                ]
            },
            {
                "title": "85 - Ce qui suscite le bien de la communauté musulmane",
                "hadiths": [
                    {"number": "270", "text": "Le Messager d'Allah (s) a dit : Ma communauté continuera de vivre dans le bien et la sérénité tant que ses membres s'aimeront, respecteront ce qui leur a été confiés, s'éloigneront de ce qui est interdit, honoreront l'invité, feront leurs prières et s'acquitteront de l'aumône (<i>zakāt</i>).<sup>295</sup>"},
                    {"number": "271", "text": "Le Messager d'Allah (s) a dit : Cette communauté demeurera sous la main et la protection d'Allah tant que les récitateurs ne courtiseront pas les souverains, que les savants ne disculperont pas les dépravés, et que les bons ne s'associeront pas aux méchants. En revanche, s'ils venaient à le faire, Allah lèvera d'eux Sa main et fera régner leurs oppresseurs sur eux.<sup>296</sup>"}
                ]
            },
            {
                "title": "86 - Le statut de la communauté musulmane dans l'Au-delà",
                "hadiths": [
                    {"number": "272", "text": "Le Messager d'Allah (s) a dit : Le Jour de la Résurrection, je serai le prophète le plus suivi parmi les prophètes.<sup>297</sup>"},
                    {"number": "273", "text": "Le Messager d'Allah (s) a dit : Au paradis, il y aura cent vingt rangs et ma communauté occupera quatre-vingts rangs.<sup>298</sup>"}
                ]
            },
            {
                "title": "87 - Ce qui enlève la splendeur de la communauté musulmane",
                "hadiths": [
                    {"number": "274", "text": "<i>Al-Malāḥim wa al-Fitan</i> rapporte de Thawbān, le serviteur du Messager d'Allah (s): Le Messager d'Allah (s) a dit : «Bientôt, les autres communautés vous attaqueront comme des affamés attaquent un plat.» L'une des personnes présentes lui demanda : «Est-ce à cause du fait que nous serons minoritaires ce jour-là ?» Il (s) répondit: «Vous serez au contraire très nombreux, mais vous serez comme l'écume d'un déluge; Allah enlèvera votre grandeur et votre majesté du cœur de vos ennemis et Il jettera l'abattement dans les vôtres.» Une autre personne l'interrogea: «Ô Messager d'Allah ! Que signifie cet abattement ?» Il (s) répondit : «C'est l'amour pour ce bas-monde et l'aversion de la mort.»<sup>299</sup>"},
                    {"number": "275", "text": "Le Messager d'Allah (s) a dit : Lorsque ma communauté magnifiera la vie de ce bas-monde, Allah ôtera d'elle la grandeur et l'éclat de l'islam.<sup>300</sup><br><br><span class=\"reference-note\">(Voir également : 69. Le groupe ; 130. La divergence)</span>"}
                ]
            },
            {
                "title": "88 - Ce que le Prophète (s) craint pour sa communauté",
                "hadiths": [
                    {"number": "276", "text": "Le Messager d'Allah (s) a dit : En vérité, je crains trois choses pour ma communauté : l'obéissance aux instincts cupides et avares, le fait de suivre ses passions, et un guide qui égare.<sup>301</sup>"},
                    {"number": "277", "text": "Le Messager d'Allah (s) a dit : Je crains trois choses pour ma communauté : l'égarement après le savoir, des tentations qui égarent, et [la recherche de la satisfaction] des désirs gustatifs et sensuels.<sup>302</sup>"},
                    {"number": "278", "text": "Le Messager d'Allah (s) a dit : Le pire à craindre pour ma communauté est de trois sortes: la chute d'un savant, le débat d'un hypocrite qui utilise le Coran, et un [attachement au] monde qui vous fait périr. Craignez donc cette vie pour vos propres personnes.<sup>303</sup>"},
                    {"number": "279", "text": "Le Messager d'Allah (s) a dit : Ce que je crains le plus pour ma communauté après ma disparition est le gain illicite, les passions cachées et l'usure.<sup>304</sup>"},
                    {"number": "280", "text": "Le Messager d'Allah (s) a dit : Ce que je crains le plus pour ma communauté est le fait de suivre ses passions et d'entretenir de grands espoirs, car la passion détourne l'homme de la Vérité, et les grands espoirs lui font oublier l'Au-delà.<sup>305</sup>"},
                    {"number": "281", "text": "Le Messager d'Allah (s) a dit : «Ce que je crains le plus pour vous est l'associationnisme mineur.» L'un d'eux lui demanda : «Quel est l'associationnisme mineur, ô Messager d'Allah?» Il répondit : «C'est l'ostentation hypocrite.»<sup>306</sup>"},
                    {"number": "282", "text": "Le Messager d'Allah (s) a dit : Ce que je crains de pire pour ma communauté est l'hypocrite éloquent.<sup>307</sup>"},
                    {"number": "283", "text": "Le Messager d'Allah (s) a dit : Ce que je crains de pire pour ma communauté est l'éclat de ce bas-monde et la profusion de ses biens.<sup>308</sup>"}
                ]
            }
        ]
    }

    # Update Part 16 - L'IMĀMAT (1) (Index 17) - Modify ONLY Subparts 89 to 99
    part16 = data[17]
    subparts_to_keep = part16["subparts"][11:] # Keep 100 to 114
    
    new_subparts = [
        {
            "title": "89 - L'importance de l'Imāmat",
            "introduction": "«<i>Aujourd'hui, J'ai parachevé pour vous votre religion, et accompli sur vous Mon bienfait. Et J'agrée l'islam comme religion pour vous.</i>»<sup>309</sup>",
            "hadiths": [
                {"number": "284", "text": "L'Imām 'Alī (as) a dit : L'Imāmat est la clé de voûte de la communauté [musulmane].<sup>310</sup>"},
                {"number": "285", "text": "L'Imām al-Bāqir (as) a dit : L'islam est fondé sur cinq [piliers] : la prière, l'aumône, le jeûne, le pèlerinage obligatoire (<i>ḥajj</i>) et la <i>wilāya</i>.<sup>311</sup> On n'a jamais autant invité à une chose qu'à la <i>wilāya</i>.<sup>312</sup>"},
                {"number": "286", "text": "L'Imām al-Kāẓim (as) a dit : L'Imāmat est une lumière, comme Allah l'a exprimé : «<i>Croyez en Allah, et en Son messager, ainsi qu'en la Lumière que Nous avons fait descendre</i>».<sup>313</sup> Puis il (as) dit : La lumière dont il est question est l'Imām.<sup>314</sup>"},
                {"number": "287", "text": "L'Imām al-Riḍā (as) a dit : A la fin de sa vie, lors du pèlerinage de l'Adieu, le verset «<i>Aujourd'hui, J'ai parachevé pour vous votre religion</i>» fut révélé au Messager d'Allah (s). Ainsi, la question de l'Imāmat est de parachever la religion.<sup>315</sup>"},
                {"number": "288", "text": "L'Imām al-Riḍā (as) a dit : En vérité, l'Imāmat est le pilier de l'islam fécond, et c'est sa branche la plus noble.<sup>316</sup>"},
                {"number": "289", "text": "L'Imām al-Riḍā (as) a dit : En vérité, l'Imāmat est les rênes de la religion, le système des musulmans, la réforme et la prospérité de la vie terrestre, et l'honneur des croyants.<sup>317</sup><br><br><span class=\"reference-note\">(Voir également : 233. Le chemin, section 1119)</span>"}
            ]
        },
        {
            "title": "90 - La supériorité de l'Imāmat vis-à-vis de la prophétie",
            "introduction": "«<i>[Et rappelle-toi] quand ton Seigneur eut éprouvé Abraham par certains commandements, et qu'il les eut accomplis, le Seigneur lui dit : «Je vais faire de toi un Imām pour les gens.»</i>»<sup>318</sup>",
            "hadiths": [
                {"number": "290", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, Allah le Béni et le Très-Haut a fait d'Ibrāhīm un serviteur avant de faire de lui un prophète. Ensuite, Allah a fait de lui un prophète avant de faire de lui un messager ; puis Allah a fait de lui un messager avant de faire de lui un ami intime, et Allah a fait de lui un ami intime avant de faire de lui un Imām. Ainsi, lorsqu'Il eût réuni en lui tous ces rangs, Il dit : «<i>Je vais faire de toi un Imām pour les gens.</i>»<sup>319</sup>"}
            ]
        },
        {
            "title": "91 - La nécessité d'un Imām",
            "hadiths": [
                {"number": "291", "text": "L'Imām al-Bāqir (as) a dit : Si l'Imām venait à disparaître de la terre ne serait-ce une heure, la terre et ses habitants oscilleraient, comme la vague d'une mer agitée qui emporte ses occupants.<sup>320</sup>"},
                {"number": "292", "text": "L'Imām al-Ṣādiq (as) a dit : La terre n'est jamais dépourvue d'Imām. Ainsi, il réfute les croyants s'ils venaient à rajouter quelque chose [à la religion], et il complète s'ils venaient à en oublier quelque chose.<sup>321</sup>"}
            ]
        },
        {
            "title": "92 - La Preuve (al-ḥujjat) est un Imām connu",
            "hadiths": [
                {"number": "293", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la preuve (<i>al-Ḥujjat</i>, l'autorité) d'Allah le Tout-Puissant auprès de Sa création n'est établie que par le biais d'un Imām afin qu'il soit connu.<sup>322</sup>"}
            ]
        },
        {
            "title": "93 - L'Imām peut être apeuré et caché",
            "hadiths": [
                {"number": "294", "text": "L'Imām 'Alī (as) a dit : Ô Allah, en vérité, la terre n'est jamais dépourvue d'un être qui maintient pour Allah Ses preuves ; qu'il soit visible et connu, ou apeuré et occulté afin que les arguments et preuves évidentes d'Allah ne soient jamais invalidés.<sup>323</sup>"},
                {"number": "295", "text": "L'Imām al-Bāqir (as) a dit : La terre ne pourrait demeurer [existante] sans la présence d'un Imām visible ou occulté.<sup>324</sup>"}
            ]
        },
        {
            "title": "94 - Sans la présence de l'Imām, la terre serait engloutie",
            "hadiths": [
                {"number": "296", "text": "L'Imām al-Ṣādiq (as) a dit : Si la terre restait sans Imām, elle serait engloutie.<sup>325</sup>"},
                {"number": "297", "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, la terre ne saurait être sans la présence d'une Preuve [autorité], car seule une Preuve peut réformer les gens et seule une Preuve peut réformer la terre.<sup>326</sup><br><br><span class=\"reference-note\">(Voir également : 88. L'argument)</span>"}
            ]
        },
        {
            "title": "95 - L'appel de chaque nation par son chef (Imām)",
            "introduction": "«<i>Le jour où Nous appellerons chaque groupement d'hommes par leur chef (Imām).</i>»<sup>327</sup>",
            "hadiths": [
                {"number": "298", "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour du Jugement, [...] un appel venant d'Allah le Tout-Puissant se fera entendre : «Que celui qui a suivi un Imām dans ce bas-monde le suive et aille là où va son Imām», et alors «<i>les meneurs désavoueront les suiveurs...</i>»<sup>328</sup>.<sup>329</sup>"}
            ]
        },
        {
            "title": "96 - L'importance de la connaissance de l'Imām",
            "hadiths": [
                {"number": "299", "text": "Le Messager d'Allah (s) a dit : Celui qui meurt sans connaître son Imām mourra d'une mort païenne.<sup>330</sup>"},
                {"number": "300", "text": "Le Messager d'Allah (s) a dit : Celui qui meurt sans Imām mourra d'une mort païenne.<sup>331</sup>.<sup>332</sup>"},
                {"number": "301", "text": "Interrogé au sujet de la connaissance d'Allah, l'Imām Ḥusayn (as) répondit : [C'est] la connaissance que les gens de chaque époque ont de l'Imām à qui l'obéissance est obligatoire.<sup>333</sup>"},
                {"number": "302", "text": "L'Imām al-Ṣādiq (as) a dit en commentant la Parole du Très-Haut «<i>Et celui à qui la sagesse est donnée, c'est un bien immense qui lui est donné</i>»<sup>334</sup> : [La sagesse] est l'obéissance à Allah et la connaissance de l'Imām.<sup>335</sup>"},
                {"number": "303", "text": "L'Imām al-Ṣādiq (as) a dit : L'Imām est le guide entre Allah le Tout-Puissant et Sa création, celui qui le connaît est croyant et celui qui le rejette est mécréant.<sup>336</sup>"},
                {"number": "304", "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui nous méconnaît mais ne nous rejette pas est égaré jusqu'à ce qu'il revienne à la guidance qu'Allah lui a prescrite, et qui consiste en notre obéissance obligatoire. Toutefois, Allah le jugera selon Sa bonne volonté s'il meurt en étant égaré.<sup>337</sup>"}
            ]
        },
        {
            "title": "97 - Les conditions de l'Imāmat et les caractéristiques de l'Imām",
            "introduction": "«<i>Et Nous avons désigné parmi eux des dirigeants qui guidaient [les gens] suivant Notre ordre aussi longtemps qu'ils enduraient et croyaient fermement en Nos signes.</i>»<sup>338</sup><br><br>«<i>Celui qui guide vers la Vérité est-il plus digne d'être suivi, ou bien celui qui ne guide qu'autant qu'il est lui-même guidé ? Qu'avez-vous à formuler un jugement pareil ?</i>»<sup>339</sup>",
            "hadiths": [
                {"number": "305", "text": "L'Imām 'Alī (as) a dit : N'assumeront cette mission [de l'Imāmat] que des gens de patience, de clairvoyance, et ceux qui en connaissent les circonstances.<sup>340</sup>"},
                {"number": "306", "text": "L'Imām 'Alī (as) a dit : L'Imām doit avoir un cœur clairvoyant, une langue éloquente et une âme impétueuse dans l'établissement de la vérité.<sup>341</sup>"},
                {"number": "307", "text": "L'Imām 'Alī (as) a dit : Celui qui se proclame Imām pour les gens doit commencer par s'instruire lui-même avant de vouloir instruire les autres, et avant d'éduquer [les gens] par sa parole, il doit d'abord les éduquer par sa propre conduite.<sup>342</sup>"},
                {"number": "308", "text": "L'Imām 'Alī (as) a dit : N'exécute l'ordre d'Allah – loué soit-Il – que celui qui ne fait pas preuve de complaisance [ne peut être soudoyé], qui ne fait aucune concession, et qui ne poursuit pas ses propres convoitises.<sup>343</sup>"},
                {"number": "309", "text": "L'Imām 'Alī (as) a dit : Parmi les caractéristiques les plus importantes de l'Imām à qui l'on doit obéissance et allégeance est qu'il soit connu en tant qu'exempt de toute faute, faux pas, péché intentionnel, ainsi que de tout péché, petit ou grand. Il ne se méprend pas, ne se trompe pas, n'est pas distrait par une chose nuisant à la religion ou par toute autre distraction. Il est le plus savant au sujet des prescriptions d'Allah concernant ce qui est licite et illicite, ainsi qu'au sujet de Ses obligations, de Ses traditions et de Ses lois. Il est indépendant des autres alors que les autres ont besoin de lui. Il est la plus généreuse des personnes et la plus courageuse.<sup>344</sup>"},
                {"number": "310", "text": "L'Imām 'Alī (as) a dit : Vous savez que celui qui est chargé du règlement des affaires concernant l'intimité, les vies, les gains, les commandements ainsi que la direction des musulmans ne doit pas être avare, car il sera attiré par leur fortune ; ni un ignorant, car il les égarera par son ignorance ; ni un impitoyable, car il les privera de leurs besoins [c'est-à-dire que de par la crainte qu'il inspire, les gens n'auront pas recours à lui pour répondre à leurs besoins] ; ni un injuste dans la répartition des biens publics, ni un corrupteur qui accepte d'être soudoyé pour un jugement et qui néglige le droit, ni celui qui n'applique pas la <i>sunna</i> (tradition) et causera la perte de l'<i>umma</i> (communauté des croyants).<sup>345</sup>"},
                {"number": "311", "text": "L'Imām Ḥusayn (as) a écrit dans sa lettre aux gens de Kūfa : Par ma vie, n'est vraiment Imām que celui qui gouverne par le Livre, qui maintient la justice, qui professe la religion véridique et qui se contrôle pour Allah.<sup>346</sup>"},
                {"number": "312", "text": "L'Imām al-Bāqir (as) a dit en exposant les traits de l'Imām : La pureté [légitimité] de la naissance, une éducation droite et juste, et le fait de rester à l'écart des distractions et divertissements.<sup>347</sup>"},
                {"number": "313", "text": "L'Imām al-Riḍā (as) a dit en décrivant l'Imām : Il doit être capable de diriger et être éclairé dans la politique.<sup>348</sup>"}
            ]
        },
        {
            "title": "98 - Ce qui a été ordonné aux Imāms justes",
            "hadiths": [
                {"number": "314", "text": "L'Imām 'Alī (as) a dit : En vérité, Allah a fait de moi un Imām pour Sa création. Il m'a astreint à faire que ma personne, ma nourriture, ma boisson et mes vêtements soient comme ceux des faibles [de la communauté] afin que les pauvres me suivent dans ma pauvreté et que la richesse des riches ne soit pas un moyen d'intimidation.<sup>349</sup>"},
                {"number": "315", "text": "L'Imām 'Alī (as) a dit : L'Imām n'a d'autre obligation que [d'appliquer] ce dont le Seigneur l'a chargé : la transmission d'exhortation, l'effort pour prodiguer de [bons] conseils, raviver la <i>sunna</i>, appliquer les lois divines face à ceux qui le méritent, et faire parvenir à chacun la part [du trésor public] qui lui revient.<sup>350</sup>"}
            ]
        },
        {
            "title": "99 - Les droits et devoirs réciproques entre l'Imām et la communauté",
            "hadiths": [
                {"number": "316", "text": "L'Imām 'Alī (as) a dit : Le devoir de l'Imām est de gouverner selon ce qu'Allah a révélé et il doit restituer les dépôts. S'il agit ainsi, le devoir des gens est de l'écouter, de lui obéir et de lui répondre s'il fait appel à eux.<sup>351</sup>"},
                {"number": "317", "text": "L'Imām 'Alī (as) a dit : Ainsi, il est du devoir du gouverneur de ne pas changer son comportement vis-à-vis de ses sujets lorsqu'une grâce l'atteint ou lorsqu'il bénéficie d'une richesse. Il faut que les grâces dont Allah l'a comblé le rapprochent de ses serviteurs et le rendent compatissant envers ses frères. Parmi mes devoirs envers vous figure celui que je ne vous cache rien si ce n'est en temps de guerre, que je n'agisse pas sans vous consulter sauf en ce qui concerne les commandements [de la religion], que je vous donne ce qui vous revient sans retard et sans m'arrêter avant de l'avoir complètement accompli, et que je vous considère comme égaux en droits. Si je m'astreins à cela, les bienfaits d'Allah vous seront indubitablement accordés et vous me devrez obéissance.<sup>352</sup>"}
            ]
        }
    ]
    
    part16["subparts"] = new_subparts + subparts_to_keep
    data[17] = part16

    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
