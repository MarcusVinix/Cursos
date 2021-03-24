for numeros in "123456789":
    print("Numero: ", numeros)
else:
    print("FIM")

for numeros in range(10):
    if numeros > 6:
        break
    print("Numero: ", numeros)
else:
    print("FIM")

for nomes in ["Marcus", "Natsu", "Goku", "kirito"]:
    print("Nomes: ", nomes)
else:
    print("Fim nomes")

dadostupla = [("a", "b"), ("c", "d"), ("e", "f")]
for (alf1, alf2) in dadostupla:
    print(alf2)

for numeros in range(20, 30, 2):
    if numeros == 25:
        continue
    print("Numero: ", numeros)
else:
    print("FIM")

for numeros in range(50, 40, -1):
    print("Numero: ", numeros)
else:
    print("FIM")
for numeros in range(-6, 6):
    print("Numero: ", numeros)
else:
    print("FIM")
for tabuada in range(1,10):
    print("7 * %d  = %d" % (tabuada, (7*tabuada)))

numTabuada = int(input("Digite um numero para a tabuada: "))
for tabuada in range(1, 10):
    print("%d * %d = %d" % (numTabuada, tabuada, (numTabuada * tabuada)))

somaTotal = 0
for soma in range(1, 12):
    somaTotal += soma
    print("A smoa é %d" %somaTotal)
