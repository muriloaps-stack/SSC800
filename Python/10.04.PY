import numpy as np

N = int(input())

mat = []
for _ in range(N):
    linha = list(map(int, input().split()))
    mat.append(linha)   

a = np.array(mat)

diagonal = np.trace(a)

print(diagonal)