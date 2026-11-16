# 06 — Insight de Folha de Pagamento | FinVERTEX Analytics

**Escopo:** composição e evolução dos custos com pessoal  
**Período documentado:** janeiro/2024 a dezembro/2026

## 1. Evidências observadas

O relatório de Data Quality registra **6.009 linhas** na fato de folha de pagamento e **200 funcionários** na dimensão de funcionários (182 ativos e 18 desligados).

As validações aritméticas documentadas não encontraram divergências nos 6.009 registros para as fórmulas verificadas:

- Salário líquido estimado = salário-base + horas extras + benefícios − descontos.
- Custo total do empregador = salário-base + horas extras + benefícios + encargos.

O dashboard apresenta:

| Indicador | Valor exibido |
|---|---:|
| Custo total da folha | R\$ 97,93 milhões |
| Custo médio por centro de custo | R\$ 6,02 milhões |
| Custo médio por colaborador | R\$ 497,08 mil |
| Variação da folha | 19,93% |

Os gráficos mostram a composição por salário-base, benefícios e encargos, a evolução quadrimestral e a intensidade mensal do custo da folha.

## 2. Interpretação

A validação aritmética indica consistência entre os componentes e os cálculos derivados na base examinada. Ela não equivale a auditoria trabalhista, tributária ou previdenciária.

Os indicadores de custo médio por centro e por colaborador precisam ter sua fórmula, unidade e período explicitados antes de serem usados como referência gerencial. Em particular, o valor exibido como custo médio por colaborador deve ser conferido quanto à agregação e ao período de cálculo.

A variação de 19,93% deve ser interpretada conforme o período-base e a fórmula efetivamente configurados no dashboard.

## 3. Impacto para a gestão

A análise da folha permite observar o peso relativo de salário-base, benefícios e encargos, além de acompanhar mudanças ao longo do tempo. A distinção entre custo total do empregador e valor líquido estimado é importante para evitar comparações inadequadas.

## 4. Recomendações

- Documentar a fórmula e o período de cada KPI da folha.
- Validar o custo médio por colaborador com a granularidade da fato e a contagem distinta de funcionários.
- Comparar salário-base, benefícios e encargos ao longo dos quadrimestres.
- Investigar variações relevantes por centro de custo.
- Manter a ressalva de que as validações realizadas são aritméticas, não uma auditoria de conformidade legal.

## 5. Limitações

A documentação de modelagem registra que a granularidade exata da fato de folha deve ser confirmada antes de assumir que cada linha representa um funcionário por competência. Essa confirmação é especialmente importante para medidas médias e contagens de colaboradores.

---
**Síntese:** os cálculos aritméticos da folha foram validados nos 6.009 registros, mas médias e variações precisam ter granularidade, fórmula e período claramente definidos para interpretação gerencial.

---

<div align="center">

**FINVERTEX ANALYTICS**  
Dados • Qualidade • Inteligência • Decisões

**RENATO LEONE | DATA ANALYTICS & BUSINESS INTELLIGENCE**

</div>
