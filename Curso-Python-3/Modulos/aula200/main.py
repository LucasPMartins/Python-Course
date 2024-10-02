# Pillow: redimensionar imagens com Python
# https://pillow.readthedocs.io/en/stable/
# pip install pillow

from PIL import Image  # Importa a biblioteca Pillow para manipulação de imagens
from pathlib import Path  # Importa a biblioteca pathlib para manipulação de caminhos

# Define a pasta raiz como o diretório do arquivo atual
ROOT_FOLDER = Path(__file__).parent
# Define o caminho da imagem original
ORIGIN = ROOT_FOLDER / 'origin.png'
# Define o caminho para salvar a nova imagem
NEW_IMAGE = ROOT_FOLDER / 'new_image.png'

# Abre a imagem original
pil_image = Image.open(ORIGIN)

# Mostra o tamanho da imagem original
print(pil_image.size)
# Desempacota a tupla de tamanho da imagem em largura e altura
width, height = pil_image.size
# Obtém as informações EXIF da imagem, se existirem
exif = pil_image.info.get('exif')

# Define a nova largura da imagem
new_width = 640
# Calcula a nova altura da imagem mantendo a proporção
new_height = round(height * new_width / width)

# Redimensiona a imagem para o novo tamanho
new_image = pil_image.resize(size=(new_width, new_height))

# Salva a nova imagem com otimização e qualidade de 70, mantendo as informações EXIF
new_image.save(NEW_IMAGE, optimize=True, quality=70, exif=exif)