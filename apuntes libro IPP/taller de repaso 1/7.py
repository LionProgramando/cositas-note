cont = 0 
frase =input("Frase: ")

for i in frase:
    if i == " ":
        cont = cont +1 
print("\n\nLe frase tiene",cont,"espacios")