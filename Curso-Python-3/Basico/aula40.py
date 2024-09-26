'''Calculadora com while'''


while True:
    try:
        entrada1 = input("Digite um número:")
        entrada2 = input("Digite outro número:")
        num1 = int(entrada1)
        num2 = int(entrada2)
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")
        opcao = input('Escolha uma opção:')
        if opcao == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif opcao == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif opcao == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif opcao == '4':
            print(f"{num1} / {num2} = {num1 / num2:.2fs}")
        elif opcao == '0':
            break
        else:
            print('Opção inválida!')
    except:
        print("ERRO!")
print("Fim do programa")