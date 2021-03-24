from tkinter import *
from os import popen
import os
from tkinter import messagebox
class Sistema:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)
        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(label="Clientes", command=self.cadastrarCliente)
        self.menuCadastro.add_command(label="Fornecedores", command=self.calculadora)
        self.menuCadastro.add_command(label="Estoque", command=self.chamaArquivoTexto)
        self.menuCadastro.add_command(label="Sair", command=self.fechar)
        self.menu.add_cascade(label="Cadastro",menu=self.menuCadastro)
        self.menuConsulta = Menu(self.menu)
        self.menuConsulta.add_command(label="Clientes")
        self.menuConsulta.add_command(label="Fornecedores")
        self.menuConsulta.add_command(label="Estoque")
        self.menu.add_cascade(label="Consulta", menu=self.menuConsulta)
        master.config(menu=self.menu)
    
    def cadastrarCliente(self):
        print("Cliclou em cadastrar")
    def calculadora(self):
        popen("calc.exe")
    def chamaArquivoTexto(self):
        os.startfile("teste.txt")
    def fechar(self):
       exit()
def sair():
    if  messagebox.askyesno("Fechar Janela", "Tem certeza de que deseja fechar a janela?"):
        exit()
    else:
        pass

def menus():
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", sair)
    root.geometry("600x400")
    root.title("Sistema de Estoque")
    Sistema(root)
    root.mainloop()