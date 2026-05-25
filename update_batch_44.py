import json
import os

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
# Part 173 (index 174) - L'ADULTÈRE
# ============================================================
p173 = 174

# Subpart 859 - L'interdiction de l'adultère
s859 = find_subpart(p173, "859"); eh(s859)
s859['hadiths'] = [
    {
        "number": "2726",
        "text": "Le Messager d'Allah (s) a dit : La colère d'Allah le Tout-Puissant sera sévère vis-à-vis de la femme mariée qui a rempli son regard [de désir] pour un homme autre que son mari ou un proche parent [non mari]. Si elle agit ainsi, Allah anéantira tout acte qu'elle accomplit, et si elle fait entrer un autre homme dans son lit, Allah la fera brûler de plein droit dans le Feu après l'avoir châtiée dans sa tombe.<sup>3076</sup>"
    },
    {
        "number": "2727",
        "text": "L'Imām 'Alī (as) a dit : Celui qui a un sens de l'honneur ne commet jamais d'adultère.<sup>3077</sup>"
    },
    {
        "number": "2728",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le Jour du Jugement, la personne la plus sévèrement châtiée sera un homme qui a déposé sa semence dans un utérus qui lui était interdit.<sup>3078</sup>"
    },
    {
        "number": "2729",
        "text": "L'Imām al-Riḍā (as) a dit : L'adultère a été interdit en raison de la turpitude qu'il engendre dont le meurtre, la perte des filiations, le délaissement de l'éducation des enfants, la corruption des lignées, et toutes sortes d'autres turpitudes qui ressemblent à cela.<sup>3079</sup>"
    }
]

# Subpart 860 - Les conséquences de l'adultère
s860 = find_subpart(p173, "860"); eh(s860)
s860['hadiths'] = [
    {
        "number": "2730",
        "text": "Le Messager d'Allah (s) a dit : Ô 'Alī, l'adultère a six conséquences ; trois dans ce bas-monde, et trois dans l'Au-delà. Dans ce bas-monde, il ruine la beauté, précipite la mort, et coupe l'accès à la subsistance. Dans l'Au-delà, il entraîne un jugement funeste, le courroux du Tout-Miséricordieux, et le séjour éternel dans le Feu.<sup>3080</sup>"
    },
    {
        "number": "2731",
        "text": "L'Imām 'Alī (as) a dit : L'adultère suscite la pauvreté.<sup>3081</sup>"
    },
    {
        "number": "2732",
        "text": "L'Imām al-Bāqir (as) a dit : Nous avons trouvé ceci écrit dans le livre du Messager d'Allah (s) : «Si l'adultère prédomine après moi [après mon décès], les morts subites augmenteront.»<sup>3082</sup>"
    }
]

# ============================================================
# Part 174 (index 175) - LE RENONCEMENT
# ============================================================
p174 = 175

# Subpart 862 - La vertu du renoncement
s862 = find_subpart(p174, "862"); eh(s862)
s862['hadiths'] = [
    {
        "number": "2739",
        "text": "L'Imām 'Alī (as) a dit : En vérité, parmi les qualités qui permettent de faire grandir la foi figure le renoncement aux plaisirs de ce monde.<sup>3090</sup>"
    },
    {
        "number": "2740",
        "text": "L'Imām al-Bāqir (as) a dit : Dans l'un de Ses entretiens intimes avec Moïse (as), Allah a dit : Le meilleur ornement de ceux qui cherchent à s'embellir [pour Moi] est le renoncement aux plaisirs de ce monde dont ils peuvent se passer.<sup>3091</sup>"
    },
    {
        "number": "2741",
        "text": "L'Imām al-Ṣādiq (as) a dit : Tout le bien a été placé dans un lieu, et sa clé est le renoncement aux plaisirs de ce monde.<sup>3092</sup>"
    }
]

