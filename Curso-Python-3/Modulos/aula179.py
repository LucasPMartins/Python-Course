# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'aula178-ex.csv'
print(CAMINHO_CSV)
# csv.reader -> list
# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)
#     # next(leitor)
#     for linha in leitor:
#         print(linha)

# csv.DictReader -> dict
with open(CAMINHO_CSV, 'r',encoding='utf8') as arquivo:
    leitor = csv.DictReader(arquivo)
    # next(leitor)
    for linha in leitor:
        print(linha['Nome'],linha['Idade'],linha['Endereço'])