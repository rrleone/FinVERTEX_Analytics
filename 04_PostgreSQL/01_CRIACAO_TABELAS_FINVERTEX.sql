
-- ============================================================
-- FinVERTEX_Analytics
-- Etapa 04.02 — Criação das tabelas PostgreSQL
-- PostgreSQL 17
-- ============================================================

-- DIMENSÕES
CREATE TABLE IF NOT EXISTS dim_calendario (
    data DATE PRIMARY KEY,
    ano SMALLINT,
    trimestre SMALLINT,
    mes_numero SMALLINT,
    mes_nome VARCHAR(20),
    ano_mes VARCHAR(7),
    dia SMALLINT,
    dia_semana_numero SMALLINT,
    dia_semana_nome VARCHAR(20),
    fim_de_semana BOOLEAN
);

CREATE TABLE IF NOT EXISTS dim_funcionario (
    id_funcionario INTEGER PRIMARY KEY,
    nome_completo VARCHAR(150),
    email_corporativo VARCHAR(150),
    genero VARCHAR(30),
    data_admissao DATE,
    data_demissao DATE,
    cargo VARCHAR(100),
    departamento VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    salario_base NUMERIC(14,2),
    status_funcionario VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS dim_cliente (
    id_cliente INTEGER PRIMARY KEY,
    razao_social VARCHAR(200),
    email_contato VARCHAR(150),
    telefone VARCHAR(30),
    cidade VARCHAR(100),
    uf CHAR(2),
    segmento VARCHAR(100),
    porte VARCHAR(50),
    data_inicio_relacionamento DATE
);

CREATE TABLE IF NOT EXISTS dim_fornecedor (
    id_fornecedor INTEGER PRIMARY KEY,
    razao_social VARCHAR(200),
    email_financeiro VARCHAR(150),
    telefone VARCHAR(30),
    cidade VARCHAR(100),
    uf CHAR(2),
    categoria_fornecedor VARCHAR(100),
    status_fornecedor VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS dim_plano_contas (
    id_conta INTEGER PRIMARY KEY,
    nome_conta VARCHAR(150),
    tipo_conta VARCHAR(50),
    grupo_dre VARCHAR(100),
    natureza VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS dim_centro_custo (
    id_centro_custo INTEGER PRIMARY KEY,
    codigo_centro VARCHAR(30),
    nome_centro_custo VARCHAR(150),
    grupo_custo VARCHAR(100)
);


-- ============================================================
-- TABELAS FATO
-- ============================================================

CREATE TABLE IF NOT EXISTS fato_lancamentos_financeiros (
    id_lancamento INTEGER PRIMARY KEY,
    data_lancamento DATE,
    data_lancamento_data DATE,
    tipo_lancamento VARCHAR(50),
    id_conta INTEGER,
    id_centro_custo INTEGER,
    id_cliente INTEGER,
    id_fornecedor INTEGER,
    descricao TEXT,
    valor NUMERIC(16,2),
    status_lancamento VARCHAR(30),
    meio_pagamento VARCHAR(50),

    CONSTRAINT fk_lancamento_calendario
        FOREIGN KEY (data_lancamento_data)
        REFERENCES dim_calendario(data),

    CONSTRAINT fk_lancamento_conta
        FOREIGN KEY (id_conta)
        REFERENCES dim_plano_contas(id_conta),

    CONSTRAINT fk_lancamento_centro_custo
        FOREIGN KEY (id_centro_custo)
        REFERENCES dim_centro_custo(id_centro_custo),

    CONSTRAINT fk_lancamento_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES dim_cliente(id_cliente),

    CONSTRAINT fk_lancamento_fornecedor
        FOREIGN KEY (id_fornecedor)
        REFERENCES dim_fornecedor(id_fornecedor)
);


CREATE TABLE IF NOT EXISTS fato_orcamento (
    id_orcamento INTEGER PRIMARY KEY,
    competencia VARCHAR(7),
    competencia_data DATE,
    id_conta INTEGER,
    id_centro_custo INTEGER,
    valor_orcado NUMERIC(16,2),
    status_orcamento VARCHAR(30),

    CONSTRAINT fk_orcamento_calendario
        FOREIGN KEY (competencia_data)
        REFERENCES dim_calendario(data),

    CONSTRAINT fk_orcamento_conta
        FOREIGN KEY (id_conta)
        REFERENCES dim_plano_contas(id_conta),

    CONSTRAINT fk_orcamento_centro_custo
        FOREIGN KEY (id_centro_custo)
        REFERENCES dim_centro_custo(id_centro_custo)
);


CREATE TABLE IF NOT EXISTS fato_fluxo_caixa (
    id_movimento_caixa INTEGER PRIMARY KEY,
    data_movimento DATE,
    data_movimento_data DATE,
    tipo_movimento VARCHAR(30),
    id_lancamento INTEGER,
    id_conta INTEGER,
    id_centro_custo INTEGER,
    valor_movimento NUMERIC(16,2),
    status_conciliacao VARCHAR(30),
    instituicao_financeira VARCHAR(100),

    CONSTRAINT fk_fluxo_calendario
        FOREIGN KEY (data_movimento_data)
        REFERENCES dim_calendario(data),

    CONSTRAINT fk_fluxo_conta
        FOREIGN KEY (id_conta)
        REFERENCES dim_plano_contas(id_conta),

    CONSTRAINT fk_fluxo_centro_custo
        FOREIGN KEY (id_centro_custo)
        REFERENCES dim_centro_custo(id_centro_custo)
);


CREATE TABLE IF NOT EXISTS fato_folha_pagamento (
    id_folha INTEGER PRIMARY KEY,
    id_funcionario INTEGER,
    competencia VARCHAR(7),
    competencia_data DATE,
    salario_base NUMERIC(14,2),
    horas_extras NUMERIC(10,2),
    valor_horas_extras NUMERIC(14,2),
    beneficios NUMERIC(14,2),
    encargos NUMERIC(14,2),
    descontos NUMERIC(14,2),
    salario_liquido_estimado NUMERIC(14,2),
    custo_total_empresa NUMERIC(14,2),

    CONSTRAINT fk_folha_funcionario
        FOREIGN KEY (id_funcionario)
        REFERENCES dim_funcionario(id_funcionario),

    CONSTRAINT fk_folha_calendario
        FOREIGN KEY (competencia_data)
        REFERENCES dim_calendario(data)
);


-- ============================================================
-- ÍNDICES PARA RELACIONAMENTOS E CONSULTAS
-- ============================================================

CREATE INDEX IF NOT EXISTS idx_lancamento_conta
    ON fato_lancamentos_financeiros(id_conta);

CREATE INDEX IF NOT EXISTS idx_lancamento_centro
    ON fato_lancamentos_financeiros(id_centro_custo);

CREATE INDEX IF NOT EXISTS idx_fluxo_conta
    ON fato_fluxo_caixa(id_conta);

CREATE INDEX IF NOT EXISTS idx_orcamento_conta
    ON fato_orcamento(id_conta);

CREATE INDEX IF NOT EXISTS idx_folha_funcionario
    ON fato_folha_pagamento(id_funcionario);


