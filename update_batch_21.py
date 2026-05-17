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
# Part 108 (index 109) - La vérité
# ============================================================
p108 = 109

# s548 already has 1647 and an incomplete 1648 - fix it first
s548 = find_subpart(p108, "548")
# Remove the broken 1648 entry and re-add it correctly
s548['hadiths'] = [h for h in s548.get('hadiths', []) if h.get('number') != '1648']
s548['hadiths'].append({
    "number": "1648",
    "text": "L'Imām 'Alī (as) a dit : Sachez que la vérité est [comme] une monture domptée montée par ses propriétaires et dont ils tiennent ses rênes. Ainsi, elle les emmène sereinement jusqu'à atteindre un grand [lieu] ombragé.<sup>1887</sup>"
})
s548['hadiths'].extend([
    {
        "number": "1649",
        "text": "L'Imām 'Alī (as) a dit : Celui qui aspire à l'honneur sans la vérité sera humilié, et celui qui s'oppose à la vérité sera avili.<sup>1888</sup>"
    },
    {
        "number": "1650",
        "text": "L'Imām al-Ṣādiq (as) a dit : Il n'y a pas de faux qui se dresse face à la vérité sans que la vérité ne triomphe sur le faux, c'est ce que signifie la parole <i>«Nous lançons la Vérité contre le faux qui le subjugue, et le voilà qui disparaît...»</i><sup>1889, 1890</sup>"
    }
])

s549 = find_subpart(p108, "549")
clear_hadiths(s549)
s549['introduction'] = "«Certes, Nous vous avions apporté la Vérité ; mais la plupart d'entre vous détestaient la vérité.»<sup>1891</sup>"
s549['hadiths'].extend([
    {
        "number": "1651",
        "text": "L'Imām 'Alī (as) a dit : En fait, la vérité est lourde et difficile, mais douce alors que le faux est léger et facile, mais il tue.<sup>1892</sup>"
    },
    {
        "number": "1652",
        "text": "L'Imām al-Bāqir (as) a dit : Au moment de sa mort, mon père 'Alī ibn al-Ḥusayn (as) me serra contre sa poitrine et me dit : «Ô mon fils ! Je te conseille ce que mon père, à son décès, m'a conseillé – et il mentionna ce que son père lui avait conseillé : «Ô mon fils, patiente face à la vérité même si elle est amère.»<sup>1893</sup>"
    }
])

s550 = find_subpart(p108, "550")
clear_hadiths(s550)
s550['hadiths'].extend([
    {
        "number": "1653",
        "text": "Le Messager d'Allah (s) a dit : La plus pieuse des personnes est celle qui dit la vérité, qu'elle soit dans son intérêt ou à son détriment.<sup>1894</sup>"
    },
    {
        "number": "1654",
        "text": "L'Imām 'Alī (as) a dit : Il est écrit sur la poignée d'une épée du Messager d'Allah (s) : «Dis la vérité, même si c'est à ton détriment».<sup>1895</sup>"
    },
    {
        "number": "1655",
        "text": "L'Imām 'Alī (as) a dit : En vérité, la meilleure personne auprès d'Allah est celle pour qui le fait d'agir selon la vérité – même si cela lui apporte une perte et un malheur - est plus aimé que ce qui est faux, même si cela lui apporte un profit et un accroissement [de ses richesses].<sup>1896</sup>"
    },
    {
        "number": "1656",
        "text": "L'Imām al-Kāẓim (as) a dit : Dis la vérité même si cela conduit à ta ruine, car en vérité, en cela réside ton salut … Et écarte-toi du faux même si cela peut te sauver, car en vérité, en cela réside ta ruine.<sup>1897</sup>"
    }
])

s551 = find_subpart(p108, "551")
clear_hadiths(s551)
s551['hadiths'].extend([
    {
        "number": "1657",
        "text": "Le Messager d'Allah (s) a dit : Que la crainte qu'éprouve vis-à-vis des gens n'empêche pas la personne de dire la vérité lorsqu'elle la connaît. Le meilleur des combats (<i>jihād</i>) est une parole vraie dite face à un dirigeant oppresseur.<sup>1898</sup>"
    },
    {
        "number": "1658",
        "text": "Parmi les conseils qu'il donna à son fils Ḥusayn (as), l'Imām 'Alī (as) a dit : Ô mon fils ! Je te recommande de craindre Allah dans la prospérité et dans la pauvreté, et de dire la vérité dans la satisfaction et dans la colère.<sup>1899</sup>"
    }
])

