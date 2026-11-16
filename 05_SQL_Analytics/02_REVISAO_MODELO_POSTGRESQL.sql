
-- ============================================================
-- FINVERTEX ANALYTICS
-- 02 - REVISAO DO MODELO POSTGRESQL
-- ============================================================


-- ============================================================
-- QUERY 01: TABELAS E QUANTIDADE DE COLUNAS
-- Objetivo: verificar a estrutura do banco
-- ============================================================

SELECT
    table_name,
    COUNT(*) AS quantidade_colunas
FROM information_schema.columns
WHERE table_schema = 'public'
GROUP BY table_name
ORDER BY table_name;


-- ============================================================
-- QUERY 02: RELACIONAMENTOS E CHAVES ESTRANGEIRAS
-- Objetivo: identificar relacionamentos entre tabelas
-- ============================================================

SELECT
    tc.table_name AS tabela_origem,
    kcu.column_name AS coluna_origem,
    ccu.table_name AS tabela_destino,
    ccu.column_name AS coluna_destino,
    tc.constraint_name AS nome_relacionamento
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.constraint_schema = kcu.constraint_schema
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
    AND ccu.constraint_schema = tc.constraint_schema
WHERE
    tc.constraint_type = 'FOREIGN KEY'
    AND tc.table_schema = 'public'
ORDER BY
    tc.table_name,
    kcu.column_name;


-- ============================================================
-- QUERY 03: REVISAO DAS CHAVES PRIMARIAS (PK)
-- Objetivo: identificar as chaves primarias de cada tabela
-- ============================================================

SELECT
    tc.table_name AS tabela,
    kcu.column_name AS coluna_chave_primaria,
    tc.constraint_name AS nome_constraint
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.constraint_schema = kcu.constraint_schema
WHERE
    tc.constraint_type = 'PRIMARY KEY'
    AND tc.table_schema = 'public'
ORDER BY
    tc.table_name,
    kcu.column_name;

-- ============================================================
-- QUERY 04: VALIDACAO DE CHAVES PRIMARIAS DUPLICADAS
-- Objetivo: verificar duplicidade de identificadores
-- ============================================================

SELECT
    'dim_cliente' AS tabela,
    COUNT(*) - COUNT(DISTINCT id_cliente) AS duplicidades
FROM public.dim_cliente

UNION ALL

SELECT
    'dim_funcionario',
    COUNT(*) - COUNT(DISTINCT id_funcionario)
FROM public.dim_funcionario

UNION ALL

SELECT
    'dim_fornecedor',
    COUNT(*) - COUNT(DISTINCT id_fornecedor)
FROM public.dim_fornecedor

UNION ALL

SELECT
    'dim_centro_custo',
    COUNT(*) - COUNT(DISTINCT id_centro_custo)
FROM public.dim_centro_custo

UNION ALL

SELECT
    'dim_plano_contas',
    COUNT(*) - COUNT(DISTINCT id_conta)
FROM public.dim_plano_contas;



-- ============================================================
-- QUERY 05: VALIDACAO DE CLIENTES NOS LANCAMENTOS
-- Objetivo: identificar lancamentos com cliente inexistente
-- ============================================================

SELECT
    COUNT(*) AS clientes_sem_correspondencia
FROM public.fato_lancamentos_financeiros f
LEFT JOIN public.dim_cliente d
    ON f.id_cliente = d.id_cliente
WHERE
    f.id_cliente IS NOT NULL
    AND d.id_cliente IS NULL;

-- ============================================================
-- QUERY 06: VALIDACAO DE FORNECEDORES NOS LANCAMENTOS
-- Objetivo: identificar fornecedores sem correspondencia na dimensao
-- ============================================================

SELECT
    COUNT(*) AS fornecedores_sem_correspondencia
FROM public.fato_lancamentos_financeiros f
LEFT JOIN public.dim_fornecedor d
    ON f.id_fornecedor = d.id_fornecedor
WHERE
    f.id_fornecedor IS NOT NULL
    AND d.id_fornecedor IS NULL;

-- ============================================================
-- QUERY 07: VALIDACAO DE CONTAS NOS LANCAMENTOS
-- Objetivo: identificar contas sem correspondencia na dimensao
-- ============================================================

SELECT
    COUNT(*) AS contas_sem_correspondencia
FROM public.fato_lancamentos_financeiros f
LEFT JOIN public.dim_plano_contas d
    ON f.id_conta = d.id_conta
WHERE
    f.id_conta IS NOT NULL
    AND d.id_conta IS NULL;


-- ============================================================
-- QUERY 08: VALIDACAO DE CONTAS NOS LANCAMENTOS FINANCEIROS
-- ============================================================

SELECT
    COUNT(*) AS contas_sem_correspondencia
FROM public.fato_lancamentos_financeiros f
LEFT JOIN public.dim_plano_contas d
    ON f.id_conta = d.id_conta
WHERE
    f.id_conta IS NOT NULL
    AND d.id_conta IS NULL;


-- ============================================================
-- QUERY 09: VALIDACAO DE CENTROS DE CUSTO NOS LANCAMENTOS
-- ============================================================

