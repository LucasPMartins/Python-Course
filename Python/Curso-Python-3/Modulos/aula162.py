# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone

data = datetime.now()
print(data.timestamp()) # isso está na base de dados
print(datetime.fromtimestamp(1722814836.37233)) # número de segundos 
# data_str = '2024/08/04 20:20:56'
# data_str = '04/08/2024'
# str_formato = '%d/%m/%Y'# %H:%M:%S
# data = datetime.strptime(data_str,str_formato)

# data = datetime(2024, 8, 4, 20, 20, 5,tzinfo=timezone('Asia/Tokyo'))
# print(data)     #ano mes dia hr min seg


