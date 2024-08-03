# 12 - Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante
#  a classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. 
#  Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
#  Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. 
#  Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e 
#  uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e 
#  imprime o saldo resultante.
from ex05 import ContaCorrente

class ContaInvestimento(ContaCorrente):
    def __init__(self, numero: int, correntista: str, saldo: float = 0, taxajuros: float = 0.0) -> None:
        super().__init__(numero, correntista, saldo)
        self.taxaJuros = taxajuros
    def adicioneJuros (self):
        if isinstance(self.taxaJuros, int):
            self.taxaJuros = self.taxaJuros/100
        self.saldo += self.taxaJuros*self.saldo

conta = ContaInvestimento(123,'Lucas',1000,10)
conta.adicioneJuros()
conta.adicioneJuros()
conta.adicioneJuros()
conta.adicioneJuros()
conta.adicioneJuros()
print(conta.saldo)
