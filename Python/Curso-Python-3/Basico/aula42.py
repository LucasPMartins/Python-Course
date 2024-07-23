frase = 'qpoiopfmaspmdapvm,spkfepoa,gpqpvmaspdgpasjs'

i = 0
letra = ''
qtd = 0
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == " ":
        i += 1
        continue
    qtd_letra_atual = frase.count(letra_atual)
    if qtd < qtd_letra_atual:
        qtd = qtd_letra_atual
        letra = letra_atual
    i += 1

print(f'A letra que mais apareceu é "{letra}" e apareceu {qtd} vezes')
