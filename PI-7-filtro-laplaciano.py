from commons import extrairMatrizCinza, salvarImagem
import numpy as np

laplacian_masks = {
    "a": [[0, -1,  0],
          [-1,  4, -1],
          [0, -1,  0]],
    
    "b": [[-1, -1, -1],
          [-1,  8, -1],
          [-1, -1, -1]],
    
    "c": [[0,  1,  0],
          [1, -4,  1],
          [0,  1,  0]],
    
    "d": [[1,  1,  1],
          [1, -8,  1],
          [1,  1,  1]]
}

def duplicarBordas(matriz, tamanho_mascara=3):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    pad = tamanho_mascara - 1

    novaMatriz = [[0 for _ in range(colunas + pad)] for _ in range(linhas + pad)]

    for i in range(linhas):
        for j in range(colunas):
            novaMatriz[i][j] = matriz[i][j]

    for i in range(linhas):
        for k in range(pad):
            novaMatriz[i][colunas + k] = matriz[i][colunas - 1]

    for k in range(pad):
        for j in range(colunas):
            novaMatriz[linhas + k][j] = matriz[linhas - 1][j]

    ultimo = matriz[linhas - 1][colunas - 1]
    for ki in range(pad):
        for kj in range(pad):
            novaMatriz[linhas + ki][colunas + kj] = ultimo

    return novaMatriz


def aplicarMascaraLaplaciano(matriz, mascara):
    linhas = len(matriz)
    colunas = len(matriz[0])

    matriz = [[int(matriz[i][j]) for j in range(colunas)] for i in range(linhas)]

    # Trata as bordas
    matrizExpandida = duplicarBordas(matriz)

    matrizNova = [[0 for _ in range(colunas)] for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            soma = 0
            for mi in range(3):
                for mj in range(3):
                    soma += matrizExpandida[i+mi][j+mj] * mascara[mi][mj]

            # Normalização para [0, 255]
            if soma < 0:
                soma = 0
            elif soma > 255:
                soma = 255

            matrizNova[i][j] = soma

    return matrizNova

def main():
    matrizCinza = extrairMatrizCinza()

    print("Selecione a máscara Laplaciana:")
    print("1 - Máscara A")
    print("2 - Máscara B")
    print("3 - Máscara C")
    print("4 - Máscara D")
    opcao = int(input())

    mascara = None
    nomeMascara = ""
    if opcao == 1:
        mascara = laplacian_masks["a"]
        nomeMascara = "a"
    elif opcao == 2:
        mascara = laplacian_masks["b"]
        nomeMascara = "b"
    elif opcao == 3:
        mascara = laplacian_masks["c"]
        nomeMascara = "c"
    elif opcao == 4:
        mascara = laplacian_masks["d"]
        nomeMascara = "d"
    else:
        print("Opção inválida.")
        return

    matrizFiltrada = aplicarMascaraLaplaciano(matrizCinza, mascara)

    matrizFiltrada = np.array(matrizFiltrada, dtype=np.uint8)

    matrizFiltrada = np.array(matrizFiltrada, dtype=np.uint8)
    salvarImagem(matrizFiltrada, f"laplaciano_{nomeMascara}.png")

if __name__ == "__main__":
    main()
