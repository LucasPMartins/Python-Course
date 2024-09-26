#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

while True:
    C = input('Digite a temperatura em graus Celsius:')
    try:
        C_int = int(C)
        F = C_int * (9/5) + 32
        print(f'A temperatura em graus Celsius {C} é {F:.2f} em graus Fahrenheit')
        break
    except:
        print('Ocorreu um erro!')