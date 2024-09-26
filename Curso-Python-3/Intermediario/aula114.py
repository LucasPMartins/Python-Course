import json

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Martins',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('./intermediario/aula114.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False, # Coloca acentos, etc
        indent=2, # Formatação
    )

with open('./intermediario/aula114.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])