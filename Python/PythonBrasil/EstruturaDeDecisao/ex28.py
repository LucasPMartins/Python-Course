# 28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne 
# da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for 
# feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um 
# cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, 
# tipo de pagamento, valor do desconto e valor a pagar.

print('                       Até 5 Kg           Acima de 5 Kg \n\
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg\n\
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg\n\
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')
tipo = input('Escolha um tipo de carne:').upper()
kg = float(input('Digite a quantidade de carne (em Kg):'))
pagamento = input('Forma de pagamento (Dinheiro ou Cartão):').upper()

if tipo == 'FILE DUPLO':
    if kg < 5:
        total = kg * 4.9
    else:
        total = kg * 5.8
elif tipo == 'ALCATRA':
    if kg < 5:
        total = kg * 5.9
    else:
        total = kg * 6.8
elif tipo == 'PICANHA':
    if kg < 5:
        total = kg * 6.9
    else:
        total = kg * 7.8

if pagamento == 'CARTÃO':
    desconto = total * 0.05
else:
    pagamento = 'DINHEIRO'

print('------============================------')
print('Cupom Fiscal:')
print(f'Tipo: {tipo}      Quantidade: {kg}Kg')
print(f'Preço Total: R$ {total:.2f}')
print(f'Tipo de pagamento: {pagamento}')
print(f'Valor do desconto: {desconto:.2f}    Valor a pagar: R${total-desconto:.2f}')
print('------============================------')


