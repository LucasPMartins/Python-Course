# 15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo.

n = int(input('Digite um número:'))
print(f'Série de Fibonacci até o {n}-ésimo termo:')
if n != 1 and n != 2 and n > 0:
    fibo = [1,1]
    count = 0
    for i,num in enumerate(fibo):
        fibo.append(fibo[i+1] + fibo[i])
        count += 1
        if count == n - 2:
            break
    print(fibo) 
else:
    if n == 1 or n == 2:
        print(1)        
    else:
        print('Valor inválido')

def fibonacci(n):
    # Lista para armazenar a série de Fibonacci
    fibo = [1, 1]

    # Se n for 1 ou 2, retornar diretamente os elementos correspondentes
    if n == 1:
        return [1]
    elif n == 2:
        return fibo

    # Gerar os termos da série de Fibonacci até o n-ésimo termo
    for i in range(2, n):
        fibo.append(fibo[i-1] + fibo[i-2])

    return fibo
