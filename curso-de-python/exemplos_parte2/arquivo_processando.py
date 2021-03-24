arquivo = open("texto.txt", "w") #r = ler, w = escrever
print("O nome do arquivo aberto é ", arquivo.name)

arquivo.write("#Lista de personagens de animes:\n\n")
arquivo.write("*Goku\n")
arquivo.write("*Naruto\n")
arquivo.write("*Kirito\n")
arquivo.write("*Natsu\n")
arquivo.write("%Isso não deve ser impresso \n")
arquivo.write("*Asuna\n")
arquivo.flush()

arquivo =open ("texto.txt", "r") #r = ler, w = escrever
for linha in arquivo.readlines():
    if linha[0] == "#":
        print(linha[1:].center(80))
    elif linha[0] == "*":
        print(linha[1:].ljust(80))
arquivo.close()
