# 13 - Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome 
# (um string) e um salário(um double). Escreva um construtor com dois parâmetros 
# (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno 
# programa que teste sua classe.

class Funcionario:
    def __init__(self,nome:str,salario:float) -> None:
        self._nome = nome
        self._salario = salario
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self,salario):
        self._salario = salario
    