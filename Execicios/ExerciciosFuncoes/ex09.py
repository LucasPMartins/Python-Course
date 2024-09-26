# 9 - Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança
# um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar
# 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada,
# isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5,
# 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados
# até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar
# este Ponto novamente.

import random

def verificar(dado,jogada,ponto=1):
    perdeu = [2,3,12]
    ganhou = [7,11]
    if jogada == 1:
        if dado in ganhou:
            return 'Você ganhou!'
        elif dado in perdeu:
            return 'Você perdeu!'
        else:
            return dado
    else:
        if dado == 7:
             return 'Você perdeu!'
        elif dado == ponto:
             return 'Você ganhou!'
        else:
            return None

def main():
    ponto = None
    jogada = 0

    while True:
        jogar = input('Jogar? (s/n): ')
        if jogar.lower() != 's':
            break

        jogada += 1
        dado = random.randint(2, 12)
        print('Dado jogado:', dado)

        resultado = verificar(dado, jogada, ponto if ponto else dado)
        
        if resultado in ['Você ganhou!', 'Você perdeu!']:
            print(resultado, '\n')
            jogada = 0
            ponto = None
        elif jogada == 1:
            ponto = resultado
            print('Seu ponto é', ponto)
        else:
            print('Continue jogando...')

if __name__ == "__main__":
    main()