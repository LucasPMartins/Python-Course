# 7 - Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário
# (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.

frase = input('Digite uma fras: ').lower()
espacos = frase.count(' ')
vogais = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u') 
print('A frase tem:',espacos,'espaços')
print('A frase tem:',vogais,'vogais')