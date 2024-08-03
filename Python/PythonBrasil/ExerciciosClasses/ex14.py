# 14 - Aprimore a classe do exercício anterior para adicionar o método aumentarSalario 
# (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
# Exemplo de uso:
# harry=funcionário("Harry",25000)
# harry.aumentarSalario(10)

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

    def aumentarSalario(self, porcentualDeAumento):
        if isinstance(porcentualDeAumento,int):
            porcentualDeAumento /= 100
        self._salario += porcentualDeAumento * self._salario

lucas =  Funcionario('Lucas',2300)
lucas.aumentarSalario(15)
print(lucas.salario)