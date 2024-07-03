#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

while True:
    lado = input('Digite o lado do quadradado:')
    try:
        lado_int = int(lado)
        area = lado_int*lado_int
        print(f'A área do quadrado é {area}')
        print(f'O dobro da área é {area*2}')
        break
    except:
        print("Ocorreu um erro!")