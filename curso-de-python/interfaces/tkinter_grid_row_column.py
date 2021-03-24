#from tkinter import *
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.criarBotoes()
        

    def criarBotoes(self):
      
        #usando grid
        self.botao1 = tk.Button(self, text="1 botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao1.grid(row="1", column="1")
        self.botao2 = tk.Button(self, text="2 botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao2.grid(row="2", column="2")
        self.botao3 = tk.Button(self, text="3 botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao3.grid(row="3", column="3")
        self.botao4 = tk.Button(self, text="4 botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao4.grid(row="1", column="3")
        self.botao5 = tk.Button(self, text="5 botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao5.grid(row="3", column="1")
        

    
root = tk.Tk()

#criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("TESTE")
minhaAplicacao.master.maxsize(1024, 768)
minhaAplicacao.master.geometry("800x600")

#inicia a aplicação
minhaAplicacao.mainloop()
