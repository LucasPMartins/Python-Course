# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'Lucas'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Lucas', 'Sobrenome')
# p1.nome = 'Maria'
# p1.sobrenome = 'Martins'
p2 = Pessoa('Maria', 'Martins')
# p2.nome = 'Maria'
# p2.sobrenome = 'Martins'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
