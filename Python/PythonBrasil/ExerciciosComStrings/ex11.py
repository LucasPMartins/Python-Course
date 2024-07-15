# 11 - Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras
# lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6
# vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!

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
    palavra = ['_' for i in range(len(palavra_secreta))]
    errou = 0

    while True:
        if errou == 6:
            print('Você foi enforcado, você perdeu!')
            break
        if ''.join(palavra) == palavra_secreta:
            print('Você ganhou! A palavra era:', palavra_secreta)
            break
        try:
            letra = input('Digite uma letra: ').upper()
            if letra in palavra_secreta:
                print('A palavra é: ', end='')
                ocorrencias = []
                for i, l in enumerate(palavra_secreta):
                    if l == letra:
                        ocorrencias.append(i)
                while ocorrencias:
                    palavra[ocorrencias.pop()] = letra
                for letra_aux in palavra:
                    print(letra_aux, end=' ')
                print('\n')
            else:
                errou += 1
                print(f'-> Você errou pela {errou}ª vez. Tente de novo!\n')
        except ValueError:
            print('Digite um valor válido!')
except FileNotFoundError as e:
    print(e)
