# 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.


while True:
    try:
        nome = input('Digite seu nome:')
        senha = input('Digite uma senha:')
        if nome == senha:
            print('A senha não pode ser igual ao nome do usuário')
        else:
            break
    except Exception as e:
        print("Erro:",e)