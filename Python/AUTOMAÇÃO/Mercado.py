import mysql.connector

# Função para conectar ao banco de dados MySQL
def conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='supermercado'
    )

# Função para registrar entrada de lote (ex: L010025 → Produto 01, +25 unidades)
def registrar_lote(cod):
    try:
        id_prod = int(cod[1:3])       # Extrai o código do produto (2 dígitos após 'L')
        qtd = int(cod[3:])            # Extrai a quantidade
    except ValueError:
        print("Erro: código de lote inválido.")
        return

    con = conectar()
    cur = con.cursor()
    try:
        # Verifica se o produto existe
        cur.execute("SELECT nome FROM produtos WHERE codigo_produto = %s", (id_prod,))
        prod = cur.fetchone()
        if not prod:
            print(f"Produto {id_prod:02d} não encontrado.")
            return

        # Atualiza a quantidade em estoque
        cur.execute("UPDATE produtos SET quantidade = quantidade + %s WHERE codigo_produto = %s", (qtd, id_prod))
        con.commit()
        print(f"Lote registrado: +{qtd} unidades de {prod[0]}.")
    except mysql.connector.Error as e:
        print(f"Erro no banco: {e}")
    finally:
        cur.close()
        con.close()

# Função para adicionar produto ao carrinho (ex: P01)
def adicionar_produto(cod, cesta):
    try:
        id_prod = int(cod[1:])  # Extrai o código do produto (após 'P')
    except ValueError:
        print("Erro: código de produto inválido.")
        return

    con = conectar()
    cur = con.cursor()
    try:
        # Busca nome, preço e estoque do produto
        cur.execute("SELECT nome, preco, quantidade FROM produtos WHERE codigo_produto = %s", (id_prod,))
        info = cur.fetchone()
        if not info:
            print("Produto não encontrado.")
            return

        nome, valor, estoque = info
        if estoque <= 0:
            print(f"Produto sem estoque: {nome}")
            return

        # Atualiza o estoque no banco
        cur.execute("UPDATE produtos SET quantidade = quantidade - 1 WHERE codigo_produto = %s", (id_prod,))

        # Adiciona ao carrinho (ou atualiza se já existir)
        if id_prod in cesta:
            cesta[id_prod]['qtd'] += 1
            cesta[id_prod]['subtotal'] += float(valor)
        else:
            cesta[id_prod] = {
                'nome': nome,
                'qtd': 1,
                'unitario': float(valor),
                'subtotal': float(valor)
            }

        con.commit()
        print(f"Adicionado ao carrinho: {nome} (R$ {valor:.2f})")
    except mysql.connector.Error as e:
        print(f"Erro no banco: {e}")
    finally:
        cur.close()
        con.close()

# Função para processar boletos FEBRABAN (44 ou 48 dígitos, iniciados com '8')
def processar_febraban(cod, boletos):
    # Remove caracteres não numéricos
    numerico = ''.join(d for d in cod if d.isdigit())

    # Se for linha digitável (48 dígitos), converte para código de barras (44)
    if len(numerico) == 48:
        numerico = numerico[0:11] + numerico[12:23] + numerico[24:35] + numerico[36:47]

    # Verifica validade do código
    if len(numerico) != 44 or numerico[0] != '8':
        print(f"Erro: boleto inválido. Código lido ({len(numerico)} dígitos): {numerico}")
        return

    # Determina o tipo de segmento com base no segundo dígito
    tipo = int(numerico[1])
    if tipo == 1:
        origem = 'Prefeituras'
    elif tipo == 2:
        origem = 'Saneamento'
    elif tipo == 3:
        origem = 'Energia e Gás'
    elif tipo == 4:
        origem = 'Telecomunicações'
    elif tipo == 5:
        origem = 'Órgãos Públicos'
    elif tipo == 6:
        origem = 'Carnês'
    elif tipo == 7:
        origem = 'Multas de Trânsito'
    elif tipo == 9:
        origem = 'Uso Bancário'
    else:
        origem = 'Outros'

    # Se o terceiro dígito for '6', o valor está presente entre as posições 4 a 14
    if numerico[2] == '6':
        valor = int(numerico[4:15]) / 100
    else:
        valor = 0.0

    # Armazena o boleto na lista
    boletos.append({
        'origem': origem,
        'valor': float(valor),
        'codigo': numerico,
        'segmento': tipo
    })

    print(f"Conta adicionada: {origem} - R$ {valor:.2f}")

