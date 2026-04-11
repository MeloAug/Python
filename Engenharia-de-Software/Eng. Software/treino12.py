#DATAFRAME em Python
import pandas as pd

data = {
    'Nome': ['Inacio', 'José', 'Eduardo'],
    'Idade': [56, 77, 92],
    'Cidade': ['BA', 'SP', 'PE']
}
df = pd.DataFrame (data)
#Filtrar com duas condições (use & para E, | para OU)
#Exemplo: idade > 20 E cidade igual a 'São Paulo'
filtro_complexo = df [(df ['Idade'] > 90) & (df['Cidade'] == 'PE')]
print (filtro_complexo)