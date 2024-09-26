# 49 - Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
# Imprima no final a soma da série.

n = int(input('N:'))
m = 1
s = 0
print('S = ',end='')
for i in range(1,n+1):
    if i == n:
        print(f'{i}/{m}')
        break
    print(f'{i}/{m} + ',end='')
    s += i/m
    m += 2
print('S =',round(s,2))