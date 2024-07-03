# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido.

try:
    letra = input('Digite seu sexo (M ou F):').upper()
    if letra == 'M':
        print('Masculino')
    elif letra == 'F':
        print("Feminino")
    else:
        print('Sexo inválido!')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")