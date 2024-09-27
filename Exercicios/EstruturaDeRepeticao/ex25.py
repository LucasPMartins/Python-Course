# 25 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
# verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e 
# então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input('Digite um número:'))
media = 0
for i in range(n):
    Idade = float(input(f'Idade {i+1}:'))
    media += Idade

media = media/n
print('Media:',media,end='')
if media > 0 and media <= 25:
    print('Jovem')
elif media > 25 and media <= 60:
    print('Adulta')
else:
    print('Idose')
