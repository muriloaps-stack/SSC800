while True:
    N, M, S = map(int, input().split())
    if N == 0 and M == 0 and S == 0:
        break

    arena = []
    x = y = 0
    # direção: 0=N, 1=L, 2=S, 3=O
    direcao = 0

    for i in range(N):
        linha = list(input().strip())
        arena.append(linha)
        for j in range(M):
            if linha[j] in 'NSLO':
                x, y = i, j
                if linha[j] == 'N': direcao = 0
                elif linha[j] == 'L': direcao = 1
                elif linha[j] == 'S': direcao = 2
                else: direcao = 3   # 'O'
                arena[i][j] = '.'  # vira vazio

    comandos = input().strip()
    coletadas = 0

    # deslocamentos para cada direção
    dx = [-1, 0, 1, 0]  # N L S O
    dy = [0, 1, 0, -1]

    for c in comandos:
        if c == 'D':        # gira direita
            direcao = (direcao + 1) % 4
        elif c == 'E':      # gira esquerda
            direcao = (direcao - 1) % 4
        else:  # 'F'
            nx = x + dx[direcao]
            ny = y + dy[direcao]

            # verifica limites e parede
            if 0 <= nx < N and 0 <= ny < M and arena[nx][ny] != '#':
                x, y = nx, ny
                if arena[x][y] == '*':   # achou figurinha
                    coletadas += 1
                    arena[x][y] = '.'    # remove figurinha

    print(coletadas)
