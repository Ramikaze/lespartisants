import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

def find_subpart(part_index, search_str):
    for s in data[part_index].get('subparts', []):
        if search_str in s['title']:
            return s
    return None

def clear_hadiths(s):
    if s:
        s['hadiths'] = []
        if 'introduction' in s:
            del s['introduction']

# ============================================================
# Part 113 (index 114) - Le licite (page 315)
# ============================================================
p113 = 114
s575 = find_subpart(p113, "575")
clear_hadiths(s575)
s575['hadiths'].append({
    "number": "1733",
    "text": "Le Messager d'Allah (s) a dit : Il n'est pas licite pour un homme d'utiliser ce qui appartient à son frère, sauf avec son accord.<sup>1981</sup>"
})

# ============================================================
# Part 114 (index 115) - La clémence (pages 315-316)
# ============================================================
p114 = 115
s576 = find_subpart(p114, "576")
s577 = find_subpart(p114, "577")
s578 = find_subpart(p114, "578")
s579 = find_subpart(p114, "579")
s580 = find_subpart(p114, "580")

for s in [s576, s577, s578, s579, s580]:
    clear_hadiths(s)

s576['hadiths'].extend([
    {
        "number": "1734",
        "text": "Le Messager d'Allah (s) a dit : Le clément est presque un prophète.<sup>1982</sup>"
    },
    {
        "number": "1735",
        "text": "L'Imām 'Alī (as) a dit : La clémence est la perfection de la raison.<sup>1983</sup>"
    },
    {
        "number": "1736",
        "text": "L'Imām 'Alī (as) a dit : La clémence ordonne les affaires du croyant.<sup>1984</sup>"
    },
    {
        "number": "1737",
        "text": "L'Imām 'Alī (as) a dit : La beauté de l'homme est dans sa clémence.<sup>1985</sup>"
    },
    {
        "number": "1738",
        "text": "L'Imām al-Riḍā (as) a dit : L'homme ne peut être un serviteur [d'Allah] que lorsqu'il est clément.<sup>1986</sup>"
    }
])

s577['hadiths'].extend([
    {
        "number": "1739",
        "text": "L'Imām 'Alī (as) a dit : Par l'éminence de la raison, la clémence devient profuse.<sup>1987</sup>"
    },
    {
        "number": "1740",
        "text": "L'Imām 'Alī (as) a dit : Attache-toi à faire preuve de clémence, car elle est véritablement le fruit du savoir.<sup>1988</sup>"
    },
    {
        "number": "1741",
        "text": "L'Imām 'Alī (as) a dit : La clémence et la tempérance sont des jumeaux engendrant la haute et noble résolution.<sup>1989</sup>"
    },
    {
        "number": "1742",
        "text": "L'Imām 'Alī (as) a dit : Si tu n'es pas clément, efforce-toi de le paraître, car peu nombreux sont ceux qui essaient de ressembler à un groupe sans finir par devenir comme lui.<sup>1990</sup>"
    }
])

s578['hadiths'].extend([
    {
        "number": "1743",
        "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve de clémence a le dessus.<sup>1991</sup>"
    },
    {
        "number": "1744",
        "text": "L'Imām 'Alī (as) a dit : Celui qui est clément envers son adversaire l'aura vaincu.<sup>1992</sup>"
    },
    {
        "number": "1745",
        "text": "L'Imām 'Alī (as) a dit : La première compensation de la personne clémente pour cette qualité est que les gens l'aideront face à l'ignorant.<sup>1993</sup>"
    },
    {
        "number": "1746",
        "text": "L'Imām 'Alī (as) a dit : Faire preuve de clémence dans un moment de forte colère protège contre la colère du Tout-Puissant.<sup>1994</sup>"
    },
    {
        "number": "1747",
        "text": "L'Imām al-Ṣādiq (as) a dit : La clémence suffit comme auxiliaire et aide.<sup>1995</sup>"
    }
])

s579['hadiths'].extend([
    {
        "number": "1748",
        "text": "L'Imām 'Alī (as) a dit : Le clément est celui qui supporte ses frères.<sup>1996</sup>"
    },
    {
        "number": "1749",
        "text": "Interrogé au sujet de la clémence, l'Imām Ḥasan (as) répondit : [C'est de] retenir sa colère et de se contrôler.<sup>1997</sup>"
    }
])

s580['hadiths'].extend([
    {
        "number": "1750",
        "text": "Luqmān (as) a dit : Le clément n'est connu que dans la colère.<sup>1998</sup>"
    },
    {
        "number": "1751",
        "text": "Lorsqu'on lui demanda quelle était la plus clémente des personnes, l'Imām 'Alī (as) répondit: C'est celle qui ne se met pas en colère.<sup>1999</sup>"
    },
    {
        "number": "1752",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : En vérité, l'homme que la clémence atteint au milieu de sa colère m'étonne.<sup>2000</sup>"
    }
])

# ============================================================
# Part 115 (index 116) - La stupidité (pages 317-318)
# ============================================================
p115 = 116
s581 = find_subpart(p115, "581")
s582 = find_subpart(p115, "582")
s583 = find_subpart(p115, "583")
s584 = find_subpart(p115, "584")
s585 = find_subpart(p115, "585")

