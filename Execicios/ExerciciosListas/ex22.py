# 22 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte
# de Informática, com a intenção de fazer um levantamento nas sucatas encontradas
# nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
# encontram lá, testando e anotando o estado de cada um deles, para verificar o que
# se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento.
# O programa deverá receber um número indeterminado de entradas, cada uma contendo:
# um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza; 
# necessita troca do cabo ou conector; 
# quebrado ou inutilizado
# Uma identificação igual a zero encerra o programa. 
# Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%

defeitos = [{'nome':'necessita da esfera','qtd':0},{'nome':'necessita de limpeza','qtd':0},
            {'nome':'necessita troca do cabo ou conector','qtd':0},{'nome':'quebrado ou inutilizado','qtd':0}]
qtd = 0

while True:
    try:
        codigo = int(input('Digite a identificação do tipo de defeito (1, 2, 3, 4 ou 0 p/ Sair):'))
        if codigo == 0:
            break
        if 1 <= codigo <= 4:
            defeitos[codigo - 1]['qtd'] += 1
            qtd += 1
        else:
            raise IndexError('Informe um valor entre 1 e 4 ou 0 para sair!')
    except Exception as e:
        print(e)

print('Quantidade de mouses:', qtd)
print('Situação\t\t\t\tQuantidade\t  Percentual')
defeitos = sorted(defeitos, key=lambda item: item['qtd'],reverse=True)
for i, cod in enumerate(defeitos):
    percentual = round(cod['qtd'] / qtd * 100, 2)
    if cod['nome'] == 'necessita troca do cabo ou conector':
        print(f"{i+1} - {cod['nome']}     {cod['qtd']} \t\t    {percentual}%")
        continue
    print(f"{i+1} - {cod['nome']} \t\t    {cod['qtd']} \t\t    {percentual}%")