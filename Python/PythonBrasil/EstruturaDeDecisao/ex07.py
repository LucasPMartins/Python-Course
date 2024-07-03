# 7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

try:
    num1 = float(input('Digite um número:'))
    num2 = float(input('Digite outro número:'))
    num3 = float(input('Digite outro número:'))
    print('O maior número é',num1 if num1 > num2 and num1 > num3 else num2 if num2 > num3 and num2 > num1 else num3)
    print('O menor número é',num1 if num1 < num2 and num1 < num3 else num2 if num2 < num3 and num2 < num1 else num3)
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")