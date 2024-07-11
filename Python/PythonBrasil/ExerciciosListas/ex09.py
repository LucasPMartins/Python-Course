# 9 - Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
# a soma dos quadrados dos elementos do vetor.

vetor_A = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for num in vetor_A:
    soma += num**2

print('Soma dos quadrados dos elementos do vetor:',soma)