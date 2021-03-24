#funções lambda

def soma(num1, num2):
    print("A soma é: ", (num1+num2))
soma(6, 7)

somarLambda = lambda num1, num2: num1 + num2
print("A soma lambda é: ", somarLambda(6,7))

multiplicar = lambda num1, num2: num1 * num2
print("A multiplicação lambda é: ", multiplicar(5,5))