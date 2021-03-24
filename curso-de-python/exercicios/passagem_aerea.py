assentosVagos = [8, 7, 0, 24, 11, 60]
quantidadeRotas = len(assentosVagos)
print("Compra de passagens aereas:")
print("\n")
for rota, assentosDisponiveis in enumerate(assentosVagos):
    print("A rota %d possui %d assentos disponiveis!!" % (rota+1, assentosDisponiveis))
print("\n")
while True:
    rotaEscolhida = int(input("Escolha uma rota de 1 a %d (para sair digite 0): " % quantidadeRotas))
    if rotaEscolhida == 0:
        print("Sistema finalizado...Tchau!!")
        break
    if rotaEscolhida > quantidadeRotas or rotaEscolhida < 1:
        print("Rota inválida...")
    elif assentosVagos[rotaEscolhida-1] == 0:
        print("Rota com vagas indisponiveis")
    else:
        print("Há apenas %d passagens disponiveis para essa rota!" % (assentosVagos[rotaEscolhida-1]))
        quantidadePassagens = int(input("Quantas passagens você deseja comprar?: "))
        if quantidadePassagens > assentosVagos[rotaEscolhida-1]:
            print("você escolheu uma quantidade de passagens maior do que o disponivel!")
        elif quantidadePassagens < 1:
            print("Escolha uma quantidade de passagens maior do que 0!")
            print("Há apenas %d passagens disponiveis para essa rota!" % (assentosVagos[rotaEscolhida-1]))
        else:
            assentosVagos[rotaEscolhida-1] -= quantidadePassagens
            print("Compra da(s) passagem(ns) finalizada com sucesso!!!")
            print("\n")
            for rota, assentosDisponiveis in enumerate(assentosVagos):
                print("A rota %d possui %d assentos Vagos!!" % (rota+1, assentosDisponiveis))
            print("\n")
