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

# Part 90 (index 91) - Les limites et peines légales (al-ḥudūd)
p90 = 91
s481 = find_subpart(p90, "481")
s482 = find_subpart(p90, "482")

for s in [s481, s482]:
    clear_hadiths(s)

s481['hadiths'].extend([
    {
        "number": "1450",
        "source": "Tanbīh al-Khawāṭir",
        "text": "Lorsque le Messager d'Allah (s) lapida un homme pour adultère, un homme dit à son compagnon : «Il est mort sur le champ comme un chien.» Lorsque le Prophète (s) passa avec eux devant une carcasse d'animal, il leur dit : «Mangez-en une bouchée.» Ils dirent : «Ô Messager d'Allah, comment mangerions-nous une carcasse ?!» Il dit : «Ce que vous avez dit de votre frère est plus nauséabond que cela.»<sup>1665</sup>"
    },
    {
        "number": "1451",
        "source": "Kanz al-'Ummāl",
        "text": "rapporte de 'Abd al-Raḥmān ibn Abī Laylā : En vérité, 'Alī (as) a appliqué la peine légale sur un homme et la foule s'est mise à injurier et à maudire ce dernier. 'Alī (as) dit alors : «Il ne sera plus questionné à propos de ce péché [vos injures l'en ont expié].»<sup>1666</sup>"
    }
])

s482['hadiths'].extend([
    {
        "number": "1452",
        "text": "Le Messager d'Allah (s) a dit : Pas de peine légale à l'encontre d'une personne qui a avoué [sa faute] après avoir été soumise à une calamité.<sup>1667</sup>"
    },
    {
        "number": "1453",
        "text": "L'Imām 'Alī (as) a dit : La peine légale ne s'applique pas à l'encontre d'un homme ou d'une femme que l'on a forcé [à commettre un péché].<sup>1668</sup>"
    }
])

# Part 91 (index 92) - La guerre
p91 = 92
s483 = find_subpart(p91, "483")
s484 = find_subpart(p91, "484")
s485 = find_subpart(p91, "485")
s486 = find_subpart(p91, "486")
s487 = find_subpart(p91, "487")

for s in [s483, s484, s485, s486, s487]:
    clear_hadiths(s)

s483['hadiths'].extend([
    {
        "number": "1454",
        "text": "L'Imām 'Alī (as) a dit : La divergence est un motif de guerre.<sup>1669</sup>"
    },
    {
        "number": "1455",
        "text": "L'Imām 'Alī (as) a dit : L'obstination est un motif de guerre.<sup>1670</sup>"
    },
    {
        "number": "1456",
        "text": "L'Imām 'Alī (as) a dit : Abstenez-vous de l'obstination blâmable, car elle suscite les guerres.<sup>1671</sup>"
    }
])

s484['hadiths'].append({
    "number": "1457",
    "text": "L'Imām 'Alī (as) a dit : Oui, je fais appel à vous pour combattre ces gens jour et nuit, en secret et en public et je vous ai dit : «Attaquez-les avant qu'ils ne vous attaquent, car par Allah, aucun peuple n'est attaqué au sein de sa demeure sans qu'il ne soit déshonoré.»<sup>1672</sup>"
})

s485['hadiths'].extend([
    {
        "number": "1458",
        "text": "Le Messager d'Allah (s) a dit : Liez-vous d'amitié avec les gens, donnez-leur un sursis et ne les attaquez pas avant de les avoir appelé [à la vérité] ; car j'aime davantage que les hommes de cette terre, citadins ou nomades, me soient ramenés en étant musulmans, plutôt que vous me rameniez leurs femmes et leurs enfants [en tant que prisonniers] alors que vous avez tué les hommes."
    },
    {
        "number": "1459",
        "text": "L'Imām 'Alī (as) a dit lors de la bataille de Ṣiffīn : Par Allah, je n'ai jamais retardé la guerre même d'une journée sans espérer que certains parmi eux me rejoignent afin d'être guidés grâce à moi et reposer dans ma lumière. J'aime davantage cela que de les tuer dans leur égarement.<sup>1674</sup>"
    },
    {
        "number": "1460",
        "text": "L'Imām Ḥusayn (as) a dit : En réalité, le mal de la guerre est rapide et son goût est amer. Par conséquent, celui qui s'y est préparé et apprêté et qui n'est pas atteint [moralement] avant le déclenchement de la guerre, est son maître ; alors que celui qui s'y précipite avant que ne soit venu le moment approprié et avant d'acquérir assez de perspicacité sur [la nature des] efforts [à fournir] ne sera d'aucune utilité à sa troupe, et il détruira sa propre personne.<sup>1675</sup>"
    }
])

s486['hadiths'].append({
    "number": "1461",
    "text": "L'Imām 'Alī (as) a dit dans l'un de ses conseils à Ziyād ibn Naḍr : Sache que l'avant-garde des gens sont leurs yeux, et que les yeux de l'avant-garde sont leurs éclaireurs. Ainsi, lorsque tu quittes ton pays et que tu te rapproches de ton ennemi, n'hésite pas à envoyer des éclaireurs dans toutes les directions et dans certaines vallées, forêts ainsi que dans des cachettes et dans tout coin afin que vous ne soyez pas subitement attaqués par votre ennemi et que vous ne soyez pas pris dans une embuscade.<sup>1676</sup>"
})

s487['hadiths'].extend([
    {
        "number": "1462",
        "text": "Le Messager d'Allah (s) a dit : Les émissaires et les otages ne doivent pas être tués.<sup>1677</sup>"
    },
    {
        "number": "1463",
        "text": "L'Imām 'Alī (as) a dit : Placez les combattants cuirassés à l'avant et ceux qui ne sont pas protégés à l'arrière. Serrez vos mâchoires car cela permet d'amoindrir l'effet d'un coup d'épée sur le crâne, et esquivez les lances sur les côtés car cela change la direction de leurs lames. Fermez les yeux car cela renforce l'esprit et apaise le cœur. Faites taire les voix car cela éloigne l'échec.<sup>1678</sup>"
    },
    {
        "number": "1464",
        "text": "L'Imām 'Alī (as) a dit : Ne les combattez que lorsqu'ils commencent à vous combattre car vous aurez ainsi, par la grâce d'Allah, un argument [selon lequel vous êtes dans le vrai], et le fait de les laisser jusqu'à ce qu'ils commencent à vous combattre est aussi un argument vis-à-vis d'eux. Si, par la permission d'Allah, l'ennemi est défait, ne tuez pas les fuyards, ne frappez pas une personne sans défense, n'achevez pas les blessés et ne portez pas atteinte aux femmes.<sup>1679</sup>"
    }
])

new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1450-1464")
