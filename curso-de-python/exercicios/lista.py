listaFamilia = []
while True:
    pessoaFamilia = input("Digite o nome da sua familia (0 se acabou)")
    if pessoaFamilia == "0":
        break
    listaFamilia.append(pessoaFamilia)
for a in listaFamilia:
    print(a)
print("FIM DO FOR")
print("\n")

i = 0
while i < len(listaFamilia):
    print(listaFamilia[i])
    i += 1
print("FIM DO WHILE")
