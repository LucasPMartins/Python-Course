# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - # + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4
import re # Regular Expressions
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html,'html.parser')
# Uma coisa comum de ocorrer quando trabalhamos com o bs4.BeautifulSoup. 
# é problemas com caracteres. Isso ocorre devido a uma falha na detecção do 
# encoding.
# bytes_html = response.content
# parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
# Você pode detectar isso no HTML pela tag meta charset dentro da <head>:
# <meta charset="UTF-8">

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    
    if article is not None:
        for p in article.select('p'):
            # substitui todo espaço maior que 1 pra um 1 espaço só
            print(re.sub(r'\s{1,}', ' ',p.text).strip())

