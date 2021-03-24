'''while true:
    print("laço inifinito ... nao para nunca")

while 1:
    print("laço inifinito ... nao para nunca")'''

x=1
while x <= 9:
    print("Numero: ", x)
    x += 1
else:
    print("FIM WHILE")

numTabuada = int(input("Digite o numero da tabuada: "))
indice = 1
while indice <= 9:
    print("%d * %d = %d" % (numTabuada, indice, (numTabuada * indice)))
    indice += 1
else:
    print("FIM DA TABUADA DO WHILE")
