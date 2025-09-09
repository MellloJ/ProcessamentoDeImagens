from PIL import Image
import numpy as np

def extrairMatrizCinza():
    image = Image.open("imagens/ai-generated-8366447_640.jpg")
    image = image.convert("L")  # Convertendo para escala de cinza
    matriz = np.array(image)
    return matriz

def extrairMatrizBinaria(threshold=128):
    """
    Extrai matriz binária (preto e branco) da imagem.
    Pixels >= threshold viram 1 (branco), abaixo viram 0 (preto).
    """
    image = Image.open("imagens/ai-generated-8366447_640.jpg")
    image = image.convert("L")
    matriz = np.array(image)
    matriz_binaria = (matriz >= threshold).astype(np.uint8)
    return matriz_binaria

def salvarImagem(matrizNova, nomeNovaImagem):
    novaImagem = Image.fromarray(matrizNova)  # Convertendo de volta para imagem
    novaImagem.save(f'imagens/{nomeNovaImagem}')
    novaImagem.show()