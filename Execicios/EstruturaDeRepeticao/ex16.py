# 16 - A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

print(f'Série de Fibonacci até que o valor seja maior que 500:')
fibo = [1,1]
for i in range(2,500) :
    fibo.append(fibo[i-1] + fibo[i-2])
    if fibo[i] > 500:
        break
print(fibo) 