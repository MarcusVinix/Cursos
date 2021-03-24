#from tkinter import *
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.criarBotoes()
        

    def criarBotoes(self):
      
        #usando as posicoes
        self.botao1 = tk.Button(self, text="1 botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao1.pack(side="top")
        self.botao2 = tk.Button(self, text="2 botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao2.pack(side="top")
        self.botao3 = tk.Button(self, text="left botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao3.pack(side="left")
        self.botao4 = tk.Button(self, text="right botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao4.pack(side="right")
        self.botao5 = tk.Button(self, text="bottom botão", fg="white", bg="black", font=("Verdana","16", "italic", "bold"))
        self.botao5.pack(side="bottom")

        

    
root = tk.Tk()

#criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("TESTE")
minhaAplicacao.master.maxsize(1024, 768)
minhaAplicacao.master.geometry("800x600")

#inicia a aplicação
minhaAplicacao.mainloop()
