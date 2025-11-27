import urllib.request
from html.parser import HTMLParser
import unicodedata
import sys

def normalizar(texto):
    """
    Remove acentos, converte para minúsculas e remove espaços extras
    nas bordas.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn'
                  ).strip().lower()

# --- Variáveis globais para controlar o estado do parser ---
# O parser vai modificar estas variáveis à medida que lê o HTML
horarios = {}
capturando = None       # Pode ser '1', '2' ou None
dentro_strong = False   # Flag para saber se estamos dentro de uma tag <strong>

class Parser(HTMLParser):
    """
    Parser customizado para extrair os horários dos bandecos.
    Ele procura por tags <strong> contendo 'unidade area 1' ou 'unidade area 2'
    e captura todo o texto que vem depois, até encontrar a próxima tag <strong>.
    """
    
    def handle_starttag(self, tag, attrs):
        global dentro_strong
        # Quando encontramos <strong>, ativamos a flag
        if tag == "strong":
            dentro_strong = True

    def handle_endtag(self, tag):
        global dentro_strong
        # Quando saímos de <strong>, desativamos a flag
        if tag == "strong":
            dentro_strong = False

    def handle_data(self, data):
        global capturando, horarios, dentro_strong
        
        # Limpa o texto: substitui non-breaking space (xa0) e remove espaços
        texto = data.replace('\xa0', ' ').strip()

        # Ignora strings de texto vazias
        if not texto:
            return

        # 1. Procura por Títulos (que estão dentro de <strong>)
        if dentro_strong:
            t_norm = normalizar(texto)
            
            # Se acharmos o título da Área 1, começamos a capturar para '1'
            if "unidade area 1" in t_norm:
                capturando = "1"
                horarios[capturando] = "" # Inicia/limpa a string de horários
                return
            
            # Se acharmos o título da Área 2, começamos a capturar para '2'
            elif "unidade area 2" in t_norm:
                capturando = "2"
                horarios[capturando] = "" # Inicia/limpa a string de horários
                return
            
            # Se já estávamos capturando e achamos outro título 
            # (ex: CRHEA, Moradia), paramos a captura.
            elif capturando and ("crhea" in t_norm or "moradia estudantil" in t_norm):
                capturando = None
                return
                
        # 2. Se estamos no "modo de captura", anexamos o texto
        if capturando:
            # Adiciona o texto ao dicionário e uma quebra de linha
            horarios[capturando] += texto + "\n"

def main():
    """
    Função principal: busca o HTML, executa o parser e imprime o resultado
    com base na entrada do usuário.
    """
    try:
        # --- 1. Obter o HTML ---
        url = "https://www.puspsc.usp.br/transporte-alimentacao-e-moradia/"
        # O user-agent é adicionado para simular um navegador,
        # alguns sites bloqueiam requisições de scripts.
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            html = response.read().decode("utf-8")

        # --- 2. Processar o HTML ---
        parser = Parser()
        parser.feed(html)

        # --- 3. Limpar os dados ---
        # Remove quebras de linha extras no início ou fim de cada bloco
        for k in horarios:
            horarios[k] = horarios[k].strip()

        # --- 4. Obter entrada do usuário ---
        campus_escolhido = input()

        # --- 5. Imprimir a Saída ---
        if campus_escolhido in horarios:
            print(horarios[campus_escolhido])
        else:
            print(f"Erro: Campus '{campus_escolhido}' não encontrado nos dados.", file=sys.stderr)

    except urllib.error.URLError as e:
        print(f"Erro ao acessar a URL: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}", file=sys.stderr)

# Executa a função main quando o script for rodado
if __name__ == "__main__":
    main()