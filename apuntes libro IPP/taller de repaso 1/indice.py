frutas=["Mora","Fresa","Sandía","Piña","Uva"]

precioxlb=[0.50, 1.00, 1.55, 1.20, 2.00]

for i in range(len(frutas)):
    fruta = frutas[i]
    precio=precioxlb[i]
    if precio < 1.50:
        print(fruta)