lista = []
suma = 0
media = 0

for i in range(10):
    numero = int(input("Dame diez numeros: "))
    lista.append(numero)
    suma += numero

for i in lista:
    print(i)

media = suma / len(lista)

print("la suma es ", suma)
print("La media es", media)