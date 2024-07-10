# 45 - Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
# o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o
# gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por
# resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite
# o gabarito da prova antes dos alunos usarem o programa.

gabarito = ['A','B','C','D','E','E','D','C','B','A']
alunos = []
alunos_qtd = 0

possiveis_respostas = set('ABCDE')

for i,pergunta in enumerate(gabarito):
    gabarito[i] = input(f'Nova reposta da pergunta {i}:')

while True:
    try:
        acertos, i = 0, 0
        print(f'Escolha um resposta A, B, C, D e E. Aluno {alunos_qtd}:')
        while i < 10:
            resposta = input(f'Pergunta {i+1}:').upper()
            if resposta in possiveis_respostas:
                if resposta == gabarito[i]:
                    acertos += 1
                i += 1
            else:
                print('Resposta inválida!')
        alunos.append(acertos)
        alunos_qtd += 1
        repetir = input('Continuar? (S/ para SIM) R:').upper()
        if repetir != 'S':
            break
    except Exception as e:
        print(e)

# Maior e Menor Acerto;
maior, menor = (0,alunos[0]), (0,alunos[0])
media = 0
for i,aluno in enumerate(alunos):
    if alunos[i] > maior:
        maior = (i,alunos[i])
    if alunos[i] < menor:
        menor = (i,alunos[i])
    media += alunos[i]
print(f'O aluno com maior nota "{maior[1]}" é {maior[0]}')
print(f'O aluno com menor nota "{menor[1]}" é {menor[0]}')

print('Total de Alunos que utilizaram o sistema:',alunos_qtd)
print('A Média das Notas da Turma:',media/alunos_qtd)