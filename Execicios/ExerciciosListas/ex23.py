# 23 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço
# em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador
# de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários
# com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu
# gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125

# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, 
# você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
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
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória,
# caso sejam necessários, de forma a agilizar a execução do programa. A conversão da
# espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função
# separada, que será chamada pelo programa principal. O cálculo do percentual de uso
# também deverá ser feito através de uma função, que será chamada pelo programa principal.

def bytes_para_megabytes(bytes):
    return bytes / (1024 * 1024)

def calcular_percentual(uso, total):
    return (uso / total) * 100

def gerar_relatorio(usuarios, total_espaco):
    with open("relatório.txt", "w") as relatorio:
        relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n")
        relatorio.write("------------------------------------------------------------------------\n")
        relatorio.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n")
        
        for i, usuario in enumerate(usuarios, start=1):
            espaco_mb = bytes_para_megabytes(usuario['espaco'])
            percentual = calcular_percentual(usuario['espaco'], total_espaco)
            relatorio.write(f"{i:<4} {usuario['nome']:<15} {espaco_mb:>10.2f} MB {percentual:>20.2f}%\n")
        
        espaco_medio = total_espaco / len(usuarios)
        relatorio.write(f"\nEspaço total ocupado: {bytes_para_megabytes(total_espaco):.2f} MB\n")
        relatorio.write(f"Espaço médio ocupado: {bytes_para_megabytes(espaco_medio):.2f} MB\n")

def main():
    usuarios = []
    total_espaco = 0

    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            nome = linha[:15].strip()
            espaco = int(linha[15:].strip())
            usuarios.append({'nome': nome, 'espaco': espaco})
            total_espaco += espaco
    
    gerar_relatorio(usuarios, total_espaco)

if __name__ == "__main__":
    main()
