# 35 - Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista
# dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

lista = []

num = int(input('Digite um número: '))
for j in range(1, num + 1):
    count = 0
    for i in range(1,j + 1):
        if j%i == 0:
            count += 1
    if count <= 2:
        lista.append(j)
print(f'Lista de números primos entre 1 e {num}: ',lista)