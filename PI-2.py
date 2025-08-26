def rotulacao(matrix):
    matriz_rotulada = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    proximo_rotulo = 1
    equivalencias = dict()

    for linha in range(len(matrix)):
        for coluna in range(len(matrix[0])):
            if matrix[linha][coluna] == 1 and matriz_rotulada[linha][coluna] == 0:
                rotulo_esquerda = rotulo_cima = 0

                try:
                    rotulo_cima = matriz_rotulada[linha-1][coluna]
                except IndexError:
                    pass

                try:
                    rotulo_esquerda = matriz_rotulada[linha][coluna-1]
                except IndexError:
                    pass

                if rotulo_esquerda == 0 and rotulo_cima == 0:
                    matriz_rotulada[linha][coluna] = proximo_rotulo
                    proximo_rotulo += 1

                elif rotulo_esquerda != 0 and rotulo_cima != 0 and rotulo_esquerda != rotulo_cima:
                    matriz_rotulada[linha][coluna] = min(rotulo_esquerda, rotulo_cima)
                    # Registrar equivalência entre os labels
                    equivalencias.setdefault(rotulo_esquerda, set()).add(rotulo_cima)
                    equivalencias.setdefault(rotulo_cima, set()).add(rotulo_esquerda)

                elif rotulo_esquerda != 0:
                    matriz_rotulada[linha][coluna] = rotulo_esquerda

                elif rotulo_cima != 0:
                    matriz_rotulada[linha][coluna] = rotulo_cima

                elif rotulo_esquerda == rotulo_cima:
                    matriz_rotulada[linha][coluna] = rotulo_esquerda

    print("\nEquivalências de rótulos:")
    for rotulo, equivalentes in equivalencias.items():
        print(f"{rotulo}: {sorted(equivalentes)}")

    # Segunda passagem: substituir labels equivalentes pelo menor label do grupo
    # Construir grupos de equivalência
    def encontrar_representante(rotulo, representantes):
        while representantes[rotulo] != rotulo:
            rotulo = representantes[rotulo]
        return rotulo

    # Inicializa cada rótulo como seu próprio representante
    representantes = {k: k for k in range(1, proximo_rotulo)}

    for rotulo, equivalentes in equivalencias.items():
        for equivalente in equivalentes:
            raiz_rotulo = encontrar_representante(rotulo, representantes)
            raiz_equivalente = encontrar_representante(equivalente, representantes)
            if raiz_rotulo != raiz_equivalente:
                menor = min(raiz_rotulo, raiz_equivalente)
                maior = max(raiz_rotulo, raiz_equivalente)
                representantes[maior] = menor

    # Mapeia cada rótulo ao seu representante final
    mapa_rotulos = {k: encontrar_representante(k, representantes) for k in representantes}

    # Substitui na matriz rotulada
    for linha in range(len(matriz_rotulada)):
        for coluna in range(len(matriz_rotulada[0])):
            if matriz_rotulada[linha][coluna] in mapa_rotulos:
                matriz_rotulada[linha][coluna] = mapa_rotulos[matriz_rotulada[linha][coluna]]

    return matriz_rotulada

def main():
    matriz = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1]
    ]

    print("Matriz original:")
    for linha in matriz:
        print(' '.join(str(x) for x in linha))

    matriz_rotulada = rotulacao(matriz)

    print("\nMatriz rotulada:")
    for linha in matriz_rotulada:
        print(' '.join(str(x) for x in linha))

if __name__ == "__main__":
    main()