import numpy as np

# lê N e M
N, M = map(int, input().split())

# lê a matriz
mat = []
for _ in range(N):
    linha = list(map(float, input().split()))
    mat.append(linha)

mat = np.array(mat)

# cálculos por coluna (axis=0)
medias = np.mean(mat, axis=0)
minimos = np.min(mat, axis=0)
maximos = np.max(mat, axis=0)

# imprime com 6 casas decimais
print(*[f"{x:.6f}" for x in medias])
print(*[f"{x:.6f}" for x in minimos])
print(*[f"{x:.6f}" for x in maximos])
