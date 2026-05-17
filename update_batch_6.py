import json

with open('aune-sagesse-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('[')
end_idx = content.rfind(']') + 1
data = json.loads(content[start_idx:end_idx])

# Helper function to find subpart
def find_subpart(part_index, subpart_start_str):
    for s in data[part_index].get('subparts', []):
        if s['title'].startswith(subpart_start_str):
            return s
    return None

part17 = 18
s127 = find_subpart(part17, "127")
s127['hadiths'].append({
    "number": "408",
    "text": "L'Imām 'Alī (as) a dit : Je n'ai jamais douté de la Vérité depuis qu'elle m'a été montrée.<sup>452</sup>"
})

part18 = 19
s128 = find_subpart(part18, "128")
s129 = find_subpart(part18, "129")
s130 = find_subpart(part18, "130")
s131 = find_subpart(part18, "131")
s132 = find_subpart(part18, "132")

for s in [s128, s129, s130, s131, s132]:
    s['hadiths'] = []

s128['hadiths'].extend([
    {
        "number": "409",
        "text": "Le Messager d'Allah (s) a dit : En vérité, ma fille a été nommée Fāṭima car Allah le Tout-Puissant l'a écartée (<i>faṭama</i>) et a écarté (<i>faṭamahā</i>) ceux qui l'aiment du Feu.<sup>453</sup>"
    },
    {
        "number": "410",
        "text": "L'Imām al-Ṣādiq (as) a dit : Fāṭima, que la paix d'Allah soit sur elle, a neuf noms auprès d'Allah le Tout-Puissant : Fāṭima, la véridique (<i>al-Ṣiddīqa</i>), la bénie (<i>al-Mubāraka</i>), l'immaculée (<i>al-Ṭāhira</i>), la pure (<i>al-Zakiyya</i>), la satisfaite (<i>al-Rāḍiyya</i>), celle qui est agréée par Allah (<i>al-Marḍiyya</i>), celle a qui parle [aux anges] (<i>al-Muḥadditha</i>), et la radieuse (<i>al-Zahrā'</i>).<sup>454</sup>"
    },
    {
        "number": "411",
        "source": "Ma'ānī al-Akhbār",
        "text": "'Ammāra a dit : J'ai demandé à l'Imām al-Ṣādiq (as) : «Pourquoi Fāṭima était-elle appelée «al-Zahrā'» [la radieuse] ?» Il répondit : «En vérité, lorsqu'elle se tenait dans son lieu de prière, sa lumière irradiait les gens du ciel de la même façon que la lumière des astres irradie les gens de la terre.»<sup>455</sup>"
    }
])

s129['hadiths'].extend([
    {
        "number": "412",
        "text": "Le Messager d'Allah (s) a dit : Fāṭima est une partie de moi, celui qui la réjouit m'aura réjouit, celui qui l'a attristé m'aura attristé. Fāṭima est l'être qui m'est le plus cher.<sup>456</sup>"
    },
    {
        "number": "413",
        "text": "Le Messager d'Allah (s) a dit : En vérité, Fāṭima est une partie de moi, elle est la lumière de mes yeux et le fruit de mon cœur. Ce qui l'attriste m'attriste, ce qui la réjouit me réjouit. En vérité, elle sera la première de ma famille à me rejoindre [après ma mort].<sup>457</sup>"
    }
])

s130['hadiths'].extend([
    {
        "number": "414",
        "text": "Le Messager d'Allah (s) a dit : Ma fille Fāṭima est la maîtresse des femmes des deux mondes.<sup>458</sup>"
    },
    {
        "number": "415",
        "text": "Le Messager d'Allah (s) a dit : Fāṭima est la maîtresse des femmes du Paradis.<sup>459</sup>"
    },
    {
        "number": "416",
        "text": "Le Messager d'Allah (s) a dit : Concernant ma fille Fāṭima, elle est la maîtresse des femmes du monde, des premières aux dernières.<sup>460</sup>"
    }
])

s131['hadiths'].append({
    "number": "417",
    "text": "Le Messager d'Allah (s) a dit à Fāṭima (as) : En vérité, Allah est en colère vis-à-vis de ce qui te met en colère, et Il est satisfait lorsque tu es satisfaite.<sup>461</sup>"
})

s132['hadiths'].append({
    "number": "418",
    "text": "L'Imām 'Alī (as) a dit alors qu'il enterrait Fāṭima (as) : Que le salut soit sur toi, ô Messager d'Allah, de ma part et de la part de ta fille qui séjourne à tes côtés et qui s'est empressée de te rejoindre. Ô Messager d'Allah ! Ma patience s'est amoindrie en perdant celle que tu as élue, et mon endurance a diminué ; néanmoins, j'ai de la consolation en ayant enduré l'énorme difficulté et l'événement si douloureux de ta séparation. Je t'ai alors allongé dans ta tombe alors que tu avais expiré ton dernier souffle, [lorsque ta tête] était entre mon cou et ma poitrine. <i>«Certes nous sommes à Allah, et c'est à Lui que nous retournerons.»</i><sup>462</sup> Maintenant, le dépôt [Fāṭima] [que tu m'avais confié] a été restitué et ce qui fut donné a été repris. Concernant ma tristesse, elle est sans limites ; concernant mes nuits, elles resteront sans sommeil jusqu'à ce qu'Allah me choisisse pour la demeure dans laquelle tu résides. Ta fille t'informera bientôt de l'oppression de ta communauté à son égard. Interroge-la en détail et demande-lui l'ensemble des informations sur la situation. Cela a commencé alors que tu venais à peine de nous quitter et que ton souvenir était encore présent. Que le salut soit sur vous deux, le salut de celui qui est accablé par la tristesse, et non de celui qui est dégoûté ni haineux. Si je m'éloigne, ce ne sera pas par lassitude et si je reste, ce ne sera pas par doute à propos de ce qu'Allah a promis aux endurants.<sup>463</sup>"
})

part19 = 20
s133 = find_subpart(part19, "133")
s134 = find_subpart(part19, "134")

s133['hadiths'] = [{
    "number": "419",
    "text": "L'Imām al-Bāqir (as) a dit : En vérité, lorsque la mort de l'Emir des Croyants - que les prières d'Allah soient sur lui – approcha, il dit à son fils Ḥasan : «Approche-toi de moi afin que je te dise un secret que le Messager d'Allah (s) m'a confié, et que je te confie le dépôt qu'il m'a confié.» Et il le fit.<sup>464</sup>"
}]

# For 134, since the user already added 421, we just prepend 420
h420 = {
    "number": "420",
    "text": "Le Messager d'Allah (s) a dit : Ḥasan est de moi et je suis de lui. Allah aime celui qui l'aime. Ḥasan et Ḥusayn sont mes deux petits-fils les plus spéciaux.<sup>465</sup>"
}
if not s134.get('hadiths'):
    s134['hadiths'] = [h420]
elif s134['hadiths'][0].get('number') != "420":
    s134['hadiths'].insert(0, h420)

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 408-420")
