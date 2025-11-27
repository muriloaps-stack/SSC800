DROP DATABASE IF EXISTS supermercado;
CREATE DATABASE supermercado;
USE supermercado;

-- Produtos cadastrados
CREATE TABLE produtos (
    codigo_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL DEFAULT 0
);

-- Vendas realizadas
CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL,
    total_produtos DECIMAL(10,2) NOT NULL,
    total_boletos DECIMAL(10,2) NOT NULL
);

-- Itens vendidos (detalhe dos produtos)
CREATE TABLE itens_venda (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT NOT NULL,
    codigo_produto INT NOT NULL,
    quantidade INT NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_venda) REFERENCES vendas(id_venda),
    FOREIGN KEY (codigo_produto) REFERENCES produtos(codigo_produto)
);


-- Boletos pagos junto com a venda
CREATE TABLE boletos_venda (
    id_boleto INT AUTO_INCREMENT PRIMARY KEY,
    id_venda INT NOT NULL,
    descricao VARCHAR(60) NOT NULL,        -- Ex.: "Energia e Gás"
    valor DECIMAL(10,2) NOT NULL,
    codigo_boleto VARCHAR(60) NOT NULL,    -- Código FEBRABAN completo (44 ou 48 dígitos)
    segmento INT NOT NULL,                 -- Código do segmento (1-9 conforme FEBRABAN)
    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_venda) REFERENCES vendas(id_venda)
);


-- Produtos iniciais
INSERT INTO produtos (nome, preco) VALUES
("Refrigerante Coca-Cola Lata 350ml", 4.50),
("Salgadinho Doritos Pacote 300g", 8.50),
("Biscoito Recheado Trakinas Chocolate 126g", 1.80),
("Cerveja Skol 350ml", 4.20);
