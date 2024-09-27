# 10 - Data com mês por extenso. Construa uma função que receba uma data no formato
# DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente,
# valide a data e retorne NULL caso a data seja inválida.

import datetime

def data_extenso(data):
    mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
           'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    if isinstance(data,datetime.datetime):
        return f'{data.day} de {mes[data.month - 1]} de {data.year}'
    return 'Data invalida!'

def main():
    while True:
        try:
            data = input('Digite uma data (DD/MM/AAAA):')
            data = datetime.datetime.strptime(data, "%d/%m/%Y")
            print('Data por extenso:',data_extenso(data))
            break
        except ValueError:
            print('Digite uma data valida!')

if __name__ == '__main__':
    main()