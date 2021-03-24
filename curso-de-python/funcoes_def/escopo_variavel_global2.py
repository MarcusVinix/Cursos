#modulo
nome = "MARCUS" #variavel global
nome1 = "GOKU"  #variavel global
nome2 = "NATSU" #variavel global

def nomes():
    nome3 = "KIRITO" #variavel local
    nome2 = "naruto" #variavel local, sobrescreve a variavel global nome2
    print(nome2)

nomes()
print(nome2)

def somaLista(lista):
    global soma
    for numLista in lista:
        soma += numLista
    return soma
soma = 0
#print(somaLista([2,3,6,7,8,]))

def somaLista1(lista):
    global soma
    for numLista in lista:
        if type(numLista) is list: #se o tipo do item é uma lista
            somaLista1(numLista)
        else: 
            soma += numLista
    return soma

soma = 0
#print(somaLista1([5,4,3,2,6]))
print(somaLista1([[5,6], [2,2,1,6]]))