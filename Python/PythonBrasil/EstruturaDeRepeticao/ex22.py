# 22 - Altere o programa de cálculo dos números primos, informando, caso o número 
# não seja primo, por quais número ele é divisível.

num = int(input('Digite um número inteiro:'))
count = 0
print('Divisível por: ')
for i in range(1,num + 1):
    if num%i == 0:
        print(i,end=' ')
        count += 1
if count > 2:
    print('\nNão é primo')
else:
    print('\nÉ primo')