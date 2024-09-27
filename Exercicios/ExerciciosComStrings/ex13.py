# 13 - Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que
# adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá
# uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
# O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve
# ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import os
import random

# Função para verificar se o arquivo existe e escolher uma palavra aleatoriamente
def escolher_palavra_aleatoria(nome_arquivo):
    if not os.path.isfile(nome_arquivo):
        raise FileNotFoundError(f"O arquivo '{nome_arquivo}' não foi encontrado.")

    with open(nome_arquivo, 'r') as arquivo:
        palavras = arquivo.readlines()
    palavras = [palavra.strip().upper() for palavra in palavras]
    return random.choice(palavras)

# Nome do arquivo de palavras
nome_arquivo = 'palavras.txt'

# Escolher a palavra secreta aleatoriamente
try:
    palavra_secreta = escolher_palavra_aleatoria(nome_arquivo)
    palavra = []
    used_index = set()
    while True:
        i = random.randint(0,len(palavra_secreta) - 1)
        if i not in used_index:
            palavra.append(palavra_secreta[i])
            used_index.add(i)
        if len(used_index) == len(palavra_secreta):
            break
    errou = 0
    while True:
        if errou == 6:
            print('Você perdeu! A palavra era:',palavra_secreta)
            break
        try:
            print('Palavra:',*palavra)
            tentativa = input('Digite uma palavra: ').upper()
            if tentativa == palavra_secreta:
                print('Você ganhou! A palavra era:', palavra_secreta)
                break
            else:
                errou += 1
                print(f'-> Você errou pela {errou}ª vez. Tente de novo!\n')
        except ValueError:
            print('Digite um valor válido!')
except FileNotFoundError as e:
    print(e)