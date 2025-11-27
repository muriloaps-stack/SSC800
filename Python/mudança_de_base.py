import numpy as np
import sys


try:
    c1_coords = list(map(int, input().split()))
    c2_coords = list(map(int, input().split()))
    c3_coords = list(map(int, input().split()))
except Exception:
    
    sys.exit()

# Monta a matriz C -> B (cada vetor c1,c2,c3 como coluna)
dados = [c1_coords, c2_coords, c3_coords]
matriz_C_para_B = np.array(dados).T

# Configura impressão (para a matriz inversa)
np.set_printoptions(precision=5, suppress=True)


try:
    matriz_B_para_C = np.linalg.inv(matriz_C_para_B)
except np.linalg.LinAlgError:
    print('Erro: A matriz de entrada não é invertível (vetores L.D.).')
    sys.exit()

print('--- Matriz de C para B ---')
print(matriz_C_para_B)
print()
print('--- Matriz de B para C ---')
print(matriz_B_para_C)
