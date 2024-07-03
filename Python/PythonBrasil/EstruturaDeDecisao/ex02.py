# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
try:
    num = float(input('Digite um valor:'))
    print('O número é','positivo' if num >= 0 else 'negativo')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")