# Subpart 863 - La signification réelle du renoncement
s863 = find_subpart(p174, "863"); eh(s863)
s863['introduction'] = (
    "«<i>Afin que vous ne vous tourmentiez pas au sujet de ce qui vous a échappé, "
    "ni n'exultiez pour ce qu'Il vous a donné. Et Allah n'aime point tout présomptueux plein de gloriole.</i>»<sup>3093</sup>"
)
s863['hadiths'] = [
    {
        "number": "2742",
        "text": "Le Messager d'Allah (s) a dit : Le renoncement aux plaisirs de ce monde consiste à réduire ses espoirs [en lui], à remercier pour chaque grâce, ainsi qu'à faire preuve de piété et à éviter tout ce qu'Allah a interdit.<sup>3094</sup>"
    },
    {
        "number": "2743",
        "text": "Le Messager d'Allah (s) a dit : Le renoncement n'est pas de s'interdire ce qui est licite, mais c'est de trouver plus sûr ce qu'il y a entre les mains d'Allah que ce qu'il y a entre ses propres mains.<sup>3095</sup>"
    },
    {
        "number": "2744",
        "text": "L'Imām 'Alī (as) a dit : Le renoncement est résumé dans deux phrases [du Coran, dans lequel] Allah le Très-Haut a dit : «<i>Afin que vous ne vous tourmentiez pas au sujet de ce qui vous a échappé, ni n'exultiez pour ce qu'Il vous a donné. Et Allah n'aime point tout présomptueux plein de gloriole.</i>»<sup>3096</sup> Ainsi, celui qui ne regrette pas le passé ni ne se réjouit des biens qu'il obtient aura réuni les deux aspects du renoncement.<sup>3097</sup>"
    },
    {
        "number": "2745",
        "text": "L'Imām al-Ṣādiq (as) a dit : Le renoncement est la clé de la porte de l'Au-delà et de l'immunité vis-à-vis du Feu, et il consiste à s'abstenir de toute chose qui t'occupe au détriment d'Allah, et ce sans regretter sa perte, sans admirer le fait de l'avoir délaissée, sans attente d'en être délivré, sans rechercher des louanges pour cela ni aucune contrepartie. Il faut plutôt voir sa perte comme une source de repos et sa présence comme un vice, de telle sorte que tu fuies toujours le vice et que tu recherches le repos.<sup>3098</sup>"
    }
]

# Subpart 864 - Les caractéristiques de celui qui renonce
s864 = find_subpart(p174, "864"); eh(s864)
s864['hadiths'] = [
    {
        "number": "2746",
        "text": "L'Imām 'Alī (as) a dit : Celui qui renonce aux plaisirs de ce monde est tel que les choses interdites ne vainquent pas sa patience [et sa persévérance dans la voie d'Allah], et que l'obtention des choses licites ne le détourne pas de la gratitude [envers Allah].<sup>3099</sup>"
    },
    {
        "number": "2747",
        "text": "L'Imām 'Alī (as) a dit : En vérité, ceux qui renoncent aux plaisirs de ce monde sont tels que leurs cœurs pleurent même s'ils rient [en apparence], ils ressentent un profond chagrin même s'ils manifestent de la joie [en apparence], et ils sont remplis de colère contre eux-mêmes même s'ils se réjouissent de ce qui leur a été accordé comme subsistance.<sup>3100</sup>"
    },
    {
        "number": "2748",
        "text": "Interrogé au sujet de celui qui renonce aux plaisirs de ce monde, l'Imām al-Ṣādiq (as) a dit : C'est celui qui délaisse les choses licites de ce monde par crainte des comptes [et du Jugement à leur sujet], et qui délaisse les choses illicites par crainte de subir un châtiment à cause d'elles.<sup>3101</sup>"
    }
]

# Subpart 867 - Celui qui fait preuve du plus grand renoncement
s867 = find_subpart(p174, "867"); eh(s867)
s867['hadiths'] = [
    {
        "number": "2756",
        "text": "L'Imām 'Alī (as) a dit : Celui qui a renoncé aux plaisirs de ce monde sans se préoccuper de sa bassesse ni rivaliser pour sa gloire sera guidé par Allah sans besoin de la guidance d'une créature, Il lui accordera le savoir sans besoin d'étudier, Il ancrera la sagesse dans sa poitrine et Il la répandra sur sa langue.<sup>3109</sup>"
    },
    {
        "number": "2757",
        "text": "L'Imām 'Alī (as) a dit : Renonce aux plaisirs de ce monde et la miséricorde se répandra sur toi.<sup>3110</sup>"
    },
    {
        "number": "2758",
        "text": "L'Imām 'Alī (as) a dit : Le renoncement aux plaisirs de ce monde est la plus grande source de repos.<sup>3111</sup>"
    },
    {
        "number": "2759",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Celui qui renonce aux plaisirs de ce monde fera facilement face à ses malheurs et ils ne l'affecteront pas.<sup>3112</sup>"
    },
    {
        "number": "2760",
        "text": "L'Imām al-Ṣādiq (as) a dit : Il est interdit à vos cœurs de goûter la douceur de la foi tant qu'ils ne renoncent pas aux plaisirs de ce monde.<sup>3113</sup>"
    },
    {
        "number": "2761",
        "text": "Le Messager d'Allah (s) a dit : Celui qui fait preuve du plus grand renoncement est celui qui s'abstient des choses illicites.<sup>3114</sup>"
    },
    {
        "number": "2762",
        "text": "L'Imām 'Alī (as) a dit : Ne sois pas de ceux qui aspirent à l'Au-delà en agissant en fonction du monde terrestre... Ceux-là parlent de ce bas-monde comme ceux qui y ont renoncé, tout en y agissant à la manière de ceux qui le désirent.<sup>3115</sup>"
    },
    {
        "number": "2763",
        "text": "L'Imām 'Alī (as) a dit : Le meilleur renoncement est de cacher son renoncement.<sup>3116</sup>"
    }
]

