# 50 - Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
# Faça um programa que calcule o valor de H com N termos.

n = int(input('N:'))
H = 0
print('H = ',end='')
for i in range(1,n+1):
    if i == n:
        print(f'1/{i}')
        break
    if i == 1:
        print('1 + ',end='')
    else:
        print(f'1/{i} + ',end='')
    H += 1/i

print('H =',round(H,2))