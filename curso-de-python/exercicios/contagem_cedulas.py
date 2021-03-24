valor = float(input("Digite o valor: "))
cedulas = 0
valorCedulaAtual = 100
valorASerEntregue = valor
while True:
    if valorCedulaAtual <= valorASerEntregue:
        cedulas += 1
        valorASerEntregue -=valorCedulaAtual
    else:
        if cedulas > 0:
            print("%d cedula(s) de R$ %5.2f" % (cedulas, valorCedulaAtual))
        if valorASerEntregue == 0:
            break
        if valorCedulaAtual == 100:
            valorCedulaAtual = 50
        elif valorCedulaAtual == 50:
            valorCedulaAtual =  20
        elif valorCedulaAtual == 20:
            valorCedulaAtual = 10
        elif valorCedulaAtual == 10:
            valorCedulaAtual = 5
        elif valorCedulaAtual == 5:
            valorCedulaAtual = 2
        cedulas = 0
