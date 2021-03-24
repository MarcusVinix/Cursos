import random

for num in range(10):  #irá  gerar sequencia de 0 a 10
    print(num)
print("\n")

for num in range(10):  #irá  gerar valores aleatórios
    print(random.randint(1, 50))
print("\n")

for num in range(10):  #irá  gerar valores 0 ou 1
    print(random.random())
print("\n")

for num in range(10): #irá  gerar valores ponto flutuante
    print(random.uniform(20, 30))
print("\n")

lista = [1,2,3,4,5,6,7,8,9]
print(lista)
random.shuffle(lista)
print(lista)
