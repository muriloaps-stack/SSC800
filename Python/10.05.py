import numpy as np

# --- Entrada ---
N, M = map(int, input().split())

valores = []
for _ in range(N):
    valores.extend(map(int, input().split()))

K = int(input())

# --- Verificação de perda de elementos ---
total_original = N * M
total_novo = K * K

if total_original != total_novo:
    print("Aviso: perda de elementos no reshape")
    # manter somente os primeiros K*K elementos
    valores = valores[:total_novo]

# --- Reshape ---
mat = np.array(valores).reshape(K, K)

# --- Transposição ---
mat_transposta = mat.T

# --- Saída ---
for linha in mat_transposta:
    print(*linha)
