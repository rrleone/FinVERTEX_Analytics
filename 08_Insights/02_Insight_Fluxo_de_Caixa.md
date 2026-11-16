# 02 — Insight de Fluxo de Caixa | FinVERTEX Analytics

**Escopo:** entradas, saídas, conciliação e comportamento temporal  
**Período principal:** 2024–2026

## 1. Evidências observadas

- A fato de fluxo de caixa contém **4.958 movimentos**.
- Foram identificadas **2.800 entradas** e **2.158 saídas**.
- Os status de conciliação encontrados são `Confirmado` (3.748 movimentos) e `Conciliado` (1.210 movimentos).
- O relatório de Data Quality registra aproximadamente **R\$ 152,98 milhões** em movimentos Confirmados e **R\$ 49,04 milhões** em movimentos Conciliados.
- O dashboard apresenta entradas de aproximadamente **R\$ 134,28 milhões**, saídas de **R\$ 60,21 milhões** e saldo líquido de movimentações de **R\$ 66,53 milhões**.
- O prazo entre lançamento e movimento de caixa foi, em média, **7,63 dias**; a mediana foi de 8 dias. Em 302 casos, o movimento ocorreu na mesma data do lançamento; em 4.656, ocorreu depois.
- Foram identificadas 31 movimentações entre 01/01/2027 e 15/01/2027 associadas a lançamentos de dezembro de 2026.

## 2. Interpretação

Os dados mostram uma diferença temporal entre o registro do lançamento e a movimentação de caixa. Essa diferença é compatível com um intervalo operacional, mas a base não permite determinar, por si só, a causa de cada prazo.

Os status `Confirmado` e `Conciliado` foram mantidos na análise do fluxo conforme a decisão de considerar ambos. Entretanto, a documentação de Data Quality registra que a definição de negócio desses dois status ainda precisa ser esclarecida.

As movimentações de janeiro de 2027 não devem ser descartadas: estão associadas a lançamentos de dezembro de 2026 e demonstram que data de lançamento e data de caixa podem pertencer a períodos diferentes.

## 3. Impacto para a gestão

A análise de fluxo de caixa ajuda a acompanhar a realização financeira e a distribuição temporal das movimentações. A distinção entre data de lançamento e data de movimento é essencial para análises mensais, conciliações e fechamento de períodos.

## 4. Recomendações

- Formalizar a definição operacional dos status `Confirmado` e `Conciliado`.
- Monitorar o prazo entre lançamento e movimento, investigando exceções relevantes.
- Preservar as 31 movimentações de janeiro de 2027 e manter o calendário estendido até 31/01/2027.
- Analisar entradas e saídas separadamente por período, centro de custo e conta.
- Não chamar o saldo líquido calculado de saldo bancário disponível sem saldo inicial e demais informações bancárias.

## 5. Limitações e reconciliação necessária

O relatório de Data Quality apresenta valores agregados por status de conciliação, enquanto o dashboard exibe totais de entradas e saídas. Antes de publicar uma reconciliação financeira definitiva, é necessário conferir que os filtros, períodos e critérios de inclusão são idênticos.

A documentação também registra totais de caixa diferentes dos totais de receita e despesa em algumas análises. Receita/despesa e entrada/saída são conceitos distintos e devem permanecer separados.

---
**Síntese:** o fluxo possui movimentações correspondentes aos lançamentos realizados e um intervalo médio de 7,63 dias entre registro e caixa. A padronização dos status e a leitura correta dos períodos são os principais pontos de controle.

---

<div align="center">

**FINVERTEX ANALYTICS**  
Dados • Qualidade • Inteligência • Decisões

**RENATO LEONE | DATA ANALYTICS & BUSINESS INTELLIGENCE**

</div>
