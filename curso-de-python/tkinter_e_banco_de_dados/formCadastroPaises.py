#coding: utf-8
from Tkinter import *
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

novoPais = True

def cadastro():
   
    conexao = conexaoBancoDeDados()
    codigo = editCodigo.get()
    nomePais = editPais.get()
    cidade = editCity.get()
    telcode = editTelcode.get()
    cursor = conexao.cursor()
    if novoPais:
        sql = "insert into place (country, city, telcode) values ('"+nomePais+"', '"+cidade+"', '"+telcode+"')"
    else:
        sql = "update place set country ='"+editPais.get()+"', city = '"+editCity.get()+"', telcode =  '"+editTelcode.get()+"' where id ="+codigo

    try:
        cursor.execute(sql)
        conexao.commit()
        labelStatus['text']= "Dados Gravados com Sucesso!"
    except mysql.connector as erro:
        print("Não foi possivel gravar no banco de dados, erro:  ", erro)

    #botaoAlterar.configure(state="normal")
    #botaoExcluir.configure(state="normal")
    botaoNovo.configure(state="normal")
    botaoCancelar.configure(state="disabled")
    botaoGravar.configure(state="disabled")


    desabilitarCampos()
    pesquisar()
    conexao.close()

def limparCampos():
    editCodigo.configure(state="normal") #habilita editar
    editCodigo.delete(0, END)
    editPais.delete(0, END)
    editCity.delete(0, END)
    editTelcode.delete(0, END)
  
    editPais.focus()

def novo():
    habilitarCampos()
    limparCampos()
    global novoPais
    novoPais = True
    editCodigo.configure(state="readonly")
    editPesquisa.delete(0, END)
    botaoAlterar.configure(state="disabled")
    botaoExcluir.configure(state="disabled")
    botaoGravar.configure(state="normal")
    botaoNovo.configure(state="disabled")
    botaoCancelar.configure(state="normal")
    labelStatus['text']= "Inserindo um novo Registro"
  
   
    

def desabilitarCampos():
    editCodigo.configure(state="readonly")
    editPais.configure(state="readonly")
    editCity.configure(state="readonly")
    editTelcode.configure(state="readonly")

def habilitarCampos():
    
    editPais.configure(state="normal")
    editCity.configure(state="normal")
    editTelcode.configure(state="normal")

def cancelar():
    pesquisar()
    desabilitarCampos()
    botaoAlterar.configure(state="normal")
    botaoExcluir.configure(state="normal")
    botaoNovo.configure(state="normal")
    botaoGravar.configure(state="disabled")
    botaoCancelar.configure(state="disabled")
    labelStatus['text']= ""


def pesquisar():
    habilitarCampos()
    conexao = conexaoBancoDeDados()
    nome = editPesquisa.get()
    cursor = conexao.cursor()
    sql = "select * from place where country like '%"+nome+"%'"
    try:
        cursor.execute(sql)
        dadosPais = cursor.fetchone()
        if dadosPais:
            #print(dadosPais[0])
            editCodigo.configure(state="normal")
            limparCampos()
            editCodigo.insert(0, dadosPais[0])
            editCodigo.configure(state="readonly")
            editPais.insert(0, dadosPais[1])
            editCity.insert(0, dadosPais[2])
            editTelcode.insert(0, dadosPais[3]) 
    except mysql.connector as erro:
        print("Não conseguil listar, erro:  ", erro)
    botaoAlterar.configure(state="normal")
    botaoExcluir.configure(state="normal")
    botaoCancelar.configure(state="disabled")
    botaoNovo.configure(state="normal")
    labelStatus['text']= "Pesquisando..."
    desabilitarCampos()
    
    conexao.close()

def excluir():
    conexao = conexaoBancoDeDados()
    codigo = editCodigo.get()
    cursor = conexao.cursor()
    sql = "delete from place where id = "+codigo
    try:
        cursor.execute(sql)
        conexao.commit()
        print("dados excluido com sucesso!!")
    except mysql.connector as erro:
        print("Não conseguiu excluir no banco de dados, erro:  ", erro)
    editPesquisa.delete(0, END)
    pesquisar()
    
    conexao.close()

def alterar():
    habilitarCampos()
    botaoAlterar.configure(state="disabled")
    botaoExcluir.configure(state="disabled")
    botaoNovo.configure(state="disabled")
    botaoGravar.configure(state="normal")
    botaoCancelar.configure(state="normal")
    labelStatus['text']= "Alterando Dados"
    global novoPais
    novoPais = False
   

formPaises = Tk()
formPaises.title("Cadastro de Paises")
formPaises.geometry("500x350+300+200") #coluna+linha

#titulo
titulo = Label(formPaises, text="Cadastro de Paises")
titulo.grid(row=0, stick=W+E+N+S, pady=10, padx=10)
separa = Frame(height=2, bd=1, relief=SUNKEN)
separa.grid(row=1, stick=W+E+N+S, columnspan=4)

#pesquisa
labelPesquisa = Label(formPaises, text="Pesquisar:")
labelPesquisa.grid(row=2, column=0, pady=15)
editPesquisa = Entry()
editPesquisa.grid(row=2, column=1, pady=15)
botaoPesquisa = Button(formPaises, text="Pesquisar", command= pesquisar)
botaoPesquisa.grid(row=2, column=3, padx=10, pady=15)

#Labels paises
labelCodigo = Label(formPaises, text="Codigo: ")
labelPais = Label(formPaises, text="Pais: ")
labelCity = Label(formPaises, text="City: ")
labelTelcode = Label(formPaises, text="Telcode: ")

#entradas (ENTRY)
editCodigo = Entry(state="readonly")
editPais = Entry()
editCity = Entry()
editTelcode = Entry()

#Posicionamento no formulario dos Labels e edits de paises
labelCodigo.grid(row=4, stick=W, padx=10)
editCodigo.grid(row=4, column=1, pady=5)
labelPais.grid(row=5, stick=W, padx=10)
editPais.grid(row=5, column=1, pady=5)
labelCity.grid(row=6, stick=W, padx=10)
editCity.grid(row=6, column=1, pady=5)
labelTelcode.grid(row=7, stick=W, padx=10)
editTelcode.grid(row=7, column=1, pady=5)

#botoes para manutenção
botoes = Frame()
botaoNovo = Button(botoes, text="Novo", command=novo)
botaoGravar = Button(botoes, text="Gravar", command=cadastro, state="disabled")
botaoAlterar = Button(botoes, text="Alterar", command=alterar)
botaoExcluir = Button(botoes, text="Excluir", command=excluir)
botaoCancelar = Button(botoes, text="Cancelar", command=cancelar, state="disabled")

botaoNovo.grid(row=1, column=0, pady=10, padx= 2)
botaoGravar.grid(row=1, column=1, pady=10, padx= 2)
botaoAlterar.grid(row=1, column=2, pady=10, padx= 2)
botaoExcluir.grid(row=1, column=3, pady=10, padx= 2)
botaoCancelar.grid(row=1, column=4, pady=10, padx= 2)

labelStatus = Label(botoes, text="Status: ")
labelStatus.grid(row=2, column=1, pady=10, padx= 2, columnspan=5)

separa1 = Frame(height=2, bd=1, relief=SUNKEN)
separa1.grid(row=9, stick=W+E+N+S, columnspan=4, pady=10)

botoes.grid(row=10, column=1)

pesquisar()
desabilitarCampos()
mainloop()
