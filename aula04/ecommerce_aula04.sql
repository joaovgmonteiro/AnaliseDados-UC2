-- ============================================
-- 1. HABILITAR IMPORTAÇÃO LOCAL
-- ============================================
-- SET GLOBAL local_infile = 1;
-- OPT_LOCAL_INFILE=1

-- ============================================
-- 2. CRIAR BANCO DE DADOS
-- ============================================
DROP DATABASE IF EXISTS ecommerce_aula04;
CREATE DATABASE ecommerce_aula04;
USE ecommerce_aula04;

-- ============================================
-- 3. CRIAÇÃO DAS TABELAS
-- ============================================

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    telefone VARCHAR(20),
    data_cadastro DATE NOT NULL
);

CREATE TABLE enderecos (
    id_endereco INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    logradouro VARCHAR(150),
    numero VARCHAR(10),
    cidade VARCHAR(80),
    estado VARCHAR(2),
    cep VARCHAR(10),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL
);

CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    id_categoria INT NOT NULL,
    estoque INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_pedido DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE itens_pedido (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

CREATE TABLE pagamentos (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    metodo VARCHAR(30) NOT NULL,
    data_pagamento DATETIME NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);

-- ============================================
-- 4. IMPORTAÇÃO DOS ARQUIVOS CSV
-- ============================================

-- CLIENTES
LOAD DATA LOCAL INFILE 'C:\\dados_ecommerce\\clientes.csv'
INTO TABLE clientes
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(nome, email, telefone, data_cadastro);

-- ENDEREÇOS
LOAD DATA LOCAL INFILE 'C:\\dados_ecommerce\\enderecos.csv'
INTO TABLE enderecos
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(id_cliente, logradouro, numero, cidade, estado, cep);

-- CATEGORIAS
LOAD DATA LOCAL INFILE 'C:\\dados_ecommerce\\categorias.csv'
INTO TABLE categorias
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(nome);

-- PRODUTOS
LOAD DATA LOCAL INFILE 'C:\\dados_ecommerce\\produtos.csv'
INTO TABLE produtos
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(nome, preco, id_categoria, estoque);

-- PEDIDOS
LOAD DATA LOCAL INFILE 'C:\\dados_ecommerce\\pedidos.csv'
INTO TABLE pedidos
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(id_cliente, data_pedido, status);

-- ITENS DO PEDIDO
LOAD DATA LOCAL INFILE 'C:\\dados_ecommerce\\itens_pedido.csv'
INTO TABLE itens_pedido
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(id_pedido, id_produto, quantidade, preco_unitario);

-- PAGAMENTOS
LOAD DATA LOCAL INFILE 'C:\\dados_ecommerce\\pagamentos.csv'
INTO TABLE pagamentos
CHARACTER SET latin1
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(id_pedido, valor, metodo, data_pagamento);

-- ============================================
-- FIM DO SCRIPT
-- ============================================