# ============================================================
# Part 175 (index 176) - LE MARIAGE
# ============================================================
p175 = 176

# Subpart 868 - L'incitation au mariage
s868 = find_subpart(p175, "868"); eh(s868)
s868['introduction'] = (
    "«<i>Mariez les célibataires d'entre vous et les gens de bien parmi vos esclaves, hommes et femmes. "
    "S'ils sont pauvres, Allah les rendra riches par Sa grâce. Car [la grâce d'] Allah est immense et Il "
    "est Omniscient.</i>»<sup>3120</sup>"
    "<br><br>«<i>Et parmi Ses signes Il a créé de vous, pour vous, des épouses afin que vous trouviez auprès "
    "d'elles votre quiétude, et a mis entre vous de l'affection et de la bonté. Il y a en cela des signes "
    "pour les gens qui réfléchissent.</i>»<sup>3121</sup>"
    "<br><br><span class=\"reference-note\">(Voir également : Coran 3:39, 16:72, 30:32, 25:74)</span>"
)
s868['hadiths'] = [
    {
        "number": "2764",
        "text": "L'Imām 'Alī (as) a dit : Si celui qui a renoncé [aux plaisirs de ce monde] fuit les gens, recherche-le, et si celui qui y a renoncé recherche la compagnie des gens, fuis-le.<sup>3117</sup>"
    },
    {
        "number": "2765",
        "text": "L'Imām Zayn al-'Ābidīn (as) a dit : Allah a dit : Ô fils d'Adam, sois satisfait de ce que Je t'ai donné, tu seras celui qui fait le plus preuve de renoncement parmi les gens.<sup>3118</sup>"
    },
    {
        "number": "2766",
        "text": "L'Imām al-Kāẓim (as) a dit : Celui qui parmi vous est le plus patient face aux malheurs est celui qui a le plus renoncé aux plaisirs de ce monde.<sup>3119</sup>"
    },
    {
        "number": "2767",
        "text": "Le Messager d'Allah (s) a dit : Celui qui aspire à rencontrer Allah en étant pur et purifié doit Le rencontrer accompagné de sa femme.<sup>3122</sup>"
    },
    {
        "number": "2768",
        "text": "Le Messager d'Allah (s) a dit : Aucune institution en islam n'est plus aimée par Allah le Tout-Puissant et plus estimée que le mariage.<sup>3123</sup>"
    }
]

