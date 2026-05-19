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
# Chapter 129 (index 130) - LA SINCÉRITÉ (continuation)
# ============================================================
p129 = 130

# Section 624 - Les signes caractéristiques de la personne sincère
s624 = find_subpart(p129, "624")
ensure_hadiths(s624)
s624['hadiths'].extend([
    {
        "number": "1881",
        "text": "L'Imām 'Alī (as) a dit : L'adoration sincère et pure est quand l'homme n'espère qu'en son Seigneur et qu'il ne craint que [les conséquences de] son propre péché.<sup>2140</sup>"
    },
    {
        "number": "1882",
        "text": "L'Imām al-Ṣādiq (as) a dit : L'acte sincère est celui dont tu ne souhaites les louanges que d'Allah le Tout-Puissant.<sup>2141</sup>"
    },
    {
        "number": "1883",
        "text": "Ma'ānī al-Akhbār : L'Archange Gabriel (as) a dit lorsque le Prophète lui demanda de lui expliquer ce qu'était la sincérité : Le sincère est celui qui ne demande rien aux gens jusqu'à ce qu'il trouve lui-même, et lorsqu'il trouve, il est satisfait. Et lorsqu'il lui reste quelque chose, il la donne pour Dieu. En effet, celui qui ne demande rien aux créatures reconnaît en réalité sa servitude exclusive vis-à-vis d'Allah le Tout-Puissant, et lorsqu'il trouve [ce dont il a besoin] et qu'il en est satisfait, il est satisfait vis-à-vis d'Allah et Allah le Béni et le Très-Haut est satisfait de lui. Et lorsqu'il donne pour Allah, il a alors atteint le rang de la confiance en son Seigneur le Tout-Puissant.<sup>2142</sup>"
    }
])

# Section 625 - Ce qui suscite la sincérité
s625 = find_subpart(p129, "625")
ensure_hadiths(s625)
s625['hadiths'].extend([
    {
        "number": "1884",
        "text": "L'Imām 'Alī (as) a dit : La cause de la sincérité est la certitude.<sup>2143</sup>"
    },
    {
        "number": "1885",
        "text": "L'Imām 'Alī (as) a dit : Le fruit du savoir est la sincérité de l'acte.<sup>2144</sup>"
    },
    {
        "number": "1886",
        "text": "L'Imām 'Alī (as) a dit : Réduis tes espoirs et tes actes deviendront sincères.<sup>2145</sup>"
    },
    {
        "number": "1887",
        "text": "L'Imām 'Alī (as) a dit : La racine de la sincérité est de ne plus espérer obtenir ce qui est entre les mains des gens.<sup>2146</sup>"
    }
])

# Section 626 - Les effets de la sincérité
s626 = find_subpart(p129, "626")
ensure_hadiths(s626)
s626['hadiths'].extend([
    {
        "number": "1888",
        "text": "Le Messager d'Allah (s) a dit : Allah le Tout-Puissant a dit : «Dès que Je regarde le cœur du serviteur et que Je trouve qu'il a un amour sincère pour Ma seule obéissance et qu'il recherche Ma satisfaction, Je me charge aussitôt de ses programmes et de ses affaires.»<sup>2147</sup>"
    },
    {
        "number": "1889",
        "text": "Le Messager d'Allah (s) a dit : Dès qu'un serviteur d'Allah le Tout-Puissant consacre avec sincérité quarante matins [de dévotion] à Allah, il verra les sources de la sagesse se répandre de son cœur à sa langue.<sup>2148</sup>"
    },
    {
        "number": "1890",
        "text": "L'Imām 'Alī (as) a dit : Celui qui a purifié et rendu sincère son intention restera exempt et pur de toute bassesse.<sup>2149</sup>"
    },
    {
        "number": "1891",
        "text": "L'Imām al-Ṣādiq (as) a dit : «En vérité, toute chose s'humilie devant le croyant et il est craint par toute chose.» Il ajouta : «S'il fait preuve de sincérité pour Allah, alors Allah fera en sorte qu'il soit craint par toute chose, même par les animaux sauvages et venimeux de la terre, ainsi que les oiseaux du ciel.»<sup>2150</sup>"
    }
])

# ============================================================
# Chapter 130 (index 131) - LA DIVERGENCE
# ============================================================
p130 = 131

