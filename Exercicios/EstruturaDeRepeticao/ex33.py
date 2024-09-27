# 33 - O Departamento Estadual de Meteorologia lhe contratou para desenvolver um 
# programa que leia as um conjunto indeterminado de temperaturas, e informe ao final
# a menor e a maior temperaturas informadas, bem como a média das temperaturas.

while True:
    print('Departamento Estadual de Meteorologia (S p/ Sair)')
    i = 0
    Media, Maior = 0.0, 0.0
    try:
        while True:
            i += 1
            valor = float(input(f'Temperatura {i}: '))
            if i == 1:
                Menor = valor
            Maior = valor if valor > Maior else Maior
            Menor = valor if valor < Menor else Menor
            Media += valor
    except Exception as e:
        print(f'Menor Temperatura: {Menor} e Maior Temperatura: {Maior}')
        print(f'Média das temperaturas: {Media/i}')
        break