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

def tipoGrafo(matriz):
    tipo = '0'
    tipo2 = '0'
    qtd = np.shape(matriz)[0]

    if np.sum(np.diagonal(matriz)) > 0:
        tipo2 = '3'
    else:
        for i in range(0, qtd):
            for j in range(0, qtd):
                if matriz[i][j] > 1:
                    tipo2 = '2'
                    break

    for vi in range(0, qtd):
        for vj in range(vi + 1, qtd):
            if matriz[vi][vj] == matriz[vj][vi]:
                tipo = '0'
            else:
                tipo = '1'

    res = (int(tipo2 + tipo))
    return res;







