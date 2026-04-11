#Banco de dados em Python

import sqlite3
banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE funcionarios (nome text, idade integer, email text)")
#cursor.execute("INSERT INTO funconarios VALUES('Auguto',23, 'augusto@gmail.com')")
#cursor.execute("INSERT INTO funcionarios VALUES('Auguto Melo',30, 'augustomelo@gmail.com')")
banco.commit()
#para acessar os dados no Banco de Dados DB
idade_sel=30
cursor.execute("SELECT * FROM funcionarios where idade =?", (idade_sel,))
print(cursor.fetchall())