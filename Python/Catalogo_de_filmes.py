# Leitura inicial
N = int(input())

filmes = []

for _ in range(N):
    linha = input().rstrip("\n")
    titulo, genero, ano = linha.split(";")
    filmes.append({
        "Titulo": titulo,
        "Genero": genero,
        "Ano": int(ano)
    })

# Loop das consultas
while True:
    op = int(input())
    
    if op == 4:
        break

    valor = input().rstrip("\n")  # preserva espaços quando necessário

    resultados = []

    # [1] Buscar por gênero (case-insensitive)
    if op == 1:
        alvo = valor.casefold()
        for f in filmes:
            if f["Genero"].casefold() == alvo:
                resultados.append(f["Titulo"])

    # [2] Buscar por ano (igualdade exata)
    elif op == 2:
        ano_busca = int(valor)
        for f in filmes:
            if f["Ano"] == ano_busca:
                resultados.append(f["Titulo"])

    # [3] Buscar substring no título (case-insensitive)
    elif op == 3:
        termo = valor.casefold()
        for f in filmes:
            if termo in f["Titulo"].casefold():
                resultados.append(f["Titulo"])

    # Ordena títulos
    resultados.sort()

    # Se vazio, imprime NENHUM
    if not resultados:
        print("NENHUM")
    else:
        for t in resultados:
            print(t)
