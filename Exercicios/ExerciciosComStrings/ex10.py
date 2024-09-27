# 10 - Número por extenso. Escreva um programa que solicite ao usuário a digitação
# de um número até 99 e imprima-o na tela por extenso.

unidade = ['um','dois','três','quatro','cinco','seis','sete','oito','nove','dez']
excecao = ['onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezena = ['vinte','trita','quarenta','cinquenta','sessenta','setenta','oitenta','noventa']
while True:
    try:
        num = int(input('Digite um número entre 1 e 99 (0=fim): '))
        if num == 0:
            break
        if 1 <= num <= 10:
            print(num,'por extenso:',unidade[num-1])
        elif 11 <= num <= 19:
            print(num,'por extenso:',excecao[num-11])
        elif 20 <= num <= 99:
            print(num,'por extenso:',dezena[num//10 - 2],f'e {unidade[num%10 - 1]}' if num % 10 != 0 else '')
    except ValueError:
        print('Digite um valor válido!')