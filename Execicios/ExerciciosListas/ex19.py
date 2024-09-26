# 19 - Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete
# feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete
# e informe ao final o resultado da mesma. O programa deverá ler os valores até ser
# informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores
# além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções
# devem ser armazenados num vetor. Após os dados terem sido completamente informados,
# o programa deverá calcular a percentual de cada um dos concorrentes e informar o
# vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

print('Qual o melhor Sistema Operacional para uso em servidores?\n')
print('As possíveis respostas são:\n')

possiveis_respostas = ['Windows Server','Unix','Linux',
                       'Netware','Mac OS','Outro']

respostas = [0] * 6
votos = 0

for i,p_respo in enumerate(possiveis_respostas):
    print(f'{i + 1} -',p_respo)

while True:
    try:
        resposta = int(input('Escolha uma opção (0=fim):'))
        if resposta == 0:
            break
        if 1 <= resposta <= 6:
            respostas[resposta - 1] += 1
            votos += 1
        else:
            raise IndexError('Informe um valor entre 1 e 6 ou 0 para sair!')
    except Exception as e:
        print(e)
maior =(0,0)
print('Sistema Operacional     Votos   %')
for i in range(6):
    if respostas > maior[1]:
        maior = (i,respostas)
    print(f'{possiveis_respostas[i]}\t{respostas[i]}\t{round((respostas[i]/votos)*100,1)}%')
print('Total\t',votos)

print(f' O Sistema Operacional mais votado foi o {possiveis_respostas[maior[0]]}, com {maior[1]} votos, correspondendo a {round((maior[1]/votos)*100,1)}% dos votos.')