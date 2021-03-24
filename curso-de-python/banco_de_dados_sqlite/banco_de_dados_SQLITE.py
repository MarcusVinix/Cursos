import sqlite3
#criar a conexão com o bando de dados
con = sqlite3.connect("pessoas")

#com cursor podemos manipular o banco através de SQL (create, insert, select etc)
cur = con.cursor()

#variavel sql para criar uma tabela no banco de dados pessoas
sql = "create table pessoa"\
      "(pesCodigo integer primary key,"\
      "pesNome varchar(50),"\
      "pesEmail varchar(50))"

#criar  uma tabela no banco de dados pessoa
#cur.execute(sql)

#inserir dados na tabela
sql = "insert into pessoa values (2, 'Kirito', 'kirito@gmail.com')"
cur.execute(sql)

#confirma a transação
con.commit()

#pesquisa todos os registro de pessoa
sql  = "select * from pessoa"
cur.execute(sql)

#recuperando o resultado da pesquisa
recset = cur.fetchall()

#listando dados do banco
for registro in recset:
      print(registro)