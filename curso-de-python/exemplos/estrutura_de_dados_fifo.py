passageiros = ["Marcus", "Goku", "Naruto", "Kirito", "Natsu", "Asuna", "Asta"]
posicaoUltimo = len(passageiros)

while True:
    print("Tem %d passageiros na fila!" %posicaoUltimo)
    print("Os passageiros na fila são: ")
    for i, num in enumerate(passageiros):
        print("Passageiro: [%d] --> %s" % (i+1, num))
    print("\n")
    print("Possiveis opçoes a serem selecionadas:")
    print("Digite 1 para adicionar uma pessooa na fila")
    print("Digite 2 para dizer que pessoa foi atendida (saiu da fila)")
    print("Digite 3 para sair")
    print("\n")
    acao = int(input("Informe a operação (1, 2 ou 3): "))
    if acao == 1:
        pessoa = input("Digite o nome da pessoa que entrou na fila: ")
        passageiros.append(pessoa)
        posicaoUltimo += 1
    elif acao == 2:
        if (len(passageiros)) > 0:
            passageiros.pop(0) # retira o 1 que entrou (fifo)
            posicaoUltimo -= 1
        else:
            print("A fila está vazia")
    elif acao == 3:
        print("------------------FIM-------------------")
        break
    else:
        print("Você escolheu uma opção inválida, escolha 1, 2 ou 3")
