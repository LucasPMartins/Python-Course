# 15 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
# encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser
# armazenado). Após esta entrada de dados, faça: Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;
import os

notas = []

while True:
    try:
        nota = float(input('Digite sua nota:'))
        if nota == -1:
            break
        notas.append(nota)
    except Exception as e:
        print(e)
        os.system('pause')

print('Quantidade de valores lidos:',len(notas))
print('Valores informados:',*notas)
notas.reverse()
print('Valores informados na ordem reversa:')
for nota in notas:
    print(nota)

soma = sum(nota for nota in notas)
print('Soma:',soma)
print('Média:',soma/len(notas))
acima_media = list(filter(lambda nota: nota > soma/len(notas),notas))
print('Quantidade de valores acima da média:',len(acima_media))
abaixo_sete = list(filter(lambda nota: nota < 7,notas))
print('FIM')