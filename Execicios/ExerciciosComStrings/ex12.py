# 12 - Valida e corrige número de telefone. Faça um programa que leia um número de telefone,
# e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente.
# O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

print('Valida e corrige número de telefone')
telefone = input('Telefone:').replace('-','')
if len(telefone) < 8:
    novo_telefone = '3'*(8 - len(telefone))
    novo_telefone += telefone
    print(f'Telefone possui {len(telefone)} dígitos. Vou acrescentar o digito três na frente.')
print('Telefone corrigido sem formatação:',novo_telefone)
print('Telefone corrigido com formatação:',f'{novo_telefone[:4]}-{novo_telefone[4:]}')