# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def verifica_num(numero):
    if numero.isnumeric():
        return True
    else:
        return False

soma = 0
i = 0
while i < 4:
    num = input(f"Nota {i+1}:")
    if not verifica_num(num):
        print("Digite uma nota válida!")
        continue
    soma += int(num)
    i += 1

print(f"A média das notas é {soma/4}")

