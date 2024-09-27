# 5 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros.
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.
# Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
# a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M.
# ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores
# de entrada todas as vezes que desejar.

def converter_hora(hora24, minuto24):
    if hora24 >= 0 and hora24 < 12:
        periodo = 'A'
        hora12 = hora24 if hora24 != 0 else 12
    else:
        periodo = 'P'
        hora12 = hora24 - 12 if hora24 > 12 else 12
    return hora12, minuto24, periodo

def exibir_hora(hora12, minuto12, periodo):
    periodo_str = 'A.M.' if periodo == 'A' else 'P.M.'
    print(f"{hora12}:{minuto12:02d} {periodo_str}")

def main():
    while True:
        try:
            hora24 = int(input("Digite a hora (0-23): "))
            minuto24 = int(input("Digite os minutos (0-59): "))
            
            if (hora24 < 0 or hora24 > 23) or (minuto24 < 0 or minuto24 > 59):
                print("Hora ou minutos inválidos. Tente novamente.")
                continue
            
            hora12, minuto12, periodo = converter_hora(hora24, minuto24)
            exibir_hora(hora12, minuto12, periodo)
            
            repetir = input("Deseja converter outra hora? (s/n): ")
            if repetir.lower() != 's':
                break
        
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
        
if __name__ == "__main__":
    main()