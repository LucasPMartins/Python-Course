# Pillow: redimensionar imagens com Python
# https://pillow.readthedocs.io/en/stable/
# pip install pillow

from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGIN = ROOT_FOLDER / 'origin.png'
NEW_IMAGE = ROOT_FOLDER / 'new_image.png'

pil_image = Image.open(ORIGIN) # Abre a imagem

print(pil_image.size) # Mostra o tamanho da imagem
width, height = pil_image.size # desempacotamento de tupla
exif = pil_image.info.get('exif') # Informações da imagem

# width    new_width 
# height   new_height
new_width = 640
new_height = round(height * new_width / width)
# print(width, height, new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height)) # Redimensiona a imagem

new_image.save(NEW_IMAGE,optimize=True,quality=70,exif=exif,) # Salva a imagem