# Subpart 869 - Le blâme des célibataires
s869 = find_subpart(p175, "869"); eh(s869)
s869['hadiths'] = [
    {
        "number": "2769",
        "text": "Le Messager d'Allah (s) a dit : Le mariage est ma tradition ; dès lors, celui qui rejette ma tradition ne fait pas partie de moi.<sup>3124</sup>"
    },
    {
        "number": "2770",
        "text": "Le Messager d'Allah (s) a dit : Lorsqu'une jeune personne se marie au début de sa jeunesse, son démon intérieur crie de rage : «Malheur à elle, malheur à elle ! Elle a préservé de moi deux tiers de sa religion.» Dès lors, que le serviteur fasse preuve de piété et craigne Allah pour le tiers restant.<sup>3125</sup>"
    },
    {
        "number": "2771",
        "text": "Le Messager d'Allah (s) a dit : Lorsque le serviteur se marie, en réalité, il complète la moitié de sa foi. Dès lors, qu'il fasse preuve de piété et craigne Allah dans la seconde moitié.<sup>3126</sup>"
    },
    {
        "number": "2772",
        "text": "Le Messager d'Allah (s) a dit : Une personne mariée endormie est meilleure auprès d'Allah qu'une personne célibataire qui jeûne et passe sa nuit en prière.<sup>3127</sup>"
    },
    {
        "number": "2773",
        "text": "Le Messager d'Allah (s) a dit : Prenez un conjoint car en vérité, cela suscitera une augmentation de votre subsistance.<sup>3128</sup>"
    },
    {
        "number": "2774",
        "text": "Le Messager d'Allah (s) a dit : Mariez les célibataires parmi vous car en vérité, Allah embellira [par cela] leurs caractéristiques morales, Il augmentera leur subsistance, et Il accroîtra leur noblesse.<sup>3129</sup>"
    },
    {
        "number": "2775",
        "text": "L'Imām al-Ṣādiq (as) a dit : Deux raka'āt de prière accomplis par une personne mariée sont meilleurs que soixante-dix raka'āt accomplis par une personne non mariée.<sup>3130</sup>"
    },
    {
        "number": "2776",
        "text": "Le Messager d'Allah (s) a dit : Les pires parmi vos morts sont les célibataires.<sup>3131</sup>"
    },
    {
        "number": "2777",
        "text": "Le Messager d'Allah (s) a dit : Les pires d'entre vous sont les célibataires. Deux raka'āt de prière accomplis par une personne mariée sont meilleurs que soixante-dix raka'āt de prière accomplis par une personne non mariée.<sup>3132</sup>"
    }
]

# Subpart 870 - La rétribution de ceux qui aident leurs frères [musulmans] à se marier
s870 = find_subpart(p175, "870"); eh(s870)
s870['hadiths'] = [
    {
        "number": "2778",
        "text": "L'Imām al-Ṣādiq (as) a dit : Celui qui aide une personne célibataire à se marier sera parmi ceux qu'Allah le Tout-Puissant regardera [avec miséricorde] le Jour de la Résurrection.<sup>3133</sup>"
    },
    {
        "number": "2779",
        "text": "L'Imām al-Kāẓim (as) a dit : Trois types de personnes seront ombragées par l'ombre du Trône d'Allah le Jour où il n'y aura d'ombre que son ombre : celle qui a aidé son frère musulman à se marier, celle qui l'a servi, et celle qui a caché [ses fautes].<sup>3134</sup>"
    }
]

# Subpart 871 - L'incitation à hâter le mariage des jeunes filles
s871 = find_subpart(p175, "871"); eh(s871)
s871['hadiths'] = [
    {
        "number": "2780",
        "text": "L'Imām al-Riḍā (as) a dit : L'Archange Gabriel (as) descendit auprès du Prophète (s) et dit : «Ô Muḥammad, en vérité, ton Seigneur te salue et te dit : «En vérité, les jeunes filles parmi les femmes sont semblables aux fruits de l'arbre : lorsque le fruit arrive à maturité, rien ne peut le préserver si ce n'est de le récolter, sans quoi le soleil le détériorera et le vent l'altérera. De même, lorsque les jeunes filles arrivent à maturité, leur seul recours est le mari, sinon, elles ne seront pas préservées de la tentation.»» Le Messager d'Allah (s) monta alors sur le minbar, rassembla les gens, et porta à leur connaissance ce qu'Allah le Tout-Puissant avait ordonné.<sup>3135</sup>"
    }
]

# Subpart 872 - L'importance accordée à la religion lors du choix d'un conjoint
s872 = find_subpart(p175, "872"); eh(s872)
s872['hadiths'] = [
    {
        "number": "2781",
        "text": "Le Messager d'Allah (s) a dit : Celui qui se marie avec une femme uniquement pour sa beauté ne trouvera pas en elle ce qu'il aime, et celui qui se marie avec elle pour son argent sera confié par Allah à ce dernier. Dès lors, cherchez à [épouser] celles qui sont religieuses.<sup>3136</sup>"
    },
    {
        "number": "2782",
        "text": "Le Messager d'Allah (s) a dit : Il ne faut pas privilégier la beauté du visage d'une femme aux dépens de la beauté de sa foi.<sup>3137</sup>"
    },
    {
        "number": "2783",
        "text": "Le Messager d'Allah (s) a dit : Si quelqu'un dont la religion et l'intégrité vous satisfont vient [vous faire une proposition de mariage], alors mariez-vous avec lui. Si vous ne le faites pas, la discorde et la corruption prévaudront sur terre.<sup>3138</sup>"
    },
    {
        "number": "2784",
        "text": "L'Imām Hasan (as) a dit à un homme qui lui avait demandé conseil au sujet du mariage de sa fille : Marie-la à un homme pieux car s'il l'aime, il l'honorera et s'il ne l'aime pas, il ne sera pas injuste envers elle.<sup>3139</sup>"
    }
]

