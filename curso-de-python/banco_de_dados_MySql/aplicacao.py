print("-----------------Sistema para cadastro de Paises-----------------")
import mysql.connector
from mysql.connector import errorcode
import sys

def conexaoBancoDeDados():
    try:
        cnx = mysql.connector.connect(user='root',
                                        database='cursodego',
                                        host='127.0.0.1',
                                        password='batata123')
        #print("Conseguil conectar ao banco de dados")
    except mysql.connector.Error as err:
        print("Não conseguil conectar ao banco de dados")
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou senha inválidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Base de dados não existe")
        else:
            print(err)
    return cnx

def cadastro(conexao):
    print("Digite os dados do pais: \n")
    nomePais = raw_input("Pais: ")
    cidade = raw_input("Cidade: ")
    telcode = raw_input("Telcode: ")
    cursor = conexao.cursor()
    sql = "insert into place (country, city, telcode) values ('"+nomePais+"', '"+cidade+"', '"+telcode+"')"
    print(sql)

    try:
        cursor.execute(sql)
        conexao.commit()
        print("dados gravados com sucesso!!")
    except mysql.connector as erro:
        print("Não foi possivel gravar no banco de dados, erro:  ", erro)
    conexao.close()
    menu()

def excluir(conexao):
    codigo = raw_input("Digite o id do pais: ")
    cursor = conexao.cursor()
    sql = "delete from place where id = "+codigo
    try:
        cursor.execute(sql)
        conexao.commit()
        print("dados excluido com sucesso!!")
    except mysql.connector as erro:
        print("Não conseguiu excluir no banco de dados, erro:  ", erro)
    conexao.close()
    menu()

def alterar(conexao):
    codigo = raw_input("Digite o id do pais que quer alterar: ")
    city = raw_input("Digite o novo pais: ")
    cursor = conexao.cursor()
    sql = "update place set country ='"+city+"' where id ="+codigo
    try:
        cursor.execute(sql)
        conexao.commit()
        print("dados alterado com sucesso!!")
    except mysql.connector as erro:
        print("Não conseguiu alterar no banco de dados, erro:  ", erro)
    conexao.close()
    menu()


def listarTodos(conexao):
    cursor = conexao.cursor()
    sql = "select * from place"
    try:
        cursor.execute(sql)
        dadosPais = cursor.fetchall()
        #quantidade = 0
        print("---------------------------------------")
        print("------------------Lista de Paises---------------------")
        print("---------------------------------------")
        for dados in dadosPais:
            codigo = dados[0]
            country = dados[1]
            city = dados[2]
            telcode = dados[3]
            print("Código = ",codigo,"Coutry = ",country,"City = ",city,"telcode = ",telcode)
            #quantidade+=1
       # print("\nListou %d paises" % quantidade)
        print("\nListou %d paises" % (len(dadosPais)))
    except mysql.connector as erro:
        print("Não conseguil listar, erro:  ", erro)
    conexao.close()
    menu()

def pesquisar(conexao):
    nome = raw_input("Digite o nome do pais a ser pesquisado: ")
    cursor = conexao.cursor()
    sql = "select * from place where country like '%"+nome+"%'"
    try:
        cursor.execute(sql)
        dadosPais = cursor.fetchall()
        #quantidade = 0
        print("---------------------------------------")
        print("------------------Lista de Paises---------------------")
        print("---------------------------------------")
        for dados in dadosPais:
            codigo = dados[0]
            country = dados[1]
            city = dados[2]
            telcode = dados[3]
            print("Código = ",codigo,"Coutry = ",country,"City = ",city,"telcode = ",telcode)
            #quantidade+=1
       # print("\nListou %d paises" % quantidade)
        print("\nListou %d paises" % (len(dadosPais)))
    except mysql.connector as erro:
        print("Não conseguil listar, erro:  ", erro)
    conexao.close()
    menu()


def menu():
    opcaoEscolhida = int(input("Escolha uma opção:\n\n1)Cadastrar\n2)Alterar\n3)Excluir\n4)Pesquisar\n5)Listar todos\n6)Sair\n\opção: "))
    try:
         if opcaoEscolhida <1 or opcaoEscolhida > 6:
            print("opção Inválida, escolha entre 1 e 6")
            menu()
    except:
        print("opção Inválida, escolha entre 1 e 6")
        menu()

    conexao = conexaoBancoDeDados()
    if opcaoEscolhida == 1:
        cadastro(conexao)
    elif opcaoEscolhida == 2:
        alterar(conexao)
    elif opcaoEscolhida == 3:
        excluir(conexao)
    elif opcaoEscolhida == 4:
        pesquisar(conexao)
    elif opcaoEscolhida == 5:
        listarTodos(conexao)
    elif opcaoEscolhida == 6:
        print("Fechando sistema")
        sys.exit()
menu()
