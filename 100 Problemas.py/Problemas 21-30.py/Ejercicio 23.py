#23. Implementar y operar con matrices

matriz1= [[0,0,0],[0,0,0],[0,0,0]]
matriz2= [[1,1,1],[1,1,1],[1,1,1]]
for i in range(3):
    for j in range(3):
        if i == j:
            matriz1[i][j] = 1
            matriz2[i][j] = 0
print(f"matriz 1: {matriz1}, matriz 2: {matriz2}")
MatrizCompleta = matriz1 + matriz2
print(MatrizCompleta)

