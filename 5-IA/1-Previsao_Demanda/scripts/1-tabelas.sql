PRAGMA foreign_keys = ON;

-- Drop de tabelas caso existam (ordem importa por causa dos relacionamentos)

DROP TABLE IF EXISTS forecast;
DROP TABLE IF EXISTS reabastecimento;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS sazonalidade;
DROP TABLE IF EXISTS estoque;
DROP TABLE IF EXISTS vendas;
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS fornecedores;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS avaliacao_forecast;

-- Criação das tabelas

CREATE TABLE fornecedores (
    id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_fornecedor TEXT NOT NULL,
    nome_contato TEXT,
    email_contato TEXT
);

CREATE TABLE categorias (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT NOT NULL
);

CREATE TABLE produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    id_categoria INTEGER,
    id_fornecedor INTEGER,
    preco_unitario REAL,
    FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY(id_fornecedor) REFERENCES fornecedores(id_fornecedor)
);

CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    email TEXT
);

CREATE TABLE vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    id_cliente INTEGER,
    data_venda TEXT NOT NULL,
    quantidade_vendida INTEGER NOT NULL,
    total_venda REAL NOT NULL,
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto),
    FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE estoque (
    id_estoque INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    quantidade_em_estoque INTEGER NOT NULL,
    data_ultimo_reabastecimento TEXT,
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto)
);

CREATE TABLE sazonalidade (
    id_sazonalidade INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    nome_temporada TEXT NOT NULL,
    data_inicio TEXT NOT NULL,
    data_fim TEXT NOT NULL,
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto)
);

CREATE TABLE forecast (
    id_forecast INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    data_forecast TEXT NOT NULL,
    quantidade_forecast INTEGER NOT NULL,
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto)
);

CREATE TABLE reabastecimento (
    id_reabastecimento INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    data_reabastecimento TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto)
);

CREATE TABLE pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_fornecedor INTEGER NOT NULL,
    data_pedido TEXT NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY(id_fornecedor) REFERENCES fornecedores(id_fornecedor),
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto)
);

CREATE TABLE avaliacao_forecast (
	id_avaliacao INTEGER PRIMARY KEY AUTOINCREMENT,
	id_produto INTEGER,
	nome_produto TEXT,
	nome_categoria TEXT,
	periodo DATE,
	quantidade_real INTEGER,
	quantidade_forecast INTEGER,
	erro_absoluto INTEGER,
	erro_quadratico INTEGER,
	erro_percentual REAL,
	data_avaliacao DATE DEFAULT CURRENT_DATE
);