mat = []
for _ in range(5):
    linha = list(map(int, input().split()))
    mat.append(linha)

maior = mat[0][0]
menor = mat[0][0]
imax = jmax = 0
imin = jmin = 0


for i in range(5):
    for j in range(5):
        if mat[i][j] > maior:
            maior = mat[i][j]
            imax = i
            jmax = j
        if mat[i][j] < menor:
            menor = mat[i][j]
            imin = i
            jmin = j


print(maior, imax, jmax)
print(menor, imin, jmin)