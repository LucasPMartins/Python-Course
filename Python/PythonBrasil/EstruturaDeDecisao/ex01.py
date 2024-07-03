# 1 - Faça um Programa que peça dois números e imprima o maior deles.

try:
    num1 = float(input('Digite um número:'))
    num2 = float(input('Digite outro número:'))
    print('O maior número é',num1 if num1 > num2 else num2)
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")
