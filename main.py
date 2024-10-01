None
meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFL": "odpowiedź na żart"
            'SHEESH': 'lekka dezaprobata'
            'CREEPY': 'straszny, złowieszczy'
            'AGGRO': 'stać się agresywnym/zły'
            }
word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # Co powinniśmy zrobić, jeśli słowo zostało znalezione?
else:
    print ("Nie ma takiego słowa w słowniku ")
    # Co powinniśmy zrobić, jeśli słowo nie zostało znalezione?
