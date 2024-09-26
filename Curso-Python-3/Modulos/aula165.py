# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime

from dateutil.relativedelta import relativedelta

data_inicio = datetime(2020,12,20)
delta_anos = relativedelta(years=5)
data_final = data_inicio + delta_anos
valor = 1_000_000

data_parcelas = []
data_parcela = data_inicio
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numeros_parcelas = len(data_parcelas)
print(f'Pagamento em {numeros_parcelas} parcelas:\n')
valor_parcelas = valor/numeros_parcelas
for i,data in enumerate(data_parcelas):
    print(f'{i+1:>3}x {data.strftime('%d/%m/%Y')}', \
          f'- R${valor_parcelas:.2f}')

print()
print(f'Você pegou R${valor:,.2f} para pagar em {delta_anos.years} anos ({numeros_parcelas} meses) ' \
      f'em parcelas de R${valor_parcelas:,.2f}')