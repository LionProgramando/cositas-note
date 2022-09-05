import random

def adivina_el_numero_computadora(x):

    print("=======================================")
    print("¡Bienvenido!")
    print("=======================================")
    print(f"Selecciona el número entre 1 y {x} para que la computadora intente adivinarlo...")

    limite_inferior = 1   #[1,x]
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #Generar una predicción
        if limite_inferior != limite_superior: #ejemplo intervalo [1,10]
            predicción= random.randint(limite_inferior,limite_superior)
        else:
            predicción= limite_inferior #también podría ser el número superior.

        # Obtener respuesta del usuario 
        respuesta= input(f"Mi predicción es {predicción}. Si es muy alta ingresa (A), Si es muy baja ingresa (B), Si es correcta ingresa (C)").lower()

        if respuesta == "a":
            limite_superior= predicción - 1 
        elif respuesta == "b":
            limite_inferior= predicción + 1
        #Intervalo inicial: [1, 10]
        #Predicción: 6
        #Respuesta: "a"
        #Intervalo: [1, 5]


    print(f"Felicitaciones, la computadora lo adivino correctamente!!!: {predicción}")

    
adivina_el_numero_computadora(20)
        
