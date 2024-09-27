# 6 - Faça um programa que use a função valorPagamento para determinar o valor a ser pago
# por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação
# e o número de dias em atraso e passar estes valores para a função valorPagamento, que
# calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
# O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa
# deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado
# um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado,
# exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações
# pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos
# sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa,
# mais 0,1% de juros por dia de atraso.

relatorio = {'Quantidade':0,'Valor total de Prestações':0.0}

def valorPagamento(valor,dias):
    if dias == 0:
        return valor
    return (valor * 0.03) + (valor * (0.001 * dias)) + valor

def main():
    while True:
        try:
            valor = float(input('Digite o valor da prestação (0=fim): R$'))
            if valor == 0:
                break
            dias = int(input('Digite número de dias em atraso: '))
            if dias < 0:
                raise ValueError()
            novo_valor = valorPagamento(valor,dias)
            relatorio['Quantidade'] += 1
            relatorio['Valor total de Prestações'] += novo_valor
            print('O valor a ser pago é R$',novo_valor)
        except ValueError:
            print("Entrada inválida. Digite 0 para Sair.")

if __name__ == '__main__':
    main()
    print('Relatório:',relatorio)