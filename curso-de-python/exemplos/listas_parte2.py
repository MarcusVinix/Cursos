nomes = ["Marcus", "Vinicius", "Goku"]
print("Lista nomes: ", nomes)
nomes1 = nomes #faz cópia igual (mesmo endereço de memória)
print("lista nomes1: ", nomes1)
nomes[0] = "Kirito"
print("Lista nomes: ", nomes)
print("Lista nomes1: ", nomes1)
nomes.append("Naruto")
print("Lista nomes: ", nomes)
print("Lista nomes1: ", nomes1)
nomes1.append("Natsu")
print("Lista nomes: ", nomes)
print("Lista nomes1: ", nomes1)
nomes1[3] = "Asuna"
print("Lista nomes: ", nomes)
print("Lista nomes1: ", nomes1)
nomes2 = nomes[:] #faz cópia independente (outro endereço de memória)
print("Lista nomes: ", nomes)
print("Lista nomes1: ", nomes1)
print("Lista nomes2", nomes2)
nomes[0] = "FLASH"
print("Lista nomes: ", nomes)
print("Lista nomes: ", nomes1)
print("Lista nomes: ", nomes2)
cursos =  ["Python", "HTML", "CSS3", "JavaScript","MySql","Go","Python","HTML","Go"]
print(cursos)
print(cursos.count("Python")) #quantos elementos Python tem na Lista
cursos =  ["Python", "HTML", "CSS3", "JavaScript","MySql","Go","Python","HTML","Go"]
print(cursos)
print(cursos.index("Go"))
cursos.reverse() # inverte a Lista
print(cursos)
