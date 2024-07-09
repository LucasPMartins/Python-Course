# 27 - Faça um programa que calcule o número médio de alunos por turma. Para isto,
# peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas
# não podem ter mais de 40 alunos.

turmas = int(input('Digite o número de turmas:'))

media = 0
for i in range(turmas):
    while True:
        alunos = int(input(f'Turma {i+1}:'))
        if alunos <= 40:
            media += alunos
            break

print('A média de alunos por turma é:',media/turmas)