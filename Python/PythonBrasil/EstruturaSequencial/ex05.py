#Faça um Programa que converta metros para centímetros.

while True:
    metros = input("Entre com o valor em metros:")
    try:
        metros_int = int(metros)
        print(f"O valor {metros} metros em centimetros é {metros_int*60}")
        break
    except:
        print("Ocorreu um erro!")