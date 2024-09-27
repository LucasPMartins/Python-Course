# 17 - Faça um Programa que peça um número correspondente a um determinado ano e 
# em seguida informe se este ano é ou não bissexto.

try:
    ano = int(input('Digite um ano:'))
    if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
        print('É um ano bissexto')
    else:
        print('Não é bissexto')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")


