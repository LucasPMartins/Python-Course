# 10 - Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
# vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados
# dos dois outros vetores

vetor_A = [1,2,3,4,5,6,7,8,9,10]
vetor_B = [1,2,3,4,5,6,7,8,9,10]
vetor_C = []

count = 0
for num in vetor_A:
    vetor_C.append(num)
    vetor_C.append(vetor_B[count])
    count += 1

print(vetor_A)
print(vetor_B)
print(vetor_C)