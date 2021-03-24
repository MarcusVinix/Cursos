import os

print(os.listdir(".")) #mostra arquivos e pastas no diretório atual
print(os.listdir("exercicios")) #mostra arquivos e pastas no diretório exercicios
#os.mkdir("GHOST")
print(os.getcwd()) #mostra diretorio atual
os.chdir("GHOST") #entra dentro do diretorio GHOST
print(os.getcwd()) #mostra diretorio atual
open("arquivo.txt", "w").close()
print(os.listdir("."))  #mostra arquivos e pastas no diretório atual
#os.makedirs("Naruto/Goku/kirito/natsu") #cria as 3 pastas uma dentro da outra separando pela /
#os.rename("Naruto", "Natsu") #renomeia
#os.mkdir("cursos") #criar diretorios
#os.rmdir("cursos") #remove diretorios
#os.remove("arquivo.txt") 

print(os.getcwd()) #mostra o diretorio atual
os.chdir("..") #retorna ao diretorio anterior
print(os.getcwd()) #mostra o diretorio atual
for arquivoOuPasta in os.listdir("."):
    if os.path.isdir(arquivoOuPasta):
        print("Diretorio: ", arquivoOuPasta)
    elif os.path.isfile(arquivoOuPasta):
        print("Arquivo: ", arquivoOuPasta)


