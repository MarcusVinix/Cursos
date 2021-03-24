#from tkinter import *
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.criarBotoes()
        

    def criarBotoes(self):
      
        botoes = ["7", "8","9","+","4","5","6","/","1","2","3","*","0","C","-","="]
        linha = 1
        coluna = 1
        for qualBotao in botoes:
            self.botao = tk.Button(self, text=qualBotao, width=6, height=3)
            self.botao.grid(row=linha, column=coluna)
            if coluna >= 4:
                linha+=1
                coluna=0
            coluna +=1
root = tk.Tk()

#criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("TESTE")
minhaAplicacao.master.maxsize(1024, 768)
#minhaAplicacao.master.geometry("800x600")

#inicia a aplicação
minhaAplicacao.mainloop()
