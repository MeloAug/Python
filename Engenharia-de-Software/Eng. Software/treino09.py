#DATAFRAME em Python
import pandas as pd

#Criando um DATAFRAME a partir de um dicionário
data = {
    'Nome' : ['Ana', 'Bruno', 'Carlos'],
    'Idade': [25, 30, 22],
    'Cidade': ['SP', 'RJ', 'PE']
}
df = pd.DataFrame(data)

#Exibindo o DataFrame
print (df)
print ()

#Acessando uma coluna
print (df['Nome'])
print ()

#Filtrando dados (Idade > 23)
print (df[df['Idade'] > 23])