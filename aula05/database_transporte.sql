-- Criar base de dados de transporte 
CREATE DATABASE transporte;

-- Entrar na base de dados para criar outros objetos
USE transporte;

-- Criar a tabela cartões
CREATE TABLE cartoes (
	id_cartao BIGINT PRIMARY KEY,
-- Varchar: Ocupa apenas o espaço digitado. Ex: 10caracteres vão ocupar 10 no lugar de 20
    tipo VARCHAR(20), 
    data_emissao DATE
);

-- Criar a tabela linhas
CREATE TABLE linhas (
	id_linha INT,
    codigo VARCHAR(10),
    descricao VARCHAR(100),
    PRIMARY KEY (id_linha)
);

-- Criar a tabela veiculos
CREATE TABLE veiculos (
	id_veiculo INT,
    prefixo VARCHAR(10),
    id_linha INT,
    PRIMARY KEY (id_veiculo),
    FOREIGN KEY (id_linha) REFERENCES linhas (id_linha)
);

-- Criar tabela viagens
CREATE TABLE viagens (
	id_viagem BIGINT,
    id_cartao BIGINT,
    id_veiculo INT,
    data_hora DATETIME,
    local_embarque VARCHAR(100),
    PRIMARY KEY (id_viagem),
    FOREIGN KEY (id_cartao) REFERENCES cartoes (id_cartao),
    FOREIGN KEY (id_veiculo) REFERENCES veiculos (id_veiculo)
);

-- Criar tabela GPS_veiculo
CREATE TABLE gps_veiculo (
	id_gps BIGINT,
    id_veiculo INT,
    data_hora DATETIME,
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    velocidade DECIMAL(5,2),
    PRIMARY KEY (id_gps),
    FOREIGN KEY (id_veiculo) REFERENCES veiculos (id_veiculo)
);

