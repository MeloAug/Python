#DATAFRAME python
import pandas as pd

#Criando um DataFrame apartir de um dicionario
data= {
    'Nome': ['Ana', 'Bruno', 'Carlos'],
    'Idade': [25, 30, 22],
    'Cidade': ['SP', 'RJ', 'PE']
}

df = pd.DataFrame(data)

#Selecionar múltiplas colunas
print (df[['Nome', 'Cidade']])