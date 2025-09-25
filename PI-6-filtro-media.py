from commons import extrairMatrizCinza, salvarImagem
import numpy as np

def filtroMedia(matriz, tamanhoJanela=3):
    linhas = len(matriz)
    colunas = len(matriz[0])
    offset = tamanhoJanela // 2

    # Criar matriz nova para armazenar o resultado
    matrizNova = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # Percorrer cada pixel da matriz original
    for i in range(linhas):
        for j in range(colunas):
            soma = 0
            cont = 0

            # Percorrer a vizinhança
            for x in range(-offset, offset+1):
                for y in range(-offset, offset+1):
                    linhaViz = i + x
                    colunaViz = j + y

                    # Tratamento de borda por duplicação
                    if linhaViz < 0:
                        linhaViz = 0
                    elif linhaViz >= linhas:
                        linhaViz = linhas - 1
                    if colunaViz < 0:
                        colunaViz = 0
                    elif colunaViz >= colunas:
                        colunaViz = colunas - 1

                    soma += int(matriz[linhaViz][colunaViz])
                    cont += 1

            # Média da vizinhança
            matrizNova[i][j] = soma // cont

    return matrizNova

def main():
    matrizCinza = extrairMatrizCinza()

    print("Aplicando Filtro da Média...")
    matrizFiltrada = filtroMedia(matrizCinza, tamanhoJanela=3)

    salvarImagem(np.array(matrizFiltrada, dtype=np.uint8), "imagem_filtro_media.png")

if __name__ == "__main__":
    main()
