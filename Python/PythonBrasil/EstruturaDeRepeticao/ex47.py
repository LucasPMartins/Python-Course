# 47 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados
# alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a
# descrição acima informada (retirar o melhor e o pior salto e depois calcular a média
# com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída 
# do programa deve ser conforme o exemplo abaixo:
# Atleta: Aparecido Parente
# Nota: 9.9
# Nota: 7.5
# Nota: 9.5
# Nota: 8.5
# Nota: 9.0
# Nota: 8.5
# Nota: 9.7

# Resultado final:
# Atleta: Aparecido Parente
# Melhor nota: 9.9
# Pior nota: 7.5
# Média: 9,04

while True:
    try:
        nome = input('Atleta:')
        if nome == '':
            break
        votos = []
        for i in range(7):
            voto = float(input('Nota:'))
            votos.append(voto)
        print('')
        maior, menor = votos[0], votos[0] 
        media = 0.0
        for voto in votos:
            if voto > maior:
                maior = voto
            if voto < menor:
                menor = voto
            media += voto
        media -= (maior + menor)
        print('Resultado final:')
        print(f'Atleta: {nome}')
        print(f'Melhor nota:: {maior:.1f}')
        print(f'Pior nota: {menor:.1f}')
        print(f'Média: {media/5:.1f}')
    except Exception as e:
        print(e)