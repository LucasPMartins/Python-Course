# 8 - Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
# Por exemplo: 127 -> 721.

def reverso(numero):
    numero_list = list(str(numero))
    numero_list.reverse()
    return int(''.join(numero_list))

print(123,'->',reverso(123))