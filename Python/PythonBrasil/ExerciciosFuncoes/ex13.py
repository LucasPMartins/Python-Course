# 13 - Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um
# número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma.
# Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
# 8  3  4 
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as
# características acima. Dica: produza todas as combinações possíveis e verifique a soma
# quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar
# uma matriz 3x3.

import itertools

def eh_quadrado_magico(quadrado):
    # Verifica se todas as linhas têm a mesma soma
    soma_linhas = [sum(quadrado[i:i+3]) for i in range(0, 9, 3)]
    if len(set(soma_linhas)) != 1:
        return False
    
    # Verifica se todas as colunas têm a mesma soma
    soma_colunas = [quadrado[i] + quadrado[i+3] + quadrado[i+6] for i in range(3)]
    if len(set(soma_colunas)) != 1:
        return False
    
    # Verifica se as diagonais têm a mesma soma
    soma_diagonal1 = quadrado[0] + quadrado[4] + quadrado[8]
    soma_diagonal2 = quadrado[2] + quadrado[4] + quadrado[6]
    if soma_diagonal1 != soma_diagonal2:
        return False
    
    # Verifica se a soma das linhas, colunas e diagonais são iguais
    if soma_linhas[0] == soma_colunas[0] == soma_diagonal1:
        return True
    
    return False

def encontrar_quadrados_magicos():
    # Gera todas as permutações dos números de 1 a 9
    permutacoes = itertools.permutations(range(1, 10))
    
    quadrados_magicos = []
    for perm in permutacoes:
        if eh_quadrado_magico(perm):
            quadrados_magicos.append(perm)
    
    return quadrados_magicos

def imprimir_quadrado(quadrado):
    for i in range(0, 9, 3):
        print(quadrado[i], quadrado[i+1], quadrado[i+2])
    print()

# Encontra e imprime todos os quadrados mágicos
quadrados_magicos = encontrar_quadrados_magicos()
print(f"Total de quadrados mágicos encontrados: {len(quadrados_magicos)}\n")

for quadrado in quadrados_magicos:
    imprimir_quadrado(quadrado)
