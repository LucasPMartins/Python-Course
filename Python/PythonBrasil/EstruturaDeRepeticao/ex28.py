# 28 - Faça um programa que calcule o valor total investido por um colecionador em
# sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar
# a quantidade de CDs e o valor para em cada um.

cd = int(input('Digite o número de cd:'))

media = 0
for i in range(cd):
    while True:
        valor = int(input(f'Turma {i+1}:'))
        if valor >= 0:
            media += valor
            break
print('Valor Total:',media)
print('O valor médio gasto em cada CD:',media/cd)