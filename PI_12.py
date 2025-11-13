from commons import extrairMatrizCinza, salvarImagem
import numpy as np

def filtro_sobel(matriz_cinza):
    """
    Aplica o Filtro de Sobel (detector de bordas) em uma matriz de imagem 
    em escala de cinza.
    """
    
    kernel_x = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    
    kernel_y = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]
    
    altura = len(matriz_cinza)
    largura = len(matriz_cinza[0])
    
    matriz_sobel = []
    for _ in range(altura):
        matriz_sobel.append([0] * largura)

    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            
            soma_x = 0
            soma_y = 0
            
            for ki in range(3):
                for kj in range(3):
                    pixel_i = i + ki - 1
                    pixel_j = j + kj - 1

                    valor_pixel = int(matriz_cinza[pixel_i][pixel_j])
                    
                    soma_x += valor_pixel * kernel_x[ki][kj]
                    soma_y += valor_pixel * kernel_y[ki][kj]
            
            # M(x,y) ≈ |gx| + |gy|
            # magnitude = abs(soma_x) + abs(soma_y)

            # M(x,y) root(gx² + gy²)
            magnitude = (soma_x ** 2 + soma_y ** 2) ** 0.5
            
            if magnitude > 255:
                magnitude = 255
            
            matriz_sobel[i][j] = int(magnitude)
            
    return matriz_sobel

def main():
    # Carrega a imagem de entrada e extrai a matriz de pixels
    try:
        matriz_original = extrairMatrizCinza()
    except FileNotFoundError:
        print("Erro: Arquivo de imagem não encontrado. Verifique o caminho.")
        return
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return

    # Aplica o filtro de Sobel para detectar bordas
    matriz_bordas = filtro_sobel(matriz_original)

    # Salva a imagem resultante
    salvarImagem(np.array(matriz_bordas, dtype=np.uint8), "imagem_sobel.png")
    print("Imagem com Filtro de Sobel salva como 'imagem_sobel.png'")

if __name__ == "__main__":
    main()