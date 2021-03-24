import sys

arquivo = open("personagens.txt", "w") #r = ler, w = escrever

arquivo.write("Lista de personagens de animes:\n\n")
arquivo.write("Goku\n")
arquivo.write("Naruto\n")
arquivo.write("Kirito\n")
arquivo.write("Natsu\n")
arquivo.write("Asuna\n")
arquivo.flush()
#arquivo close()
print("O modo ao qual o seu arquivo foi aberto", arquivo.mode)

print("O arquivo está fechado?", arquivo.closed)

arquivo = open("personagens.txt", "r")  #r = ler, w = escrever
print("O modo ao qual o seu arquivo foi aberto", arquivo.mode)

for linha in arquivo.readlines():
    print("print comum: ",linha)
    sys.stdout.write("Print usando SYS: %s" % linha)

arquivo.close()
print("O arquivo está fechado?", arquivo.closed)
