# 5 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene
# os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

par = []
impar = []
vetor = []

for i in range(20):
    num = int(input('Digite um número:'))
    if num%2 == 0:
        par.append(num)
    else:
        impar.append(num)
    vetor.append(num)

print('Vetor =',vetor)
print('Par =',par)
print('Impar =',impar)