s552 = find_subpart(p108, "552")
clear_hadiths(s552)
s552['hadiths'].extend([
    {
        "number": "1659",
        "text": "Le Messager d'Allah (s) a dit : Accepte la vérité de toute personne qui vient à toi avec elle, que cette personne soit modeste ou noble, et même si elle t'est détestable. Et rejette le faux de toute personne qui vient à toi avec lui, qu'elle soit modeste ou noble, et même si tu l'aimes.<sup>1900</sup>"
    },
    {
        "number": "1660",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'honneur est de faire preuve d'humilité face à la vérité lorsqu'elle te fait face.<sup>1901</sup>"
    }
])

s553 = find_subpart(p108, "553")
clear_hadiths(s553)
s553['hadiths'].append({
    "number": "1661",
    "text": "L'Imām 'Alī (as) a dit : La vérité ne peut pas être connue par les hommes ; connais la vérité [d'abord] et tu [re]connaîtras ses adeptes.<sup>1902</sup><br><br><span class=\"hadith-footnote\">(Voir également : 137. Le bien, section 679)</span>"
})

s554 = find_subpart(p108, "554")
clear_hadiths(s554)
s554['hadiths'].extend([
    {
        "number": "1662",
        "text": "L'Imām 'Alī (as) a dit : La vérité est la plus vaste des choses quand il s'agit de sa description, et la plus restreinte quand il s'agit de pratiquer la justice. Dès qu'elle est en faveur de quelqu'un, elle devient contre lui [à une autre occasion], et dès qu'elle est contre quelqu'un, elle est en sa faveur [à une autre occasion]. Et si quelqu'un était en sa faveur et jamais contre elle, ce pourrait uniquement être pour Allah loué soit-Il.<sup>1903</sup>"
    },
    {
        "number": "1663",
        "text": "L'Imām 'Alī (as) a dit : Que la défense du droit de quelqu'un ne vous empêche pas de défendre la vérité lorsqu'elle est contre lui.<sup>1904</sup>"
    }
])


# ============================================================
# Part 109 (index 110) - Les droits
# ============================================================
p109 = 110

s555 = find_subpart(p109, "555")
s556 = find_subpart(p109, "556")
s557 = find_subpart(p109, "557")
s558 = find_subpart(p109, "558")

for s in [s555, s556, s557, s558]:
    clear_hadiths(s)

s555['hadiths'].extend([
    {
        "number": "1664",
        "text": "Le Messager d'Allah (s) a dit : En vérité, les droits d'Allah<sup>1905</sup> – glorifiée soit sa louange – sont trop vastes pour que les serveurs [d'Allah] puissent tous les réaliser, et en vérité, les grâces d'Allah sont trop nombreuses pour pouvoir être comptabilisées par les serviteurs. En revanche, [la moindre chose que vous pouvez faire est de] commencer vos journées et vos nuits en étant repentants.<sup>1906</sup>"
    },
    {
        "number": "1665",
        "text": "L'Imām 'Alī (as) a dit : [...] Pourtant, Il – loué soit-Il – a fait en sorte que Son droit vis-à-vis des serviteurs soit qu'ils Lui obéissent, et Il a fait de leur rétribution [pour leurs actes d'obéissance] une augmentation de leur récompense par pure bonté de Sa part.<sup>1907</sup>"
    }
])

s556['hadiths'].append({
    "number": "1666",
    "text": "L'Imām 'Alī (as) a dit : Allah - loué soit-Il - a donné la priorité aux droits de Ses serviteurs avant Ses propres droits. Par conséquent, celui qui satisfait les droits des serviteurs d'Allah est conduit à satisfaire les droits d'Allah.<sup>1908</sup>"
})

s557['hadiths'].append({
    "number": "1667",
    "text": "L'Imām 'Alī (as) a dit : Le plus grand des droits qu'Allah - loué soit-Il - a rendu obligatoire est le droit du gouverneur sur les gouvernés, et le droit des gouvernés sur le gouverneur.<sup>1909</sup>"
})

s558['hadiths'].extend([
    {
        "number": "1668",
        "text": "L'Imām al-Bāqir (as) a dit : Parmi les droits du croyant sur son frère croyant figure celui de rassasier sa faim, de couvrir sa nudité, de le délivrer de son malheur, de rembourser ses dettes et lorsqu'il meurt, de le remplacer [pour subvenir aux besoins] de sa famille et de ses enfants.<sup>1910</sup>"
    },
    {
        "number": "1669",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui honore la religion d'Allah honore les droits de ses frères, et celui qui prend sa religion à la légère prend à la légère [les droits de] ses frères.<sup>1911</sup>"
    },
    {
        "number": "1670",
        "text": "L'Imām al-Ṣādiq (as) a dit : Allah ne peut être mieux adoré que par la réalisation des droits du croyant.<sup>1912</sup>"
    }
])


new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done updating hadiths 1648-1670")