# Finaliza a venda, registra no banco e imprime o resumo
def concluir_venda(cesta, boletos):
    if not cesta and not boletos:
        print("Nenhum item para finalizar.")
        return

    total_produtos = sum(float(item['subtotal']) for item in cesta.values())
    total_boletos = sum(float(b['valor']) for b in boletos)
    total_geral = total_produtos + total_boletos

    con = conectar()
    cur = con.cursor()
    try:
        # Registra o total da venda
        cur.execute("""
            INSERT INTO vendas (total, total_produtos, total_boletos)
            VALUES (%s, %s, %s)
        """, (total_geral, total_produtos, total_boletos))
        venda_id = cur.lastrowid

        # Registra cada item de produto
        for id_prod, item in cesta.items():
            cur.execute("""
                INSERT INTO itens_venda (id_venda, codigo_produto, quantidade, subtotal)
                VALUES (%s, %s, %s, %s)
            """, (venda_id, id_prod, item['qtd'], item['subtotal']))

        # Registra cada boleto FEBRABAN
        for b in boletos:
            cur.execute("""
                INSERT INTO boletos_venda (id_venda, descricao, valor, codigo_boleto, segmento)
                VALUES (%s, %s, %s, %s, %s)
            """, (venda_id, b['origem'], b['valor'], b['codigo'], b['segmento']))

        con.commit()

        # Mostra resumo da compra
        print("\n--- COMPRA FINALIZADA ---")
        if cesta:
            print("\nProdutos:")
            for item in cesta.values():
                print(f"{item['nome']} - Qtde: {item['qtd']} - Subtotal: R$ {item['subtotal']:.2f}")
        if boletos:
            print("\nBoletos:")
            for b in boletos:
                print(f"{b['origem']} - Código: {b['codigo']} - Valor: R$ {b['valor']:.2f}")
        print(f"\nTOTAL PRODUTOS: R$ {total_produtos:.2f}")
        print(f"TOTAL BOLETOS: R$ {total_boletos:.2f}")
        print(f"TOTAL GERAL:   R$ {total_geral:.2f}\n")
    except mysql.connector.Error as e:
        print(f"Erro ao finalizar venda: {e}")
    finally:
        cur.close()
        con.close()

# Função para limpar uma linha digitável (remove traços, espaços, etc.)
def limpar_codigo(linha):
    return ''.join(c for c in linha if c.isdigit())

# Interface principal do sistema
def main():
    cesta = {}       # Dicionário de produtos adicionados ao carrinho
    boletos = []     # Lista de boletos FEBRABAN lidos

    print("\nSistema iniciado. Aguardando leituras...")
    print("- Use L<codigo><qtd> para entrada de lote (ex: L010025)")
    print("- Use P<codigo> para adicionar produto ao carrinho (ex: P01)")
    print("- Use boleto FEBRABAN (44 ou 48 dígitos começando com 8) para adicionar contas")
    print("- Digite 'fim' para finalizar compra")
    print("- Digite 'sair' para encerrar execução do sistema\n")

    while True:
        entrada = input("→ Entrada: ").strip()
        
        if entrada.lower() == 'fim':
            if cesta or boletos:
                concluir_venda(cesta, boletos)
                cesta.clear()
                boletos.clear()
            else:
                print("Carrinho vazio. Nada a finalizar.")
            continue     

        # Entrada de lote
        if entrada.startswith('L') and len(entrada) == 7:
            registrar_lote(entrada)

        # Adicionar produto
        elif entrada.startswith('P') and len(entrada) == 3:
            adicionar_produto(entrada, cesta)

        # Processar boleto FEBRABAN (aceita 44 ou 48 dígitos iniciando com 8)
        elif entrada.startswith("8"):
            if len(entrada) != 44:
                entrada = limpar_codigo(entrada)
            processar_febraban(entrada, boletos)

        # Encerrar sistema
        elif entrada.lower() == "sair":
            break

        else:
            print("Entrada inválida. Verifique o formato.")

# Executa a interface principal
if __name__ == "__main__":
    main()
