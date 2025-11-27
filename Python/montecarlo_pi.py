import random
import math
import matplotlib.pyplot as plt

def distancia(x, y):
    return math.sqrt(x**2 + y**2)

def gerar_pontos(N):
    pontos = []
    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        pontos.append((x, y))
    return pontos

def pontos_no_circulo(pontos):
    dentro = 0
    for (x, y) in pontos:
        if distancia(x, y) <= 1:
            dentro += 1
    return dentro

def estimar_pi(N):
    pontos = gerar_pontos(N)
    dentro = pontos_no_circulo(pontos)
    pi_estimado = 4 * (dentro / N)
    return pi_estimado, pontos

def plotar_pontos(pontos):
    dentro_x = [x for (x, y) in pontos if distancia(x, y) <= 1]
    dentro_y = [y for (x, y) in pontos if distancia(x, y) <= 1]
    fora_x = [x for (x, y) in pontos if distancia(x, y) > 1]
    fora_y = [y for (x, y) in pontos if distancia(x, y) > 1]

    plt.figure(figsize=(6,6))
    plt.scatter(dentro_x, dentro_y, color='blue', s=1, label='Dentro do círculo')
    plt.scatter(fora_x, fora_y, color='red', s=1, label='Fora do círculo')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title('Simulação Monte Carlo para estimar π')
    plt.show()

def main():
    N = int(input())  # sem texto no input
    random.seed(42)
    pi_estimado, pontos = estimar_pi(N)

    print(f"Numero de pontos: {N}")
    print(f"Valor estimado de pi: {pi_estimado:.6f}")

    # plotar_pontos(pontos)  # comente ao enviar no RunCodes

if __name__ == "__main__":
    main()
