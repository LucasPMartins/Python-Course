#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

while True:
    grana_hora = input('Quanto você ganha por hora? \nR:')
    horas_trabalhadas = input('Quantas horas trabalhadas no mês? \nR:')
    try:
        grana_hora_int = int(grana_hora)
        horas_trabalhadas_int = int(horas_trabalhadas)
        print(f"O seu salário total referente a esse mês é {grana_hora_int*horas_trabalhadas_int}")
        break
    except:
        print("Ocorreu um erro!")
