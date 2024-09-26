import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0,9))

count = 10
resultado = 0
for digito_1 in cpf[:9]:
    resultado += int(digito_1) * count
    count -= 1
resultado = (resultado * 10) % 11
digito_1 = resultado if resultado <= 9 else 0 
cpf += str(digito_1)

count = 11
resultado = 0
for digito_2 in cpf[:10]:
    resultado += int(digito_2) * count
    count -= 1
resultado = (resultado * 10) % 11
digito_2 = resultado if resultado <= 9 else 0 

cpf += str(digito_2)

print("----======= GERADOR DE CPF's =======----\n")

print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\n")

