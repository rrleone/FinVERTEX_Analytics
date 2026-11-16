# FinVERTEX Analytics

## Relatório Consolidado de Data Quality e Análise Exploratória Financeira

**Versão:** Consolidada --- Scripts 01 a 31\
**Etapa:** Data Quality / Data Understanding\
**Empresa fictícia:** FinVERTEX Serviços Corporativos S.A.\
**Período analítico principal:** 2024--2026\
**Status:** Etapa exploratória concluída; recomenda-se avançar para
Business Intelligence após validações de negócio pendentes.

------------------------------------------------------------------------

# 1. Sumário executivo

Este relatório consolida as análises de Data Profiling, qualidade,
integridade, consistência de regras de negócio e exploração financeira
realizadas sobre os dados sintéticos da FinVERTEX Analytics.

O conjunto de dados contém **10 arquivos CSV e 27.422 registros**. A
etapa foi conduzida por meio de 31 scripts Python, com foco em
identificar problemas de qualidade, validar relacionamentos, verificar
regras financeiras e produzir achados relevantes para futuras análises
de BI.

## Principais conclusões

-   As chaves primárias avaliadas não apresentaram valores nulos ou
    duplicados.
-   Os relacionamentos entre fatos e dimensões foram validados sem IDs
    órfãos.
-   As regras de classificação de lançamentos por tipo contábil foram
    consistentes.
-   Os cálculos aritméticos da folha de pagamento apresentaram
    consistência nos 6.009 registros avaliados.
-   Os 4.958 lançamentos realizados possuem movimentação correspondente
    no fluxo de caixa; os 1.748 pendentes não possuem movimentação.
-   Foram identificadas 31 movimentações de caixa em janeiro de 2027,
    relacionadas a lançamentos de dezembro de 2026. Essas movimentações
    devem ser preservadas.
-   A definição de negócio dos status `Confirmado` e `Conciliado`
    precisa ser esclarecida.
-   O conjunto de lançamentos pendentes soma aproximadamente **R\$ 70,93
    milhões**. Esse valor não deve ser interpretado como dívida vencida,
    inadimplência ou atraso sem informação de vencimento.

A etapa de Data Quality encontrou poucos problemas estruturais críticos
nos dados examinados. O principal trabalho remanescente é esclarecer
definições de negócio e preparar os dados para modelagem e análise
financeira.

------------------------------------------------------------------------

# 2. Objetivo e escopo

## 2.1 Objetivo

Avaliar a qualidade e a consistência dos dados antes da construção de
indicadores, análises financeiras e dashboards.

## 2.2 Escopo técnico

Foram investigados:

-   estrutura, tipos de dados e dimensões;
-   valores ausentes;
-   duplicidade de registros e chaves;
-   integridade referencial;
-   validade e consistência de datas;
-   regras de classificação financeira;
-   consistência entre lançamentos e fluxo de caixa;
-   validação aritmética da folha de pagamento;
-   orçamento;
-   conciliação;
-   lançamentos pendentes;
-   análises exploratórias por período, conta, tipo e centro de custo.

## 2.3 Limitações de escopo

Os dados são sintéticos e representam um cenário de laboratório. Os
resultados demonstram aplicação de métodos analíticos, mas não comprovam
a situação de uma empresa real.

A validação aritmética da folha não representa auditoria de legislação
trabalhista, tributária ou previdenciária.

------------------------------------------------------------------------

# 3. Inventário dos dados

  Arquivo                                 Registros   Colunas
  ------------------------------------ ------------ ---------
  `dim_funcionario.csv`                         200        12
  `dim_cliente.csv`                              80         9
  `dim_fornecedor.csv`                           60         8
  `dim_calendario.csv`                        1.096        10
  `dim_plano_contas.csv`                         23         5
  `dim_centro_custo.csv`                         10         4
  `fato_lancamentos_financeiros.csv`          6.706        11
  `fato_orcamento.csv`                        8.280         6
  `fato_fluxo_caixa.csv`                      4.958         9
  `fato_folha_pagamento.csv`                  6.009        11
  **Total**                              **27.422**       ---

## 3.1 Padrões de dados

