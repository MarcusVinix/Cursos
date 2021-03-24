def pesquisar(lista, codigo):
    for i, codigos in enumerate(lista):
        if codigos == codigo:
            return ("Codigo %d encontrado no indice %d" % (codigo, i))
    return ("O codigo %d não foi localizado" % codigo)
listaProdutos = [4, 8, 2, 67, 5, 12]
print(pesquisar(listaProdutos, 8))
print(pesquisar(listaProdutos, 5))
print(pesquisar(listaProdutos, 11))
print(pesquisar(listaProdutos, 2))

dicionarioCursos = {"pyhton": 130,
                    "java": 110,
                    "arduino": 90}

def pesquisarDicionario(dicionarioPesquisar, cursoPesquisar):
    if cursoPesquisar in dicionarioPesquisar:
        print("Esse curso foi localizado, o seu preço é R$ %5.2f" % dicionarioPesquisar[cursoPesquisar])
    else:
        print("Esse curso não foi localizado")

pesquisarDicionario(dicionarioCursos, "java")