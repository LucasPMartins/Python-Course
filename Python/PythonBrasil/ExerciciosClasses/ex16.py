# 16 - Crie uma "porta escondida" no programa do programa do bichinho virtual que 
# mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto 
# quando uma opção secreta, não listada no menu, for informada na escolha do usuário. 
# Dica: acrescente um método especial str() à classe Bichinho.

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

    def __str__(self) -> str:
        return f'Nome: {self.nome}, Idade: {self.idade}, Humor: {self.humor()}\n'\
               f'Fome: {self.fome} e Saude: {self.saude}'


# Exemplo de uso
tamagushi = Tamagushi("Tama")
print(tamagushi)
print('Humor:',tamagushi.humor())
print(tamagushi)