# Lê número de pessoas
N = int(input())

# Dicionário: chave = nome em minúsculas, valor = conjunto de cartas
pessoas = {}

for _ in range(N):
    linha = input().strip().split()
    nome = linha[0]
    cartas = set(linha[1:])  # conjunto de cartas
    pessoas[nome.lower()] = cartas

# Função para obter string do nome da operação
def nome_operacao(cmd):
    if cmd == 'U':
        return 'UNIAO'
    elif cmd == 'I':
        return 'INTERSECAO'
    elif cmd == 'D':
        return 'DIFERENCA'
    elif cmd == 'S':
        return 'DIFERENCA_SIMETRICA'

# Processamento das consultas
while True:
    consulta = input().strip()
    if consulta == "FIM":
        break

    partes = consulta.split()
    if len(partes) != 3:
        # Caso estranho, mas não deve ocorrer segundo o enunciado
        print("CONSULTA COM COMANDO INVALIDO")
        continue

    nome1, comando, nome2 = partes
    nome1_lower = nome1.lower()
    nome2_lower = nome2.lower()

    # 1) Validar nomes
    if nome1_lower not in pessoas or nome2_lower not in pessoas:
        print("CONSULTA COM NOME INVALIDO")
        continue

    # 2) Validar comando
    if comando not in ['U', 'I', 'D', 'S']:
        print("CONSULTA COM COMANDO INVALIDO")
        continue

    # Recuperar conjuntos
    conj1 = pessoas[nome1_lower]
    conj2 = pessoas[nome2_lower]

    # 3) Operações
    if comando == 'U':
        resultado = conj1 | conj2
    elif comando == 'I':
        resultado = conj1 & conj2
    elif comando == 'D':
        resultado = conj1 - conj2
    elif comando == 'S':
        resultado = conj1 ^ conj2

    # Ordenar resultado lexicograficamente
    resultado_ordenado = sorted(resultado)

    # Se vazio, imprimir "VAZIO"
    if len(resultado_ordenado) == 0:
        resultado_str = "VAZIO"
    else:
        resultado_str = " ".join(resultado_ordenado)

    # Imprimir saída no formato pedido
    print(f"{nome1} {nome_operacao(comando)} {nome2} : {resultado_str}")
