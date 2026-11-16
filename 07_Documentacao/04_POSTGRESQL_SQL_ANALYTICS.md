# FinVERTEX_Analytics
## Documentação Técnica — PostgreSQL e SQL Analytics

**Projeto:** FinVERTEX_Analytics  
**Etapa:** PostgreSQL e SQL Analytics  
**Status:** Concluída

---

## 1. Objetivo

Estruturar e validar a camada de dados financeiros do projeto FinVERTEX_Analytics utilizando PostgreSQL, garantindo consistência estrutural, integridade referencial e disponibilidade dos dados para análises financeiras e de negócio.

A etapa também teve como objetivo desenvolver consultas SQL para exploração e análise dos dados, apoiando futuras análises no Power BI.

## 2. Ambiente tecnológico

- PostgreSQL 17
- pgAdmin 4
- Visual Studio Code
- SQL

## 3. Estrutura do banco de dados

Banco de dados: `finvertex_analytics`

O modelo relacional é composto por 10 tabelas.

### Tabelas dimensionais

- `dim_calendario`
- `dim_centro_custo`
- `dim_cliente`
- `dim_fornecedor`
- `dim_funcionario`
- `dim_plano_contas`

### Tabelas fato

- `fato_fluxo_caixa`
- `fato_folha_pagamento`
- `fato_lancamentos_financeiros`
- `fato_orcamento`

## 4. Volume de dados

| Tabela | Registros |
|---|---:|
| dim_calendario | 1.127 |
| dim_funcionario | 200 |
| dim_cliente | 80 |
| dim_fornecedor | 60 |
| dim_plano_contas | 23 |
| dim_centro_custo | 10 |
| fato_lancamentos_financeiros | 6.706 |
| fato_orcamento | 8.280 |
| fato_fluxo_caixa | 4.958 |
| fato_folha_pagamento | 6.009 |
| **Total** | **27.453** |

## 5. Validação estrutural

Foram realizadas verificações para:

- Identificação das tabelas e colunas;
- Identificação das chaves primárias;
- Identificação dos relacionamentos;
- Verificação de duplicidade nas chaves dimensionais;
- Validação de integridade referencial.

### Resultados

- 10 tabelas identificadas;
- 10 chaves primárias identificadas;
- 13 relacionamentos por chave estrangeira identificados;
- Nenhuma duplicidade encontrada nas chaves dimensionais verificadas;
- Nenhuma referência órfã identificada nas relações verificadas.

As verificações de integridade referencial retornaram zero registros sem correspondência.

## 6. SQL Analytics

Foram desenvolvidas consultas para explorar os dados financeiros e apoiar análises de negócio.

### Análises realizadas

1. Lançamentos financeiros por tipo;
2. Lançamentos por tipo e status;
3. Participação percentual dos tipos;
4. Evolução mensal dos lançamentos;
5. Variação mensal absoluta da receita (MoM);
6. Variação percentual mensal da receita (MoM);
7. Receita acumulada no ano (YTD);
8. Orçamento por mês e status;
9. Orçamento versus realizado;
10. Movimentação mensal do fluxo de caixa;
11. Conciliação do fluxo de caixa;
12. Custo mensal da folha de pagamento;
13. Custo da folha por departamento;
14. Consultas complementares de revisão do orçamento.

## 7. Recursos SQL utilizados

Durante as análises foram utilizados:

- `SELECT`, `WHERE`, `GROUP BY` e `ORDER BY`;
- `COUNT`, `SUM`, `AVG`, `MIN` e `MAX`;
- `DATE_TRUNC` e `EXTRACT`;
- CTEs com `WITH`;
- Função de janela `LAG`;
- Funções de janela com `OVER`;
- `JOIN`, `LEFT JOIN`, `INNER JOIN` e `FULL OUTER JOIN`;
- `COALESCE`, `NULLIF` e `ROUND`.

## 8. Principais aplicações de negócio

As consultas desenvolvidas permitem:

- Avaliar receitas e despesas;
- Comparar lançamentos por tipo e status;
- Analisar tendências mensais;
- Avaliar variações de receita;
- Acompanhar receita acumulada;
- Comparar orçamento e realizado;
- Monitorar movimentações e conciliações de caixa;
- Avaliar custos de folha de pagamento;
- Comparar custos entre departamentos.

## 9. Arquivos relacionados

### PostgreSQL

`04_PostgreSQL/01_CRIACAO_TABELAS_FINVERTEX.sql`

### SQL Analytics

`05_SQL_Analytics/01_ANALISE_EXPLORATORIA_FINANCEIRA.sql`

`05_SQL_Analytics/02_REVISAO_MODELO_POSTGRESQL.sql`

## 10. Conclusão

A etapa PostgreSQL e SQL Analytics foi concluída.

O banco de dados foi estruturado, carregado e submetido a verificações de integridade. As consultas SQL foram desenvolvidas e revisadas para apoiar análises financeiras, temporais, orçamentárias, de fluxo de caixa e de folha de pagamento.

A camada SQL está preparada para servir como base para a próxima etapa do projeto: integração e modelagem no Power BI.

**Status:** PostgreSQL e SQL Analytics concluídos.