# Section 627
s627 = find_subpart(p130, "627")
ensure_hadiths(s627)
s627['introduction'] = "«Les hommes ne formaient [à l'origine] qu'une seule communauté. Puis ils divergèrent. Et si ce n'était une décision préalable de ton Seigneur, les litiges qui les opposaient auraient été tranchés.»<sup>2151</sup>"
s627['hadiths'].append({
    "number": "1892",
    "text": "L'Imām al-Bāqir (as) a dit : Avant Noé, les hommes étaient une seule communauté agissant selon la nature originelle divine (<em>fiṭra</em>). Ils n'étaient ni guidés ni égarés ; puis Allah envoya les prophètes.<sup>2152</sup>"
})

# Section 628
s628 = find_subpart(p130, "628")
ensure_hadiths(s628)
s628['introduction'] = "«Cramponnez-vous tous ensemble au câble [<em>ḥabl</em>] d'Allah et ne soyez pas divisés ; et rappelez-vous le bienfait d'Allah sur vous : lorsque vous étiez ennemis, c'est Lui qui réconcilia vos cœurs. Puis, par Son bienfait, vous êtes devenus frères.»<sup>2153</sup>"
s628['hadiths'].extend([
    {
        "number": "1893",
        "text": "Le Messager d'Allah (s) a dit : Aucune communauté n'a connu de divergences après son prophète sans que les défenseurs du faux parmi elle triomphent sur ceux qui défendent la vérité.<sup>2154</sup>"
    },
    {
        "number": "1894",
        "text": "L'Imām 'Alī (as) a dit : Demeurez avec la grande majorité, car la main d'Allah est avec le [plus large] groupe. Gare à la division, car celui qui dévie parmi les gens devient une proie de Satan, de même que [la brebis] qui dévie du troupeau devient la proie du loup.<sup>2155</sup>"
    },
    {
        "number": "1895",
        "text": "L'Imām 'Alī (as) a dit : Par Allah, je crois que ce groupe vous dominera bientôt en raison de son unité autour de leur fausseté et de votre division autour de votre vérité.<sup>2156</sup>"
    },
    {
        "number": "1896",
        "text": "L'Imām 'Alī (as) a dit : Il n'y a pas deux prétentions qui se contredisent sans que l'une d'elles soit erronée.<sup>2157</sup>"
    }
])

# Section 629
s629 = find_subpart(p130, "629")
ensure_hadiths(s629)
s629['hadiths'].append({
    "number": "1897",
    "text": "Ma'ānī al-Akhbār : 'Abd al-Mū'min al-Anṣārī a dit : J'ai dit à l'Imām al-Ṣādiq (as) : «En vérité, des gens ont rapporté que le Messager d'Allah (s) a dit : «La séparation de ma communauté est une miséricorde.»» L'Imām (as) dit : «Ils disent vrai.» Je lui dis alors : «Si leur séparation est une miséricorde, alors dans ce cas leur union est-elle un châtiment ?» Il répondit : «[Le sens de cette parole] n'est pas ce que tu en as compris ni ce qu'ils en ont compris. En vérité, il voulait parler de cette parole d'Allah : «Pourquoi de chaque clan quelques hommes ne viendraient-ils pas s'instruire dans la religion, pour pouvoir à leur retour avertir leur peuple afin qu'ils soient sur leur garde.» Ainsi, Il leur a ordonné de se rendre auprès du Messager d'Allah (s), de le fréquenter et de s'instruire auprès de lui, puis de retourner chez les leurs pour leur enseigner [ce qu'ils ont appris]. [Le Prophète] a voulu ainsi désigner la séparation [physique] de leurs contrées, et non la séparation et la divergence au sujet de la religion d'Allah, car la religion est unique.»<sup>2158</sup><sup>2159</sup>"
})

# Section 630
s630 = find_subpart(p130, "630")
ensure_hadiths(s630)
s630['hadiths'].append({
    "number": "1898",
    "text": "L'Imām al-Ṣādiq (as) a dit : Lorsque le Messager d'Allah (s) fut interrogé au sujet du groupe de sa communauté, il dit : «Le groupe de ma communauté sont les gens de vérité, même s'ils sont peu nombreux.»<sup>2160</sup>"
})

# Section 631
s631 = find_subpart(p130, "631")
ensure_hadiths(s631)
s631['hadiths'].extend([
    {
        "number": "1899",
        "text": "L'Imām 'Alī (as) a dit : En vérité, vous êtes des frères de la religion d'Allah, rien ne vous a divisé hormis la malveillance des fors intérieurs et les mauvaises consciences. A cause de cela, vous ne porterez plus les charges les uns des autres, ni ne vous conseillerez, ni ne dépenserez les uns pour les autres, ni n'aurez de l'affection les uns pour les autres.<sup>2161</sup>"
    },
    {
        "number": "1900",
        "text": "L'Imām 'Alī (as) a dit : Si les ignorants s'étaient tus, les gens n'auraient pas été en proie aux divergences.<sup>2162</sup>"
    }
])

