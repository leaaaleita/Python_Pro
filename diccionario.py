#Leaa
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "VAINA": "Cosa",
            "JEVI":"Algo que es chévere/cool",
            "TATO":"Se usa de la misma forma que el OK."
                }
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
        print('---------------------')
    else:
    # ¿Qué hacer si no se encuentra la palabra?
        print("Esa no la tengo")
        print('---------------------')

print("ya no me preguntes más >:c")
