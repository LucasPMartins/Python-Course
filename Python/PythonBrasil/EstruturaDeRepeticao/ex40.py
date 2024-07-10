# 40 - Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre
# acidentes de trânsito. Foram obtidos os seguintes dados:
# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). 
# Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
cidades = []
for i in range(5):
    codigo = input('Código da cidade:')
    veiculos = int(input(' Número de veículos de passeio (em 1999):'))
    acidentes = int(input('Número de acidentes de trânsito com vítimas (em 1999):'))
    cidade = {}
    cidade = {'codigo':codigo,'veiculos':veiculos,'acidentes':acidentes}
    cidades.append(cidade)

menor_indice = cidades[0]
maior_indice = cidades[0]
media_veiculos = 0
media_2000 = (0,0)

for cidade in cidades:
    if cidade['acidentes'] > maior_indice['acidentes']:
        maior_indice = cidade
    if cidade['acidentes'] < menor_indice['acidentes']:
        menor_indice = cidade
    media_veiculos += cidade['veiculos']
    if cidade['veiculos'] < 2000:
        media_2000[1] += cidade['veiculos']
        media_2000[0] += 1

media_veiculos /= 5
media_2000 = media_2000[1]/media_2000[0]

print('Maior índice de acidentes de transito:',maior_indice)
print('Menor índice de acidentes de transito:',menor_indice)
print('A média de veículos nas cinco cidades juntas:',media_veiculos)
print('A média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio:',media_2000)