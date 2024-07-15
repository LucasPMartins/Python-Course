# 8 - Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica
# se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos.
# Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é
# o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo
# ou não.

frase = input('Digite uma frase ou palavra: ')
teste = frase.replace(' ','')
teste_reverso = list(teste)
teste_reverso.reverse()
teste_reverso = ''.join(teste_reverso)
if teste == teste_reverso:
    print(f'{frase} é palíndromo')
else:
    print(f'{frase} não é palíndromo')