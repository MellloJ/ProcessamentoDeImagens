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
                    novaLinha.append(matriz[i][j])
                novaMatriz.append(novaLinha)
            return novaMatriz
            
    elif tipoInterpolacao == "bilinear":
        if tipoOperacao == "ampliacao":
            print("Realizando interpolação bilinear para ampliação.")
        elif tipoOperacao == "reducao":
            print("Realizando interpolação bilinear para redução.")

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

    qtdLinhas = 4
    qtdColunas = 4

    matriz = [
        [20, 40, 40, 20],
        [40, 20, 54, 30],
        [60, 30, 80, 40],
        [70, 70, 20, 60]
    ]

    print("Matriz: ")
    for i in range(qtdLinhas):
        for j in range(qtdColunas):
            print(matriz[i][j], end=" ")
        print()

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
    for linha in matriz:
        print(' '.join(str(x) for x in linha))

    print("\nNova matriz:")
    if matrizNova is not None:
        for linha in matrizNova:
            print(' '.join(str(x) for x in linha))
    else:
        print("Nenhuma matriz nova gerada.")

if __name__ == "__main__":
    main()