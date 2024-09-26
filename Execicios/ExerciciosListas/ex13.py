# 13 - Faça um programa que receba a temperatura média de cada mês do ano e armazene-as
# em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as
# temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso:
# 1 – Janeiro, 2 – Fevereiro, . . . ).

def mes(numero):
    meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ]
    if 1 <= numero <= 12:
        return meses[numero - 1]
    else:
        return 'Número inválido'

temperatura_media = []
media = 0.0
for i in range(12):
    temperatura = float(input(f'Digite a temperatura média de {mes(i+1)}: '))
    temperatura_media.append(temperatura)
    media += temperatura

media /= 12
print('Temperaturas acima da média anual de ',round(media,2),'°C:',sep='')
for i,temperatura in enumerate(temperatura_media):
    if temperatura > media:
        print(f'{mes(i+1)}:\t{temperatura}°C')