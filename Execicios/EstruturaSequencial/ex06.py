#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

while True:
    raio = input('Digite o raio do círculo:')
    try:
        raio_int = int(raio)
        area = (raio_int**2)*math.pi
        print(f'A área do círculo de raio {raio} é {area:.2f}')
        break
    except:
        print("Ocorreu um erro!")