print("Sem usar funções, a soma é: ", (5+6))

def soma(num1, num2):
    print("Usando funções (DEF), a soma é: ", (num1+num2))

def subtracao(num1, num2):
    print("Usando funções (DEF), a subtração é: ", (num1 - num2))

def divisao(num1, num2):
    print("Usando funções (DEF), a divisão é: ", (num1 / num2))

def multiplicacao(num1, num2):
    print("Usando funções (DEF), a multiplicação é: ", (num1 * num2))

soma(23, 45)
subtracao(89, 56)
divisao(87, 54)
multiplicacao(34, 3)

#usando comando return
def soma1(num1, num2):
    return(num1+num2)

valor1 = 70
valor2 = 80
print("Usando funções (DEF) com return, a soma é ", soma(8,7))
print("Usando funções (DEF) com return, a soma é ", soma(valor1,valor2))

def numeroPar(numero):
    return(numero % 2 == 0)
print("O numero 4 é par? ", numeroPar(4))
print("O numero 5 é par? ", numeroPar(5))

def parOuImpar(numero1):
    if numeroPar(numero1):
        return "par"
    else:
        return "impar"

print("O numero 7 é ", parOuImpar(7))
print("O numero 8 é ", parOuImpar(8))
