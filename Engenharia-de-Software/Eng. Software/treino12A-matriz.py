import numpy as np

#Lista de listas (3x2)
lista = [[1, 2], [3, 4], [5, 6]]
matriz = np.array(lista)

print (matriz)
print()

#Transformar lista única em matriz 2x3
lista_unica = [1, 2, 3, 4, 5, 6]
matriz_2x3 = np.array(lista_unica).reshape(2, 3)
print (matriz_2x3)