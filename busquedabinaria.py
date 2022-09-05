
import random
import time 


def búsqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i 
    return -1        

#print(búsqueda_ingenua(mi_lista, 10))
#aqui la respuesta será 3 el indice del elemento que estamos buscando 
#print(búsqueda_ingenua(mi_lista, 15))
#si se busca uno que no está aparece el -1 al completarse el ciclo 

def búsqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 #inicio de la lista.
    if limite_superior is None:
        limite_superior = len(lista)-1 #final de la lista. 
    
    if limite_superior < limite_inferior:
        return -1 

    punto_medio = (limite_inferior + limite_superior) //2
#Ejemplo:
    #[1, 3, 5, 10, 12] #lista 
    # 0  1  2  3   4  #indice
    #punto medio = (0+4) // 2 = 4 | 2 = 2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif  objetivo < lista[punto_medio]:
        return  búsqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return búsqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)

if __name__=='__main__':
    
    #Vamos a crear una lista ordenada con 100000 números aleatorios.
    tamaño= 100000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))

    lista_ordenada= sorted(list(conjunto_inicial))

    # vamos a medir el tiempo que toma conseguir elementos en lista.
    #busqueda_ingenua.
    inicio= time.time()
    #for objetivo in lista_ordenada:
     #   búsqueda_ingenua( lista_ordenada,objetivo)
      #  fin = time.time()
       # print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")
    
    #Medir el tiempo de busqueda binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        búsqueda_binaria(lista_ordenada,objetivo)
    fin= time.time()
    print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")


#range(len(lista)): -> 0,1,2,3, ...., len(lista)-1
