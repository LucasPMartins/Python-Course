# 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
# valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    try:
        num = int(input('Digite uma nota entre 0 e 10:'))
        if num < 0 or num > 10:
            print('Valor inválido, digite novamente!')
        else:
            break
    except Exception as e:
        print("Erro:",e)