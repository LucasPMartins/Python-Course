# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

numeros = 1,2,3,4,5,6,7,8,9,10
r = multiplicao(*numeros)
print(r)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def par_impar(numero):
    try:
        if numero % 2 == 0:
            return "PAR"
        return "IMPAR"
    except:
        print("Não foi possivel realizar a operção!")

num = 8
r = par_impar(num)
print('O número',num,'é',r)