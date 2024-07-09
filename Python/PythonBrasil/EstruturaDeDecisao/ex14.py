# 13 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
# sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for 
# A, B ou C ou “REPROVADO” se o conceito for D ou E.

try:
    nota1 = float(input('Digite a nota 1:'))
    nota2 = float(input('Digite a nota 2:'))
    media = (nota1 + nota2) / 2
    conceito = 'A' if media >= 9 and media <= 10 \
                else 'B' if media >= 7.5 and media < 9 \
                else 'C' if media >= 6 and media < 7.5 \
                else 'D' if media >= 4 and media < 6 \
                else 'E'
    print('O aluno foi','Aprovado' if media >= 6 else 'Reprovado')
    print(f'Com conceito {conceito} e média igual a {media}')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")

