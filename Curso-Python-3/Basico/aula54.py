"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    os.system("cls")
    print('---=== LISTA DE COMPRAS ===---\n')
    if lista == []:
        print("Lista de compras vazia!\n")
    else:
        for indice,produto in enumerate(lista):
            print(f'{indice} - {produto}')
    opcao = input('O que deseja fazer?\n[I]nserir [A]pagar [S]air:').upper()
    if len(opcao) != 1:
        print('Opção invalida!')
        continue
    if opcao == 'I':
        novo_produto = input('Digite o nome do novo produto a ser adicionado:')
        lista.append(novo_produto)
    elif opcao == 'A':
        while True:
            indice = input('Digite o indice do produto a ser removido:')

            # try:
            #     indice = int(indice_str)
            #     del lista[indice]
            # except ValueError:
            #     print('Por favor digite número int.')
            # except IndexError:
            #     print('Índice não existe na lista')
            # except Exception:
            #     print('Erro desconhecido')

            if indice.isdecimal():
                indice = int(indice)
                if indice > len(lista) - 1 or indice < 0:
                    print('Digite um indice válido!')
                else:
                    lista.pop(indice)
                    break
            else:
                print('Digite um indice válido!')
    elif opcao == 'S':
        break
