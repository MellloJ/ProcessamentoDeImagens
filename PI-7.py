from commons import extrairMatrizCinza, salvarImagem
import numpy as np

def filtroMedia(matriz, tamanhoJanela=3):
    linhas = len(matriz)
    colunas = len(matriz[0])
    offset = tamanhoJanela // 2

    matriz = matriz.tolist()

    matrizExpandida = [linha[:] for linha in matriz]

    # Tratando as bordas
    for i in range(linhas):
        ultimaColuna = matriz[i][-1]
        for _ in range(offset):
            matrizExpandida[i].append(ultimaColuna)

    ultimaLinha = matrizExpandida[-1][:]
    for _ in range(offset):
        matrizExpandida.append(ultimaLinha[:])

    matrizNova = [[0 for _ in range(colunas)] for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            soma = 0
            cont = 0

            for x in range(-offset, offset+1):
                for y in range(-offset, offset+1):
                    linhaViz = i + x
                    colunaViz = j + y
                    soma += int(matrizExpandida[linhaViz][colunaViz])
                    cont += 1

            matrizNova[i][j] = soma // cont

    return matrizNova

def main():
    matrizCinza = extrairMatrizCinza()

    tamanhoJanela = 3

    matrizFiltrada = filtroMedia(matrizCinza, tamanhoJanela=tamanhoJanela)

    salvarImagem(np.array(matrizFiltrada, dtype=np.uint8), f"imagem_filtro_media_{tamanhoJanela}x{tamanhoJanela}.png")

if __name__ == "__main__":
    main()
