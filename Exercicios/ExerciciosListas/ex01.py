# 1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []

for i in range(5):
    num = int(input('Digite um número:'))
    vetor.append(num)

print(vetor)