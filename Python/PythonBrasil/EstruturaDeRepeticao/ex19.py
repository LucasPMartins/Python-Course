# 19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input('Digite quantos números serão utilizados:'))
numeros = list(range(n))
while True:
    try:
        menor, maior, soma = 0, 0, 0
        for i,num in enumerate(numeros):
            numeros[i] = int(input(f'Número {i+1}:'))
            if numeros[i] > 1000 or numeros[i] < 0:
                raise ValueError('Digite número entre 0 e 1000!')
            soma += numeros[i]
            maior = numeros[i] if numeros[i] > maior else maior
        print('Números digitados:',numeros)
        menor = numeros[0]
        for num in numeros:
            if num < menor:
                menor = num
        print(f'{menor=} ,{maior=} e {soma=}')
        break
    except Exception as e:
        print('Erro:',e)