-   Arquivos CSV delimitados por ponto e vírgula.
-   Codificação UTF-8 com BOM.
-   Datas no padrão `YYYY-MM-DD`.
-   Valores numéricos com ponto decimal.
-   Nomes de colunas em `snake_case`.
-   Valores monetários armazenados sem símbolos de moeda.

------------------------------------------------------------------------

# 4. Data Profiling

## 4.1 Funcionários

A dimensão de funcionários possui 200 registros e 12 colunas.

-   182 funcionários ativos.
-   18 funcionários desligados.
-   182 valores nulos em `data_demissao`, correspondentes a funcionários
    ativos.
-   Nenhuma linha completamente duplicada identificada na análise
    inicial.

Os nulos de `data_demissao` são **esperados e semanticamente válidos**
para funcionários ativos. Não devem ser preenchidos artificialmente.

## 4.2 Lançamentos financeiros

A tabela possui 6.706 registros e 11 campos.

  Tipo             Quantidade
  -------------- ------------
  Receita               3.803
  Despesa               2.584
  Investimento            319
  **Total**         **6.706**

Status:

  Status        Quantidade
  ----------- ------------
  Realizado          4.958
  Pendente           1.748
  **Total**      **6.706**

Campos opcionais:

-   `id_cliente`: 3.065 valores nulos.
-   `id_fornecedor`: 3.803 valores nulos.

Esses nulos são compatíveis com relações condicionais: nem todo
lançamento precisa estar associado a cliente e fornecedor
simultaneamente. A regra deve ser mantida conforme a natureza do
lançamento.

Estatísticas de `valor`:

-   Média: R\$ 40.701,93
-   Desvio padrão: R\$ 20.990,93
-   Mínimo: R\$ 2.562,66
-   Mediana: R\$ 39.727,93
-   Máximo: R\$ 84.969,41

## 4.3 Orçamento

A tabela de orçamento contém 8.280 registros e 6 colunas.

-   Competências de janeiro/2024 a dezembro/2026.
-   Todos os registros analisados possuem status aprovado.
-   Valores positivos.
-   Nenhum nulo ou duplicidade identificada nas validações realizadas.
-   Valor mínimo: R\$ 15.008,39.
-   Valor máximo: R\$ 179.988,48.

## 4.4 Fluxo de caixa

A tabela contém 4.958 movimentos e 9 colunas.

  Tipo de movimento     Quantidade
  ------------------- ------------
  Entrada                    2.800
  Saída                      2.158

Status:

  Status de conciliação     Quantidade
  ----------------------- ------------
  Confirmado                     3.748
  Conciliado                     1.210

Período: 03/01/2024 a 15/01/2027.

Valores:

-   Mínimo: R\$ 2.562,66.
-   Máximo: R\$ 84.969,41.

## 4.5 Folha de pagamento

A tabela contém 6.009 registros e 11 colunas. Os campos permitem avaliar
salário-base, horas extras, benefícios, encargos, descontos, valor
líquido estimado e custo total do empregador.

------------------------------------------------------------------------

# 5. Validações de qualidade e integridade

## 5.1 Chaves primárias

As chaves primárias avaliadas não apresentaram valores nulos ou
duplicados:

  Tabela                      Registros Resultado
  ------------------------- ----------- -----------
  Funcionários                      200 Aprovado
  Clientes                           80 Aprovado
  Fornecedores                       60 Aprovado
  Centros de custo                   10 Aprovado
  Plano de contas                    23 Aprovado
  Lançamentos financeiros         6.706 Aprovado
  Orçamento                       8.280 Aprovado
  Fluxo de caixa                  4.958 Aprovado
  Folha de pagamento              6.009 Aprovado

## 5.2 Integridade referencial

Foram avaliadas relações entre fatos e dimensões. Não foram
identificados IDs órfãos nos relacionamentos verificados.

  Relacionamento                       Registros verificados Resultado
  ---------------------------------- ----------------------- -------------------
  Folha → Funcionário                                  6.009 Sem IDs inválidos
  Lançamento → Plano de contas                         6.706 Sem IDs inválidos
  Lançamento → Centro de custo                         6.706 Sem IDs inválidos
  Lançamento → Cliente                       3.641 não nulos Sem IDs inválidos
  Lançamento → Fornecedor                    2.903 não nulos Sem IDs inválidos
  Orçamento → Plano de contas                          8.280 Sem IDs inválidos
  Orçamento → Centro de custo                          8.280 Sem IDs inválidos
  Fluxo de caixa → Lançamento                          4.958 Sem IDs inválidos
  Fluxo de caixa → Plano de contas                     4.958 Sem IDs inválidos
  Fluxo de caixa → Centro de custo                     4.958 Sem IDs inválidos

