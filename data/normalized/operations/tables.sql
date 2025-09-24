-- SELECT 'DROP TABLE IF EXISTS ' || quote_ident(tablename) || ' CASCADE;'
-- FROM pg_tables
-- WHERE schemaname = 'public';

-- DROP TABLE IF EXISTS paises CASCADE;
-- DROP TABLE IF EXISTS clientes CASCADE;
-- DROP TABLE IF EXISTS pedidos CASCADE;
-- DROP TABLE IF EXISTS vendedores CASCADE;
-- DROP TABLE IF EXISTS fornecedores CASCADE;
-- DROP TABLE IF EXISTS produtos CASCADE;
-- DROP TABLE IF EXISTS categorias CASCADE;
-- DROP TABLE IF EXISTS vendas CASCADE;
-- DROP TABLE IF EXISTS transportadoras CASCADE;

CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT
);

CREATE TABLE fornecedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE paises (
    id TEXT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE transportadoras (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE vendedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    contato VARCHAR(255),
    cidade VARCHAR(255),
    pais_id TEXT,
    FOREIGN KEY (pais_id) REFERENCES paises(id) ON DELETE CASCADE
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT,
    vendedor_id INT,
    data DATE NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE,
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id) ON DELETE CASCADE
);

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    fornecedor_id INT,
    categoria_id INT,
    FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id) ON DELETE CASCADE
);

CREATE TABLE vendas (
    pedido_id INTEGER,
    produto_id INTEGER,
    transportadora_id INTEGER,
    quantidade INTEGER,
    valor_vendas DECIMAL(10, 2),
    custo_vendas DECIMAL(10, 2),
    margem_bruta DECIMAL(10, 2),
    frete DECIMAL(10, 2),
    desconto DECIMAL(10, 2),
    PRIMARY KEY (pedido_id, produto_id),  -- Chave composta
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),  -- Chave estrangeira referenciando a tabela pedidos
    FOREIGN KEY (produto_id) REFERENCES produtos(id),  -- Chave estrangeira referenciando a tabela produtos
    FOREIGN KEY (transportadora_id) REFERENCES transportadoras(id)  -- Chave estrangeira referenciando a tabela transportadoras
);
