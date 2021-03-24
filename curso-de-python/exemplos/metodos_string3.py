dados = ['Marcus', 'Naruto', 'Goku', 'Midorya']

print(dados)
print("\n".join(dados))
print("-".join(dados))
print("***********".join(dados))

palavra = "unknow"
print("ljus =", palavra.ljust(10), "casa")
print("rjust =", "casa", palavra.rjust(10))

print("Partition, divide a string em uma tupla com 3 elementos: ", "MarcusViniciusSouza".partition("Vinicius"))
print("Partition, divide a string em uma tupla com 3 elementos: ", "xyzxyzx".partition("y"))
print("Partition, divide a string em uma tupla com 3 elementos: ", "MarcusViniciusSouza".partition("Marcus"))
print("Partition, divide a string em uma tupla com 3 elementos: ", "xyz".partition("x"))
print("RPartition, divide a string em uma tupla com 3 elementos: ", "MarcusViniciusSouza".rpartition("Vinicius"))
print("RPartition, divide a string em uma tupla com 3 elementos: ", "xyz".rpartition("y"))
print("RPartition, divide a string em uma tupla com 3 elementos: ", "MarcusViniciusSouza".rpartition("Souza"))
print("RPartition, divide a string em uma tupla com 3 elementos: ", "xyzxyzx".rpartition("x"))
print("split -> divide a String em lista: ", "Marcus Vinicius Souza".split())
print("split -> divide a String em lista: ", "Marcus Vinicius Souza".rsplit())
print("split -> divide a String em lista: ", "Marcus;Vinicius;Souza".split(";"))
print("split -> divide a String em lista: ", "Marcus;Vinicius;Souza".split(";"))
