from commons import extrairMatrizCinza, salvarImagem
import numpy as np

def somarImagens(matriz1, matriz2):
    matrizSoma = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[i])):
            soma = int(matriz1[i][j]) + int(matriz2[i][j])
            if soma > 255:
                soma = (int(matriz1[i][j]) + int(matriz2[i][j])) // 2
            linha.append(soma)
        matrizSoma.append(linha)
    return matrizSoma

def subtrairImagens(matriz1, matriz2):
    matrizSub = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[i])):
            sub = int(matriz1[i][j]) - int(matriz2[i][j])
            if sub < 0:
                sub = 0
            linha.append(sub)
        matrizSub.append(linha)
    return matrizSub

def main():
    matriz1 = extrairMatrizCinza()
    matriz2 = extrairMatrizCinza("imagens/pexels-snapwire-147388.jpg")

    matrizSoma = somarImagens(matriz1, matriz2)
    matrizSub = subtrairImagens(matriz1, matriz2)

    salvarImagem(np.array(matrizSoma, dtype=np.uint8), "imagem_soma.png")
    salvarImagem(np.array(matrizSub, dtype=np.uint8), "imagem_subtracao.png")

if __name__ == "__main__":
    main()
