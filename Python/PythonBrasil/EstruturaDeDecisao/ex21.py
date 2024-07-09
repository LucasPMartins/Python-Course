# 21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário
# a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais
# e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas 
# existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

def retorna_extenso(numero):
    if numero == 1:
        return 'uma'
    elif numero == 2:
        return  'duas'
    elif numero == 3:
        return 'três'
    elif numero == 4:
        return 'quatro'
    elif numero == 5:
        return 'cinco'
    elif numero == 6:
        return 'seis'
    elif numero == 7:
        return 'sete'
    elif numero == 8:
        return 'oito'
    elif numero == 9:
        return 'nove'
    else:
        raise ValueError('Out of Range')

while True:
    try:
        valor = float(input('Valor do saque: R$'))
        if valor > 10 and valor <= 600:
            centena = valor//100
            cinquenta = (valor%100)//50
            dez = ((valor%100) - cinquenta*50)//10
            cinco = (valor%10)//5
            um = ((valor%10) - cinco*5)
            if centena > 0:
                print(retorna_extenso(centena),'nota' if centena == 1 else 'notas', 'de 100')
            if cinquenta > 0:
                print(retorna_extenso(cinquenta),'nota' if cinquenta == 1 else 'notas', 'de 50')
            if dez > 0:
                print(retorna_extenso(dez),'nota' if dez == 1 else 'notas', 'de 10')
            if cinco > 0:
                print(retorna_extenso(cinco),'nota' if cinco == 1 else 'notas', 'de 5')
            if um > 0:
                print(retorna_extenso(um),'nota' if um == 1 else 'notas', 'de 1')
    except Exception as e:
        print(f"\nOcorreu um erro!\n Erro:{e}\n")
