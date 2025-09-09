# Transformações geométricas
from commons import *
import numpy as np
import math

def translacao(matriz, tx, ty):
    nova_matriz = np.zeros_like(matriz, dtype=np.uint8)

    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):

            x_novo, y_novo = i + tx, j + ty

            if 0 <= x_novo < matriz.shape[0] and 0 <= y_novo < matriz.shape[1]:
                nova_matriz[x_novo][y_novo] = matriz[i][j]

    return nova_matriz

def transformacao(tipo,matriz):
    nova_matriz = np.zeros_like(matriz, dtype=np.uint8)

    if tipo == "translacao":
        # Exemplo
        tx, ty = 100, 100  
        nova_matriz = translacao(matriz, tx, ty)

    return nova_matriz

def main():
    matriz = extrairMatrizColorida()
    nova_matriz = transformacao("translacao", matriz)

    salvarImagem(nova_matriz, "imagem_transladada.png")

if __name__ == "__main__":
    main()