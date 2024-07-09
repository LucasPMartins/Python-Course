# 20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o 
# fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

while True:
    try:
        num = int(input('Digite um número inteiro positivo (-1 para Sair):'))
        if num == -1:
            break
        if num > 16 or num < 0:
            raise ValueError('Digite números inteiros positivos e menores que 16')
        else:
            resultado = 1
            print(f'{num}! = ',end='')
            for i in reversed(range(1,num + 1)):
                resultado *= i
                print(f'{i}',end='')
                if i == 1:
                    print(' = ',end='')
                else:
                    print('.',end='')
        print(resultado)
    except Exception as e:
        print(e)