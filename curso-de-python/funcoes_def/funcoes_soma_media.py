def  somarLista(lista):
    totalSoma = 0
    for numeroLista in lista:
        totalSoma += numeroLista
    return totalSoma

def mediaLista(lista):
    return(somarLista(lista)/len(lista))

listaNumeros = [5, 8, 3, 9, 4, 1, 7]

print("A soma da lista é:", somarLista(listaNumeros))
print("A media da lista é:", mediaLista(listaNumeros))

def somaEMedia(lista):
    totalSoma = 0
    for numeroLista in lista:
        totalSoma += numeroLista
    return (totalSoma/len(lista))

print("A media da lista (com a soma junto):", somaEMedia(listaNumeros))