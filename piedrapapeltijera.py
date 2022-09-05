import random 

def jugar ():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel y 'ti' para tijeras.\n").lower()

    computadora = random.choice(['pi','pa','ti',]) 

    if usuario == computadora:
        return '¡Empate!'
    
    if gano_el_jugador(usuario,computadora):
        return '¡Ganaste!'

    return '¡Perdiste!'

def gano_el_jugador(jugador,oponente):
    #Retornar el valor 'True' si gana el jugador
    #Piedra gana a tijera (pi > ti)
    #tijera gana a papel (ti > pa)
    #papel gana a piedra (pa > pi)

    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False

print(jugar())




