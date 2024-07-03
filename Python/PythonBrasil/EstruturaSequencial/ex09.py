#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

while True:
    f = input('Digite a temperatura em graus Fahrenheit:')
    try:
        f_int = int(f)
        C = 5 * ((f_int-32) / 9)
        print(f'A temperatura em graus Fahrenheit {f} é {C:.2f} em graus Celsius')
        break
    except:
        print('Ocorreu um erro!')