meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una risa pero expresada en letras",
            "JEEZ": "Un gesto de sorpresa"
            }
word = input()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("no tenemos un significado para esa palabra")
