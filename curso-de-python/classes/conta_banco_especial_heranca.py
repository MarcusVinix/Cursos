class ContaBanco:
    def __init__(self, cliente, numeroConta, saldo=0):
        self.saldo = saldo
        self.cliente = cliente
        self.numeroConta = numeroConta
    def deposito(self, valor):
        self.saldo += valor
        print("Foi depositado R$%d em sua conta" % valor)
    def saque(self, valor):
        self.saldo -= valor
        print("Foi sacado R$%d de sua conta" % valor)
    def relatorio(self):
        print("Cliente: %s, conta numero: %s, saldo: %8.2f" % (self.cliente, self.numeroConta, self.saldo))
    
#herança 
class ContaEspecial(ContaBanco):
    def __init__(self, cliente, numeroConta, saldo=0, limite=0):
        ContaBanco.__init__(self, cliente, numeroConta, saldo=0)
        self.limite = limite
    def saque(self, valor):
        self.saldo += self.limite
        self.saldo -= valor
        print("Cliente: %s, conta numero: %s, saldo: %8.2f" % (self.cliente, self.numeroConta, self.saldo))
        
conta1 = ContaEspecial("MARCUS VINICIUS", "99999", 500, 2000)
conta1.saque(800)
    