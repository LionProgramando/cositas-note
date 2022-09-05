import random

def adivina_el_numero(x):

    print("=======================================")
    print("¡Bienvenido!")
    print("=======================================")
    print("Tu meta es adivinar el numero generado por la computadora.")

    numero_aleatorio = random.randint(1,x) #Numero aleatorio entre "1" y "X".

    adivinar = 0

    while adivinar != numero_aleatorio:
        #El usuario ingresa un número
        adivinar = (int(input(f"adivina un numero entre 1 y {x} ")))#f-string

        if adivinar < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño")
        elif adivinar > numero_aleatorio:
            print("Intenta otra vez, este número es mayor")

    print(f"¡Felicitaciones! Adivinaste el número {numero_aleatorio} correctamente")

adivina_el_numero(10)