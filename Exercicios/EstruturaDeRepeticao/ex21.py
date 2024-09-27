# 21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número
# primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um número inteiro:'))
count = 0
for i in range(1,num + 1):
    if num%i == 0:
        count += 1
if count > 2:
    print('Não é primo')
else:
    print('É primo')