for s in [s581, s582, s583, s584, s585]:
    clear_hadiths(s)

s581['hadiths'].extend([
    {
        "number": "1753",
        "text": "L'Imām 'Alī (as) a dit : La stupidité est la pire des maladies.<sup>2001</sup>"
    },
    {
        "number": "1754",
        "text": "L'Imām 'Alī (as) a dit : La stupidité est la pire des indigences.<sup>2002</sup>"
    },
    {
        "number": "1755",
        "text": "L'Imām 'Alī (as) a dit : L'ennemi ne cause pas plus de tort à son ennemi que le sot n'en cause à lui-même.<sup>2003</sup>"
    }
])

s582['hadiths'].extend([
    {
        "number": "1756",
        "text": "Interrogé au sujet du sot, Jésus (as) répondit : [C'est] celui qui est imbu de son propre avis et de sa personne, qui pense qu'il a tous les mérites et vertus et non le contraire, qui a décidé qu'il avait tous les droits et qu'il n'était astreint à aucun devoir ; tel est le sot et il n'existe aucun moyen de le guérir.<sup>2004</sup>"
    },
    {
        "number": "1757",
        "text": "L'Imām 'Alī (as) a dit : Celui qui remarque les défauts des autres, les leur reproche puis les admet pour lui-même est le sot par excellence.<sup>2005</sup>"
    },
    {
        "number": "1758",
        "text": "L'Imām 'Alī (as) a dit : La sottise de l'homme se reconnaît par sa condescendance dans la prospérité et par son humiliation dans le malheur.<sup>2006</sup>"
    },
    {
        "number": "1759",
        "text": "L'Imām 'Alī (as) a dit : Parmi les signes de la sottise figure la versatilité.<sup>2007</sup>"
    },
    {
        "number": "1760",
        "text": "L'Imām 'Alī (as) a dit : Ne réponds pas à tout ce que les gens te disent, car cela suffit pour être [considéré comme] sot.<sup>2008</sup>"
    }
])

s583['hadiths'].extend([
    {
        "number": "1761",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit dans l'une de ses recommandations à son fils al-Bāqir (as) : Mon fils ! Garde-toi de prendre le sot pour compagnon ou de les fréquenter. Reste éloigné de lui et ne lui parle pas car en vérité, le sot est vil, qu'il soit présent ou absent. S'il parle sa sottise le déshonore, s'il se tait c'est en raison de son incapacité à parler. S'il effectue un travail le gâche, et s'il lui est confié une responsabilité il échoue. Son propre savoir ne l'enrichit pas et le savoir des autres ne lui est d'aucune utilité, il n'applique pas les conseils qu'on lui prodigue et son associé ne trouve pas de repos, sa mère souhaite faire son deuil, sa femme de le perdre, son voisin de vivre loin de lui, et celui qui s'assied à ses côtés d'être seul plutôt qu'en sa compagnie. S'il est le moins important [du point de vue du statut] de l'assemblée, il rabaisse ceux qui sont au-dessus de lui, et s'il est le plus important, il dénigre les autres.<sup>2009</sup>"
    },
    {
        "number": "1762",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui ne s'abstient pas d'établir des liens d'amitié avec un sot ne tardera pas à adopter son caractère.<sup>2010</sup>"
    }
])

s584['hadiths'].extend([
    {
        "number": "1763",
        "text": "L'Imām 'Alī (as) a dit : Le plus sot est celui qui croit être la personne la plus intelligente.<sup>2011</sup>"
    },
    {
        "number": "1764",
        "text": "L'Imām 'Alī (as) a dit : Le plus sot est celui qui fait obstacle à la bienfaisance et s'attend à ce qu'on le remercie, et qui agit mal et s'attend à une bonne récompense.<sup>2012</sup>"
    },
    {
        "number": "1765",
        "text": "L'Imām 'Alī (as) a dit : Le plus sot est celui qui réprouve les autres pour un vice alors qu'il a le même.<sup>2013</sup>"
    }
])

s585['hadiths'].append({
    "number": "1766",
    "text": "L'Imām 'Alī (as) a dit : Garder le silence face à un sot est la meilleure réponse.<sup>2014</sup>"
})

# ============================================================
# Part 116 (index 117) - Le bain (page 319)
# ============================================================
p116 = 117
s586 = find_subpart(p116, "586")
clear_hadiths(s586)

s586['hadiths'].extend([
    {
        "number": "1767",
        "text": "L'Imām 'Alī (as) a dit : Quel bon lieu est celui où l'on prend son bain ! Il rappelle le feu [de l'Enfer] et il fait partir les impuretés [du corps].<sup>2015</sup>"
    },
    {
        "number": "1768",
        "text": "L'Imām al-Ṣādiq (as) a dit : Trois choses font grossir et trois font maigrir. Celles qui font grossir sont d'aller [trop] souvent au bain, de sentir les bonnes odeurs et de porter des vêtements doux. En revanche, les trois qui font maigrir sont de manger [trop] souvent des œufs, du poisson et des dattes non mûres.<sup>2016</sup>"
    }
])


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1733-1768")
