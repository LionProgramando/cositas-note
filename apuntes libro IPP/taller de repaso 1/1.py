from math import trunc

num = float(input("Ingrese un número\n"))

if num > 999 and num < 9999:
    print("El número si tiene 4 dígitos")
else:
    print("el número no tiene a 4 dígitos")

if num > 0:
    print("El número",num,"es positivo")
else:
    print("El número",num,"no es positivo")

if num - trunc(num) == 0:
    print("El número es entero")
else:
    print("El número no es entero")