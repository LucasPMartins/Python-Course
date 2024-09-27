# 5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por 
# aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

try:
    nota1 = float(input('Digite a nota 1:'))
    nota2 = float(input('Digite a nota 2:'))
    media = (nota1 + nota2) / 2
    print('O aluno foi','Aprovado com Distinção' if media == 10 else 'Aprovado' if media >= 7 else 'Reprovado')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")