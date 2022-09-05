bienvenida = "Bienvenido, quiero pedirte unas datos para que interactuemos... ¿aceptas?"
print(bienvenida)
respuesta_de_usuario = input("Ingresa 1 para si y 2 para no ")

while respuesta_de_usuario != 1 or 2:

    respuesta_de_usuario = input("O! no has respondido bien, intentalo nuevamente ")

if respuesta_de_usuario == 1:
    print("Bien, comencemos")
    print(".................")
    nombre = input("Dime, ¿cual es tu nombre?")

else: 
    print("lo puedo entender, no te quieres divertir conmigo")


