# 44 - Em uma eleição presidencial existem quatro candidatos. Os votos são informados
# por meio de código. Os códigos utilizados são: 1 , 2, 3, 4  - Votos para os respectivos 
# candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. 
# Para finalizar o conjunto de votos tem-se o valor zero.

import os

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
voto_nulo = 0
voto_branco = 0

while True:
    try:
        os.system('cls')
        print('1 - João')
        print('2 - José')
        print('3 - Ricardo')
        print('4 - Pedro')
        print('5 - Voto Nulo')
        print('6 - Voto em Branco')
        voto = int(input('Escolha seu voto (-1 para Sair):'))
        if voto == -1:
            break
        else:
            if voto == 1:
                candidato_1 += 1
            elif voto == 2:
                candidato_2 += 1
            elif voto == 3:
                candidato_3 += 1
            elif voto == 4:
                candidato_4 += 1
            elif voto == 5:
                voto_nulo += 1
            elif voto == 6:
                voto_branco += 1
            else:
                print('voto inválido!')
    except Exception as e:
        print(e)
total = candidato_1 + candidato_2 + candidato_3 + candidato_4 + voto_branco + voto_nulo
print('O total de votos para cada candidato:')
print('1 - João:',candidato_1)
print('2 - José:',candidato_2)
print('3 - Ricardo:', candidato_3)
print('4 - Pedro:', candidato_4)
print('O total de votos nulos:',voto_nulo)
print('O total de votos em branco:',voto_branco)
print('A percentagem de votos nulos sobre o total de votos:',round(total/voto_nulo,2))
print('A percentagem de votos em branco sobre o total de votos:',round(total/voto_branco,2)) 
print('O conjunto de votos tem-se o valor zero:')
if candidato_1 == 0:
    print('João',end='- ')
if candidato_2 == 0:
    print('José',end='- ')
if candidato_3 == 0:
    print('Ricardo',end='- ')
if candidato_4 == 0:
    print('Pedro',end='- ')
if voto_nulo == 0:
    print('Voto nulo',end='- ')
if voto_branco == 0:
    print('Voto em branco')