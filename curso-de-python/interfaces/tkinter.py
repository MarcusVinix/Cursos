from tkinter import *
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.criarBotoes()
        self.criarLabels()
        self.entradaDados()

    def criarBotoes(self):
        #forma1 de criar botoes
        self.botao = Button(self)
        self.botao["text"]="Welcome the python"
        self.botao["fg"]="red"
        self.botao["bg"]="blue"
        self.botao.pack(side="top")

        #segunda forma decriar botoes
        self.botao1 = Button(self, text="Segundo botão", fg="white", bg="black")
        self.botao1.pack(side="top")

    def criarLabels(self):
        self.label = Label(self)
        self.label["text"]="Welcome the python"
        self.botao.pack(side="top")

    def entradaDados(self):
        self.edit = Entry(self)
        self.edit.pack(side="top")

#criando a aplicação
minhaAplicacao = App()

minhaAplicacao.master.title("TESTE")
minhaAplicacao.master.maxsize(1024, 768)
minhaAplicacao.master.geometry("800x600")

#inicia a aplicação
minhaAplicacao.mainloop()
