#Banco de dados em Python

import sqlite3
banco = sqlite3.connect('banco_2B.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE pessoa2(id_cpf integer primary key AUTOINCREMENT NOT NULL, nome text, idade integer, email text)")
#cursor.execute("INSERT INTO pessoa2 (nome, idade, email) VALUES('Amanda', 30, 'augustomeloae@gmail.com')")
#cursor.execute("INSERT INTO pessoa2 (nome, idade, email) VALUES('lidia Oli', 31, 'lididsda@gmail.com')")
cursor.execute("UPDATE pessoa2 SET nome = 'Lucas' WHERE id_cpf = 4;")
banco.commit()

#para acessar os dados no Banco de Dados DB
cursor.execute("SELECT * FROM pessoa2")
for pessoa2 in cursor.fetchall():
    print(pessoa2)