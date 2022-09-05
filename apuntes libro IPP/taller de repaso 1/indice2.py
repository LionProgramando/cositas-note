frutas=["Mora","Fresa","Mora","Piña","Uva"]

cantidad=[5, 10, 3, 5, 10]

clientes=["Axell", "Zarinna", "Luis", "Joel", "Kevin"]

for i in range(len(frutas)):
    fruta = frutas[i]
    if fruta=="Mora":
        can=cantidad[i]
        cli=clientes[i]
        print(cli,can)