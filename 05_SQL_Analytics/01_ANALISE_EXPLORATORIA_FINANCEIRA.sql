
-- ============================================================
-- FINVERTEX ANALYTICS
-- FASE 05 - SQL ANALYTICS
-- ANALISE EXPLORATORIA FINANCEIRA
-- ============================================================
--
-- Objetivo:
-- Explorar, validar e analisar os dados financeiros antes
-- da construcao dos indicadores e dashboards no Power BI.
--
-- IMPORTANTE:
-- Execute uma query por vez no pgAdmin.
--
-- ============================================================


-- ============================================================
-- QUERY 01: LANCAMENTOS FINANCEIROS POR TIPO
-- Objetivo: analisar quantidade, total, media, minimo e maximo
-- ============================================================

SELECT
    tipo_lancamento,
    COUNT(*) AS quantidade_lancamentos,
    SUM(valor) AS valor_total,
    AVG(valor) AS valor_medio,
    MIN(valor) AS menor_lancamento,
    MAX(valor) AS maior_lancamento
FROM public.fato_lancamentos_financeiros
GROUP BY tipo_lancamento
ORDER BY valor_total DESC;


-- ============================================================
-- QUERY 02: LANCAMENTOS POR TIPO E STATUS
-- Objetivo: comparar lancamentos realizados e pendentes
-- ============================================================

SELECT
    tipo_lancamento,
    status_lancamento,
    COUNT(*) AS quantidade,
    SUM(valor) AS valor_total
FROM public.fato_lancamentos_financeiros
GROUP BY
    tipo_lancamento,
    status_lancamento
ORDER BY
    tipo_lancamento,
    status_lancamento;


-- ============================================================
-- QUERY 03: LANCAMENTOS REALIZADOS POR TIPO
-- Objetivo: calcular participacao percentual dos tipos
-- ============================================================

SELECT
    tipo_lancamento,
    COUNT(*) AS quantidade,
    SUM(valor) AS valor_realizado,
    ROUND(
        SUM(valor) /
        SUM(SUM(valor)) OVER () * 100,
        2
    ) AS percentual_total
FROM public.fato_lancamentos_financeiros
WHERE status_lancamento = 'Realizado'
GROUP BY tipo_lancamento
ORDER BY valor_realizado DESC;


-- ============================================================
-- QUERY 04: EVOLUCAO MENSAL DOS LANCAMENTOS
-- Objetivo: analisar valores realizados por mes e categoria
-- ============================================================

SELECT
    DATE_TRUNC('month', data_lancamento_data)::DATE AS mes,
    tipo_lancamento,
    COUNT(*) AS quantidade_lancamentos,
    SUM(valor) AS valor_total
FROM public.fato_lancamentos_financeiros
WHERE status_lancamento = 'Realizado'
GROUP BY
    DATE_TRUNC('month', data_lancamento_data),
    tipo_lancamento
ORDER BY
    mes,
    tipo_lancamento;


-- ============================================================
-- QUERY 05: VARIACAO MENSAL ABSOLUTA DA RECEITA (MoM)
-- Objetivo: comparar receita realizada com mes anterior
-- ============================================================

WITH receita_mensal AS (
    SELECT
        DATE_TRUNC('month', data_lancamento_data)::DATE AS mes,
        SUM(valor) AS receita_realizada
    FROM public.fato_lancamentos_financeiros
    WHERE
        tipo_lancamento = 'Receita'
        AND status_lancamento = 'Realizado'
    GROUP BY DATE_TRUNC('month', data_lancamento_data)
)

SELECT
    mes,
    receita_realizada,
    LAG(receita_realizada) OVER (
        ORDER BY mes
    ) AS receita_mes_anterior,
    receita_realizada -
    LAG(receita_realizada) OVER (
        ORDER BY mes
    ) AS variacao_valor
FROM receita_mensal
ORDER BY mes;


-- ============================================================
-- QUERY 06: VARIACAO PERCENTUAL MENSAL DA RECEITA (MoM)
-- Objetivo: calcular crescimento ou reducao percentual
-- ============================================================

WITH receita_mensal AS (
    SELECT
        DATE_TRUNC('month', data_lancamento_data)::DATE AS mes,
        SUM(valor) AS receita_realizada
    FROM public.fato_lancamentos_financeiros
    WHERE
        tipo_lancamento = 'Receita'
        AND status_lancamento = 'Realizado'
    GROUP BY DATE_TRUNC('month', data_lancamento_data)
),

