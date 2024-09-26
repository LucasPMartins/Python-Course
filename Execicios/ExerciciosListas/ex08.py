# 8 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação
# no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

vetor = []

for i in range(5):
    altura = float(input('Digite sua altura:'))
    idade = float(input('Digite sua idade:'))
    pessoa = (altura,idade)
    vetor.append(pessoa)

vetor.reverse()
print(vetor)
