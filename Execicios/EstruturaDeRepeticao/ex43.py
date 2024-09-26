# 43 - O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral
# do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

cardapio = [{'nome': 'Cachorro Quente', 'codigo': 100 , 'preco': 1.20},\
            {'nome': 'Bauru Simples', 'codigo': 101, 'preco':1.30},\
            {'nome': 'Bauru com ovo', 'codigo': 102, 'preco': 1.50},\
            {'nome': 'Hambúrguer', 'codigo': 103, 'preco':1.20},\
            {'nome': 'Cheeseburguer', 'codigo': 104, 'preco': 1.30},\
            {'nome': 'Refrigerante', 'codigo': 105, 'preco': 1.00}]

print('  ----==== CARDÁPIO ====----')
print(' Especificação   Código  Preço')
for item in cardapio:
    print(f'{item['nome']}\t  {item['codigo']}\t  {item['preco']}')
print('(0 para Sair)')
total = 0.0

while True:
    try:
        codigo = int(input('Digite o código do produto:'))
        if codigo == 0:
            break
        qtd = int(input('Digite a quantidade:'))
        for produto in cardapio:
            if produto['codigo'] == codigo:
                preco = produto['preco'] * qtd
                print('Preço do pedido: R$',round(preco,2))
                total += preco
    except Exception as e:
        print(e)

print('Total a pagar: R$',total)