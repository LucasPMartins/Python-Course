# 12 - Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
# quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

vetor = []
media = 0.0
for i in range(30):
    altura = float(input('Digite sua altura:'))
    idade = float(input('Digite sua idade:'))
    aluno = (altura,idade)
    vetor.append(aluno)
    media += altura

media /= 30
count = 0
for aluno in vetor:
    if aluno[1] > 13 and aluno[0] < media:
        count += 1
print('Média:',media)
print(f'Quantidade de alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos: {count}')