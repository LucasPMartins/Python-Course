# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que
# João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

while True:
    peso = input("Digite o peso do peixe: ")
    try:
        peso_float = float(peso)
        if peso_float <= 50:
            print('Não é necessário pagar multa, peso está de acordo com regulamento de pesca do estado de São Paulo')
        else:
            excesso = peso_float - 50
            multa = 4 * excesso
            print(f'Multa por excesso de peso. Excesso = {excesso:.2}KG, Multa = R${multa:.2f}')
        break
    except Exception as e:
        print(e)