# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = set('aeiou')

try:
    letra = input('Digite um letra:')
    if letra.isalpha() and letra.lower() in vogais:
        print(f'{letra} é uma vogal.')
    else:
        print(f'{letra} é uma consoante.')
except Exception as e:
    print(f"\nOcorreu um erro!\n Erro:{e}\n")