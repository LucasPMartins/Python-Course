# 11 - Embaralha palavra. Construa uma função que receba uma string como parâmetro
# e devolva outra string com os carateres embaralhados. Por exemplo: se função receber
# a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
# de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em
# caixa alta ou caixa baixa, independentemente de como foram digitados.
import random

def embaralha(palavra):
    i = 0
    lista = list(palavra)
    trocados = set()
    while i < len(lista):
        num_aleatorio = random.randint(0,len(lista) - 1)
        if num_aleatorio in trocados:
            continue
        trocados.add(num_aleatorio)
        temp = lista[num_aleatorio]
        lista[num_aleatorio] = lista[i]
        lista[i] = temp
        i += 2
    return ''.join(lista)

palavra = 'Python'
print(palavra,'=',embaralha(palavra))