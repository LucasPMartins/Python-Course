#Faça um Programa que peça dois números e imprima a soma.
while True:
    num1 = input("Digite um número:")
    if num1.isdecimal():
        break
    else:
        print("Digite um valor válido!")

while True:
    num2 = input("Digite outro número:")
    if num2.isdecimal():
        break
    else:
        print("Digite um valor válido!")

print(f"A soma de {num1} e {num2} é {int(num1) + int(num2)}")