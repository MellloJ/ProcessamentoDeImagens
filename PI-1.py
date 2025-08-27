from PIL import Image
import numpy as np

def extrairMatriz():
    image = Image.open("imagens/ai-generated-8366447_640.jpg")
    image = image.convert("L")  # Convertendo para escala de cinza
    matriz = np.array(image)
    return matriz

def interpolaMatriz(matriz, tipoInterpolacao, tipoOperacao):
    novaMatriz = []
    if tipoInterpolacao == "vizinho":
        if tipoOperacao == "ampliacao":
            print("Realizando interpolação vizinho mais próximo para ampliação.")

            # Construindo o a estrutura da nova matriz:
            numLinhas = 2 * len(matriz) - 1
            numColunas = 2 * len(matriz[0]) - 1

            # inicialização da nova Matriz
            novaMatriz = [[0 for _ in range(numColunas)] for _ in range(numLinhas)]

            for i in range(numLinhas):
                for j in range(numColunas):

                    # Valores originais
                    if i % 2 == 0 and j % 2 == 0:

                        currentVal = matriz[i//2][j//2]

                        novaMatriz[i][j] = currentVal

                        try:
                            novaMatriz[i+1][j] = currentVal
                        except IndexError:
                            pass

                        try:
                            novaMatriz[i+1][j+1] = currentVal
                        except IndexError:
                            pass

                        try:
                            novaMatriz[i][j+1] = currentVal
                        except IndexError:
                            pass
            return novaMatriz

        elif tipoOperacao == "reducao":
            print("Realizando interpolação vizinho mais próximo para redução.")
            for i in range(len(matriz)):
                # Se a linha for ímpar, pula para a próxima
                if i % 2 != 0:
                    continue

                novaLinha = []
                for j in range(len(matriz[i])):
                    # Se a coluna for ímpar, pula para a próxima
                    if j % 2 != 0:
                        continue

                    novaLinha.append(matriz[i][j])
                novaMatriz.append(novaLinha)
            return novaMatriz
            
    elif tipoInterpolacao == "bilinear":
        matriz = np.array(matriz, dtype=np.int32)
        
        if tipoOperacao == "ampliacao":
            print("Realizando interpolação bilinear para ampliação.")

            # Construindo o a estrutura da nova matriz:
            numLinhas = 2 * len(matriz) - 1
            numColunas = 2 * len(matriz[0]) - 1

            # inicialização da nova Matriz
            novaMatriz = [[0 for _ in range(numColunas)] for _ in range(numLinhas)]

            # Preenchendo os valores iniciais:
            for i in range(numLinhas):
                for j in range(numColunas):
                    # Valores originais
                    if i % 2 == 0 and j % 2 == 0:
                        novaMatriz[i][j] = matriz[i//2][j//2]

            # Interpolação
            for i in range(numLinhas):
                for j in range(numColunas):

                    # Valores originais
                    if i % 2 == 0 and j % 2 == 0:
                        try:
                            novaMatriz[i][j+1] = (novaMatriz[i][j] + novaMatriz[i][j+2]) // 2
                        except IndexError:
                            pass

                        try:
                            novaMatriz[i+1][j+1] = (novaMatriz[i][j] + novaMatriz[i+2][j] + novaMatriz[i][j+2] + novaMatriz[i+2][j+2]) // 4
                        except IndexError:
                            pass

                        try:
                            novaMatriz[i+1][j] = (novaMatriz[i][j] + novaMatriz[i+2][j]) // 2
                        except IndexError:
                            pass
            return novaMatriz

        elif tipoOperacao == "reducao":
            print("Realizando interpolação bilinear para redução.")

            linhas = len(matriz)
            colunas = len(matriz[0])

            #Duplicando a ultima linha e/ou coluna se os valores não forem pares
            if linhas % 2 != 0:
                matriz.append(matriz[-1][:])  # cópia da última linha
                linhas += 1
            if colunas % 2 != 0:
                for i in range(linhas):
                    matriz[i].append(matriz[i][-1]) # cópia do último elemento de cada linha (coluna nova)
                colunas += 1

            # Cria nova matriz com metade das dimensões
            novaMatriz = [[0 for _ in range(colunas // 2)] for _ in range(linhas // 2)]

            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if i % 2 == 0 and j % 2 == 0:
                        novoValor = (matriz[i][j] + matriz[i][j+1] + matriz[i+1][j] + matriz[i+1][j+1]) // 4

                        novaMatriz[i//2][j//2] = novoValor

            return novaMatriz

def main():
    # print("Quantas linhas a matriz possui?")
    # qtdLinhas = int(input())
    # print("Quantas colunas a matriz possui?")
    # qtdColunas = int(input())

    # matriz =  [[0 for j in range(qtdColunas)] for i in range(qtdLinhas)]

    # for i in range(qtdLinhas):
    #     for j in range(qtdColunas):
    #         print(f"Elemento [{i}][{j}]: ")
    #         matriz[i][j] = int(input())

    # qtdLinhas = 4
    # qtdColunas = 4

    # matriz = [
    #     [20, 40, 40, 20],
    #     [40, 20, 54, 30],
    #     [60, 30, 80, 40],
    #     [70, 70, 20, 60]
    # ]

    matriz = extrairMatriz()

    qtdLinhas = len(matriz)
    qtdColunas = len(matriz[0])

    print("Matriz: ")
    # for i in range(qtdLinhas):
    #     for j in range(qtdColunas):
    #         print(matriz[i][j], end=" ")
    #     print()

    print("Escolha a interpolação a ser realizada:")
    print("1 - Interpolação Vizinho mais proximo")
    print("2 - Interpolação Bilinear")
    interpolacaoSelecionada = int(input()) 

    print("Selecione a opção de interpolação:")
    print("1 - Ampliação")
    print("2 - Redução")
    opcaoInterpolacao = int(input())

    matrizNova = None
    match interpolacaoSelecionada:
        case 1:
            print("Interpolação Vizinho mais proximo selecionada.")
            if opcaoInterpolacao == 1:
                matrizNova = interpolaMatriz(matriz, "vizinho", "ampliacao")
            if opcaoInterpolacao == 2:
                matrizNova = interpolaMatriz(matriz, "vizinho", "reducao")
        case 2:
            print("Interpolação Bilinear selecionada.")
            if opcaoInterpolacao == 1:
                matrizNova = interpolaMatriz(matriz, "bilinear", "ampliacao")
            if opcaoInterpolacao == 2:
                matrizNova = interpolaMatriz(matriz, "bilinear", "reducao")
        case _:
            print("Interpolação inválida.")

    print("\nMatriz original:")
    # for linha in matriz:
    #     print(' '.join(str(x) for x in linha))

    print("\nNova matriz:")
    if matrizNova is not None:
        interpolacao = "vizinho" if interpolacaoSelecionada == 1 else "bilinear"
        operacao = "ampliacao" if opcaoInterpolacao == 1 else "reducao"

        nomeNovaImagem = f'/imagem_{operacao}_{interpolacao}.jpg'

        # Convertendo a matriz em um array NumPy para poder gerar e exibir a imagem novamente
        matrizNova = np.array(matrizNova, dtype=np.uint8)

        # for linha in matrizNova:
        #     print(' '.join(str(x) for x in linha))

        novaImagem = Image.fromarray(matrizNova)  # Convertendo de volta para imagem
        novaImagem.save(f'imagens/{nomeNovaImagem}')
        novaImagem.show()
    else:
        print("Nenhuma matriz nova gerada.")

if __name__ == "__main__":
    main()