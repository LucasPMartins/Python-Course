# 3 - Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    try:
        nome = input('Digite seu nome:')
        if len(nome) <= 3:
            raise ValueError('Nome inválido')
        idade = input('Digite sua idade:')
        if int(idade) < 0 or int(idade) > 150:
            raise ValueError('Idade inválida')
        salario = input('Digite seu salário: R$')
        if float(salario) < 0:
            raise ValueError('Salário deve ser maior ou igual a zero')
        sexo = input('Digite seu sexo: "f" ou "m"').lower()
        if sexo != 'f' and sexo != 'm':
            raise ValueError('Sexo inválido') 
        estado = input('Digite seu Estado Civil: "s", "c", "v", "d"').lower()
        if estado != 's' and estado != 'c' and estado != 'v' and estado != 'd':
            raise ValueError('Estado Civil inválido') 
        break
    except Exception as e:
        print('Erro:',e)