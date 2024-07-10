# 48 - Faça um programa que peça um numero inteiro positivo e em seguida mostre este
# numero invertido.
# Exemplo:
#   12376489
#   => 98467321

while True:
    try:
        lista = list(input('Digite um número inteiro positivo:'))
        lista.reverse()
        num = int(''.join(lista))
        print('Inverso:',num)
    except Exception as e:
        print(e)