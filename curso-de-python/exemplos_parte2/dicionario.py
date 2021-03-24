listaNomes = ["Goku", "Naruto", "trynda", "Garen"]
print(listaNomes[1])
print("Lista: ", listaNomes)
dicionarioNomes = {1:"Marcus",
                   2:"Vinicius",
                   3:"Jinx",
                   4:"Ashe"}
print(dicionarioNomes[1])
print(dicionarioNomes.keys())
print(dicionarioNomes.values())
print(dicionarioNomes)
dicionarioCursos = {"python":130,
                    "java":110,
                    "arduino":90}

#acrescentar elementos ao dicionario
dicionarioCursos["android"] = 146
dicionarioCursos[1] = "neri"
tresChaves = (2,3,4)
dicionarioCursos[tresChaves] = "Tres chaves"

print("Dicionário: ", dicionarioCursos)
print("Chaves: ", dicionarioCursos.keys())
print("Valor das chaves: ", dicionarioCursos.values())
print("Itens (chaves e valores): ", dicionarioCursos.items())
print("\n")
print("For cursos")
for cursos in dicionarioCursos:
    print(cursos)
print("\n")
print("For cursos valores")
for cursosValues in dicionarioCursos.values():
    print(cursosValues)
print("\n")
print("For cursos keys")
for cursosKeys in dicionarioCursos.keys():
    print(cursosKeys)
print("\n")
print("For cursos Items (chaves e valores)")
for cursosItems in dicionarioCursos.items():
    print(cursosItems)


print("O preço do curso de java é = %d" % dicionarioCursos["java"])
print("java" in dicionarioCursos)

#implementando pesquisa
while True:
    cursoPesquisar = input("Digite o nome do curso a ser pesquisado (ou fim para sair): ")
    if cursoPesquisar == "fim":
        break
    if cursoPesquisar in dicionarioCursos:
        print("Esse curso foi localizado!", cursoPesquisar)
    else:
        print("Esse curso não foi localizado!", cursoPesquisar)
