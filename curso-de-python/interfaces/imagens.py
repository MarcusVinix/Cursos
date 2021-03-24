from tkinter import *
root = Tk()
label = Label(text="Testando", padx=10).pack(side=LEFT)
imagem = PhotoImage(file="goku.png")
labelImage = Label(root, image=imagem).pack(side=RIGHT)
root.mainloop()
