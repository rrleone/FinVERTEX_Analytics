# 04 — Insight de Orçado vs. Realizado | FinVERTEX Analytics

**Escopo:** execução orçamentária e desvios  
**Período orçamentário documentado:** janeiro/2024 a dezembro/2026

## 1. Evidências observadas

O relatório de Data Quality registra que a fato de orçamento possui:

- **8.280 registros**;
- competências de janeiro/2024 a dezembro/2026;
- status preenchido e aprovado em todos os registros analisados;
- valores positivos;
- nenhuma duplicidade identificada na chave de negócio formada por competência, conta e centro de custo nas validações realizadas.

O dashboard apresenta os seguintes indicadores agregados:

| Indicador | Valor exibido |
|---|---:|
| Valor orçado | R\$ 804,09 milhões |
| Valor realizado | R\$ 60,21 milhões |
| Desvio orçamentário | R\$ 743,88 milhões |
| Percentual de execução | 7,49% |

O dashboard também apresenta a evolução do percentual de execução por quadrimestre e o desvio por centro de custo.

## 2. Interpretação

Os valores exibidos indicam uma diferença expressiva entre o orçamento agregado e o valor realizado utilizado no visual. Entretanto, antes de interpretar essa diferença como economia, folga orçamentária ou desempenho, é necessário confirmar que orçamento e realizado estão comparados na mesma granularidade, período, escopo de contas e centros de custo.

O relatório de Data Quality confirma a consistência estrutural da base orçamentária, mas integridade estrutural não garante, por si só, comparabilidade semântica entre as medidas do dashboard.

## 3. Impacto para a gestão

Uma comparação orçamentária confiável permite identificar áreas com execução acima ou abaixo do planejado. Uma comparação com escopos diferentes pode produzir desvios matematicamente corretos, mas inadequados para decisões gerenciais.

## 4. Recomendações prioritárias

- Confirmar se o realizado compara apenas despesas ou inclui outras naturezas de lançamento.
- Garantir que orçamento e realizado usem o mesmo período e os mesmos filtros de conta e centro de custo.
- Validar a granularidade mensal do orçamento e sua relação com a dimensão calendário.
- Verificar se os valores orçados estão agregados uma única vez, sem duplicação por relacionamentos.
- Só classificar diferenças como economia ou excesso após confirmar a regra de sinal e o escopo comparado.
- Documentar a fórmula do percentual de execução e do desvio orçamentário.

## 5. Ponto de validação antes de publicação

O valor orçado de R\$ 804,09 milhões e o percentual de execução de 7,49% devem ser tratados como **valores apresentados no dashboard**, não como conclusão final sobre desempenho orçamentário, até que a medida de realizado e a comparabilidade entre fatos sejam auditadas.

---
**Síntese:** a base orçamentária passou pelas validações estruturais documentadas. O próximo controle decisivo é garantir que orçamento e realizado estejam sendo comparados no mesmo escopo e granularidade.

---

<div align="center">

**FINVERTEX ANALYTICS**  
Dados • Qualidade • Inteligência • Decisões

**RENATO LEONE | DATA ANALYTICS & BUSINESS INTELLIGENCE**

</div>
