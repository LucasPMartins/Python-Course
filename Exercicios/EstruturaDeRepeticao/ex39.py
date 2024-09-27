# 39 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando
# o número do aluno e o segundo representando a sua altura em centímetros. Encontre o 
# aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno 
# mais baixo, junto com suas alturas.
alunos = []

for i in range(10):
    num = int(input(f'Digite o número do aluno {i+1}:'))
    altura = float(input('Digite a altura dele:'))
    aluno = (num,altura)
    alunos.append(aluno)

aluno_alto = alunos[0]
aluno_baixo = alunos[0]

for i in alunos:
    if i[1] > aluno_alto[1]:
        aluno_alto = i
    if i[1] < aluno_baixo[1]:
        aluno_baixo = i

print('Aluno mais alto:',aluno_alto)
print('Aluno mais baixo:',aluno_baixo)