# 3 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

vetor = []
media = 0.0
for i in range(4):
    num = float(input('Digite uma nota:'))
    vetor.append(num)
    media += num

print(vetor)
print('Média:',media/4)