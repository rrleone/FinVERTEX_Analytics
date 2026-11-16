
-- KPI 01: RECEITA TOTAL
SELECT
    COUNT(*) AS quantidade_lancamentos,
    SUM(valor) AS receita_total
FROM fato_lancamentos_financeiros
WHERE tipo_lancamento = 'Receita'
  AND status_lancamento = 'Realizado';


-- KPI 02: DESPESAS TOTAIS
SELECT
    COUNT(*) AS quantidade_lancamentos,
    SUM(valor) AS despesas_totais
FROM fato_lancamentos_financeiros
WHERE tipo_lancamento = 'Despesa'
  AND status_lancamento = 'Realizado';

--KPI 03: MOVIMENTAÇÕES DE CAIXA
SELECT
    tipo_movimento,
    status_conciliacao,
    COUNT(*) AS quantidade,
    SUM(valor_movimento) AS valor_total
FROM fato_fluxo_caixa
GROUP BY
    tipo_movimento,
    status_conciliacao
ORDER BY
    tipo_movimento,


--KPI 04: VALOR ORÇADO
SELECT
    EXTRACT(YEAR FROM competencia_data) AS ano,
    status_orcamento,
    COUNT(*) AS quantidade_registros,
    SUM(valor_orcado) AS valor_orcado
FROM public.fato_orcamento
GROUP BY
    EXTRACT(YEAR FROM competencia_data),
    status_orcamento
ORDER BY
    ano,
    status_orcamento;

-- KPI 05: SALDO DE CAIXA

SELECT
    COUNT(*) AS quantidade_movimentacoes,
    SUM(
        CASE
            WHEN tipo_movimento = 'Entrada'
                THEN valor_movimento
            WHEN tipo_movimento = 'Saída'
                THEN -valor_movimento
            ELSE 0
        END
    ) AS saldo_caixa
FROM fato_fluxo_caixa;