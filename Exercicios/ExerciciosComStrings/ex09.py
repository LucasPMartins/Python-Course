# 9 - Verificação de CPF. Desenvolva um programa que solicite a digitação de um número
# de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através
# da validação dos dígitos verificadores e dos caracteres de formatação.

cpf = input('Digite o CPF: ').replace('.','').replace('-','')
soma = 0
count = 10
for num in cpf[:9]:
    soma += count * int(num)
    count -= 1
resto = (soma*10) % 11
digito_1 = resto if resto <= 9 else 0 
soma = 0
count = 11
for num in cpf[:10]:
    soma += count * int(num)
    count -= 1
resto = (soma*10) % 11
digito_2 = resto if resto <= 9 else 0 
if digito_1 == int(cpf[9]) and digito_2 == int(cpf[10]):
    print('CPF Válido!')
else:
    print('CPF Inválido!')
