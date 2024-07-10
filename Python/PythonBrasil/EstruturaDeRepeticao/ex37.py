# 37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto,
# o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
# pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo
# código. Ao encerrar o programa também deve ser informados os códigos e valores do clente
# mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos
# pesos dos clientes
lista = []
media_peso, media_altura = 0.0, 0.0
while True:
    codigo = input('Digite seu código: ')
    if codigo == '0':
        break
    cliente = {}
    cliente['codigo'] = codigo
    cliente['altura'] = float(input('Digite sua altura: '))
    media_altura += cliente['altura']
    cliente['peso'] = float(input('Digite seu peso: '))
    media_peso += cliente['peso']
    lista.append(cliente)

cliente_alto = lista[0]
cliente_baixo = lista[0]
cliente_gordo = lista[0]
cliente_magro = lista[0]

for cliente in lista:
    if cliente['altura'] > cliente_alto['altura']:
        cliente_alto = cliente
    if cliente['altura'] < cliente_baixo['altura']:
        cliente_baixo = cliente
    if cliente['peso'] > cliente_gordo['peso']:
        cliente_gordo = cliente
    if cliente['peso'] < cliente_magro['peso']:
        cliente_magro = cliente

print(f'Cliente mais alto: {cliente_alto}')
print('Cliente mais baixo: ',cliente_baixo)
print('Cliente mais gordo: ',cliente_gordo)
print('Cliente mais magro: ',cliente_magro)
print('Media de alturas: ',round(media_altura/len(lista),2))
print('Media de pesos: ',round(media_peso/len(lista),2))