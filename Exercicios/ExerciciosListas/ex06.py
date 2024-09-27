# 6 - Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
# a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

media = []
for i in range(10):
    num_media = 0.0
    for j in range(4):
        nota = float(input(f'Digite a nota do aluno {i+1}:'))
        num_media += nota
    media.append(num_media)
print('Alunos com média maior ou igual a 7.0:')
for i,aluno in enumerate(media):
    if media[i] >= 7.0:
        print(f'Aluno {i}: {media[i]}')