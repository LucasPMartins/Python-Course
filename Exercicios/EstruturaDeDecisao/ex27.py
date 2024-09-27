# 27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
# (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morangos = float(input('Digite quantos KG de morangos: '))
macas = float(input('Digite quantos KG de maçãs: '))

if morangos <= 5:
    total = morangos * 2.5
else:
    total = morangos * 2.2
if macas <= 5:
    total += macas * 1.8
else:
    total += macas * 1.5

if total > 25 or (morangos + macas) > 8:
    total -= total * 0.25

print(f'Total a pagar: R${total:.2}')
 


