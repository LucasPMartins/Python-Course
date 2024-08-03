# 15 - Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo 
# que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo 
# ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os 
# níveis de fome e tédio caem.

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

    def alimentar(self, comida):
        self.fome += comida

    def brincar(self, tempo):
        for i in range(tempo):
            self._saude += 1


# Exemplo de uso
tamagushi = Tamagushi("Tama")
print(tamagushi)
print('Humor:',tamagushi.humor())