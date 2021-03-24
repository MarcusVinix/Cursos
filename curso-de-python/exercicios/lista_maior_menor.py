temperaturas = [30, 33, 23, 44, 10, -2, -4, 2, 6, 7,9, 20, 31]
maior = temperaturas[0]
for listaTemperaturas in temperaturas:
    if listaTemperaturas > maior:
        maior = listaTemperaturas
print("Com laço FOR a maior temperatura registrada foi: ", maior)
menor = temperaturas[0]
for listaTemperaturas in temperaturas:
    if listaTemperaturas < menor:
        menor = listaTemperaturas
print("Com laço FOR a menor temperatura registrada foi: ", menor)

maior = temperaturas[0]
i = 0
while i < len(temperaturas):
    if temperaturas[i] > maior:
        maior = temperaturas[i]
    i += 1
print("Com laço while a maior temperatura registrada foi: ", maior)

menor = temperaturas[0]
i = 0
while i < len(temperaturas):
    if temperaturas[i] < menor:
        menor = temperaturas[i]
    i += 1
print("Com laço While a menor temperatura registrada foi: ", menor)
