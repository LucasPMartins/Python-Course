# 5 - Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista 
# e saldo. 
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, 
# saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero:int, correntista:str, saldo: float = 0.0) -> None:
        self.numero = numero
        self.correntista = correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.correntista = novo_nome

    def deposito(self, valor):
        if valor < 0:
            raise ValueError('Valor de depósito não deve ser negativo')
        self.saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            raise ValueError('Valor de saque inválido!')


if __name__ == "__main__":
    conta = ContaCorrente(123456, "João Silva")
    print(f"Conta: {conta.numero}, Correntista: {conta.correntista}, Saldo: {conta.saldo}")
    
    conta.deposito(1000)
    print(f"Saldo após depósito: {conta.saldo}")
    
    conta.sacar(200)
    print(f"Saldo após saque: {conta.saldo}")
    
    conta.alterarNome("Maria Oliveira")
    print(f"Novo nome do correntista: {conta.correntista}")