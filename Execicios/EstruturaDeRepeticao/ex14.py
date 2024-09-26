# 14 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
# pares e a quantidade de números impares.

numeros = list(range(10))
while True:
    try:
        pares, impares = 0, 0
        for i,num in enumerate(numeros):
            numeros[i] = int(input(f'Número {i+1}:'))
            if numeros[i] % 2 == 0:
                pares += 1
            else:
                impares += 1
        print('Números digitados:',numeros)
        print(f'{pares=} e {impares=}')
        break
    except Exception as e:
        print('Erro:',e)