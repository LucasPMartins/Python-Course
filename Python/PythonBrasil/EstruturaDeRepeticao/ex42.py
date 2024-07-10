# 42 - Faça um programa que leia uma quantidade indeterminada de números positivos
# e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e
# [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

intervalos = {'[0-25]': 0,\
              '[26-50]': 0,\
              '[51-75]': 0,\
              '[76-100]': 0}

while True:
    try:
        num = int(input('Digite um número inteiro entre 0 e 100 (-1 para Sair):'))
        if num == -1:
            break
        if num >= 0 and num <= 100:
            if num >= 0 and num <= 25:
                intervalos['[0-25]'] += 1
            elif num >= 26 and num <= 50:
                intervalos['[26-50]'] += 1
            elif num >= 51 and num <= 75:
                intervalos['[51-75]'] += 1
            else:
                intervalos['[76-100]'] += 1
        else:
            raise ValueError('Digite um número válido!')
    except Exception as e:
        print(e)

print(intervalos)