## 5.3 Validação de datas

Datas observadas:

  Entidade                  Período
  ------------------------- -------------------------
  Calendário original       01/01/2024 a 31/12/2026
  Lançamentos financeiros   01/01/2024 a 31/12/2026
  Orçamento                 Jan/2024 a Dez/2026
  Folha de pagamento        Jan/2024 a Dez/2026
  Fluxo de caixa            03/01/2024 a 15/01/2027
  Admissões                 11/01/2019 a 24/08/2026
  Desligamentos             19/07/2021 a 31/10/2026

A diferença entre o período do calendário e o fluxo de caixa foi
investigada. As 31 movimentações de janeiro/2027 estão relacionadas a
lançamentos de dezembro/2026.

**Recomendação:** ampliar a dimensão calendário até, pelo menos,
31/01/2027, mantendo 2024--2026 como período principal de análise.

## 5.4 Funcionários

-   200 funcionários.
-   182 ativos e 18 desligados.
-   Nenhum funcionário ativo com data de desligamento.
-   Nenhum funcionário desligado sem data de desligamento.
-   Status encontrados: `ativo` e `desligado`.
-   Status e datas de desligamento consistentes.

## 5.5 Folha de pagamento

Foram validadas as relações aritméticas:

-   Salário líquido estimado = salário-base + horas extras + benefícios
    − descontos.
-   Custo total do empregador = salário-base + horas extras +
    benefícios + encargos.

Resultado: **6.009 registros sem divergências aritméticas** nas fórmulas
verificadas.

Essa validação não avalia conformidade legal ou fiscal.

## 5.6 Orçamento

Validações realizadas:

-   chaves primárias sem nulos ou duplicados;
-   valores sem nulos, zeros ou negativos;
-   ausência de duplicidade na chave de negócio formada por competência,
    conta e centro de custo;
-   status preenchido;
-   status aprovado em todos os registros.

## 5.7 Fluxo de caixa

Validações realizadas:

-   chave primária sem nulos ou duplicados;
-   ID de lançamento preenchido e sem duplicidade;
-   valores sem nulos, zeros ou negativos;
-   datas válidas;
-   categorias de movimento e status dentro dos valores esperados;
-   31 movimentos após o período do calendário original.

## 5.8 Lançamentos financeiros

Validações realizadas:

-   chave primária sem nulos ou duplicados;
-   valores sem nulos, zeros ou negativos;
-   tipos válidos: Receita, Despesa e Investimento;
-   status válidos: Pendente e Realizado;
-   ausência de duplicidades na chave de negócio examinada (data, tipo,
    conta, centro de custo, valor e descrição).

------------------------------------------------------------------------

# 6. Regras de negócio validadas

## 6.1 Tipo de lançamento versus plano de contas

O cruzamento dos lançamentos com o plano de contas não encontrou
divergências de classificação.

  Tipo de lançamento     Quantidade
  -------------------- ------------
  Receita                     3.803
  Despesa                     2.584
  Investimento                  319

Todos os lançamentos classificados como Receita, Despesa ou Investimento
estavam coerentes com o tipo da conta associado.

## 6.2 Plano de contas

A dimensão possui 23 contas:

-   17 contas de Despesa;
-   4 contas de Receita;
-   2 contas de Investimento.

Natureza:

-   Devedora: 19;
-   Credora: 4.

A regra de natureza foi validada:

-   Receita → Credora;
-   Despesa → Devedora;
-   Investimento → Devedora.

Resultado: zero inconsistências nas regras avaliadas.

## 6.3 Centros de custo

