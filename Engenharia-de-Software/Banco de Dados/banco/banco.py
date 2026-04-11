#Banco de dados em Python

import sqlite3
banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios (nome text, idade integer, email text)")
#cursor.execute("INSERT INTO funcionarios VALUES('Auguto', 23, 'augusto@gmail.com')")
#cursor.execute("INSERT INTO funcionarios VALUES('Auguto Melo', 30, 'augustomelo@gmail.com')")
#cursor.execute("INSERT INTO funcionarios VALUES('lidia', 31, 'lidia@gmail.com')")
#cursor.execute("ALTER TABLE funcionarios ADD COLUMN cpf integer")
#cursor.execute("UPDATE funcionarios SET cpf = 98765432100 WHERE nome = 'lidia'")
cursor.execute("UPDATE funcionarios SET cpf = 454545454545 WHERE rowid = '2'")
banco.commit()
#para acessar os dados no Banco de Dados DB
cursor.execute("SELECT * FROM funcionarios")
for funcionarios in cursor.fetchall():
    print(funcionarios)