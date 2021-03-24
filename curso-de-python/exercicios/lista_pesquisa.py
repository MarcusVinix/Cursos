listaNomes = ["Marcus", "Vinicius", "Goku", "Kirito", "Asuna", "Natsu", "Naruto"]
print(listaNomes)
nomePesquisar = input("Digite o nome a ser pesquisado: ")
encontrou = False
numAlunos = 0
while numAlunos < len(listaNomes):
    if nomePesquisar == listaNomes[numAlunos]:
        encontrou = True
        break
    numAlunos += 1
if encontrou ==  True:
    print("Aluno localizado e matriculado")
else:
    print("Aluno não localizado e não matriculado", nomePesquisar)

for alunos in listaNomes:
    if nomePesquisar ==  alunos:
        print("Aluno localizado e matriculado")
        break
else:
    print("Aluno não localizado e não matriculado", nomePesquisar)
