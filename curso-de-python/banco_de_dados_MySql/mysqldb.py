import mysqldb
con = mysqldb.connect(db="estoque",user="root",passwd="",host="127.0.0.1")
#com cursor podemos manipular o banco atraves de SQL (create, insert, select)
cur = con.cursor()

#inserir dados na tabela
#sql = "insert into cidade (nome, uf) values ('Blumenau', 'SC')"
#cur.execute(sql)

#excluir
#cur.execute("delete from cidade where coddig=7")

#update (alterar)
cur.execute("UPDATE cidade set nome='Rondopolis', uf='MT' where codigo=6")

#pesquisa todos os registros de cidade
sql = "select * from cidade"
cur.execute(sql)

#recuperando o resultado da pesquisa
recset = cur.fetchall()

#listando dados do banco
for registros in recset:
    print("Código: %d, Nome da cidade: %s, UF: %s" %(registros[0], registros[1], registros[2]))