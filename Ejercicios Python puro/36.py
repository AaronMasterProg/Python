import numpy as papa

listas=[1,2,3],[1,2,3],[0,1,3]
lista=[1,2,3]

def mostrar_matriz(matriz):
    print(matriz.shape)
    print(type(matriz))
    print(matriz)

mostrar_matriz(papa.array(listas))

busca_numero = listas[1].index(1)

print(busca_numero)
