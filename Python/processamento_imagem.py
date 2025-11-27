import numpy as np
import imageio.v3 as iio
import sys

def aplicar_luminancia(img):
    """
    Converte uma imagem RGB para tons de cinza usando a fórmula de luminância.
    Se a imagem já for grayscale, retorna a própria imagem.
    """
    # Verifica se a imagem é colorida (3 dimensões: H, W, Canais)
    if img.ndim == 3:
        # Extrai os canais R, G, B
        R = img[:, :, 0]
        G = img[:, :, 1]
        B = img[:, :, 2]
        
        # Aplica a fórmula de luminância
        L = 0.2126 * R + 0.7152 * G + 0.0722 * B
        
        # Converte o resultado para uint8 (inteiro de 8 bits, 0-255)
        return L.astype(np.uint8)
    
    # Se a imagem já for grayscale (2 dimensões: H, W), não faz nada
    return img

def aplicar_downsampling(img, P):
    """
    Reduz a resolução da imagem selecionando pixels a cada P posições.
    """
    # Usa slicing do NumPy para pegar linhas e colunas
    # ::P significa "comece do início, vá até o fim, com passo P"
    return img[::P, ::P]

def aplicar_mirror(img, E):
    """
    Espelha a imagem horizontalmente ('H') ou verticalmente ('V').
    """
    if E == 'H':
        # Inverte a ordem das colunas (espelhamento horizontal)
        return img[:, ::-1]
    elif E == 'V':
        # Inverte a ordem das linhas (espelhamento vertical)
        return img[::-1, :]
    return img

def aplicar_gamma(img, F):
    """
    Aplica a correção gama na imagem.
    """
    # 1. Converte a imagem para float64 para precisão nos cálculos
    img_float = img.astype(np.float64)
    
    # 2. Normaliza a imagem (valores de 0.0 a 1.0)
    img_normalizada = img_float / 255.0
    
    # 3. Aplica a fórmula da correção gama
    img_corrigida = 255.0 * (img_normalizada ** (1.0 / F))
    
    # 4. Converte de volta para uint8, truncando os valores
    return img_corrigida.astype(np.uint8)

def aplicar_quantizacao(img, B):
    """
    Reduz a resolução radiométrica (número de tons) para 2^B níveis.
    """
    # Calcula quantos bits 'menos significativos' devem ser removidos
    bits_para_remover = 8 - B
    
    # 1. Desloca os bits para a direita (removendo os menos significativos)
    # 2. Desloca os bits de volta para a esquerda (preenchendo com zeros)
    img_quantizada = (img >> bits_para_remover) << bits_para_remover
    
    return img_quantizada

def main():
    """
    Função principal que lê a entrada, processa a imagem e imprime a saída.
    """
    try:
        # --- 1. Leitura da Entrada ---
        
        # Lê o nome do arquivo da imagem
        nome_arquivo = input()
        
        # Lê o número de operações
        N = int(input())
        
        # --- 2. Carregamento da Imagem ---
        
        # Carrega a imagem usando imageio
        # 'camera.png' é uma imagem de exemplo padrão no imageio
        img = iio.imread(nome_arquivo)
        
        # --- 3. Processamento das Operações ---
        
        for _ in range(N):
            # Lê a linha da operação e divide em partes
            linha_op = input().split()
            operacao = linha_op[0]
            
            if operacao == "LUMINANCE":
                img = aplicar_luminancia(img)
            
            elif operacao == "DOWNSAMPLING":
                P = int(linha_op[1])
                img = aplicar_downsampling(img, P)
                
            elif operacao == "MIRROR":
                E = linha_op[1]
                img = aplicar_mirror(img, E)
                
            elif operacao == "GAMMA":
                F = float(linha_op[1])
                img = aplicar_gamma(img, F)
                
            elif operacao == "QUANTIZATION":
                B = int(linha_op[1])
                img = aplicar_quantizacao(img, B)
        
        # --- 4. Cálculo das Estatísticas ---
        
        # Verifica se a imagem resultante não está vazia
        if img.size == 0:
            print("Erro: A imagem resultante está vazia após as operações.")
            return

        media = np.mean(img)
        desvio = np.std(img, ddof=0) # ddof=0 para desvio padrão populacional
        minimo = np.min(img)
        maximo = np.max(img)
        
        # Encontra o número de valores únicos de intensidade
        tons_unicos = len(np.unique(img))
        
        # Obtém as dimensões (Altura x Largura)
        H, W = img.shape
        
        # --- 5. Impressão da Saída ---
        
        print(f"Intensidade média: {media:.2f} | Desvio: {desvio:.2f}")
        print(f"Intensidade mínima: {minimo} | Intensidade máxima: {maximo}")
        print(f"Tons únicos: {tons_unicos}")
        print(f"Dimensão: {H} x {W}")

    except EOFError:
        pass # Fim da entrada
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}", file=sys.stderr)

# Executa a função main quando o script for rodado
if __name__ == "__main__":
    main()