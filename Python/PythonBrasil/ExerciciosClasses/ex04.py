# 4 - Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano
# que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve cres-
# cer 0,5 cm.

class Pessoa:
    def __init__(self,nome:str,idade:int,peso:float,altura:float) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def enverlhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def engordar(self, novo_peso):
        self.peso += novo_peso

    def emagrecer(self, novo_peso):
        self.peso -= novo_peso

    def crescer(self, nova_altura):
        self.altura += nova_altura