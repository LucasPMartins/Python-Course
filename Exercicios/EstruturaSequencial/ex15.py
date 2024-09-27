# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#         a. salário bruto.
#         b. quanto pagou ao INSS.
#         c. quanto pagou ao sindicato.
#         d. o salário líquido.
#         e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#             + Salário Bruto : R$
#             - IR (11%) : R$
#             - INSS (8%) : R$
#             - Sindicato ( 5%) : R$
#             = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

while True:
    grana_hora = input('Quanto você ganha por hora? \nR:')
    horas_trabalhadas = input('Quantas horas trabalhadas no mês? \nR:')
    try:
        grana_hora_int = int(grana_hora)
        horas_trabalhadas_int = int(horas_trabalhadas)
        salario = grana_hora_int*horas_trabalhadas_int
        imposto = 0.11*salario
        inss = 0.08*salario
        sindicato = 0.05*salario
        print(f"O seu Salário Bruto referente a esse mês é {salario}")
        print(f'Você pagou R${imposto:.2f} de Imposto de Renda')
        print(f'Você pagou R${inss:.2f} ao INSS')
        print(f'Você pagou R${sindicato:.2d} ao sindicato.')
        print(f'O seu Salário Liquido referente a esse mês é {salario - imposto - inss - sindicato}')
        break
    except Exception as e:
        print(f"\nOcorreu um erro!\n Erro:{e}\n")