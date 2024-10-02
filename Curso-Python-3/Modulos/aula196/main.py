# # PyPDF2 para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfReader,PdfWriter, PdfMerger

ROOT_FILE = Path(__file__).parent
ORIGIN_FILE = ROOT_FILE / 'teste.pdf'
NEW_FILE = ROOT_FILE / 'resultado'

(ROOT_FILE/'PastaNova').mkdir(exist_ok=True)
NEW_FILE.mkdir(exist_ok=True)
reader = PdfReader(ORIGIN_FILE)

# Quantidade de paginas
# print('Quantidade de paginas:',len(reader.pages))

# for page in reader.pages:
#     print(page)
#     print()


# extrai o texto da pagina
# print(page0.extract_text())

page0 = reader.pages[0]
image0 = page0.images[0]
# print(page0.images[0])

# with open(NEW_FILE / image0.name, 'wb') as fp:
#     fp.write(image0.data)

# writer.add_page(page0)

# criando um pdf para cada pag do pdf original
for i,page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(NEW_FILE / f'page{i}.pdf','wb') as fp:
        writer.add_page(page)
        writer.write(fp) # type: ignore

files = [NEW_FILE / f'page{i}.pdf' for i in range(4)]
merger = PdfMerger()

for file in files:
    merger.append(file)  # type: ignore

# merger.write(NEW_FILE / 'merged.pdf')
# merger.close()

with open(NEW_FILE / 'merged.pdf','wb') as file:
    merger.write(file) # type: ignore