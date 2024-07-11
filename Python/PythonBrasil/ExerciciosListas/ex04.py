# 4 - Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes 
# foram lidas. Imprima as consoantes.

vetor = []
consoantes = []

for i in range(10):
    letra = input('Digite um letra:')
    vetor.append(letra)

for letra in vetor:
    if letra.lower() != 'a' and letra.lower() != 'e' and letra.lower() != 'i' and letra.lower() != 'o' and letra.lower() != 'u':
        consoantes.append(letra)

print(vetor)
print("Consoantes lidas:",len(consoantes))
print('Consoantes:',consoantes)

