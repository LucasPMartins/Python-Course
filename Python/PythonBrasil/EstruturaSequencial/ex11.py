# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

while True:
    num_1 = input("Digite um número inteiro:")
    num_2 = input("Digite outro número inteiro:")
    num_3 = input("Digite um número real:")
    try:
        num_1_int = int(num_1)
        num_2_int = int(num_2)
        num_3_float = float(num_3)
        print(f'O produto do dobro do primeiro com metade do segundo é {(2*num_1_int)*(num_2_int/2)}')
        print(f'A soma do triplo do primeiro com o terceiro é {3*num_1_int + num_3_float}')
        print(f'O terceiro elevado ao cubo é {(num_3_float**3):.2f}')
        break
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")