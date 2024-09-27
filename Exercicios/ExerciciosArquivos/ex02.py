# 2 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de
# espaço em disco no seu servidor de arquivos. Para tentar resolver este
# problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
# usuários, e identificar os usuários com maior espaço ocupado. Através de
# um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo,
# chamado "usuarios.txt":

# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
# você deve criar um programa que gere um relatório, chamado "relatório.txt",
# no seguinte formato:

# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB

# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
# memória, caso sejam necessários, de forma a agilizar a execução do programa.
# A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser
# feita através de uma função separada, que será chamada pelo programa principal.
# O cálculo do percentual de uso também deverá ser feito através de uma função,
# que será chamada pelo programa principal.

def ler_relatorio(arquivo_caminho):
    usuarios = []
    with open(arquivo_caminho, 'r', encoding='utf8') as arquivo:
        lista = arquivo.readlines()
        for user in lista:
            nome = user[:15].strip()
            dados = float(user[15:].strip())
            usuarios.append((nome, dados, 0))
    return usuarios


def converte_megabytes(dado):
    return dado/10**6


def porcentual(usuarios):
    total = converte_megabytes(func_total(usuarios))
    usuarios_atualizados = []
    for user in usuarios:
        espaco_mb = converte_megabytes(user[1])
        porcento = (espaco_mb / total) * 100
        usuarios_atualizados.append((user[0], espaco_mb, porcento))
    return usuarios_atualizados


def func_total(usuarios):
    total = 0.0
    for user in usuarios:
        total += user[1]
    return total


def salva_arquivo(arquivo_caminho, usuarios):
    with open(arquivo_caminho, 'w', encoding='utf8') as arquivo:
        arquivo.write(
            'ACME Inc.               Uso do espaço em disco pelos usuários\n')
        arquivo.write(
            '------------------------------------------------------------------------\n')
        arquivo.write('Nr.  Usuário         Espaço utilizado     % do uso\n')
        for i, user in enumerate(usuarios):
            arquivo.write(
                f'{i + 1:>2}   {user[0]:<15}  {user[1]:>10.2f} MB        {user[2]:>6.2f}%\n')
        arquivo.write(f'\nEspaço total ocupado: {
                      func_total(usuarios):.2f} MB\n')
        arquivo.write(f'Espaço médio ocupado: {
                      func_total(usuarios)/len(usuarios):.2f} MB\n')
        print("Arquivo salvo com sucesso!")


def main():
    usuarios = porcentual(ler_relatorio("usuarios.txt"))
    salva_arquivo("relatório.txt", usuarios)


if __name__ == '__main__':
    main()
