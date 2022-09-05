#como concatenar cadenas de caracteres.
#Supongamos que queremos crear una cadena que diga:
#Aprende a programar con __________.

#organización = "Francisco"

#print("Aprende a programar con " + organización)
#print("aprende a programar con {}".format(organización))
#print(f"aprende a programar con {organización}")
 
adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input ("Sustantivo (Plural): ")

madlib = f"!Programar es tan {adj}! Siempre me emociona porque me relaciona con mas {verbo1}, siempre aprendo {verbo2} con Francisco y alcanzo mis {sustantivo_plural}!"

print(madlib)
