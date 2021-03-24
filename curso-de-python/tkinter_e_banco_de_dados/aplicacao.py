print("-----------------Sistema para cadastro de Paises-----------------")
import mysql.connector
from mysql.connector import errorcode
import sys
from tkinter import *

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


conexao = conexaoBancoDeDados()
cursor = conexao.cursor()
sql = "select * from place"
try:
    cursor.execute(sql)
    dadosPais = cursor.fetchall()
    corLinha = "white"
    Label(text="Lista de Paises", font=("Arial", 20)).grid(row=1, column=1,columnspan=4, pady=5)
    Label(text="codigo", relief=RIDGE, width=7, anchor=W, bg="green").grid(row=2, column=1)
    Label(text="city", relief=RIDGE, width=15, anchor=W, bg="green").grid(row=2, column=2)
    Label(text="telcode", relief=RIDGE, width=7, anchor=W, bg="green").grid(row=2, column=3)
    linha = 2
    for dados in dadosPais:
        codigo = dados[0]
        country = dados[1]
        city = dados[2]
        telcode = dados[3]
        if linha % 2 == 0:
            corLinha = "yellow"
        else:
            corLinha = "white"
        Label(text=codigo, relief=RIDGE, width=7, anchor=W, bg=corLinha).grid(row=linha+1, column=1)
        Label(text=city, relief=RIDGE, width=15, anchor=W, bg=corLinha).grid(row=linha+1, column=2)
        Label(text=telcode, relief=RIDGE, width=7, anchor=W, bg=corLinha).grid(row=linha+1, column=3)
        linha+=1
        quantidade = ("\nListou %d Paises" % (len(dadosPais)))
    Label(text=quantidade, font=("Arial", 10)).grid(row=linha+1, column=1, columnspan=4)
except mysql.connector as erro:
    print("Não conseguil listar, erro:  ", erro)
    
conexao.close()
mainloop()

