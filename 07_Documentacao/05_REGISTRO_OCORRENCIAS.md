# FinVERTEX Analytics — Registro de Ocorrências de Data Quality

## Ocorrência DQ-001 — Movimentações de caixa fora do período analítico

**Data da identificação:** 05/11/2026  
**Tabela:** `fato_fluxo_caixa`  
**Severidade:** Baixa — ocorrência explicável  
**Status:** Em análise / tratamento planejado

### Descrição
Foram identificados 31 registros com `data_movimento` posterior ao período analítico definido para o projeto (01/01/2024 a 31/12/2026).

### Evidências
- Data mínima encontrada: 01/01/2027
- Data máxima encontrada: 15/01/2027
- Registros identificados: 31
- Lançamentos financeiros correspondentes: 31
- Registros sem correspondência: 0
- Datas dos lançamentos associados: dezembro de 2026

### Análise
Os movimentos representam liquidações financeiras ocorridas após o lançamento contábil, indicando possível diferença entre a data de reconhecimento financeiro e a data de movimentação bancária.

### Decisão
Preservar os registros. Não excluir nem alterar datas.

### Tratamento planejado
Ampliar a dimensão calendário para contemplar janeiro de 2027, mantendo o período analítico principal de 2024 a 2026.

### Regra de negócio
A data do lançamento financeiro e a data da movimentação de caixa podem pertencer a períodos diferentes.
