# 8 - Faça um programa que leia 5 números e informe a soma e a média dos números.


numeros = list(range(5))
while True:
    try:
        soma, media = 0, 0
        for i,num in enumerate(numeros):
            numeros[i] = int(input(f'Número {i+1}:'))
            soma += numeros[i]
        print('Números digitados:',numeros)
        media = soma/5
        print(f'{soma=} e {media=}')
        break
    except Exception as e:
        print('Erro:',e)