comparacao AS (
    SELECT
        mes,
        receita_realizada,
        LAG(receita_realizada) OVER (
            ORDER BY mes
        ) AS receita_mes_anterior
    FROM receita_mensal
)

SELECT
    mes,
    receita_realizada,
    receita_mes_anterior,
    ROUND(
        (
            (receita_realizada - receita_mes_anterior)
            / NULLIF(receita_mes_anterior, 0)
        ) * 100,
        2
    ) AS variacao_percentual_mom
FROM comparacao
ORDER BY mes;


-- ============================================================
-- QUERY 07: RECEITA ACUMULADA NO ANO (YTD)
-- Objetivo: calcular receita realizada acumulada por ano
-- ============================================================

WITH receita_mensal AS (
    SELECT
        DATE_TRUNC('month', data_lancamento_data)::DATE AS mes,
        SUM(valor) AS receita_realizada
    FROM public.fato_lancamentos_financeiros
    WHERE
        tipo_lancamento = 'Receita'
        AND status_lancamento = 'Realizado'
    GROUP BY DATE_TRUNC('month', data_lancamento_data)
)

SELECT
    mes,
    receita_realizada,
    SUM(receita_realizada) OVER (
        PARTITION BY EXTRACT(YEAR FROM mes)
        ORDER BY mes
    ) AS receita_acumulada_ytd
FROM receita_mensal
ORDER BY mes;


-- ============================================================
-- QUERY 08: ORCAMENTO POR MES E STATUS
-- Objetivo: analisar valores orcados e situacao do orcamento
-- ============================================================

SELECT
    DATE_TRUNC('month', competencia_data)::DATE AS mes,
    status_orcamento,
    COUNT(*) AS quantidade_registros,
    SUM(valor_orcado) AS valor_orcado_total
FROM public.fato_orcamento
GROUP BY
    DATE_TRUNC('month', competencia_data),
    status_orcamento
ORDER BY
    mes,
    status_orcamento;


-- ============================================================
-- QUERY 09: ORCAMENTO VERSUS REALIZADO
-- Objetivo: comparar valores orcados com lancamentos realizados
-- por mes, conta contabil e centro de custo
-- ============================================================

WITH orcamento AS (
    SELECT
        DATE_TRUNC('month', competencia_data)::DATE AS mes,
        id_conta,
        id_centro_custo,
        SUM(valor_orcado) AS valor_orcado
    FROM public.fato_orcamento
    GROUP BY
        DATE_TRUNC('month', competencia_data),
        id_conta,
        id_centro_custo
),

realizado AS (
    SELECT
        DATE_TRUNC('month', data_lancamento_data)::DATE AS mes,
        id_conta,
        id_centro_custo,
        SUM(valor) AS valor_realizado
    FROM public.fato_lancamentos_financeiros
    WHERE status_lancamento = 'Realizado'
    GROUP BY
        DATE_TRUNC('month', data_lancamento_data),
        id_conta,
        id_centro_custo
)

SELECT
    COALESCE(o.mes, r.mes) AS mes,
    COALESCE(o.id_conta, r.id_conta) AS id_conta,
    COALESCE(o.id_centro_custo, r.id_centro_custo)
        AS id_centro_custo,
    COALESCE(o.valor_orcado, 0) AS valor_orcado,
    COALESCE(r.valor_realizado, 0) AS valor_realizado,
    COALESCE(r.valor_realizado, 0)
        - COALESCE(o.valor_orcado, 0) AS variacao_valor
FROM orcamento o
FULL OUTER JOIN realizado r
    ON o.mes = r.mes
    AND o.id_conta = r.id_conta
    AND o.id_centro_custo = r.id_centro_custo
ORDER BY
    mes,
    id_conta,
    id_centro_custo;


-- ============================================================
-- QUERY 10: MOVIMENTACAO MENSAL DO FLUXO DE CAIXA
-- Objetivo: analisar valores e quantidade por tipo de movimento
-- ============================================================

SELECT
    DATE_TRUNC('month', data_movimento_data)::DATE AS mes,
    tipo_movimento,
    COUNT(*) AS quantidade_movimentos,
    SUM(valor_movimento) AS valor_total
FROM public.fato_fluxo_caixa
GROUP BY
    DATE_TRUNC('month', data_movimento_data),
    tipo_movimento
ORDER BY
    mes,
    tipo_movimento;


-- ============================================================
-- QUERY 11: CONCILIACAO DO FLUXO DE CAIXA
-- Objetivo: analisar movimentos por status de conciliacao
-- ============================================================

