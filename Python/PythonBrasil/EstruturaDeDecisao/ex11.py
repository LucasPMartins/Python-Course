# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o 
# programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

try:
    salario = float(input('Digite seu sálario: R$'))
    (percentual,valor) = (0.2,salario * 0.2) if salario <= 280 \
        else (0.15,salario * 0.15) if salario > 280 and salario <= 700 \
            else (0.1,salario * 0.1) if salario > 700 and salario < 1500 \
                else (0.05,salario * 0.05)
    novo_salario = salario + valor
    print(f'Salário antes do reajuste: R$',salario)
    print(f'Percentual de aumento aplicado: {percentual*100}%')
    print(f'O valor aumentado: R${valor}')
    print(f'O novo salário, após o aumento: R${novo_salario}')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")