# 24 - Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
# armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi
# conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros
# aleatórios, simulando os lançamentos dos dados.

import random

vetor = [0] * 6

for i in range(100):
    num = random.randint(1,6)
    vetor[num-1] += 1

for i,vezes in enumerate(vetor):
    print(f'Lado {i+1}: {vezes} vezes')
