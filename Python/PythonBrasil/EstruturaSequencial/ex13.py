# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#         Para homens: (72.7*h) - 58
#         Para mulheres: (62.1*h) - 44.7

while True:
    sexo = input('Qual o seu sexo:(M p/ Mulher e H p/Homem)').upper()
    h = input("Digite sua altura:")
    try:
        h_float = float(h)
        if(sexo == 'H'):
            print(f'Seu peso ideial é {(72.7*h_float) - 58:.2f}')
        elif sexo == 'M':
            print(f'Seu peso ideial é {(62.1*h_float) - 44.7:.2f}')
        else:
            raise ValueError('Digite um sexo válido!')
        break
    except Exception as e:
        print(e)
