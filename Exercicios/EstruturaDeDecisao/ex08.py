# 8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é 
# sempre pelo mais barato.

try:
    num1 = float(input('Digite o preço do produto 1:'))
    num2 = float(input('Digite o preço do produto 2:'))
    num3 = float(input('Digite o preço do produto 3:'))
    print('Você deve comprar o produto',f'1 - R${num1:.2f}' if num1 < num2 and num1 < num3 
                                    else f'2 - R${num2:.2f}' if num2 < num3 and num2 < num1 
                                    else f'3 - R${num3:.2f}')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")