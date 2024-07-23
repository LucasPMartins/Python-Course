"""
Iterando strings com while
"""
#       012345678910
# nome = 'Lucas Martins'  # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'

nome  = input('Digite seu nome:')
tamanho =  len(nome)
count = 0
novo_nome = ''
while count < tamanho:
    letra = nome[count]
    novo_nome += f'*{letra}'
    count += 1
    if count == tamanho:
        novo_nome += '*'
print(novo_nome)

    # print(f'*{nome[count]}',end='')
    # count += 1
    # if count == tamanho:
    #     print("*")
