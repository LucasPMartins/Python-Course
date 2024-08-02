# 2 - Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado:
    def __init__(self,lado: int) -> None:
        self._lado = lado

    @property
    def lado(self) -> int:
        return self._lado
    @lado.setter
    def lado(self,novo_lado: int) -> None:
        if novo_lado < 0:
            raise ValueError("O lado de um quadrado não pode ser negativo.")
        self._lado = novo_lado

    def calcula_area(self) -> int:
        return self._lado**2
    
if __name__ == '__main__':
    q = Quadrado(4)
    print(q.lado)  # Acessa o getter
    q.lado = 6     # Usa o setter
    print(q.lado)
    print(q.calcula_area())