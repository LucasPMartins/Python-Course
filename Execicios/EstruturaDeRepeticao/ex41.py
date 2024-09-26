# 41 -Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
# seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor
# da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

divida = float(input('Valor de uma dívida: R$'))
print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
print(f'R${divida:.2f}\t0%\t\t1\t\t\tR${divida:.2f}')
juros = 10
for parcelas in range(1,13):
    if parcelas%3 == 0:
        nova_divida = divida*(1+(juros/100))
        print(f'R${nova_divida:.2f}\t{juros}%\t\t{parcelas}\t\t\tR${nova_divida/parcelas:.2f}')
        juros += 5