A dimensão possui 10 centros de custo, sem nulos ou duplicidades
identificadas nos campos-chave e descritivos.

  Código   Centro             Grupo
  -------- ------------------ ------------------------
  FIN      Financeiro         Financeiro
  RH       Recursos Humanos   Pessoal
  COM      Comercial          Comercial e Marketing
  TEC      Tecnologia         Tecnologia
  MKT      Marketing          Comercial e Marketing
  OPS      Operações          Operações
  ADM      Administrativo     Administrativo
  CS       Customer Success   Operações
  JUR      Jurídico           Serviços Profissionais
  DIR      Diretoria          Administrativo

## 6.4 Tipo de movimento de caixa

A regra foi validada sem divergências:

-   Receita → Entrada;
-   Despesa → Saída;
-   Investimento → Saída.

Resultados:

-   2.800 entradas correspondentes a receitas;
-   2.158 saídas correspondentes a despesas e investimentos;
-   zero divergências de classificação.

## 6.5 Status do lançamento versus fluxo de caixa

  Status do lançamento     Quantidade Movimento de caixa
  ---------------------- ------------ -------------------------
  Realizado                     4.958 Todos possuem movimento
  Pendente                      1.748 Nenhum possui movimento

A correspondência foi validada nos dados.

------------------------------------------------------------------------

# 7. Análise de lançamentos e fluxo de caixa

## 7.1 Lançamentos realizados e pendentes

  Status        Quantidade   Percentual
  ----------- ------------ ------------
  Realizado          4.958       73,93%
  Pendente           1.748       26,07%
  **Total**      **6.706**     **100%**

## 7.2 Prazo entre lançamento e movimento de caixa

Foram comparadas as datas de lançamento e de movimento de caixa para os
4.958 registros correspondentes.

  Estatística       Dias
  --------------- ------
  Média             7,63
  Desvio padrão     4,61
  Mínimo               0
  Mediana              8
  1º quartil           4
  3º quartil          12
  Máximo              15

-   302 movimentos ocorreram na mesma data do lançamento.
-   4.656 ocorreram depois do lançamento.
-   Nenhum movimento de caixa ocorreu antes do lançamento.

A diferença temporal pode representar prazo operacional entre lançamento
e movimentação. Contudo, não há informação suficiente para atribuir uma
causa definitiva.

## 7.3 Tipo de lançamento versus movimento

  Tipo             Entrada   Saída
  -------------- --------- -------
  Receita            2.800       0
  Despesa                0   1.915
  Investimento           0     243

A classificação está coerente com as regras validadas.

------------------------------------------------------------------------

# 8. Análise de conciliação

## 8.1 Distribuição geral

  Status         Quantidade   Valor total aproximado
  ------------ ------------ ------------------------
  Conciliado          1.210        R\$ 49,04 milhões
  Confirmado          3.748       R\$ 152,98 milhões

O valor médio dos movimentos:

-   Conciliado: R\$ 40.530,37.
-   Confirmado: R\$ 40.815,72.

Os dois status aparecem em bancos Safra, Bradesco, Itaú, Nubank e
Santander.

## 8.2 Evolução anual

  Ano        Conciliado       Confirmado
  ------ -------------- ----------------
  2024     390 (24,57%)   1.197 (75,43%)
  2025     409 (24,56%)   1.256 (75,44%)
  2026     401 (23,94%)   1.274 (76,06%)

O ano de 2027 é parcial, com 31 registros, e não deve ser comparado
diretamente aos anos completos.

## 8.3 Prazo de conciliação por status

  Status         Quantidade   Média de dias   Mediana   Mínimo   Máximo
  ------------ ------------ --------------- --------- -------- --------
  Conciliado          1.210            7,68         8        0       15
  Confirmado          3.748            7,61         8        0       15

O prazo médio é praticamente igual entre os status.

**Conclusão:** os dados não permitem afirmar que `Conciliado` significa
um movimento mais rápido ou mais lento do que `Confirmado`. É necessária
uma definição formal de negócio.

------------------------------------------------------------------------

# 9. Análise de lançamentos pendentes

## 9.1 Indicadores gerais

-   Quantidade: 1.748.
-   Percentual sobre os lançamentos: 26,07%.
-   Valor total: **R\$ 70.928.039,21**.
-   Período de lançamento: 01/01/2024 a 30/12/2026.

**Importante:** pendente não significa vencido, inadimplente ou em
atraso. Não existe campo de vencimento disponível nesta análise.

