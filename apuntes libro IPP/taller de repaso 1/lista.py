lista =["Axell","Piogram","youtube","Python"]
for cadena in lista:
    print("----"+cadena+"----")
    for caracter in cadena:
        mini=caracter.lower()
        if mini in "aeoáéó":
            print(mini)
print("Fin del programa")