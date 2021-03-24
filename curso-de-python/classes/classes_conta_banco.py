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
    
contaBanco = ContaBanco("Marcus Vinicius", "9999-99", 500)
contaBanco.relatorio()
contaBanco.deposito(500)
contaBanco.relatorio()
contaBanco.saque(300)
contaBanco.relatorio()