segundos= int(input("Ingrese la cantidad de segundos: "))
horas= segundos//3600
sobrante1= segundos%3600
minutos= sobrante1//60
sobrante2= sobrante1%60
print("Horas -> ",horas)
print("minutos -> ",minutos)
print("Segundos -> ",sobrante2)
