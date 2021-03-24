def soma(num1, num2):
    print("A soma é:", (num1+num2))

soma(6,7)

lista=[6, 9]
soma(*lista)

def soma2(*numeros):
    total=0
    for num in numeros:
        total += num
    print("A soma é: ", total)

lista2 = [2,6,7,9,12,45,12,8,6]
soma2(*lista2)
