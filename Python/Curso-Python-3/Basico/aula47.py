"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'secreta'
tentativas = 0
palavra = '*'*len(palavra_secreta)

print('----== Jogo da Adivinhação ==----')
while True:
    os.system("cls")
    print(f'Palavra Secreta: {palavra}')
    letra = input('Digite uma letra:').lower()
    if letra is None:
        tentativas += 1
        continue
    if len(letra) > 1:
        tentativas += 1
        print('Digite somente um letra!')
        continue
    if letra in palavra_secreta:
        if letra in palavra:
            tentativas += 1
            continue
        lista_palavra = list(palavra)
        lista_palavra_secreta = list(palavra_secreta)
        for i in range(len(palavra_secreta)):
            if lista_palavra_secreta[i] == letra:
                lista_palavra[i] = letra
        palavra = ''.join(lista_palavra)
    tentativas += 1
    if palavra == palavra_secreta:
        print('Parabéns, Você ganhou!','Tentativas:',f'{tentativas}')
        print(f'A palavra era "{palavra_secreta}"')
        break


