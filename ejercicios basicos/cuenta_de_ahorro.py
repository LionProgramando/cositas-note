inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))


#algoritmo malo--->

#inicio_de_ahorro = int(input('Ingrese el monto a depositar \n'))
#interes_anual_del_4_porciento = inicio_de_ahorro * 4 / 12

#primer_año = round(interes_anual_del_4_porciento*1)+inicio_de_ahorro
#segundo_año = round(interes_anual_del_4_porciento*2)+inicio_de_ahorro
#tercer_año = round(interes_anual_del_4_porciento*3)+inicio_de_ahorro

#print("Ahorrado + el interes de %4 en un año",primer_año)
#print("Ahorrado + el interes de %4 en dos años",segundo_año)
#print("Ahorrado + el interes de %4 een tres años",tercer_año)