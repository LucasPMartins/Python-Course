# 24 - Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input('Digite um número:'))
media = 0
for i in range(n):
    nota = float(input(f'Nota {i+1}:'))
    media += nota

media = media/n
print('Media:',media)