# 16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

while True:
    metros = input("Digite o tamanho em metros quadrados da área a ser pintada:")
    try:
        metros_float = float(metros)
        litros = metros_float/3
        latas = litros/18
        print(f'Para pintar {metros} metros será necessário {litros:.2f} litros, logo {math.ceil(latas)} latas.')
        print(f"O preço total é R${math.ceil(latas)*80}")
    except Exception as e:
        print(f"\nOcorreu um erro!\n Erro:{e}\n")