## 9.2 Pendências por tipo

  Tipo             Quantidade          Valor pendente     Valor médio
  -------------- ------------ ----------------------- ---------------
  Receita               1.003       R\$ 47.733.628,78   R\$ 47.590,86
  Despesa                 669       R\$ 20.907.355,94   R\$ 31.251,65
  Investimento             76        R\$ 2.287.054,49   R\$ 30.092,82
  **Total**         **1.748**   **R\$ 70.928.039,21**             ---

Aproximadamente 67,3% do valor pendente está associado a receitas.

## 9.3 Pendências por conta contábil

As três contas de receita operacional com maior valor pendente:

  Conta                        Quantidade               Valor
  -------------------------- ------------ -------------------
  Receita de Licenciamento            347   R\$ 17.279.870,90
  Receita de Consultoria              324   R\$ 14.951.248,44
  Receita de Serviços                 303   R\$ 14.637.060,66

As três contas somam aproximadamente **R\$ 46,87 milhões**, cerca de
66,1% do valor pendente total.

## 9.4 Pendências por centro de custo

  Centro               Quantidade     Valor pendente
  ------------------ ------------ ------------------
  Diretoria                   197   R\$ 7.881.217,16
  Marketing                   170   R\$ 7.563.699,64
  Comercial                   181   R\$ 7.527.683,07
  Administrativo              187   R\$ 7.320.454,38
  Jurídico                    173   R\$ 7.089.334,65
  Recursos Humanos            166   R\$ 7.086.742,83
  Customer Success            173   R\$ 6.996.590,77
  Operações                   177   R\$ 6.788.712,45
  Financeiro                  175   R\$ 6.752.161,65
  Tecnologia                  149   R\$ 5.921.442,61

Diretoria possui o maior valor pendente. Marketing possui o maior valor
médio por lançamento pendente, aproximadamente R\$ 44.492,35.

## 9.5 Pendências por grupo DRE

  Grupo                      Quantidade      Valor pendente
  ------------------------ ------------ -------------------
  Receita Operacional               974   R\$ 46.868.180,00
  Pessoal                           162    R\$ 4.820.229,18
  Administrativo                    148    R\$ 4.769.636,59
  Tecnologia                         75    R\$ 2.393.562,54
  CAPEX                              76    R\$ 2.287.054,49
  Comercial e Marketing              72    R\$ 2.089.665,26
  Financeiro                         46    R\$ 1.732.288,16
  Não Caixa                          44    R\$ 1.379.806,61
  Tributos                           48    R\$ 1.355.686,13
  Operações                          39    R\$ 1.203.050,75
  Serviços Profissionais             35    R\$ 1.163.430,72
  Receita Financeira                 29      R\$ 865.448,78

## 9.6 Evolução anual das pendências

  Ano      Quantidade      Valor pendente     Valor médio
  ------ ------------ ------------------- ---------------
  2024            550   R\$ 22.304.813,32   R\$ 40.554,21
  2025            617   R\$ 24.691.186,55   R\$ 40.018,13
  2026            581   R\$ 23.932.039,34   R\$ 41.191,12

2025 apresentou o maior volume. Em 2026, a quantidade e o valor pendente
diminuíram em relação a 2025.

## 9.7 Evolução mensal

-   Maior valor mensal: novembro/2026 --- R\$ 2.674.103,02, com 67
    registros.
-   Menor valor mensal: fevereiro/2024 --- R\$ 1.537.602,98, com 42
    registros.
-   Novembro teve 168 pendências somando os três anos, a maior
    quantidade por mês do calendário.

A análise temporal usa a data de lançamento, não a data de mudança do
status. Portanto, não mede o envelhecimento real do backlog nem
demonstra quanto tempo cada lançamento permaneceu pendente.

------------------------------------------------------------------------

# 10. Análise exploratória por centro de custo

O cruzamento dos lançamentos com plano de contas e centros de custo não
identificou contas ou centros sem correspondência.

