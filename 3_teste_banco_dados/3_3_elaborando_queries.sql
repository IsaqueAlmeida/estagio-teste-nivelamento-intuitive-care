-- Criando tabelas para os arquivos csv


CREATE TABLE operadoras_saude (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20),
    cnpj VARCHAR(20),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    data_registro DATE
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    competencia VARCHAR(10),
    registro_ans VARCHAR(20),
    cnpj VARCHAR(20),
    receita DECIMAL(15,2),
    despesa DECIMAL(15,2),
    resultado DECIMAL(15,2),
    patrimonio_liquido DECIMAL(15,2)
);
