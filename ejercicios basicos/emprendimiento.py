kg_payasos = 112
kg_muñecas = 75

numero_de_payasos = int(input("Ingrese el número de payasos de su último pedido "))
numero_de_muñecas = int(input("Ingrese el número de muñecas de su último pedido "))

peso_ultimo_pedido_payasos = kg_payasos * numero_de_payasos
peso_ultimo_pedido_muñecas = kg_muñecas * numero_de_muñecas
peso_paquete_total = peso_ultimo_pedido_payasos + peso_ultimo_pedido_muñecas

print("este es el peso del último pedido de payasos",peso_ultimo_pedido_payasos,"y peso último pedido de muñecas",peso_ultimo_pedido_muñecas)