Valores agregados de lançamentos por centro de custo:

  Centro               Quantidade      Valor agregado
  ------------------ ------------ -------------------
  Comercial                   706   R\$ 29.082.394,38
  Diretoria                   702   R\$ 28.965.585,35
  Jurídico                    679   R\$ 27.854.915,66
  Administrativo              708   R\$ 27.793.983,73
  Financeiro                  683   R\$ 27.596.223,92
  Marketing                   664   R\$ 27.567.452,70
  Recursos Humanos            661   R\$ 27.469.177,79
  Operações                   655   R\$ 26.365.330,87
  Tecnologia                  637   R\$ 25.422.650,86
  Customer Success            611   R\$ 24.829.394,38

**Limitação interpretativa:** esses totais agregam receitas, despesas e
investimentos. Não devem ser tratados como custos líquidos, despesas
totais ou lucro por centro de custo.

Para produzir indicadores gerenciais apropriados, será necessário
separar receitas, despesas e investimentos, além de definir regras de
alocação e sinal contábil.

------------------------------------------------------------------------

# 11. Registro de questões de Data Quality

## DQ-001 --- Movimentações de caixa fora do calendário original

**Descrição:** 31 movimentações de caixa ocorreram entre 01/01/2027 e
15/01/2027, após o término do calendário original em 31/12/2026.

**Investigação:** todas as 31 movimentações possuem lançamentos
relacionados, datados de dezembro de 2026. Não foram identificadas
movimentações órfãs.

**Decisão:** preservar os registros.

**Recomendação:** ampliar a dimensão calendário até pelo menos
31/01/2027. Manter 2024--2026 como período analítico principal.

**Classificação:** exceção temporal explicada pelo relacionamento com
lançamentos, mas requer ajuste da dimensão calendário.

## DQ-002 --- Correspondência entre status de lançamento e fluxo de caixa

**Descrição:** os 4.958 lançamentos `Realizado` possuem movimento de
caixa correspondente; os 1.748 `Pendente` não possuem movimento.

**Resultado:** regra consistente no conjunto analisado.

**Decisão:** manter a regra como validação de negócio do laboratório.

**Limitação:** não há evidência de que a regra seja universal para todos
os sistemas financeiros reais.

## DQ-003 --- Definição dos status `Confirmado` e `Conciliado`

**Descrição:** os dois status aparecem no fluxo de caixa, mas os dados
não esclarecem formalmente seu significado, hierarquia ou processo
operacional.

**Investigação:** distribuição e prazo médio são semelhantes; o tempo
entre lançamento e movimento não explica a diferença de status.

**Decisão:** preservar os rótulos originais.

**Recomendação:** obter definição do responsável financeiro antes de
criar regras de equivalência, prioridade ou KPI de conciliação.

------------------------------------------------------------------------

# 12. Principais achados e insights

## Achado 1 --- Integridade estrutural consistente

As chaves primárias e os relacionamentos avaliados não apresentaram
nulos, duplicidades ou IDs inválidos.

**Implicação:** a base está em condições favoráveis para avançar para
modelagem analítica, após os ajustes de calendário e validações de
negócio.

## Achado 2 --- Regras de classificação financeira consistentes

Tipo de lançamento, natureza da conta e tipo de movimento de caixa
apresentaram coerência nas regras testadas.

**Implicação:** as regras podem ser documentadas e reutilizadas no
processo de transformação, com confirmação do responsável de negócio.

## Achado 3 --- Folha de pagamento aritmeticamente consistente

Os 6.009 registros passaram pelas fórmulas aritméticas verificadas.

**Implicação:** os campos calculados podem ser utilizados na exploração
analítica, respeitando o limite de que não foi feita auditoria legal.

## Achado 4 --- Volume expressivo de lançamentos pendentes

O valor pendente é R\$ 70,93 milhões, com predominância de receitas.

**Implicação:** é um tema relevante para análise financeira e
acompanhamento de status.

**Cautela:** não equivale a contas vencidas ou inadimplência, pois não
há datas de vencimento.

## Achado 5 --- Concentração das pendências em receitas operacionais

Cerca de 66,1% do valor pendente está nas três contas operacionais de
receita de maior valor.

**Implicação:** essas contas podem ser priorizadas em uma análise de
acompanhamento de lançamentos.

## Achado 6 --- Status de conciliação ainda sem definição suficiente

A diferença entre `Confirmado` e `Conciliado` não é explicada pela
distribuição temporal disponível.

