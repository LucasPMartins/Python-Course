# 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre 
# arredonde os valores para cima, isto é, considere latas cheias.

import math

while True:
    metros = input("Digite o tamanho em metros quadrados da área a ser pintada:")
    try:
        metros_float = float(metros)
        litros = metros_float/6
        latas = math.ceil(litros/18)
        galoes = math.ceil(litros/3.6)
        print(f'Para pintar {metros} metros será necessário {litros:.2f} litros')
        print(f'Opcão 1: Comprar {latas} latas de 18 litros cada, R${latas*80:.2f}')
        print(f'Opção 2: Comprar {galoes} galões de 3,6 litros cada , R${galoes*25:.2f}')
        litros = litros * 1.1 # Acrescente 10% de folga
        resto = litros%18
        latas = math.ceil((litros - resto)//18)
        galoes = math.ceil(resto/3.6)
        print(f'Opção 3: Misturar {latas} latas e {galoes} galões, R${(latas*80 + galoes*25):.2f}')
        break
    except Exception as e:
        print(f"\nOcorreu um erro!\n Erro:{e}\n")