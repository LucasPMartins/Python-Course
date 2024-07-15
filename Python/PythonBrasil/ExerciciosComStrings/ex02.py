# 2 - Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o
# seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente
# letras maiúsculas. 
# Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.

nome = input('Digites seu nome: ').upper()
lista = list(nome)
lista.reverse()
nome = ''.join(lista)
print('Seu nome ao contrário em maiúsculas:',nome)