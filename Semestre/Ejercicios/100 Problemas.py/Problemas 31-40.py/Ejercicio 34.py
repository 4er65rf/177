#34. Calcular la inversa de una matriz.

def inversa_matriz(matriz):
    """
    Calcula la inversa de una matriz 2x2.
    """
    if len(matriz) != 2 or len(matriz[0]) != 2 or len(matriz[1]) != 2:
        raise ValueError("La matriz debe ser de tamaño 2x2.")

    determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    if determinante == 0:
        raise ValueError("La matriz no tiene inversa (determinante cero).")

    inversa = [
        [matriz[1][1] / determinante, -matriz[0][1] / determinante],
        [-matriz[1][0] / determinante, matriz[0][0] / determinante]
    ]

    return inversa