# ============================================================
# Chapter 131 (index 132) - LA CRÉATION
# ============================================================
p131 = 132

# Section 632
s632 = find_subpart(p131, "632")
ensure_hadiths(s632)
s632['hadiths'].extend([
    {
        "number": "1901",
        "text": "Le Messager d'Allah (s) a dit : Toute chose a été créée à partir d'eau.<sup>2163</sup>"
    },
    {
        "number": "1902",
        "text": "Le Messager d'Allah (s) a dit : Allah a créé le ciel de ce monde à partir de la vague maîtrisée.<sup>2164</sup>"
    },
    {
        "number": "1903",
        "text": "<em>Biḥār al-Anwār</em> : Ḥabbat al-'Uranī a dit : Un jour j'ai entendu 'Alī (as) prêter serment en ces termes : «Par Celui qui a créé le ciel à partir de la fumée et de l'eau.»<sup>2165</sup>"
    }
])

# Section 633
s633 = find_subpart(p131, "633")
ensure_hadiths(s633)
s633['hadiths'].extend([
    {
        "number": "1904",
        "text": "Le Messager d'Allah (s) a dit : En vérité, la première chose qu'Allah a créée est le calame, et Il lui a ordonné de transcrire toute chose qui allait exister.<sup>2166</sup>"
    },
    {
        "number": "1905",
        "text": "Le Messager d'Allah (s) a dit : La première chose qu'Allah a créée est l'intellect.<sup>2167</sup>"
    },
    {
        "number": "1906",
        "text": "Le Messager d'Allah (s) a dit : La première chose qu'Allah a créée est ma lumière.<sup>2168</sup>"
    },
    {
        "number": "1907",
        "text": "Le Messager d'Allah (s) a dit : La première chose qu'Allah le Tout-Puissant a créée sont nos esprits, et Il leur a fait professer Son unicité et Sa louange. Puis Il a créé les anges.<sup>2169</sup>"
    },
    {
        "number": "1908",
        "text": "Interrogé au sujet de la première chose qu'Allah a créée, l'Imām 'Alī (as) répondit : Il a créé la lumière.<sup>2170</sup>"
    },
    {
        "number": "1909",
        "text": "L'Imām al-Bāqir (as) a dit : La première chose qu'Allah a créée est la chose qui est à l'origine de toute chose, c'est-à-dire l'eau.<sup>2171</sup>"
    }
])

# Section 634
s634 = find_subpart(p131, "634")
ensure_hadiths(s634)
s634['introduction'] = "«Ceux qui ont mécru, n'ont-ils pas vu que les cieux et la terre formaient une masse compacte ? Ensuite Nous les avons séparés et fait de l'eau toute chose vivante. Ne croiront-ils donc pas ?»<sup>2172</sup>"
s634['hadiths'].extend([
    {
        "number": "1910",
        "text": "L'Imām 'Alī (as) a dit : Il n'a pas créé les choses d'une matière ou de modèles éternels, mais Il a créé ce qu'Il a créé et Il lui a fixé ses limites ; Il a façonné ce qu'Il a façonné et Il a parfait sa forme.<sup>2173</sup>"
    },
    {
        "number": "1911",
        "text": "L'Imām al-Bāqir (as) a dit : En vérité, Allah le Béni et le Très-Haut… n'a pas créé les êtres à partir d'une autre chose, et celui qui prétend qu'Allah le Très-Haut a créé les êtres à partir d'une chose aura mécru.<sup>2174</sup>"
    }
])

# Section 635
s635 = find_subpart(p131, "635")
ensure_hadiths(s635)
s635['hadiths'].extend([
    {
        "number": "1912",
        "text": "L'Imām 'Alī (as) a dit : Gloire à toi ! Comme est grandiose ce que nous voyons de Ta création ! Et comme toute grandeur est petite comparé à Ta puissance ! Comme est effrayant ce que nous voyons de Ton royaume ! Et comme cela est insignifiant comparé à ce qui nous est invisible de Ton autorité ! Comme Tes grâces sont répandues sur ce monde ! Et comme elles sont petites face aux grâces de l'Au-delà !<sup>2175</sup>"
    },
    {
        "number": "1913",
        "text": "L'Imām al-Bāqir (as) a dit : Peut-être croyez-vous qu'Allah n'a créé que ce monde unique, et qu'Il n'a pas créé d'autres hommes que vous ! Non par Allah, Allah a créé un million de mondes et un million d'Adam, et vous êtes les derniers de ces mondes et de ces êtres humains.<sup>2176</sup>"
    }
])

