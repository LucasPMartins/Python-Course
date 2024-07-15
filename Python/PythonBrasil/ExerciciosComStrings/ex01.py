# 1 - Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas
# seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento
# e são iguais ou diferentes no conteúdo.
# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
print('Compara duas strings')
str1 = input('String 1: ')
str2 = input('String 2: ')
print(f'Tamanho de "{str1}": {len(str1)} caracteres')
print(f'Tamanho de "{str2}": {len(str2)} caracteres')
if len(str1) - len(str2) != 0:
    print('As duas strings são de tamanhos diferentes.')
else:
    print('As duas strings são de tamanhos iguais.')
if str1 == str2:
    print('As duas strings possuem conteúdo igual.')
else:
    print('As duas strings possuem conteúdo diferente.')