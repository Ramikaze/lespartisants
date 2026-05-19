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

def ensure_hadiths(s):
    if s and 'hadiths' not in s:
        s['hadiths'] = []

# ============================================================
# Chapter 119 (index 120) - LA VIE (ajout hadith 1797)
# ============================================================
s597 = find_subpart(120, "597")
ensure_hadiths(s597)
s597['hadiths'].append({
    "number": "1797",
    "text": "L'Imām 'Alī (as) a dit : Le monothéisme est la vie de l'âme.<sup>2046</sup>"
})

# ============================================================
# Chapter 120 (index 121) - LES ANIMAUX
# ============================================================
s598 = find_subpart(121, "598")
ensure_hadiths(s598)
s598['hadiths'].extend([
    {
        "number": "1798",
        "text": "Le Messager d'Allah (s) a dit en voyant une chamelle attachée alors que sa charge était encore sur son dos : Où est son propriétaire ? Dites-lui de se préparer au procès [concernant cette chamelle] demain [au Jour de la Résurrection].<sup>2047</sup>"
    },
    {
        "number": "1799",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Allah aime la douceur et Il aide à son application. Ainsi, lorsque vous montez une bête maigre, descendez-en à un endroit approprié. Si le sol est aride, éloignez-vous en, et si la terre est verdoyante, mettez pied à terre [et laissez-la s'y reposer].<sup>2048</sup>"
    },
    {
        "number": "1800",
        "text": "Le Messager d'Allah (s) a dit : Montez les bêtes en bonne santé et gardez-les en bonne santé. Lors de vos discussions, ne les utilisez pas comme des chaises dans les rues et les marchés, car il se peut que la bête montée soit meilleure que celui qui la monte et pratique davantage le rappel d'Allah le Béni et le Très-Haut que lui.<sup>2049</sup>"
    },
    {
        "number": "1801",
        "text": "Le Messager d'Allah (s) a dit : La bête a six droits sur son propriétaire : ce dernier doit l'autoriser à paître lorsqu'il met pied à terre, l'abreuver lorsqu'il passe près d'une source d'eau, ne pas la frapper sauf si elle le mérite vraiment, ne pas lui faire porter ce qu'elle ne peut supporter, ne pas l'engager dans un voyage qu'elle ne peut supporter, et ne pas rester assis sur elle de façon trop longue.<sup>2050</sup>"
    },
    {
        "number": "1802",
        "text": "Le Messager d'Allah (s) a dit : Ne frappez pas les animaux sur leurs gueules car en vérité, ils glorifient Allah et lui rendent grâce.<sup>2051</sup>"
    },
    {
        "number": "1803",
        "text": "Le Messager d'Allah (s) a dit : Une prostituée qui passait près d'un chien au pied d'un puits qui haletait et était sur le point de mourir de soif a été pardonnée car elle a enlevé sa chaussure, l'a nouée à son voile, et a puisé de l'eau pour lui. Ainsi, pour ce geste, Allah lui a pardonné.<sup>2052</sup>"
    },
    {
        "number": "1804",
        "text": "Le Messager d'Allah (s) a dit : Tout animal - oiseau ou autre – qui est tué injustement et sans raison se plaindra [à la personne qui l'a tué] le Jour de la Résurrection.<sup>2053</sup>"
    },
    {
        "number": "1805",
        "text": "Le Messager d'Allah (s) a dit : Celui qui a tué un oiseau sans raison verra cet oiseau se plaindre le Jour de la Résurrection auprès d'Allah en disant : «Ô Seigneur, untel m'a tué en vain, il ne m'a pas tué pour une raison utile.»<sup>2054</sup>"
    },
    {
        "number": "1806",
        "text": "Le Messager d'Allah (s) a dit : Si vous étiez pardonnés pour tout ce que vous faites [subir comme injustices] aux animaux, un grand nombre [de vos péchés] serait pardonné.<sup>2055</sup>"
    },
    {
        "number": "1807",
        "text": "Le Messager d'Allah (s) a dit : Ne crains-tu pas Allah vis-à-vis de cet animal qu'Allah t'a autorisé à posséder ?! En vérité, il s'est plaint à moi de la faim et de la peine que tu lui fais subir.<sup>2056</sup>"
    },
    {
        "number": "1808",
        "text": "Le Messager d'Allah (s) a dit : Qu'Allah maudisse celui qui traite durement un animal.<sup>2057</sup>"
    },
    {
        "number": "1809",
        "text": "<em>Kanz al-'Ummāl</em> : [Le Messager d'Allah (s)] a interdit de tuer tout être vivant sauf s'il est nuisible.<sup>2058</sup>"
    },
    {
        "number": "1810",
        "text": "L'Imām al-Ṣādiq (as) a dit : En vérité, une femme a été en proie au châtiment pour avoir attaché une chatte jusqu'à ce qu'elle meure de soif.<sup>2059</sup>"
    }
])

# ============================================================
# Chapter 121 (index 122) - LA PUDEUR
# ============================================================
p121 = 122

s599 = find_subpart(p121, "599")
ensure_hadiths(s599)
s599['hadiths'].extend([
    {
        "number": "1811",
        "text": "L'Imām 'Alī (as) a dit : La pudeur est le moyen d'arriver à toute beauté.<sup>2061</sup>"
    },
    {
        "number": "1812",
        "text": "L'Imām 'Alī (as) a dit : La pudeur est la clé de tout bien.<sup>2062</sup>"
    },
    {
        "number": "1813",
        "text": "L'Imām 'Alī (as) a dit : La plus intelligente des personnes est la plus pudique.<sup>2063</sup>"
    },
    {
        "number": "1814",
        "text": "L'Imām 'Alī (as) a dit : La pudeur préserve de l'acte laid.<sup>2064</sup>"
    },
    {
        "number": "1815",
        "text": "L'Imām 'Alī (as) a dit : La pudeur est la cause de la chasteté.<sup>2065</sup>"
    }
])

s600 = find_subpart(p121, "600")
ensure_hadiths(s600)
s600['hadiths'].extend([
    {
        "number": "1816",
        "text": "Le Messager d'Allah (s) a dit : En vérité, chaque religion a une disposition naturelle, et la disposition naturelle de l'islam est la pudeur.<sup>2066</sup>"
    },
    {
        "number": "1817",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui n'a pas de pudeur est dépourvu de foi.<sup>2067</sup>"
    }
])

s601 = find_subpart(p121, "601")
ensure_hadiths(s601)
s601['hadiths'].extend([
    {
        "number": "1818",
        "text": "Le Messager d'Allah (s) a dit : La pudeur est de deux sortes : la pudeur intelligente et la pudeur stupide. La pudeur intelligente est le savoir, et la pudeur stupide est l'ignorance.<sup>2068</sup>"
    },
    {
        "number": "1819",
        "text": "L'Imām 'Alī (as) a dit : La pudeur [mêlée de honte] va de pair avec la privation.<sup>2069</sup>"
    },
    {
        "number": "1820",
        "text": "L'Imām 'Alī (as) a dit : La pudeur [mêlée de honte] empêche la subsistance.<sup>2070</sup>"
    },
    {
        "number": "1821",
        "text": "L'Imām 'Alī (as) a dit : Celui qui fait preuve de pudeur [mêlée de honte] en n'osant pas dire une parole de vérité est un sot.<sup>2071</sup>"
    }
])

s602 = find_subpart(p121, "602")
ensure_hadiths(s602)
s602['hadiths'].extend([
    {
        "number": "1822",
        "text": "Le Messager d'Allah (s) a dit : Il ne reste des proverbes des prophètes antérieurs que cette parole des gens : «Si tu n'as pas de pudeur, alors agis à ta guise.»<sup>2072</sup>"
    },
    {
        "number": "1823",
        "text": "L'Imām 'Alī (as) a dit : Celui qui n'a pas de pudeur face aux gens n'a pas de pudeur face à Allah - loué soit-Il.<sup>2073</sup>"
    }
])

s603 = find_subpart(p121, "603")
ensure_hadiths(s603)
s603['hadiths'].extend([
    {
        "number": "1824",
        "text": "Le Messager d'Allah (s) a dit : Fais preuve de pudeur vis-à-vis d'Allah comme tu fais preuve de pudeur vis-à-vis de tes voisins vertueux, car cela augmente la certitude.<sup>2074</sup>"
    },
    {
        "number": "1825",
        "text": "Le Messager d'Allah (s) a dit : Chacun de vous doit faire preuve de pudeur vis-à-vis de Ses deux anges qui vous accompagnent comme vous le feriez avec deux de vos voisins vertueux qui seraient avec vous nuit et jour.<sup>2075</sup>"
    },
    {
        "number": "1826",
        "text": "L'Imām al-Kāẓim (as) a dit : Faites preuve de pudeur vis-à-vis d'Allah dans votre intimité comme vous pouvez le faire en public vis-à-vis des gens.<sup>2076</sup>"
    }
])

s604 = find_subpart(p121, "604")
ensure_hadiths(s604)
s604['hadiths'].append({
    "number": "1827",
    "text": "L'Imām 'Alī (as) a dit : Le sommet de la pudeur est que la personne soit pudique vis-à-vis d'elle-même.<sup>2077</sup>"
})

# ============================================================
# Chapter 122 (index 123) - L'ISSUE
# ============================================================
p122 = 123

s605 = find_subpart(p122, "605")
ensure_hadiths(s605)
s605['hadiths'].extend([
    {
        "number": "1828",
        "text": "Le Messager d'Allah (s) a dit : Le croyant est dans la crainte constante d'une issue funeste [de sa vie], et jusqu'au moment de la prise de son âme et de l'apparition de l'ange de la mort face à lui, il n'est pas certain qu'il atteigne la satisfaction d'Allah.<sup>2078</sup>"
    },
    {
        "number": "1829",
        "text": "Le Messager d'Allah (s) a dit : En vérité, il se peut qu'un homme agisse pendant très longtemps selon les actes des gens du Paradis, mais qu'il finisse sa vie en commettant les actes des gens de l'Enfer.<sup>2079</sup>"
    },
    {
        "number": "1830",
        "text": "Le Messager d'Allah (s) a dit : Ne soyez pas émerveillés par [les bonnes actions d'] un être avant d'avoir vu l'issue [de sa vie] car en vérité, quelqu'un peut faire le bien pendant une longue période de sa vie ou une partie de sa vie et s'il venait alors à mourir, il irait au Paradis. Cependant, il change par la suite et commet des actes vils.<sup>2080</sup><br><br><span class=\"reference-note\">(Voir également : 190. Le bonheur, section 948)</span>"
    }
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 1797-1830 injected (pages 325-329)")
print("Chapters: 119 (+1797), 120 (1798-1810), 121 (1811-1827), 122 (1828-1830)")
print("Total hadiths added: 34")
