# 32 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
# usuário. Ex.: 5! = 5.4.3.2.1 = 120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input('Digite um número inteiro positivo:'))
if num == 0 or num == 1:
    print(1)
else:
    if num > 0:
        resultado = 1
        print(f'{num}! = ',end='')
        for i in reversed(range(1,num + 1)):
            resultado *= i
            print(f'{i}',end='')
            if i == 1:
                print(' = ',end='')
            else:
                print(' . ',end='')
        print(resultado)
    else:
        print('Erro: Digite uma valor valido!')