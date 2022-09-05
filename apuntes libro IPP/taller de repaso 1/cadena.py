cadena = input("ingrese palabra: ").lower()
for caracter in cadena:
    if caracter in "aeoáéó":
        print(caracter)
