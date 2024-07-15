# 14 - Leet speak generator. Leet é uma forma de se escrever o alfabeto latino usando outros
# símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite
# muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada
# ao mundo dos jogos de computador e internet, sendo muito usada para confundir os
# iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas
# de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o
# para a grafia leet speak.

print('Tradutor de palaras pra LEET SPEAK')
entrada = input('Entrada: ').upper()
dic = {'A':4,'B':13,'C':'(','D':'[)','E':3,'F':'|=','G':6,'H':'|-|','I':'|','J':'.]','K':'|<','L':'1',
       'M':'|Y|','N':'/\\/','O':0,'P':'|>','Q':'0,','R':'|2','S':5,'T':7,'U':'[_]','V':'V','W':'\v/',
       'X':'}{','Y':'\'/','Z':2}
for letra in entrada:
    if letra in dic:
        print(dic[letra],end='')
    else:
        print(letra,end='')