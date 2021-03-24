from tkinter import *
class Conteiners:
    def __init__(self, master):
        self.conteiner1 = Frame(master)
        self.conteiner2 = Frame(master)
        self.conteiner3 = Frame(master)
        self.conteinerSeparador = Frame(height=20, width=150, bd=2, relief=SUNKEN)
        self.conteiner1.pack()
        self.conteinerSeparador.pack()
        self.conteiner2.pack()
        self.conteiner3.pack()
        Button(self.conteiner1, text="Botão 1").pack()
        Button(self.conteiner2, text="Botão 2").pack(side=LEFT)
        Button(self.conteiner2, text="Botão 3").pack(side=RIGHT)
        Button(self.conteiner3, text="Botão 4", command=self.fechar).pack()

    def fechar(self):
        exit()

def sair():
    pass

root = Tk()
root.protocol("WM_DELETE_WINDOW", sair)
Conteiners(root)
root.mainloop()
