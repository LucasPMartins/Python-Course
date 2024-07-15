# 6 - Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
# do usuário e imprima a data com o nome do mês por extenso.
# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

import datetime

def data_extenso(data):
    mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
           'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    if isinstance(data,datetime.datetime):
        return f'{data.day} de {mes[data.month - 1]} de {data.year}'
    return 'Data invalida!'

data = input('Data de Nascimento: ')
data = datetime.datetime.strptime(data,'%d/%m/%Y')
print('Você nasceu em',data_extenso(data))