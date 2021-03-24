def validar(pergunta, notaMin, notaMax):
    while True:
        nota = int(input(pergunta))
        if nota < notaMin or nota > notaMax:
            print("Atenção, a nota %d é inválida, tem que ser entre %d e %d!!" % (nota, notaMin, notaMax))
        else:
            print("Nota válida!")
            return True
validar("Digite a nota do aluno: ", 0, 10)
    