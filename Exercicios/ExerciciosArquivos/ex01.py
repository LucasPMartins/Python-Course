# 1 - Faça um programa que leia um arquivo texto contendo uma lista de endereços
# IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e
# inválidos.

# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4

# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

def isIP(numero):
    lista_aux = []
    octeto = ''
    for num in numero:
        if num == '\n':
            lista_aux.append(octeto)
            break
        if num == '.':
            lista_aux.append(octeto)
            octeto = ''
        else:
            octeto += num
    if len(lista_aux) != 4:
        return False
    try:
        for octeto in lista_aux:
            if int(octeto) > 255 or int(octeto) < 0:
                return False
    except ValueError:
        return False
    return True


validos = []
invalidos = []
with open('arquivo01.txt', 'r', encoding='utf8') as arquivo:
    lista = arquivo.readlines()
    for ip in lista:
        if isIP(ip):
            validos.append(ip)
        else:
            invalidos.append(ip)

with open('arquivoSaida.txt', 'w', encoding='utf8') as arquivo:
    arquivo.write('[Endereços válidos:]\n')
    for ip in validos:
        arquivo.write(ip)
    if validos == []:
        arquivo.write('Nenhum IP válido!\n')
    arquivo.write('\n')
    arquivo.write('[Endereços inválidos:]\n')
    for ip in invalidos:
        arquivo.write(ip)
    if invalidos == []:
        arquivo.write('Nenhum IP inválido!\n')
    arquivo.write('\n')
