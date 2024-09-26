# 5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas
# de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    try:
        A = int(input('População de A:'))
        B = int(input('População de B:'))
        taxaA = float(input('Taxa de crescimento de A:'))
        if round(taxaA) == taxaA: 
            taxaA = taxaA/100
        taxaB = float(input('Taxa de crescimento de B:'))
        if round(taxaB) == taxaB:
            taxaB = taxaB/100
        count = 0
        while A < B:
            A += A * taxaA
            B += B * taxaB
            count += 1
        print(f'Será necessários {count} anos pra que o pais A ultrapasse ou iguale a população do país B,\
            ',f'{B=:.0f}',f'{A=:.0f}')
    except Exception as e:
        print('Erro:',e)