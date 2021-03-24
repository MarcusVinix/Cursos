#from tkinter import *
import tkinter as tk
from tkinter import messagebox

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.criarBotoes()
        self.criarLabels()
        self.entradaDados()

    def criarBotoes(self):
        #forma1 de criar botoes
        self.botao = tk.Button(self)
        self.botao["text"]="Welcome the python"
        self.botao["fg"]="red"
        self.botao["bg"]="blue"
        self.botao["font"]=("Arial", "16", "italic", "bold")
        self.botao["height"]=3
        self.botao["width"]=20
        self.botao["command"]=self.acaoImprimir
        self.botao.pack(side="top")

        #segunda forma decriar botoes
        self.botao1 = tk.Button(self, text="Segundo botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"),command=self.acaoImprimir)
        self.botao1.pack(side="top")

        #botao de sair
        self.botao1 = tk.Button(self, text="SAIR", fg="yellow", bg="blue", command=root.destroy)
        self.botao1.pack(side="bottom")

    def criarLabels(self):
        self.label = tk.Label(self)
        self.label["text"]="Bem vindo ao python"
        self.label["font"]=("Arial", "16", "italic", "bold")
        self.label["height"]=3
        self.label["width"]=20
        self.label.pack(side="top")

    def entradaDados(self):
        self.edit = tk.Entry(self)
        self.edit.pack(side="bottom")
    
    def acaoImprimir(self):
        print("HEllo wolrd")
        print(self.edit.get())
        messagebox.showinfo("Texto Digitado", self.edit.get())

root = tk.Tk()

#criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("TESTE")
minhaAplicacao.master.maxsize(1024, 768)
minhaAplicacao.master.geometry("800x600")

#inicia a aplicação
minhaAplicacao.mainloop()
