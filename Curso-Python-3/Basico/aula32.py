"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número inteiro: ')
if entrada.isdigit():
    num = int(entrada)
    if (num % 2) == 0 :
        print("O número digitado é par!")
    else :
        print("O número digitado é ímpar!")
else :
    print('O valor digitado não é um número inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Quantas horas são? \nR:')
if entrada.isdigit():
    num = int(entrada)
    dia = num >= 0 and num <= 11
    tarde = num >= 12 and num <=17
    noite = num >= 18 and num <= 23
    if dia :
        print("Bom Dia!")
    elif tarde :
        print("Boa Tarde!")
    elif noite:
        print("Boa Noite!")
    else:
        print("Hora inválida!")
else : 
    print('O valor digitado não é um número inteiro')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
entrada = input("Digite seu nome:")
tamanho = len(entrada)

if entrada == '' or entrada.isalnum():
    print("Seu nome é invalido")
else :
    if tamanho <= 4 :
        print('Seu nome é curto!')
    elif tamanho <= 6 :
        print('Seu nome é normal')
    else :
        print("Seu nome é muito grande!")
