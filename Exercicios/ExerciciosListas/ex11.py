# 11 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor_A = [1,2,3,4,5,6,7,8,9,10]
vetor_B = [1,2,3,4,5,6,7,8,9,10]
vetor_C = [1,2,3,4,5,6,7,8,9,10]
vetor = []

count = 0
for num in vetor_A:
    vetor.append(num)
    vetor.append(vetor_B[count])
    vetor.append(vetor_C[count])
    count += 1

print(vetor_A)
print(vetor_B)
print(vetor_C)
print(vetor)