# 17 - Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo 
# o controle deles através de uma lista. Imite o funcionamento do programa básico, 
# mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que 
# ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário 
# executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar
# com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa 
# mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
import random
from ex16 import Tamagushi

class Fazenda:
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)
    
    def alimentar_todos(self, quantidade):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade)
    
    def brincar_com_todos(self, tempo):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)
    
    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            print(bichinho)


fazenda = Fazenda()
for i in range(5):
    nome = f'Bichinho{i+1}'
    fome_inicial = random.randint(0, 100)
    saude_inicial = random.randint(0, 100)
    idade_inicial = random.randint(0, 10)
    bichinho = Tamagushi(nome, idade_inicial ,fome_inicial, saude_inicial )
    fazenda.adicionar_bichinho(bichinho)


while True:
    print("\n1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ouvir todos os bichinhos")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        quantidade = int(input("Quantidade de comida: "))
        fazenda.alimentar_todos(quantidade)
    elif opcao == '2':
        tempo = int(input("Tempo de brincadeira: "))
        fazenda.brincar_com_todos(tempo)
    elif opcao == '3':
        fazenda.ouvir_todos()
    elif opcao == '4':
        break
    elif opcao == '999':
        for bichinho in fazenda.bichinhos:
            print(bichinho)
    else:
        print("Opção inválida!")