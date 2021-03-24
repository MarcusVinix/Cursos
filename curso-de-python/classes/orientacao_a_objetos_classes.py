#criando classe sem paramentros
class Carros:
    def __init__(self):
        self.marca = "Ferrari"
        self.cor = "Vermelha"

carro = Carros() #instaciando
print(carro.marca)
print(carro.cor)
print("\n")

carro.marca = "Chevrolet"
carro.cor = "Preta"
print(carro.marca)
print(carro.cor)
print("\n")

#criando classe com parametros
class Carros1:
    def __init__(self, pmarca, pcor):
        self.marca = pmarca
        self.cor = pcor

carro1 = Carros1("Mustang", "Amarelo") #instanciando
print(carro1.marca)
print(carro1.cor)
print("\n")
carro1.marca = "Fiat"
carro1.cor = "Azul"
print(carro1.marca)
print(carro1.cor)
