nomes = ["MARCUS", "Vinicius", "Natsu"]
print(nomes)
print(len(nomes))

notas = [4, 7 ,9, 10, 5]
print(notas)

pessoa = ["Marcus", 17,2.7, True]
print(pessoa[0])
print(pessoa[1])
print(pessoa[2])
pessoa[0] = "Vinicius"
print(pessoa[0])
print(pessoa)

#adicionar dados
alfabeto = ["a", "b", "c"]
print(alfabeto)
alfabeto += ["defg", "add"] #insere toda palavra
alfabeto += "defg" #insere caracter por caracter
print(alfabeto)
# += faz o mesmo que extend
alfabeto.extend("hijkl")

nomes = ["MARCUS", "Vinicius", "Natsu"]
print(nomes)
nomes.append("Goku") #insere na ultima posicao
print(nomes)
nomes.insert(0, "Naruto") #insere na primeira posicao
print(nomes)
nomes.insert(3, "Kirito") #insere na terceira posicao
print(nomes)
nomes.insert(-1, "Asuna") #insere na penultima posicao
print(nomes)

alfabeto = ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"]
print(alfabeto)
alfabeto.pop() #retira o ultimo elemento da lista
print(alfabeto)
del alfabeto[0] #retira o elemento de um índice
print(alfabeto)
del alfabeto[-1] #remove o ultimo
print(alfabeto)
alfabeto = ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"]
alfabeto.remove("b") #remove o primeiro B encontrado
alfabeto.remove("b") #remove o seundo B encontrado
print(alfabeto)
alfabeto = ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"]
print(alfabeto)
del alfabeto[2:]
print(alfabeto)
