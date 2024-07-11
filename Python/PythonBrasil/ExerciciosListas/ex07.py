# 7 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação
# e os números.

vetor = [1,2,3,4,5]

soma = 0
multiplicacao = 1
for numero in vetor:
    soma += numero
    multiplicacao *= numero

print('Vetor:',vetor)
print('Soma =',soma)
print('Multiplicação =',multiplicacao)