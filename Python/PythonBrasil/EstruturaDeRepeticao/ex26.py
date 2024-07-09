# 26 - Numa eleição existem três candidatos. Faça um programa que peça o número total
# de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de 
# cada candidato.

urna = {'1':0,'2':0,'3':0}

n_eleitores = int(input('Digite o número de eleitores:'))
for i in range(n_eleitores):
    print(f'----==== Eleitor {i+1} ====----')
    while True:
        voto = input('Escolha um candidato 1, 2 ou 3:')
        if voto in urna:
            urna[voto] += 1
            break
        else:
            print('Candidato inválido!')

print(urna)

ganhador = '1'
for chave in urna:
    if urna[chave] > urna[ganhador]:
        ganhador = chave

print(f'O ganhador da eleição é o candidato "{ganhador}"')