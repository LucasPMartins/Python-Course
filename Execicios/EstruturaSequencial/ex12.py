#12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte 
# fórmula: (72.7*altura) - 58

while True:
    altura = input("Digite sua altura:")
    try:
        altura_float = float(altura)
        print(f'Seu peso ideial é {(72.7*altura_float) - 58}')
        break
    except Exception as e:
        print(e)