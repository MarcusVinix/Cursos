numeros = [30, 28, 43, 54, -1, -4, -6, -7, 8, 7, 9,]
for num in numeros:
    if num % 2 == 0:
        print("O numero ", num," è par")
    else:
        print("O numero ", num, "é impar")
print("FIM DO FOR")

i = 0
while i < len(numeros):
    if numeros[i] % 2 ==  0:
        print("O numero ", numeros[i], " é par")
    else:
        print("O numero ", numeros[i], " é impar")
    i += 1
print("FIM DO WHILE")
pares = []
impares = []
for num in numeros:
    if num % 2 == 0:
         pares.append(num)
    else:
        impares.append(num)

print("Os pares são: ", pares)
print("Os impares são: ", impares)
