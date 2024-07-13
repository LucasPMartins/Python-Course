# 12 - Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres
# ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo
# que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores
# fora da faixa forem informados, eles devem ser modificados para valores dentro da
# faixa de forma elegante.

def moldura(linha=1,coluna=1):
    if linha <= 20 and coluna <= 20:
        for i in range(linha):
            if i == 0:
                print('+','-'*coluna,'+',sep='')
            else:
                print('|',' '*coluna,'|',sep='')
        print('+','-'*coluna,'+',sep='')

moldura(20,20)