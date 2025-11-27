import numpy as np

N, M = map(int, input().split())

mat = []
for _ in range(N):
    linha = list(map(float, input().split()))
    mat.append(linha)

a = np.array(mat)

positivos = np.sum(a > 0)

print(positivos)