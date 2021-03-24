import sqlite3
#criar a conexão com o bando de dados
con = sqlite3.connect("pessoas")

#com cursor podemos manipular o banco através de SQL (create, insert, select etc)
cur = con.cursor()

#inserir dados na tabela
#sql = "insert into pessoa values (2, 'Kirito', 'kirito@gmail.com')"
#cur.execute(sql)
sql = "insert into pessoa values (?, ?, ?)"
dados = [(3, "Ghost", "Ghost@gmail.com"),
        (4, "Goku", "Goku@gmail.co,"),
        (5, "Uzumaki", "uzumaki@gmail.com")]
 #inserrir vários dados
#for registros in dados:
    #cur.execute(sql,registros)

#excluir
#cur.execute("delete from pessoa where pescodigo=2")
cur.execute("delete from pessoa where pesnome like 'Goku'")


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