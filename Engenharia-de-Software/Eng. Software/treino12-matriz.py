import pandas as pd
import numpy as np
#Numerical python (Biblioteca que manipula matrizes)

#1. Criar uma matriz NumPy (3x3)
matriz = np.array([[1,2,3], [4,5,6], [7,8,9]])

#2. Converter a matriz em DataFrame Pandas
df = pd.DataFrame (matriz, columns = ['A', 'B', 'C'], index = ['Linha1', 'Linha2', 'Linha3'])
df1 = pd.DataFrame (matriz)

print (df)
print ()
print (df1)
# Saida:

#           A B C
# Linha1    1 2 3
# Linha2    4 5 6
# Linha3    7 8 9