**Implicação:** a definição de negócio deve ser esclarecida antes da
criação de indicadores executivos de conciliação.

------------------------------------------------------------------------

# 13. Limitações analíticas

1.  Não há data de vencimento dos lançamentos pendentes.
2.  Não há histórico de alterações de status.
3.  Não é possível medir aging real do backlog.
4.  Não foi definida formalmente a semântica de `Confirmado` e
    `Conciliado`.
5.  Não foi realizada auditoria contábil, tributária ou trabalhista.
6.  Totais por centro de custo incluem receitas, despesas e
    investimentos.
7.  A base é sintética e não representa dados de uma empresa real.
8.  Não foram avaliadas regras de materialidade, políticas contábeis ou
    critérios de competência além das verificações descritas.

------------------------------------------------------------------------

# 14. Recomendações para a próxima etapa

## 14.1 Antes do BI

-   Atualizar a dimensão calendário até 31/01/2027.
-   Documentar a definição dos status de fluxo de caixa.
-   Formalizar regras de classificação financeira.
-   Preservar os nulos condicionais de cliente e fornecedor.
-   Manter o registro DQ-001, DQ-002 e DQ-003.
-   Separar receitas, despesas e investimentos nas medidas analíticas.

## 14.2 Próxima fase sugerida

Avançar para **modelagem analítica e Business Intelligence**, evitando
prolongar indefinidamente a fase de profiling.

Sequência sugerida:

1.  Consolidar e versionar os scripts de Data Quality.
2.  Preparar camada de dados limpa e documentada.
3.  Definir modelo dimensional e granularidade das tabelas.
4.  Criar métricas financeiras com regras explícitas.
5.  Desenvolver análises exploratórias de negócio.
6.  Construir dashboard executivo e páginas analíticas.
7.  Documentar insights, limitações e decisões.

------------------------------------------------------------------------

# 15. Conclusão

A etapa de Data Quality e Data Understanding da FinVERTEX Analytics foi
conduzida por meio de 31 scripts Python, cobrindo profiling,
integridade, consistência de regras financeiras, folha de pagamento,
orçamento, fluxo de caixa, conciliação e lançamentos pendentes.

Os testes executados indicam que as tabelas examinadas apresentam boa
consistência estrutural e relacional. Foram identificadas exceções e
questões de negócio que devem ser documentadas, mas não há evidência,
nas validações realizadas, de falhas generalizadas de integridade.

Os principais pontos de atenção são:

-   ampliar a dimensão calendário para contemplar os movimentos de
    janeiro de 2027;
-   esclarecer os status de conciliação;
-   não interpretar pendências como atraso ou inadimplência sem
    vencimento;
-   separar receitas, despesas e investimentos nas análises por centro
    de custo.

**Recomendação final:** encerrar a etapa exploratória de Data Quality,
manter o relatório e o registro de questões como documentação oficial do
laboratório e avançar para modelagem analítica e Business Intelligence.

------------------------------------------------------------------------

## Apêndice --- Scripts executados

  Script   Tema
  -------- ------------------------------------------
  01       Data Profiling
  02       Validação do período
  03       Investigação de datas fora do calendário
  04       Validação de lançamentos e caixa
  05       Integridade referencial
  06       Chaves primárias
  07       Datas de funcionários
  08       Status de desligamento
  09       Inspeção da folha de pagamento
  10       Validação aritmética da folha
  11       Inspeção do orçamento
  12       Validação do orçamento
  13       Inspeção do fluxo de caixa
  14       Validação do fluxo de caixa
  15       Caixa versus lançamentos
  16       Tipo de lançamento versus movimento
  17       Validação do tipo de movimento
  18       Inspeção de lançamentos financeiros
  19       Validação dos lançamentos financeiros
  20       Status do lançamento versus caixa
  21       Inspeção da conciliação
  22       Conciliação temporal
  23       Prazo de conciliação
  24       Status por tipo de lançamento
  25       Inspeção do plano de contas
  26       Validação do plano de contas
  27       Inspeção dos centros de custo
  28       Validação dos centros de custo
  29       Classificação cruzada entre dimensões
  30       Análise de lançamentos pendentes
  31       Análise temporal de pendências

**Fim do relatório consolidado.**
