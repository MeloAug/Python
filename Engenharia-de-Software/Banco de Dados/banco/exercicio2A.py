#Banco de dados em Python

import sqlite3
banco = sqlite3.connect('banco_2.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS pessoa(id_cpf integer primary key NOT NULL, nome text, idade integer, email text)")
cursor.execute("INSERT INTO pessoa VALUES(011, 'Aug', 23, 'augustotu@gmail.com')")
cursor.execute("INSERT INTO pessoa VALUES(022, 'Amanda', 30, 'augustomeloae@gmail.com')")
cursor.execute("INSERT INTO pessoa VALUES(033, 'lidia Oli', 31, 'lididsda@gmail.com')")
banco.commit()

#para acessar os dados no Banco de Dados DB
cursor.execute("SELECT * FROM pessoa")
for pessoa in cursor.fetchall():
    print(pessoa)