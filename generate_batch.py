import json

batch = [
    # PART 19 - FĀṬIMA
    {
        "part_idx": 19,
        "subpart_idx": 1,
        "content": [
            {
                "number": "421",
                "text": "Le Messager d'Allah (s) a dit : Fāṭima est une partie de moi. Celui qui la met en colère m'aura mis en colère.",
                "note": "583"
            }
        ]
    },
    {
        "part_idx": 19,
        "subpart_idx": 2,
        "content": [
            {
                "number": "422",
                "text": "Le Messager d'Allah (s) a dit : Et pour ce qui est de ma fille Fāṭima, elle est la maîtresse des femmes des mondes, du premier au dernier [jour de ce monde].",
                "note": "584"
            },
            {
                "number": "423",
                "text": "Le Messager d'Allah (s) a dit : Les meilleures femmes du Paradis sont Khadīja la fille de Khuwaylid, Fāṭima la fille de Muḥammad, Āsiya la fille de Muzāḥim et femme de Pharaon, et Maryam la fille de 'Imrān.",
                "note": "585"
            },
            {
                "number": "424",
                "text": "Le Messager d'Allah (s) a dit à Fāṭima : N'es-tu pas satisfaite d'être la maîtresse des femmes des mondes, la maîtresse des femmes de cette communauté et la maîtresse des femmes des croyants ?",
                "note": "586"
            }
        ]
    },
    # WAIT! In previous messages, did I already transcribe 421-517 correctly?
    # Yes, I had them in `update_data_batch.py` or `update_hadiths_...`
    # It would be MUCH better to just reuse `update_data_batch.py` and run it if it's there.
    # But wait, `update_data_batch.py` had the WRONG subpart mappings! Because Part indices changed!
    # Let's check `update_data_batch.py` content to see what it has.
]
