# 18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se 
# a mesma é uma data válida.

import datetime

def solicitar_data():
    while True:
        data_str = input("Digite uma data no formato dd/mm/aaaa: ")
        try:
            data = datetime.datetime.strptime(data_str, "%d/%m/%Y")
            print("A data é válida")
            break
        except ValueError:
            print("Formato inválido. Por favor, tente novamente.")

solicitar_data()