SELECT
    COUNT(*) AS centros_custo_sem_correspondencia
FROM public.fato_lancamentos_financeiros f
LEFT JOIN public.dim_centro_custo d
    ON f.id_centro_custo = d.id_centro_custo
WHERE
    f.id_centro_custo IS NOT NULL
    AND d.id_centro_custo IS NULL;


-- ============================================================
-- QUERY 10: VALIDACAO DE DATAS NOS LANCAMENTOS FINANCEIROS
-- ============================================================

SELECT
    COUNT(*) AS datas_sem_correspondencia
FROM public.fato_lancamentos_financeiros f
LEFT JOIN public.dim_calendario d
    ON f.data_lancamento_data = d.data
WHERE
    f.data_lancamento_data IS NOT NULL
    AND d.data IS NULL;


-- ============================================================
-- QUERY 11: VALIDACAO DE DATAS NO ORCAMENTO
-- ============================================================

SELECT
    COUNT(*) AS datas_orcamento_sem_correspondencia
FROM public.fato_orcamento f
LEFT JOIN public.dim_calendario d
    ON f.competencia_data = d.data
WHERE
    f.competencia_data IS NOT NULL
    AND d.data IS NULL;


-- ============================================================
-- QUERY 12: VALIDACAO DE CONTAS NO ORCAMENTO
-- ============================================================

SELECT
    COUNT(*) AS contas_orcamento_sem_correspondencia
FROM public.fato_orcamento f
LEFT JOIN public.dim_plano_contas d
    ON f.id_conta = d.id_conta
WHERE
    f.id_conta IS NOT NULL
    AND d.id_conta IS NULL;


-- ============================================================
-- QUERY 13: VALIDACAO DE CENTROS DE CUSTO NO ORCAMENTO
-- ============================================================

SELECT
    COUNT(*) AS centros_orcamento_sem_correspondencia
FROM public.fato_orcamento f
LEFT JOIN public.dim_centro_custo d
    ON f.id_centro_custo = d.id_centro_custo
WHERE
    f.id_centro_custo IS NOT NULL
    AND d.id_centro_custo IS NULL;


-- ============================================================
-- QUERY 14: VALIDACAO DE DATAS NO FLUXO DE CAIXA
-- ============================================================

SELECT
    COUNT(*) AS datas_fluxo_caixa_sem_correspondencia
FROM public.fato_fluxo_caixa f
LEFT JOIN public.dim_calendario d
    ON f.data_movimento_data = d.data
WHERE
    f.data_movimento_data IS NOT NULL
    AND d.data IS NULL;


-- ============================================================
-- QUERY 15: VALIDACAO DE CONTAS NO FLUXO DE CAIXA
-- ============================================================

SELECT
    COUNT(*) AS contas_fluxo_caixa_sem_correspondencia
FROM public.fato_fluxo_caixa f
LEFT JOIN public.dim_plano_contas d
    ON f.id_conta = d.id_conta
WHERE
    f.id_conta IS NOT NULL
    AND d.id_conta IS NULL;


-- ============================================================
-- QUERY 16: VALIDACAO DE CENTROS DE CUSTO NO FLUXO DE CAIXA
-- ============================================================

SELECT
    COUNT(*) AS centros_fluxo_caixa_sem_correspondencia
FROM public.fato_fluxo_caixa f
LEFT JOIN public.dim_centro_custo d
    ON f.id_centro_custo = d.id_centro_custo
WHERE
    f.id_centro_custo IS NOT NULL
    AND d.id_centro_custo IS NULL;


-- ============================================================
-- QUERY 17: VALIDACAO DE FUNCIONARIOS NA FOLHA DE PAGAMENTO
-- ============================================================

SELECT
    COUNT(*) AS funcionarios_sem_correspondencia
FROM public.fato_folha_pagamento f
LEFT JOIN public.dim_funcionario d
    ON f.id_funcionario = d.id_funcionario
WHERE
    f.id_funcionario IS NOT NULL
    AND d.id_funcionario IS NULL;


-- ============================================================
-- QUERY 18: VALIDACAO DE DATAS NA FOLHA DE PAGAMENTO
-- ============================================================

SELECT
    COUNT(*) AS datas_folha_sem_correspondencia
FROM public.fato_folha_pagamento f
LEFT JOIN public.dim_calendario d
    ON f.competencia_data = d.data
WHERE
    f.competencia_data IS NOT NULL
    AND d.data IS NULL;


-- ============================================================
-- FIM DA REVISAO DO MODELO POSTGRESQL
-- ============================================================

-- ============================================================
-- CONCLUSAO DA REVISAO DO MODELO POSTGRESQL
-- ============================================================

-- Validacoes realizadas:
-- 1. Estrutura das 10 tabelas
-- 2. Chaves primarias das 10 tabelas
-- 3. Relacionamentos / chaves estrangeiras
-- 4. Duplicidade nas chaves das dimensoes
-- 5. Integridade referencial das relacoes verificadas
--
-- Resultado:
-- Todas as consultas de integridade referencial retornaram 0.
-- Nenhuma referencia orfa foi identificada.
--
-- Status: REVISAO POSTGRESQL CONCLUIDA