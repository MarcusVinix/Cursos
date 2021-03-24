notaAluno = int(input("Digite a nota do aluno: "))
mediaParaPassar = 6

if notaAluno >= mediaParaPassar:
    print("Aluno Aprovado!!")
    print("Parabéns!!!")
elif notaAluno >= 4:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")        
        