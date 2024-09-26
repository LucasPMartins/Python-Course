# 10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = set('mnv')

try:
    letra = input('Em qual turno você estuda?(M-matutino ou V-Vespertino ou N-Noturno)\nR:').lower()
    if letra in turno:
        if letra == 'm':
            print('Bom Dia!')
        elif letra == 'v':
            print("Boa Tarde!")
        else:
            print('Boa Noite!')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")

