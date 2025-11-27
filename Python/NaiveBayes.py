import json
import NaiveBayes
import sys

stopwords = {
    "o", "a", "os", "as", "um", "uma", "uns", "umas",
    "ele", "ela", "eles", "elas", "meu", "minha", "teu", "tua", "seu", "sua",
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "por", "para", "com", "sem", "sobre",
    "e", "ou", "mas", "porque", "que", "como", "quando", "se"
}
pontuacao_para_remover = ".,!?;:"

def filtrar_frase(frase):
    """
    Limpa uma frase: minúsculas, sem pontuação e sem stopwords.
    """
    palavras = frase.lower().split()
    filtradas = []
    for p in palavras:
        p = p.strip(pontuacao_para_remover)
        if p and p not in stopwords:
            filtradas.append(p)
    return " ".join(filtradas)

def filtrar_dados_treino(dados):
    """
    Aplica a filtragem a todas as frases do dicionário de treino.
    """
    filtrado = {}
    for classe, frases in dados.items():
        filtrado[classe] = [filtrar_frase(f) for f in frases]
    return filtrado

def main():
    try:
        # Lê as duas linhas de entrada
        dados_json = sys.stdin.readline().strip()
        frase_classificar = sys.stdin.readline().strip()

        # Converte o JSON e filtra
        dados_treino_bruto = json.loads(dados_json)
        dados_treino = filtrar_dados_treino(dados_treino_bruto)

        # Filtra também a frase de teste
        frase_filtrada = filtrar_frase(frase_classificar)

        # Treina o classificador
        classificador = NaiveBayes.Classifier(dados_treino)

        # Classifica e imprime no formato exato
        resultado = classificador.classify(frase_filtrada)
        print(f"classificacao: {resultado}")

    except EOFError:
        pass

if __name__ == "__main__":
    main()
