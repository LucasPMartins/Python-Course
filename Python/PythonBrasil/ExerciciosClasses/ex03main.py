# c) Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe
# as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
# a quantidade de pisos e de rodapés necessárias para o local.

from ex03 import Retangulo
import os

def calcula_qtd(pisos: Retangulo,medidas: float) -> tuple:
    area_local = medidas  # área do local em metros quadrados
    qtd_pisos = area_local / pisos.calcula_area()
    perimetro_local = 2 * ((medidas ** 0.5) * 2)
    qtd_rodapes = perimetro_local / pisos.calcula_perimetro()
    return round(qtd_pisos), round(qtd_rodapes)

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('---=== Calculadora de Pisos ===---\n')
        medidas = float(input('Digite as medidas do local em metros quadrados: '))
        base = float(input('Digite o comprimento do piso em centímetros: '))
        altura = float(input('Digite a largura do piso em centímetros: '))
        qtd = calcula_qtd(Retangulo(base, altura), medidas)
        print()
        print('Quantidade de pisos:', qtd[0])
        print('Quantidade de rodapés:', qtd[1])
        print()
        input('Pressione Enter para continuar...')
    except ValueError:
        print('Erro, digite um valor válido!')
        input('Pressione Enter para continuar...')