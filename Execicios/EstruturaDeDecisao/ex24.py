# 24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação
# ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga 
# se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal.

num1 = float(input('Digite um valor:'))
num2 = float(input('Digite um outro valor:'))
operacao = input('Escolha um operção: soma,subtração,muliplicação e divisão\nR:')
if operacao == 'soma':
    r = num1 + num2
    print(f'{num1} + {num2} = {r}','Par,' if r%2 == 0 else 'Impar,','Postivo e' if r > 0 else 'Negativo e','Inteiro' if round(r) == r else 'Decimal')
elif operacao == 'subtração':
    r = num1 - num2
    print(f'{num1} - {num2} = {r}','Par,' if r%2 == 0 else 'Impar,','Postivo e' if r > 0 else 'Negativo e','Inteiro' if round(r) == r else 'Decimal')
elif operacao == 'multiplicação':
    r = num1 * num2
    print(f'{num1} * {num2} = {r}','Par,' if r%2 == 0 else 'Impar,','Postivo e' if r > 0 else 'Negativo e','Inteiro' if round(r) == r else 'Decimal')
elif operacao == 'divisão':
    r = num1 / num2
    print(f'{num1} / {num2} = {r}','Par,' if r%2 == 0 else 'Impar,','Postivo e' if r > 0 else 'Negativo e','Inteiro' if round(r) == r else 'Decimal')
else:
    print('Operação Inválida!')