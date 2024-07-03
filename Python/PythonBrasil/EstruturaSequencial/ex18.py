# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

while True:
    tamanho = input('Digite o tamanho de um arquivo para download (em MB):')
    velocidade = input('Digite a velocidade de um link de Internet (em Mbps):')
    try:
        tamanho_float = float(tamanho)
        velocidade_float = float(velocidade)
        # 1 byte = 8 bits
        # Portanto, 1 megabyte (MB) = 8 megabits (Mb)
        tamanho_float *= 8
        # Tempo de download em segundos = (Tamanho do arquivo em megabits) / (Velocidade de download em megabits por segundo)
        # Tempo de download em minutos = Tempo de download em segundos / 60
        tempo = (tamanho_float/velocidade_float)/60
        print(f'O tempo aproximado de download do arquivo (em minutos) é {round(tempo)}')
        break
    except Exception as e:
        print(f"\nOcorreu um erro!\n Erro:{e}\n")