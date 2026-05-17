import json

def update():
    with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('[')
    end_idx = content.rfind(']') + 1
    data = json.loads(content[start_idx:end_idx])

    # We are adding Part 1, Part 2, and Part 3 to the beginning of the list.
    
    new_parts = []
    
    # Part 1
    part1 = {
        "title": "1 - LE SACRIFICE DE SOI",
        "subparts": [
            {
                "title": "1 - La vertu du sacrifice de soi",
                "hadiths": [
                    {"number": "1", "text": "L'Imām 'Alī (as) a dit : Le sacrifice de soi est la plus haute des vertus.<sup>1</sup>"},
                    {"number": "2", "text": "L'Imām 'Alī (as) a dit : Le sacrifice de soi est une caractéristique des bienfaisants.<sup>2</sup>"},
                    {"number": "3", "text": "L'Imām 'Alī (as) a dit : Le sacrifice de soi est le meilleur des actes de bienfaisance, et c'est le plus haut degré de la foi.<sup>3</sup>"},
                    {"number": "4", "text": "L'Imām 'Alī (as) a dit : Le sacrifice de soi est la meilleure des dévotions et la plus sublime des noblesses.<sup>4</sup>"},
                    {"number": "5", "text": "L'Imām 'Alī (as) a dit : Le sacrifice de soi est la meilleure des générosités.<sup>5</sup>"},
                    {"number": "6", "text": "L'Imām 'Alī (as) a dit : Traite l'ensemble des gens de manière équitable ; agis avec les croyants avec sacrifice.<sup>6</sup>"},
                    {"number": "7", "text": "L'Imām 'Alī (as) a dit : Le sacrifice de soi est le sommet des vertus.<sup>7</sup>"},
                    {"number": "8", "text": "L'Imām 'Alī (as) a dit : Par le sacrifice de soi, on gagne le cœur des hommes libres.<sup>8</sup><br><br><span class=\"reference-note\">(Voir également : 382. La dépense, sections 1760 et 1762)</span>"}
                ]
            },
            {
                "title": "2 - La vertu de ceux qui se sacrifient pour les autres",
                "introduction": "«<i>Il [appartient également] à ceux qui, avant eux, se sont installés dans le pays et dans la foi, qui aiment ceux qui émigrent vers eux, et ne ressentent dans leurs cœurs aucune envie pour ce que [ces immigrés] ont reçu, et qui [les] préfèrent à eux-mêmes, même s'il y a pénurie chez eux. Quiconque se prémunit contre sa propre avarice, ceux-là sont ceux qui réussissent.</i>»<sup>9</sup>",
                "hadiths": [
                    {"number": "9", "text": "<i>Al-Amālī li al-Ṭūsī</i> : Abū Hurayra a dit : Un homme vint chez le Prophète (s) et il se plaint auprès de lui de la faim. Le Messager d'Allah (s) envoya une personne auprès de ses femmes et ces dernières dirent : «Nous n'avons que de l'eau.» Le Prophète (s) dit : «Qui peut être l'hôte de cet homme cette nuit ?» L'Imām 'Alī (as) a dit : «Je serai son hôte, ô Messager d'Allah.» Il rejoignit Fāṭima et lui demanda : «Qu'as-tu à nous offrir, ô fille du Messager d'Allah ?» Elle répondit : «Nous n'avons que le dîner de nos fils, mais nous préférerons notre invité à nous-mêmes [nous le faisons passer avant nous-mêmes].» Et l'Imām dit : «ô fille de Muḥammad, fais dormir les enfants et éteins la chandelle.» À son réveil, 'Alī (as) se dirigea vers le Prophète (s) et lui fit part de ce qui s'était passé. Alors qu'il était chez le Prophète, Allah le Tout-Puissant révéla : «<i>et qui [les] préfèrent à eux-mêmes, même s'il y a pénurie chez eux</i>».<sup>10</sup>"},
                    {"number": "10", "text": "<i>Tanbīh al-Khawāṭir</i> : 'Ā'isha a dit : Le Messager d'Allah (s) n'a jamais mangé jusqu'à satiété durant trois jours de suite, et ce jusqu'à ce qu'il quitte ce monde. S'il l'avait voulu, il aurait pu manger jusqu'à satiété, mais il faisait passer les autres avant lui-même.<sup>11</sup>"},
                    {"number": "11", "text": "<i>Majma' al-Bayān</i> : Abū Ṭufayl a dit : 'Alī (as) acheta un vêtement qui lui plaisait. Il le prit et le donna comme offrande, puis il dit : «J'ai entendu le Messager d'Allah (s) dire : «Celui qui fait passer les autres avant lui-même, Allah le [fera entrer] au Paradis avant les autres le Jour de la Résurrection».»<sup>12</sup>"},
                    {"number": "12", "text": "L'Imām al-Ṣādiq (as) a dit au sujet de la parole du Très-Haut «<i>et offrent la nourriture, malgré son amour, au pauvre, à l'orphelin et au prisonnier</i>»<sup>13</sup> : Fāṭima disposait d'une poignée d'orge qu'elle accommoda sous forme de bouillie. Quand ce plat fut prêt et qu'elle le déposa devant elle [pour que sa famille le mange], un indigent vint et dit : «Qu'Allah vous fasse miséricorde ! Nourrissez-nous avec la subsistance qu'Allah vous a donnée.» 'Alī se leva et lui donna un tiers du repas. Peu après, un orphelin arriva et dit : «Qu'Allah vous fasse miséricorde ! Nourrissez-nous avec la subsistance qu'Allah vous a donnée.» 'Alī se leva et lui donna le second tiers du repas. Peu après, un prisonnier arriva et dit : «Qu'Allah vous fasse miséricorde ! Nourrissez-nous avec la subsistance qu'Allah vous a donnée.» 'Alī se leva et lui donna le dernier tiers du repas, qu'ils ne goûtèrent même pas. Allah révéla alors en leur honneur ces versets : «<i>et votre effort sera reconnu</i>»<sup>14</sup>.<sup>15</sup>"}
                ]
            }
        ]
    }
    new_parts.append(part1)

    # Part 2
    part2 = {
        "title": "2 - L'EMPLOI",
        "subparts": [
            {
                "title": "3 - L'emploi et les moyens de subsistance",
                "introduction": "«<i>Est-ce eux qui distribuent la miséricorde de ton Seigneur ? C'est Nous qui avons réparti entre eux leur subsistance dans la vie présente et qui les avons élevés en grades les uns sur les autres, afin que les uns prennent les autres à leur service. La miséricorde de ton Seigneur vaut mieux, cependant, que ce qu'ils amassent.</i>»<sup>16</sup><br><br>«<i>L'une d'elles dit : «Ô mon père, engage-le [à ton service] moyennant salaire, car le meilleur à engager est celui qui est fort et digne de confiance.»</i>»<sup>17</sup>",
                "hadiths": [
                    {"number": "13", "text": "L'Imām 'Alī a dit en commentant cette parole divine : «<i>C'est Nous qui avons réparti entre eux leur subsistance</i>» : Le Très-Haut nous a informé que l'emploi et le fait de travailler est l'un des moyens de subsistance des créatures. Par Sa sagesse, Il a fait en sorte que les aspirations, les motivations et les états [des hommes] soient divers et variés, et a fait de cela la base de la subsistance des créatures; et cela incite ainsi l'homme à avoir recours aux services de ses semblables. En effet, si chacun était obligé de construire pour lui-même, de faire ses travaux de menuiserie, et de tout produire lui-même... Les conditions de ce monde deviendraient insupportables ; les gens ne pourraient les supporter et seraient incapables d'y faire face. En revanche, Allah a parfait Son organisation en variant les aspirations afin que chacun réalise pour les autres ce qui est compatible avec ses propres capacités, et dans le but que certains soient servis par les autres et que leur conditions de vie soient viables.<sup>18</sup>"}
                ]
            },
            {
                "title": "4 - Il est déconseillé de se mettre au service de quelqu'un",
                "hadiths": [
                    {"number": "14", "text": "<i>Al-Kāfī</i> : 'Ammār al-Sābāṭī a dit : J'ai dit à l'Imām al-Ṣādiq (as) : «Un homme peut faire du commerce [seul], cependant, s'il le fait au service de quelqu'un, on lui donne la même chose que ce qu'il gagne s'il le fait seul [quelle solution est préférable ?].» Il (as) répondit : «Il ne doit pas se mettre au service de quelqu'un [s'il peut faire le même travail seul], mais qu'il implore Allah le Tout-Puissant pour sa subsistance puis qu'il fasse du commerce, car s'il est au service de quelqu'un, il limite sa propre subsistance.»<sup>19</sup>"}
                ]
            },
            {
                "title": "5 - L'intermédiaire dans l'emploi",
                "hadiths": [
                    {"number": "15", "text": "<i>Al-Kāfī</i> : Muḥammad ibn Muslim a dit : L'Imām al-Bāqir (as) ou l'Imām al-Ṣādiq (as) fut interrogé au sujet d'un homme qui accepte un travail sans l'exécuter lui-même, mais le confie à une autre personne en prélevant néanmoins un bénéfice. L'Imām (as) répondit : «Non [il ne peut agir ainsi], sauf s'il a lui-même fait une partie de ce travail.»<sup>20</sup>"}
                ]
            },
            {
                "title": "6 - L'injustice envers l'employé",
                "hadiths": [
                    {"number": "16", "text": "Le Messager d'Allah (s) a dit : Allah rendra vaines les actions de celui qui rémunère injustement son employé et Il lui interdira l'odeur du Paradis qui se sent à une distance de cinq cents années.<sup>21</sup>"},
                    {"number": "17", "text": "Le Messager d'Allah (s) a dit : Rémunérer injustement l'employé fait partie des péchés majeurs.<sup>22</sup>"}
                ]
            },
            {
                "title": "7 - Annoncer à l'employé sa rémunération et la bonne façon de la donner",
                "hadiths": [
                    {"number": "18", "text": "Le Messager d'Allah (s) a dit : Donnez sa rémunération à l'employé avant que sa sueur ne sèche, et annoncez-lui sa rémunération alors qu'il est encore en train de travailler.<sup>23</sup>"},
                    {"number": "19", "text": "L'Imām 'Alī (as) a dit : Le Messager d'Allah (s) a interdit d'employer une personne avant qu'elle ne soit informée de sa rémunération.<sup>24</sup>"}
                ]
            }
        ]
    }
    new_parts.append(part2)

    # Part 3
    part3 = {
        "title": "3 - L'ÉCHÉANCE [DE LA MORT]",
        "subparts": [
            {
                "title": "8 - L'échéance [de la mort]",
                "hadiths": [
                    {"number": "20", "text": "L'Imām 'Alī (as) a dit : Il a créé la durée [des vies], Il les a fait longues ou courtes ; Il en avance certaines et retarde d'autres, et Il a lié leurs causes avec la mort [Allah a fait de certaines choses les causes de la mort].<sup>25</sup>"},
                    {"number": "21", "text": "L'Imām 'Alī (as) a dit : Il n'y a pas plus véridique que l'échéance [de la mort].<sup>26</sup>"},
                    {"number": "22", "text": "L'Imām 'Alī (as) a dit : Quel bon remède est l'échéance [de la mort] !<sup>27</sup>"},
                    {"number": "23", "text": "L'Imām 'Alī (as) a dit : Les respirations de l'être humain sont autant de pas vers l'échéance [de sa mort].<sup>28</sup>"}
                ]
            },
            {
                "title": "9 - L'échéance [de la mort] est une citadelle fortifiée",
                "introduction": "«<i>Personne ne peut mourir que par la permission d'Allah, et au moment prédéterminé.</i>»<sup>29</sup>",
                "hadiths": [
                    {"number": "24", "text": "L'Imām 'Alī (as) a dit : L'échéance [de la mort] suffit comme garde.<sup>30</sup>"},
                    {"number": "25", "text": "L'Imām 'Alī (as) a dit : L'échéance [de la mort] est une citadelle fortifiée.<sup>31</sup>"}
                ]
            },
            {
                "title": "10 - Toute chose a une échéance",
                "hadiths": [
                    {"number": "26", "text": "L'Imām 'Alī (as) a dit : En vérité, toute chose a une durée et une échéance.<sup>32</sup>"}
                ]
            }
        ]
    }
    new_parts.append(part3)

    # We prepend them to data
    # Wait, the lowest part currently starts at 421 ("Partie 23 - La tristesse").
    # If we just insert these at the beginning, they will be parts 0, 1, 2 of the JSON array.
    # We should just insert them at the front.
    
    # Actually, we can just insert them at index 0.
    for part in reversed(new_parts):
        data.insert(0, part)

    new_json = json.dumps(data, indent=4, ensure_ascii=False)
    new_content = content[:start_idx] + new_json + content[end_idx:]
    
    with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update()
