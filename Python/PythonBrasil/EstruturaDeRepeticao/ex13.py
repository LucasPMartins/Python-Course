# 13 - Faça um programa que peça dois números, base e expoente, calcule e mostre o
# primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input('Digite a base:'))
expoente = int(input('Digite o expoente:'))

count = expoente
if count != 0 and count != 1:
    resultado = base*base
    count -= 2
else:
    if count == 0:
        resultado = 1
    else:
        resultado = base
    count -= 1
while count > 0:
    resultado *= base
    count -= 1

print(f'{base}^{expoente} =',resultado)