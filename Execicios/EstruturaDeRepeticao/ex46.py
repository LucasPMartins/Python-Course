# 46 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
# O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa
# que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois
# informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o
# pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos.
# Os saltos são informados na ordem da execução, portanto não são ordenados. O programa 
# deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser 
# conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Melhor salto:  6.5 m
# Pior salto: 5.3 m
# Média dos demais saltos: 5.9 m

# Resultado final:
# Rodrigo Curvêllo: 5.9 m

while True:
    try:
        nome = input('Atleta:')
        if nome == '':
            break
        saltos = []
        saltos.append(float(input('Primeiro Salto:')))
        saltos.append(float(input('Segundo Salto:')))
        saltos.append(float(input('Terceiro Salto:')))
        saltos.append(float(input('Quarto Salto:')))
        saltos.append(float(input('Quinto Salto:')))
        print('')
        maior, menor = saltos[0], saltos[0] 
        media = 0.0
        for salto in saltos:
            if salto > maior:
                maior = salto
            if salto < menor:
                menor = salto
            media += salto
        media -= (maior + menor)
        print(f'Melhor salto: {maior:.2f} m')
        print(f'Pior salto: {menor:.2f} m')
        print(f'Média dos demais saltos: {media/3:.2f} m')
        print('Resultado final:')
        print(f'{nome}: {media/3:.2f} m')
    except Exception as e:
        print(e)