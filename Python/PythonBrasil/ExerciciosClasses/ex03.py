# 3 - Classe Retangulo: Crie uma classe que modele um retangulo:
# a) Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b) Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcu-
# lar Perímetro;
# c) Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
# as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
# a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self,base: float | int,altura: float | int) -> None:
        self._base = base  / 100  # Convertendo de cm para m
        self._altura = altura / 100  # Convertendo de cm para m
    
    @property
    def base(self) -> float:
        return self._base
    @base.setter
    def base(self,nova_base: float) -> None:
        if nova_base < 0:
            raise ValueError("A base de um retangulo não pode ser negativo.")
        self._base = nova_base / 100  # Convertendo de cm para m
    @property
    def altura(self) -> float:
        return self._altura
    @altura.setter
    def altura(self,nova_altura: float) -> None:
        if nova_altura < 0:
            raise ValueError("A altura de um retangulo não pode ser negativo.")
        self._altura = nova_altura / 100  # Convertendo de cm para m

    def calcula_area(self) -> float:
        return self._base * self._altura

    def calcula_perimetro(self) -> float:
        return (self._base * 2 + self._altura * 2)