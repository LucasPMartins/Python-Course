# 11 - Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
soma = 0
for num in range(num1,num2):
    soma += num
    print(num,end=' ')

print(f'\n{soma=}')