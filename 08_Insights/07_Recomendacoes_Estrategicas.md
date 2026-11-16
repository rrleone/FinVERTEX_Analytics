# 07 — Recomendações Estratégicas | FinVERTEX Analytics

**Objetivo:** consolidar ações sugeridas a partir dos achados documentados nas seis perspectivas do dashboard.

As recomendações abaixo são propostas de investigação e acompanhamento. Não representam decisões tomadas por uma empresa real, pois a base é sintética.

## 1. Prioridades de validação analítica

| Prioridade | Tema | Ação recomendada | Motivo |
|---|---|---|---|
| Alta | Orçado vs. realizado | Auditar escopo, granularidade e filtros das medidas | Evitar interpretar diferenças não comparáveis como economia ou excesso |
| Alta | Fluxo de caixa | Formalizar o significado de `Confirmado` e `Conciliado` | Garantir interpretação consistente do status |
| Alta | Folha | Validar fórmula e granularidade dos KPIs médios | Evitar médias distorcidas por agregação |
| Média | Resultado e caixa | Manter medidas e fatos separados | Resultado financeiro não é sinônimo de saldo de caixa |
| Média | Despesas | Investigar contas de maior participação | Direcionar análise de custos |
| Média | Centros de custo | Avaliar os maiores centros com contexto operacional | Identificar oportunidades sem cortes lineares |
| Média | Temporalidade | Preservar movimentos de janeiro/2027 ligados a lançamentos de dezembro/2026 | Respeitar a diferença entre data de lançamento e data de caixa |

## 2. Acompanhamento gerencial recomendado

### Desempenho financeiro
Acompanhar receita, despesas, resultado e índice de despesas em períodos comparáveis. Investigar alterações relevantes antes de atribuir causas.

### Caixa e conciliação
Monitorar entradas, saídas, status e prazo entre lançamento e movimento. Não interpretar o saldo líquido calculado como saldo bancário sem saldo inicial.

### Orçamento
Comparar orçamento e realizado somente após assegurar o mesmo período, contas, centros de custo e granularidade. Documentar o sinal do desvio e a fórmula do percentual de execução.

### Custos
Usar centro de custo e categoria em conjunto. Investigar os maiores componentes, sua recorrência e sua relação com a atividade operacional.

### Folha de pagamento
Acompanhar a composição de salário-base, benefícios e encargos. Validar médias e variações com granularidade confirmada e critérios documentados.

## 3. Governança e qualidade dos dados

- Manter verificações de chaves primárias e integridade referencial.
- Preservar nulos semanticamente válidos, como data de desligamento de funcionários ativos.
- Manter calendário compatível com as datas efetivas dos fatos.
- Registrar ocorrências e decisões de tratamento.
- Separar validações técnicas de aprovações de regras de negócio.
- Registrar as regras de cálculo das medidas DAX e consultas SQL.

## 4. Conclusão

O FinVERTEX Analytics demonstra um fluxo integrado de Data Quality, ETL, PostgreSQL, SQL Analytics, modelagem dimensional e Power BI. O principal ganho analítico está em transformar dados organizados em indicadores interpretáveis, sem perder de vista a granularidade, as regras de negócio e as limitações da base.

A evolução recomendada é priorizar a auditoria das medidas de orçamento e folha, formalizar os status de conciliação e manter o monitoramento de custos, despesas e caixa.

---
**Nota:** as análises deste projeto utilizam dados sintéticos para fins de demonstração técnica e portfólio.

---

<div align="center">

**FINVERTEX ANALYTICS**  
Dados • Qualidade • Inteligência • Decisões

**RENATO LEONE | DATA ANALYTICS & BUSINESS INTELLIGENCE**

</div>