# ============================================================
# Chapter 132 (index 133) - LE CRÉATEUR
# ============================================================
p132 = 133

# Section 636
s636 = find_subpart(p132, "636")
ensure_hadiths(s636)
s636['hadiths'].append({
    "number": "1914",
    "text": "<em>Al-Tawḥīd</em> rapporte de l'Imām al-Ṣādiq (as) s'adressant à 'Abd al-Karīm ibn Abī al-'Awjā', qui reniait l'origine et la Résurrection : «Si la chose est comme ce que tu avances - ce qui n'est pas le cas -, nous serons sauvés et tu seras sauvé. En revanche, si les choses sont comme nous le disons - et c'est le cas -, nous serons sauvés et tu seras anéanti.» 'Abd al-Karīm se tourna vers ceux qui l'accompagnaient et dit : «Je sens une angoisse dans mon cœur, faites-moi sortir.» Ainsi, ils l'emmenèrent et il mourut.<sup>2177</sup>"
})

# Section 637
s637 = find_subpart(p132, "637")
ensure_hadiths(s637)
s637['introduction'] = "<strong>1 - La connaissance issue de la nature divine primordiale de l'homme</strong><br><br>«Dirige tout ton être vers la religion exclusivement [pour Allah], telle est la nature [divine] primordiale (<em>fiṭra</em>) qu'Allah a originellement donnée aux hommes.»<sup>2178</sup>"
s637['hadiths'].extend([
    {
        "number": "1915",
        "text": "Le Messager d'Allah (s) a dit : Tout nouveau-né vient au monde avec la nature divine primordiale (<em>fiṭra</em>), c'est-à-dire la connaissance [intérieure] qu'Allah le Tout-Puissant est son Créateur. C'est cela que signifie Sa parole : «Si tu leur demandes : \"Qui a créé les cieux et la terre ?\", ils diront, certes : \"Allah !\"»<sup>2179</sup><sup>2180</sup>"
    },
    {
        "number": "1916",
        "text": "L'Imām al-'Askarī (as) a dit en expliquant la <em>basmallah</em> : Allah est Celui que déifie et vénère toute créature lorsqu'elle est dans le besoin ou en difficulté, lorsque l'espoir envers toute chose autre que Lui est rompu, et lorsque plus aucun moyen ne reste en dehors de Lui.<sup>2182</sup>"
    },
    {
        "number": "1917",
        "text": "<strong>2 - La loi de la causalité</strong><br><br>«Ont-ils été créés à partir de rien ou sont-ils eux les créateurs ? Ou ont-ils créé les cieux et la terre ? Mais ils n'ont plutôt aucune conviction.»<sup>2183</sup><br><br>Interrogé par un érudit de Syrie qui lui demanda : «Allah a-t-il créé [les choses] à partir d'une autre chose ou du néant ?», l'Imām al-Bāqir (as) répondit : «Il a créé les choses mais non pas à partir d'une chose qui préexistait. S'il avait créé une chose à partir d'une autre chose, il en serait allé ainsi indéfiniment [cela aura entraîné une régression à l'infini], et il y aurait toujours eu une chose existant aux côtés d'Allah. Or, Allah était sans qu'il n'y ait avec lui autre chose.»<sup>2184</sup>"
    },
    {
        "number": "1918",
        "text": "Lorsque Abū Shākir al-Dayṣānī lui demanda : «Quelle est la preuve que tu as un Créateur ?», l'Imām al-Ṣādiq (as) lui répondit : «J'ai réalisé qu'il n'y avait que ces deux alternatives me concernant : soit je me suis créé moi-même, soit quelqu'un d'autre que moi m'a créé. Si je me suis créé moi-même, alors il n'y a que deux possibilités : soit je me suis créé alors que j'existais déjà auparavant, soit je me suis créé alors que j'étais inexistant. Si je me suis créé alors que j'existais déjà auparavant, dans ce cas, nul besoin de me créer puisque j'existais déjà. En revanche, si j'étais auparavant inexistant, dans ce cas, tu sais que le néant ne peut rien amener à l'existence. Ainsi, la troisième signification est prouvée : j'ai un Créateur et c'est Allah, le Seigneur des mondes.» L'homme se leva sans trouver de réponse à cela.<sup>2185</sup>"
    }
])

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Done! Hadiths 1881-1918 injected successfully (pages 340-347)")
print("Chapters updated: 129 (La Sincérité), 130 (La Divergence), 131 (La Création), 132 (Le Créateur)")
print(f"Total hadiths added: 38")
