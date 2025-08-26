def interpolaMatriz(matriz, tipoInterpolacao, tipoOperacao):
    novaMatriz = []
    if tipoInterpolacao == "vizinho":
        if tipoOperacao == "ampliacao":
            print("Realizando interpolação vizinho mais próximo para ampliação.")
            

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

print("Quantas linhas a matriz possui?")
qtdLinhas = int(input())
print("Quantas colunas a matriz possui?")
qtdColunas = int(input())

matriz =  [[] for i in range(qtdLinhas)]

for i in range(qtdLinhas):
    for j in range(qtdColunas):
        print(f"Elemento [{i}][{j}]: ")
        matriz[i][j] = int(input())

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

match interpolacaoSelecionada:
    case 1:
        print("Interpolação Vizinho mais proximo selecionada.")
        if opcaoInterpolacao == 1:
            interpolaMatriz(matriz, "vizinho", "ampliacao")
    case 2:
        print("Interpolação Bilinear selecionada.")
    case _:
        print("Interpolação inválida.")

match opcaoInterpolacao:
    case 1:
        print("Ampliação selecionada.")
    case 2:
        print("Redução selecionada.")
    case _:
        print("Opção de interpolação inválida.")