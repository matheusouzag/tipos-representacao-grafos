import numpy as np

'''lerGrafo: Usado para ler uma instância'''
def lerGrafo(matriz):
    with open(matriz, 'rb') as f:
        data = np.genfromtxt(f)

    return data


def verificaAdjacencia(matriz, vi, vj):
    # Para encontrar o tamanho quadrático da matriz.
    tamanho = np.shape(matriz)[0]
    # Verifica se existe os vertices na matriz, e se o valor é igual a 0 (que não seria adjacente), retornando false.
    if vi >= tamanho or vj >= tamanho or matriz[vi][vj] == 0:
        return False
    else:
        return True

