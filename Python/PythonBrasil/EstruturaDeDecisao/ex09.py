# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

try:
    num1 = float(input('Digite um número:'))
    num2 = float(input('Digite outro número:'))
    num3 = float(input('Digite outro número:'))
    lista = [num1,num2,num3]
    lista.sort(reverse=True)
    print(lista)
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")