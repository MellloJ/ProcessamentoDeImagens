from commons import extrairMatrizCinza, salvarImagem
import numpy as np

def transformarIntensidadeNegativo(matriz):
    matrizNova = []
    for i in range(len(matriz)):
        novaLinha = []
        for j in range(len(matriz[i])):
            novoValor = 255 - matriz[i][j]
            novaLinha.append(novoValor)
        matrizNova.append(novaLinha)
    return matrizNova

def main():
    matrizCinza = extrairMatrizCinza()
    matrizNegativa = transformarIntensidadeNegativo(matrizCinza)
    salvarImagem(np.array(matrizNegativa, dtype=np.uint8), "imagem_negativa.png")

if __name__ == "__main__":
    main()