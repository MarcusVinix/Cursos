panquecas= ["panqueca1", "panqueca2", "panqueca3", "panqueca4", "panqueca5", "panqueca6", "panqueca7"]
posicaoUltimo = len(panquecas)

while True:
    print("Tem %d panquecas na pilha!" %posicaoUltimo)
    print("As panquecas na pilha são: ")
    for i, num in enumerate(panquecas):
        print("panquecas: [%d] --> %s" % (i+1, num))
    print("\n")
    print("Possiveis opçoes a serem selecionadas:")
    print("Digite 1 para adicionar uma panqueca na pilha")
    print("Digite 2 para dizer que alguem pegou uma panqueca (saiu da pilha)")
    print("Digite 3 para sair")
    print("\n")
    acao = int(input("Informe a operação (1, 2 ou 3): "))
    if acao == 1:
        panquecas.append("panqueca %d" % (posicaoUltimo+1))
        posicaoUltimo += 1
    elif acao == 2:
        if (len(panquecas)) > 0:
            panquecas.pop(-1) #retira o ultimo que entro (lifo)
            posicaoUltimo -= 1
        else:
            print("A pilha de panquecas está vazia")
    elif acao == 3:
        print("------------------FIM-------------------")
        break
    else:
        print("Você escolheu uma opção inválida, escolha 1, 2 ou 3")
