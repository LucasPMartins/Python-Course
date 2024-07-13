# 7 - Faça uma função que informe a quantidade de dígitos de um determinado número inteiro
# informado. 

def digitos(numero):
    num_str = str(numero)
    return len(num_str)

print(digitos(12232))