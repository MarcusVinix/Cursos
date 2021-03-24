from tkinter import *
import mysql.connector
from mysql.connector import errorcode
import sys
import menus
class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Acesso ao sistema")
        Label(self.master, text="Usuario e Senha").grid(row=1, column=1, columnspan=2, pady=4)
        Label(self.master, text="Usuario").grid(row=2, column=1, pady=4)
        self.usuario = Entry(self.master, width=10, font=("Winddings", "10"))
        self.usuario.grid(row=2, column=2)
        self.usuario.focus_force()
        Label(self.master, text="Senha").grid(row=3, column=1, pady=4)
        self.senha = Entry(self.master, width=10, show="*", fg="darkgrey")
        self.senha.grid(row=3, column=2)
        self.status = Label(self.master, text="Status...")
        self.status.grid(row=4, column=1,columnspan=2, pady=4)
        self.entrar = Button(self.master, width=7, text="OK", command=self.validarUsuarioSenha)
        self.entrar.grid(row=5,column=1, pady=4, padx=3)
        self.sair = Button(self.master, width=7, text="Sair")
        self.sair.grid(row=5, column=2, pady=4, padx=3)
   

    def validarUsuarioSenha(self):

        
        try:
            
            cnx = mysql.connector.connect(user='root',
                                                database='cursodego',
                                                host='127.0.0.1',
                                                password='batata123')
            #print("Conseguil conectar ao banco de dados")
            cursor = cnx.cursor()
            usuario = self.usuario.get()
            senha = self.senha.get()
            sql = "select * from login where usuario like '"+usuario+"' and senha like '"+senha+"'"
            #print("sql = "+sql)
            cursor.execute(sql)
            valido = cursor.fetchall()
            if len(valido) > 0:
                self.status['text'] = "Acesso Aprovado"
                menus.menus()
            else: 
                self.status['text'] = "Acesso Negado"


        except mysql.connector.Error as err:
            
            print("Não conseguil conectar ao banco de dados")
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Usuario ou senha inválidos")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Base de dados não existe")
            else:
                print(err)
        return cnx
        
    #def validarSenha(self):
        #if self.usuario.get() == "Marcus" and self.senha.get() == "159159":
           # self.status['text'] = "Acesso Aprovado"
       # else: 
           # self.status['text'] = "Acesso Negado"

root = Tk()
Login(root)
root.mainloop()
