# 23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número 
# inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões
# que ele executou para encontrar os números primos. Serão avaliados o funcionamento,
# o estilo e o número de testes (divisões) executados.

n = int(input('Digite um número:'))
divisoes = 0
for i in range(1,n + 1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            divisoes += 1
            count += 1
    if count <= 2:
        print(i,'é primo')

print('Divisões:',divisoes)