SELECT
    status_conciliacao,
    tipo_movimento,
    COUNT(*) AS quantidade_movimentos,
    SUM(valor_movimento) AS valor_total
FROM public.fato_fluxo_caixa
GROUP BY
    status_conciliacao,
    tipo_movimento
ORDER BY
    status_conciliacao,
    tipo_movimento;


-- ============================================================
-- QUERY 12: CUSTO MENSAL DA FOLHA DE PAGAMENTO
-- Objetivo: analisar custo total da empresa com folha
-- ============================================================

SELECT
    DATE_TRUNC('month', competencia_data)::DATE AS mes,
    COUNT(*) AS quantidade_registros_folha,
    SUM(salario_liquido_estimado) AS total_salario_liquido,
    SUM(custo_total_empresa) AS custo_total_empresa,
    AVG(custo_total_empresa) AS custo_medio_por_registro
FROM public.fato_folha_pagamento
GROUP BY DATE_TRUNC('month', competencia_data)
ORDER BY mes;


-- ============================================================
-- QUERY 13: CUSTO DA FOLHA POR DEPARTAMENTO
-- Objetivo: comparar custos de pessoal por departamento e mes
-- ============================================================

SELECT
    DATE_TRUNC('month', f.competencia_data)::DATE AS mes,
    d.departamento,
    COUNT(*) AS quantidade_registros,
    SUM(f.custo_total_empresa) AS custo_total_empresa,
    AVG(f.custo_total_empresa) AS custo_medio
FROM public.fato_folha_pagamento f
INNER JOIN public.dim_funcionario d
    ON f.id_funcionario = d.id_funcionario
GROUP BY
    DATE_TRUNC('month', f.competencia_data),
    d.departamento
ORDER BY
    mes,
    custo_total_empresa DESC;
-- ============================================================
-- QUERY 14: IDENTIFICACAO DOS TIPOS DE ORCAMENTO
-- ============================================================

SELECT
    tipo_orcamento,
    COUNT(*) AS quantidade_registros,
    SUM(valor_orcado) AS valor_total_orcado
FROM public.fato_orcamento
GROUP BY tipo_orcamento
ORDER BY valor_total_orcado DESC;

-- ============================================================
-- QUERY 15: ESTRUTURA DA TABELA DE ORCAMENTO
-- ============================================================

SELECT
    column_name,
    data_type
FROM information_schema.columns
WHERE
    table_schema = 'public'
    AND table_name = 'fato_orcamento'
ORDER BY ordinal_position;

-- ============================================================
-- QUERY 15: ORCAMENTO POR STATUS
-- Objetivo: analisar valores orcados por situacao
-- ============================================================

SELECT
    status_orcamento,
    COUNT(*) AS quantidade_registros,
    SUM(valor_orcado) AS valor_orcado_total,
    AVG(valor_orcado) AS valor_orcado_medio
FROM public.fato_orcamento
GROUP BY status_orcamento
ORDER BY valor_orcado_total DESC;

-- ============================================================
-- FIM DO ARQUIVO - SQL ANALYTICS FINVERTEX
-- ============================================================


-- ============================================================
-- ENCERRAMENTO DA ETAPA SQL ANALYTICS
-- PROJETO: FinVERTEX_Analytics
-- ============================================================

-- ANALISES REALIZADAS:
-- 1. Lancamentos financeiros por tipo
-- 2. Lancamentos por tipo e status
-- 3. Participacao percentual dos tipos
-- 4. Evolucao mensal dos lancamentos
-- 5. Variacao mensal absoluta da receita (MoM)
-- 6. Variacao percentual mensal da receita (MoM)
-- 7. Receita acumulada no ano (YTD)
-- 8. Orcamento por mes e status
-- 9. Orcamento versus realizado
-- 10. Movimentacao mensal do fluxo de caixa
-- 11. Conciliacao do fluxo de caixa
-- 12. Custo mensal da folha de pagamento
-- 13. Custo da folha por departamento
-- 14. Consultas complementares de revisao do orcamento

-- RECURSOS SQL UTILIZADOS:
-- SELECT, WHERE, GROUP BY, ORDER BY
-- COUNT, SUM, AVG, MIN, MAX
-- DATE_TRUNC, EXTRACT
-- CTE (WITH)
-- LAG
-- Funcoes de janela (OVER)
-- JOIN, FULL OUTER JOIN
-- COALESCE, NULLIF, ROUND

-- STATUS:
-- Analises exploratorias revisadas.
-- Revisao estrutural do PostgreSQL concluida.
-- Integridade referencial validada.
-- Etapa SQL Analytics concluida.
