#from tkinter import *
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.criarBotoes()
        

    def criarBotoes(self):
      
        #posicionando os numeros da calculadora
        self.botao7 = tk.Button(self, text="7", width=6, height=3)
        self.botao7.grid(row="1", column="1")
        self.botao8 = tk.Button(self, text="8", width=6, height=3)
        self.botao8.grid(row="1", column="2")
        self.botao9 = tk.Button(self, text="9", width=6, height=3)
        self.botao9.grid(row="1", column="3")
        self.botaoSoma = tk.Button(self, text="+", width=6, height=3)
        self.botaoSoma.grid(row="1", column="4")
        self.botao4 = tk.Button(self, text="4", width=6, height=3)
        self.botao4.grid(row="2", column="1")
        self.botao5 = tk.Button(self, text="5", width=6, height=3)
        self.botao5.grid(row="2", column="3")
        self.botao6 = tk.Button(self, text="6", width=6, height=3)
        self.botao6.grid(row="2", column="2")
        self.botaoDiv = tk.Button(self, text="/", width=6, height=3)
        self.botaoDiv.grid(row="2", column="4")
        self.botao1 = tk.Button(self, text="1", width=6, height=3)
        self.botao1.grid(row="3", column="1")
        self.botao2 = tk.Button(self, text="2", width=6, height=3)
        self.botao2.grid(row="3", column="2")
        self.botao3 = tk.Button(self, text="3", width=6, height=3)
        self.botao3.grid(row="3", column="3")    
        self.botaoMult = tk.Button(self, text="*", width=6, height=3)
        self.botaoMult.grid(row="3", column="4")
        self.botao0 = tk.Button(self, text="0", width=6, height=3)
        self.botao0.grid(row="4", column="1")
        self.botaoCe = tk.Button(self, text="C", width=6, height=3)
        self.botaoCe.grid(row="4", column="2")
        self.botaoSub = tk.Button(self, text="-", width=6, height=3)
        self.botaoSub.grid(row="4", column="3")
        self.botaoIgual = tk.Button(self, text="=", width=6, height=3)
        self.botaoIgual.grid(row="4", column="4")

root = tk.Tk()

#criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("TESTE")
minhaAplicacao.master.maxsize(1024, 768)
#minhaAplicacao.master.geometry("800x600")

#inicia a aplicação
minhaAplicacao.mainloop()
