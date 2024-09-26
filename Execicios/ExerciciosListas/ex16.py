# 16 - Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
# vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento
# de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas
# de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
# Escreva um programa (usando um array de contadores) que determine quantos vendedores
# receberam salários nos seguintes intervalos de valores:
# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
# Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem 
# fazer vários ifs aninhados.
import os

contadores = [0] * 9
lista_intervalos = ['$200 - $299', '$300 - $399','$400 - $499','$500 - $599',
'$600 - $699','$700 - $799','$800 - $899','$900 - $999','$1000 em diante']

while True:
    try:
        vendas = float(input('Digite suas vendas brutas (-1 para Sair):'))
        if vendas == -1:
            break
        vendas *= 0.09
        salario = 200 + vendas
        intervalo = int((salario//100) - 2)
        if salario >= 1000:
            contadores[8] += 1
            intervalo = 8
        else:
            contadores[intervalo] += 1
        print('Intervalo:',lista_intervalos[intervalo])
    except Exception as e:
        print(e)
        os.system('pause')

for i,num in enumerate(contadores):
    print(f'{lista_intervalos[i]}: {num}')