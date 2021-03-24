listaNomes = ["Marcus", "Vinicius", "Goku", "Naruto", "kirito"]
print(listaNomes)
listaNomes.reverse() #inverte
print(listaNomes)

for nomesLista in listaNomes:
    print(nomesLista)

listaNomes.sort() #ordena de forma alfabetica
print(listaNomes)

for i, nomesLista in enumerate(listaNomes):
    print("Lista de nomes: ", i + 1, nomesLista)
print(nomesLista[2:])
print(listaNomes[2:])
