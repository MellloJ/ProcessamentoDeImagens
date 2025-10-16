from commons import extrairMatrizBinaria, salvarImagem
import numpy as np

# Elemento estruturante em cruz 3x3
structuring_element = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

def aplicarDilatacao(imagemBinaria):
    alturaImagem = len(imagemBinaria)
    larguraImagem = len(imagemBinaria[0])
    imagemDilatada = [[0 for _ in range(larguraImagem)] for _ in range(alturaImagem)]
    
    for linha in range(alturaImagem):
        for coluna in range(larguraImagem):
            if imagemBinaria[linha][coluna] == 1:
                # Verifica o elemento estruturante centrado em (linha,coluna)
                for indiceLinhaSE in range(len(structuring_element)):
                    for indiceColunaSE in range(len(structuring_element[0])):
                        if structuring_element[indiceLinhaSE][indiceColunaSE] == 1:
                            novaLinha = linha + indiceLinhaSE - 1  # Centro do SE está em (1,1)
                            novaColuna = coluna + indiceColunaSE - 1
                            if 0 <= novaLinha < alturaImagem and 0 <= novaColuna < larguraImagem:
                                imagemDilatada[novaLinha][novaColuna] = 1
    return imagemDilatada

def aplicarErosao(imagemBinaria):
    alturaImagem = len(imagemBinaria)
    larguraImagem = len(imagemBinaria[0])
    imagemErodida = [[0 for _ in range(larguraImagem)] for _ in range(alturaImagem)]
    
    for linha in range(alturaImagem):
        for coluna in range(larguraImagem):
            ehValido = True
            for indiceLinhaSE in range(len(structuring_element)):
                for indiceColunaSE in range(len(structuring_element[0])):
                    if structuring_element[indiceLinhaSE][indiceColunaSE] == 1:
                        novaLinha = linha + indiceLinhaSE - 1  # Centro do SE está em (1,1)
                        novaColuna = coluna + indiceColunaSE - 1
                        if 0 <= novaLinha < alturaImagem and 0 <= novaColuna < larguraImagem:
                            if imagemBinaria[novaLinha][novaColuna] != 1:
                                ehValido = False
                                break
                        else:
                            ehValido = False
                if not ehValido:
                    break
            if ehValido:
                imagemErodida[linha][coluna] = 1
    return imagemErodida

def print_image(matrizImagem):
    for linha in matrizImagem:
        print(' '.join(str(pixel) for pixel in linha))

def main():
    imagemBinaria = extrairMatrizBinaria().tolist() 
    
    print("Imagem original:")
    print_image(imagemBinaria)
    
    print("\nSelecione a operação morfológica:")
    print("1 - Dilatação")
    print("2 - Erosão")
    escolha = int(input())
    
    imagemResultado = None
    nomeOperacao = ""
    if escolha == 1:
        imagemResultado = aplicarDilatacao(imagemBinaria)
        nomeOperacao = "dilatacao"
    elif escolha == 2:
        imagemResultado = aplicarErosao(imagemBinaria)
        nomeOperacao = "erosao"
    else:
        print("Opção inválida.")
        return
    
    print(f"\nImagem {nomeOperacao}:")
    print_image(imagemResultado)
    
    # Converte para 0/255 e salva a imagem
    imagemResultadoNp = np.array(imagemResultado, dtype=np.uint8) * 255
    salvarImagem(imagemResultadoNp, f"{nomeOperacao}_cruz.png")

if __name__ == "__main__":
    main()