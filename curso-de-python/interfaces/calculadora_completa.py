from tkinter import *
import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.criarComponentes()
        

    def criarComponentes(self):
        self.edit = tk.Entry(self.master, width=34)
        self.edit.grid(row=1, column=0)
        botoes = ["7", "8","9","+","4","5","6","/","1","2","3","*","0","-","C","="]
        linha = 1
        coluna = 1
        for qualBotao in botoes:
            comando = lambda x=qualBotao:self.calcular(x)
            self.botao = tk.Button(self, text=qualBotao, width=6, height=3, command=comando)
            self.botao.grid(row=linha, column=coluna)
            if coluna >= 4:
                linha+=1
                coluna=0
            coluna +=1
    def calcular(self, valor):
        if valor == "=":
            try:
                calculo=eval(self.edit.get())
                self.edit.insert(END, "="+str(calculo))
            except:
                self.edit.insert(END, " = ERRO")
        elif valor == "C":
            self.edit.delete(0, END)
        else:
            if "=" in self.edit.get():
                self.edit.delete(0, END)
            self.edit.insert(END, valor)

root = tk.Tk()

#criando a aplicação
minhaAplicacao = App(master=root)

minhaAplicacao.master.title("TESTE")
minhaAplicacao.master.maxsize(1024, 768)
#minhaAplicacao.master.geometry("800x600")

#inicia a aplicação
minhaAplicacao.mainloop()
