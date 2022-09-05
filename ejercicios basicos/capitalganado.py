cantidad=float(input("Cantiadad a invertir "))
interes=float(input("Interes porcentual anual "))
años=int(input("¿Años? "))

print("Capital final: ", round(cantidad * (interes/100+1)**años, 2))