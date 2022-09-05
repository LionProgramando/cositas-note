#peso=int(input("ingrese su peso "))
#estatura=int(input("ingrese estatura "))

#imc= (peso/estatura)**2,2

#print("su imc es",imc)
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))