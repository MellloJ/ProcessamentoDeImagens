import numpy as np
from commons import *
from PI_9 import aplicarErosao

def extrair_contornos(matriz_original, matriz_erudida):
        imagem_original = np.asarray(matriz_original)
        imagem_erodida = np.asarray(matriz_erudida)

        # Subtração com tipo assinado para evitar underflow do uint8
        diferenca = imagem_original.astype(np.int16) - imagem_erodida.astype(np.int16)
        diferenca[diferenca < 0] = 0

        # Se entrada é binária (0/1), escalar para 0/255 para ficar visível
        if imagem_original.max() <= 1 and imagem_erodida.max() <= 1:
                diferenca = diferenca * 255

        contornos_uint8 = np.clip(diferenca, 0, 255).astype(np.uint8)
        return contornos_uint8

def main():
    imagem_binaria = extrairMatrizBinaria()
    imagem_erodida = aplicarErosao(imagem_binaria)

    imagem_binaria = np.array(imagem_binaria, dtype=np.uint8)
    imagem_erodida = np.array(imagem_erodida, dtype=np.uint8)

    imagem_contornos = extrair_contornos(imagem_binaria, imagem_erodida)
    salvarImagem(imagem_contornos, "extracao_contornos.png")
    salvarImagem(imagem_contornos, "extracao_contornos.png")

if __name__ == "__main__":
    main()
