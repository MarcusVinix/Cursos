valor = float(input("Digite o valor: "))
cedulas = 0
valorCedulaAtual = 100
valorASerEntregue = valor
cedulaOuMoeda = "Cedula(s)"
while True:
    if valorCedulaAtual <= valorASerEntregue:
        cedulas += 1
        valorASerEntregue -=valorCedulaAtual
    else:
        if cedulas > 0:
            print("%d %s de R$ %5.2f" % (cedulas, cedulaOuMoeda, valorCedulaAtual))
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
        elif valorCedulaAtual == 2:
            cedulaOuMoeda = "Moeda"
            valorCedulaAtual = 1
        elif valorCedulaAtual == 1:
            cedulaOuMoeda = "Moeda"
            valorCedulaAtual = 0.5
        elif valorCedulaAtual == 0.5:
            cedulaOuMoeda = "Moeda"
            valorCedulaAtual = 0.25
        elif valorCedulaAtual == 0.25:
            cedulaOuMoeda = "Moeda"
            valorCedulaAtual = 0.10
        elif valorCedulaAtual == 0.10:
            #valorCedulaAtual = 0.05
            print("1 moeda de 5 centavos")
            break
        cedulas = 0