# Subpart 873 - Le blâme des dots excessives
s873 = find_subpart(p175, "873"); eh(s873)
s873['hadiths'] = [
    {
        "number": "2785",
        "text": "Le Messager d'Allah (s) a dit : Les meilleures femmes de ma communauté sont celles qui ont les plus beaux visages et les dots les plus modestes.<sup>3140</sup>"
    },
    {
        "number": "2786",
        "text": "Le Messager d'Allah (s) a dit : La meilleure des dots est la plus simple.<sup>3141</sup>"
    },
    {
        "number": "2787",
        "text": "L'Imām al-Ṣādiq (as) a dit : Les choses mauvaises chez la femme sont une dot excessive et le manque de respect vis-à-vis de son mari.<sup>3142</sup>"
    }
]

# Subpart 874 - L'importance d'accorder du soin au choix d'une femme
s874 = find_subpart(p175, "874"); eh(s874)
s874['hadiths'] = [
    {
        "number": "2788",
        "text": "Le Messager d'Allah (s) a dit : Mariez-vous à une bonne famille car en vérité, le sang a une influence [les traits de caractère se transmettent par filiation].<sup>3143</sup>"
    },
    {
        "number": "2789",
        "text": "Le Messager d'Allah (s) a dit : Choisissez avec attention [la meilleure femme] pour vos semences car en vérité, les femmes donnent naissance à des enfants qui ressemblent à leurs frères et sœurs.<sup>3144</sup>"
    },
    {
        "number": "2790",
        "text": "L'Imām al-Ṣādiq (as) a transmis de ses pères (as) : Le Messager d'Allah (s) a dit aux gens : «Gare à la verdure qui pousse dans du fumier.» Ils demandèrent : «Ô Messager d'Allah, quelle est la verdure qui pousse dans le fumier ?» Il dit : «La belle femme élevée dans un mauvais environnement.»<sup>3145</sup>"
    },
    {
        "number": "2791",
        "text": "Le Messager d'Allah (s) a dit : Ne vous mariez pas avec une femme sotte, car sa compagnie est une perte et ses enfants seront tels des hyènes.<sup>3146</sup>"
    }
]

# Subpart 875 - Les droits du mari
s875 = find_subpart(p175, "875"); eh(s875)
s875['hadiths'] = [
    {
        "number": "2792",
        "text": "Le Messager d'Allah (s) a dit : La personne qui a le plus de droit sur la femme est son mari, et la personne qui a le plus de droit sur l'homme est sa mère.<sup>3147</sup>"
    },
    {
        "number": "2793",
        "text": "Le Messager d'Allah (s) a dit : Malheur à la femme qui a provoqué la colère de son mari, et bénie soit celle dont le mari est satisfait d'elle.<sup>3148</sup>"
    },
    {
        "number": "2794",
        "text": "L'Imām al-Bāqir (as) a dit : Il n'y a pas de meilleur intercesseur pour la femme auprès de son Seigneur que la satisfaction de son mari.<sup>3149</sup>"
    }
]

# ============================================================
# Sequential Sorting for all modified subparts (programmatic)
# ============================================================
modified_sections = [
    (p173, "859"), (p173, "860"),
    (p174, "862"), (p174, "863"), (p174, "864"), (p174, "867"),
    (p175, "868"), (p175, "869"), (p175, "870"), (p175, "871"),
    (p175, "872"), (p175, "873"), (p175, "874"), (p175, "875")
]

for p_idx, s_title in modified_sections:
    s = find_subpart(p_idx, s_title)
    if s and 'hadiths' in s:
        s['hadiths'].sort(key=lambda h: int(h['number']))
        print(f"Sorted Subpart {s_title} (Part index {p_idx}). Hadiths: {[h['number'] for h in s['hadiths']]}")

# Write back
new_content = content[:start_idx] + json.dumps(data, ensure_ascii=False, indent=4) + content[end_idx:]
with open('aune-sagesse-data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Data successfully saved! Hadiths Batch 44 injected and database formatted.")
