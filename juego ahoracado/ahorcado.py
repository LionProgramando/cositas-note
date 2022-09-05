
import random
import string

from palabras import palabras
from ahoracado_diagrama import vidas_diccionario_visual

def obtener_palabra_válida(palabras):
    #seleccionar una palabra al azar de la lista
    #de palabras válidas
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def ahoracado():

    print('====================================')
    print('¡Bienvenido(a) al juego del Ahorado!')
    print('====================================')

    palabra = obtener_palabra_válida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set() #No se puede escribir un par de llaves vacío porque esto crea un disccionario
    Abecedario = set(string.ascii_uppercase)#nocontiene'Ñ'

    vidas= 7 

    while len(letras_por_adivinar) > 0 and vidas > 0:
        #letras adivinadas
        # ' '.join('A','B','C','D')

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' ' .join(letras_por_adivinar)}")

        #Mostrar el estado actual de la palabra
        palabra_lista=[letra if letra in letras_adivinadas else '-' for letra in palabra]
        #mostrar estado del ahoracado
        print(vidas_diccionario_visual[vidas])
        #Mostrar las letras separadas por un espacio
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario= input("Escoge una letra: ").upper()
        
        #Si la letra escogida por el usuario está en el abecedario y no está en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in Abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            #si la letra está en la palabra o no
            # quitar la letra del conjunto de letras
            # pendientes por adivinar.
            # si no está la palabra, quitar una vida. 
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas=vidas-1
                print(f"\nTu letra, {letra_usuario} no está en la palabra")
        #si la letra escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esta letra. Por favor escoge una letra nueva")
        else:
            print("\nEsta letra no es válida.")
    # El juego llega a esta línea cuando se adivina 
    # todas las letras de las palbras o cunado se agotan las vidas del jugador.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")

ahoracado()






#Ejemplo de conjunto {'a','b','c','d'}
#ejemplo de conjunto letras 'Python' = {'P', 'y','t','h','o','n'}