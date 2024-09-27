# 19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre 
# outros. Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades, 12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

while True:
    try:
        num = int(input(f'Digite um número inteiro (<1000):'))
        if num < 1000:
            centena = num//100
            dezena = (num%100)//10
            unidade = (num%10)%10
            if centena > 0:
                print(centena,'centenas' if centena > 1 else 'centena')
            if dezena > 0:
                print(dezena,'dezenas' if dezena > 1 else 'dezena')
            if unidade > 0:
                print(unidade,'unidades' if unidade > 1 else 'unidade')
        else:
            raise ValueError('Digite um número inteiro menor que 1000!')
    except Exception as e:
        print(f"\nOcorreu um erro!\n Erro:{e}\n")