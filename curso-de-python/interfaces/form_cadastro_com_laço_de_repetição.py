from tkinter import *
Label(text="Cadastro de Paises", anchor=W, font=("Arial", 20)).grid(row=1, column=1, columnspan=4, pady=5)
camposPaises = "Pais", "City", "Telcode"

linha = 2
for campos in camposPaises:
    Label(text=campos, anchor=W, justify=LEFT).grid(row=linha, column=1, pady=5)
    Entry().grid(row=linha, column=2, pady=5)
    linha+=1
botaoGravar = Button(text="Gravar")
botaoGravar.grid(row=linha+1, column=1, pady=5)
mainloop()