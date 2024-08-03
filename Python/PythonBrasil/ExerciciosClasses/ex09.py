# 9 - Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
# Possua uma classe chamada Ponto, com os atributos x e y.
# Possua uma classe chamada Retangulo, com os atributos largura e altura.
# Possua uma função para imprimir os valores da classe Ponto
# Possua uma função para encontrar o centro de um Retângulo.

# Você deve criar alguns objetos da classe Retangulo. Cada objeto deve ter um vértice 
# de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um 
# objeto da classe Ponto. A função para encontrar o centro do retângulo deve retornar 
# o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
# O valor do centro do objeto deve ser mostrado na tela
# Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
from dataclasses import dataclass

@dataclass
class Ponto:
    x: int | float
    y: int | float

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attr = self.__dict__
        return f'{class_name}({attr})'

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __eq__(self, value) -> bool:
        return (self.x == value.x and self.y == value.y)

class Retangulo:
    def __init__(self, vertice_inicial: Ponto = Ponto(0,0), vertice_final: Ponto = Ponto(3,3)) -> None:
        self._vertice_inicial = vertice_inicial
        self._vertice_final = vertice_final
        self.base = vertice_final.x - vertice_inicial.x 
        self.altura = vertice_final.y - vertice_inicial.y

    @property
    def vertice_inicial(self) -> Ponto:
        return self._vertice_inicio
    @vertice_inicial.setter
    def vertice_inicial(self, novo_vetice: Ponto) -> None:
        if novo_vetice == self._vertice_final:
            raise ValueError('Os vertices não podem ser iguais')
        self._vertice_inicio = novo_vetice
    @property
    def vertice_final(self) -> Ponto:
        return self._vertice_final
    @vertice_final.setter
    def vertice_final(self, novo_vetice: Ponto) -> None:
        if novo_vetice == self._vertice_inicial:
            raise ValueError('Os vertices não podem ser iguais')
        self._vertice_final = novo_vetice

    def __str__(self) -> str:
        titulo = f'Retângulo: V-i{self._vertice_inicial} V-f{self._vertice_final}\n\n'
        linha1 ='*' + '-' * round(self.base) + '*'
        linha2 = ''
        for i in range(round(self.altura)):
            linha2 += '|' + ' '*round(self.base) + '|\n'
        return f'{titulo}{linha1}\n{linha2}{linha1}\n'

def imprime_ponto(valor: Ponto):
    print(valor)

def centro(retangulo:Retangulo):
    return Ponto(retangulo.base/2,retangulo.altura/2)


while True:
    try:
        print("Digite os pontos do retangulo:")
        x1 = float(input('Ponto Inicial x:'))
        y1 = float(input('Ponto Inicial y:'))
        x2 = float(input('Ponto final x:'))
        y2 = float(input('Ponto final y:'))
        ret = Retangulo(Ponto(x1,y1),Ponto(x2,y2))
        print(ret)
        print('Centro do retângulo:',centro(ret))
        print()
    except Exception as e:
        print('Erro:',e)
        input('Pressione "ESC" para sair...')
