# 7 - Faça um programa que leia 5 números e informe o maior número.

numeros = list(range(5))
while True:
    try:
        for i,num in enumerate(numeros):
            numeros[i] = int(input(f'Número {i+1}:'))
        print('Números digitados:',numeros)
        maior = 0
        for num in numeros:
            if num > maior:
                maior = num
        print('A maior número entre eles é',maior)
        break
    except Exception as e:
        print('Erro:',e)