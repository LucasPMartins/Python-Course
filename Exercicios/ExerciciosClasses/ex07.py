# 7 - Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade. 
# Métodos: Alterar Nome, Fome, Saúde e Idade;
#          Retornar Nome, Fome, Saúde e Idade 
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do 
# nosso tamagushi, este humor é uma combinação entre os  atributos Fome e Saúde,
# ou seja, um campo calculado, então não devemos criar um atributo para armazenar 
# esta informação por que ela pode ser calculada a qualquer momento.
from dataclasses import dataclass, field

@dataclass
class Tamagushi:
    _nome: str
    _idade: int = field(default=1, init=False)
    _fome: int = field(default=100, init=False)
    _saude: int = field(default=100, init=False)

    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    @property
    def fome(self) -> int:
        return self._fome
    @fome.setter
    def fome(self, valor: int) -> None:
        self._fome = valor

    @property
    def idade(self) -> int:
        return self._idade
    @idade.setter
    def idade(self, valor: int) -> None:
        self._idade = valor

    @property
    def saude(self) -> int:
        return self._saude
    @saude.setter
    def saude(self, valor: int) -> None:
        self._saude = valor

    def humor(self) -> int:
        return (self._fome + self._saude)//2


# Exemplo de uso
tamagushi = Tamagushi("Tama")
print(tamagushi)
print('Humor:',tamagushi.humor())