# FinVERTEX Analytics

## Documento de Modelagem Dimensional --- Versão 1.0

**Fase:** Modelagem Analítica e Business Intelligence\
**Objetivo:** estabelecer a arquitetura dimensional para análises
financeiras no Power BI, evitando duplicação de valores e preservando a
granularidade de cada fato.

------------------------------------------------------------------------

# 1. Princípios da modelagem

A modelagem será orientada por um modelo estrela (Star Schema), com
dimensões ao redor de tabelas fato.

Princípios adotados:

1.  Cada tabela fato mantém sua granularidade original.
2.  Dimensões filtram fatos; fatos não devem ser relacionados
    diretamente entre si para análises comuns.
3.  Relacionamentos preferencialmente `1:*`, com filtro unidirecional da
    dimensão para o fato.
4.  Chaves primárias das dimensões devem ser únicas.
5.  Medidas devem ser calculadas na tabela fato correspondente.
6.  Orçamento, lançamentos, fluxo de caixa e folha não devem ser unidos
    em uma tabela plana sem controle de granularidade.
7.  Valores de Receita, Despesa e Investimento devem ser analisados
    separadamente antes de produzir indicadores líquidos.

------------------------------------------------------------------------

# 2. Granularidade das tabelas fato

A granularidade é o significado de uma linha da tabela. Ela deve ser
documentada antes de criar medidas.

  -----------------------------------------------------------------------
  Tabela fato                         Granularidade proposta
  ----------------------------------- -----------------------------------
  `fato_lancamentos_financeiros`      Um registro por lançamento
                                      financeiro (`id_lancamento`)

  `fato_orcamento`                    Um registro por combinação de
                                      competência, conta contábil e
                                      centro de custo

  `fato_fluxo_caixa`                  Um registro por movimento de caixa
                                      (`id_movimento_caixa`)

  `fato_folha_pagamento`              Um registro por linha de folha
                                      conforme chave do arquivo;
                                      confirmar se representa funcionário
                                      por competência
  -----------------------------------------------------------------------

**Nota:** a granularidade da folha deve ser confirmada com o conteúdo
completo do arquivo e sua chave. Não assumir automaticamente uma linha
por funcionário por mês.

------------------------------------------------------------------------

# 3. Dimensões propostas

## 3.1 `dim_calendario`

Dimensão de datas compartilhada.

Campos existentes incluem data e atributos de calendário. Recomenda-se
garantir:

-   `data` ou coluna de data principal;
-   ano;
-   mês;
-   número do mês;
-   nome do mês;
-   trimestre;
-   ano-mês (ex.: `2026-11`);
-   início do mês;
-   indicador de fim de mês, se útil.

**Ajuste de Data Quality:** estender o calendário até 31/01/2027, pois o
fluxo de caixa possui 31 movimentos até 15/01/2027. O período analítico
principal permanece 2024--2026.

A coluna de data deve ser marcada como **Date table** no Power BI, após
garantir que tenha datas únicas, contínuas e sem nulos.

## 3.2 Dimensões existentes

  Dimensão             Chave               Uso principal
  -------------------- ------------------- ------------------------------
  `dim_funcionario`    `id_funcionario`    Folha, análise de pessoal
  `dim_cliente`        `id_cliente`        Receita e clientes
  `dim_fornecedor`     `id_fornecedor`     Despesas e fornecedores
  `dim_plano_contas`   `id_conta`          Classificação contábil e DRE
  `dim_centro_custo`   `id_centro_custo`   Análise gerencial por área
  `dim_calendario`     Data                Análises temporais

------------------------------------------------------------------------

# 4. Modelo estrela proposto

``` mermaid
flowchart TB
    CAL[dim_calendario]
    CTA[dim_plano_contas]
    CC[dim_centro_custo]
    CLI[dim_cliente]
    FOR[dim_fornecedor]
    FUN[dim_funcionario]

    LF[(fato_lancamentos_financeiros)]
    ORC[(fato_orcamento)]
    CX[(fato_fluxo_caixa)]
    FP[(fato_folha_pagamento)]

    CAL --> LF
    CTA --> LF
    CC --> LF
    CLI --> LF
    FOR --> LF

    CAL --> ORC
    CTA --> ORC
    CC --> ORC

    CAL --> CX
    CTA --> CX
    CC --> CX

    CAL --> FP
    FUN --> FP
```

**Importante:** o diagrama mostra dimensões compartilhadas filtrando
fatos. Não representa relacionamento direto entre as tabelas fato.

------------------------------------------------------------------------

# 5. Relacionamentos propostos

## 5.1 Lançamentos financeiros

  Dimensão          Chave dimensão      Chave fato          Cardinalidade
  ----------------- ------------------- ------------------- ---------------
  Calendário        Data                `data_lancamento`   1:\*
  Plano de contas   `id_conta`          `id_conta`          1:\*
  Centro de custo   `id_centro_custo`   `id_centro_custo`   1:\*
  Cliente           `id_cliente`        `id_cliente`        1:\*
  Fornecedor        `id_fornecedor`     `id_fornecedor`     1:\*

Cliente e fornecedor são relacionamentos opcionais, pois os IDs possuem
valores nulos em parte dos lançamentos.

## 5.2 Orçamento

  Dimensão          Chave dimensão              Chave fato          Cardinalidade
  ----------------- --------------------------- ------------------- ---------------
  Calendário        Competência / data mensal   `competencia`       1:\*
  Plano de contas   `id_conta`                  `id_conta`          1:\*
  Centro de custo   `id_centro_custo`           `id_centro_custo`   1:\*

**Atenção à competência:** se `competencia` estiver armazenada como
primeiro dia do mês, criar/usar uma chave de data mensal compatível.
Evitar relacionar orçamento a todas as datas do mês de forma ambígua.

## 5.3 Fluxo de caixa

  Dimensão          Chave dimensão      Chave fato          Cardinalidade
  ----------------- ------------------- ------------------- ---------------
  Calendário        Data                `data_movimento`    1:\*
  Plano de contas   `id_conta`          `id_conta`          1:\*
  Centro de custo   `id_centro_custo`   `id_centro_custo`   1:\*

O `id_lancamento` presente no fluxo de caixa é útil para rastreabilidade
e validação, mas **não será usado como relacionamento direto entre fatos
no modelo principal**. Um relacionamento fato-fato pode gerar
ambiguidade e duplicação em análises.

## 5.4 Folha de pagamento

  Dimensão      Chave dimensão     Chave fato                           Cardinalidade
  ------------- ------------------ ------------------------------------ ---------------
  Calendário    Competência        Campo de competência/data na folha   1:\*
  Funcionário   `id_funcionario`   `id_funcionario`                     1:\*

O campo temporal exato da folha deve ser confirmado antes de criar o
relacionamento.

------------------------------------------------------------------------

# 6. Relacionamentos no Power BI

Configuração recomendada:

-   Cardinalidade: \*\*Um para muitos (1:\*)\*\*.
-   Lado `1`: dimensão.
-   Lado `*`: tabela fato.
-   Direção do filtro: **Única**, dimensão → fato.
-   Relacionamentos ativos sempre que não houver conflito de papéis de
    data.
-   Evitar relacionamentos muitos-para-muitos.
-   Evitar filtro bidirecional como solução padrão.
-   Não criar relacionamento direto entre fatos.

## Datas com diferentes significados

A dimensão calendário pode ter mais de uma relação com uma tabela fato,
por exemplo:

-   data de lançamento;
-   data de movimento;
-   data de competência.

Se uma fato tiver múltiplas datas, manter uma relação ativa principal e
relações secundárias inativas, quando necessário, ativadas em medidas
DAX com `USERELATIONSHIP`. Isso só deve ser aplicado após confirmar a
necessidade analítica.

------------------------------------------------------------------------

# 7. Cuidados com orçamento versus realizado

Uma comparação orçamento versus realizado é uma das análises centrais do
projeto, mas exige cuidado.

O orçamento está na granularidade:

**Competência + Conta + Centro de custo**

Os lançamentos estão na granularidade:

**Lançamento individual**

Não se deve mesclar orçamento diretamente com lançamentos linha a linha,
pois o orçamento mensal pode ser repetido para cada lançamento daquele
mês/conta/centro.

A abordagem recomendada é:

1.  Relacionar ambas as fatos às dimensões compartilhadas.
2.  Criar medidas independentes de orçamento e realizado.
3.  Comparar as medidas no contexto de competência, conta e centro de
    custo.
4.  Validar se o conceito de "realizado" será baseado em
    `status_lancamento = Realizado`.
5.  Definir tratamento de sinais e tipos de lançamento para orçamento
    versus realizado.

------------------------------------------------------------------------

# 8. Medidas iniciais --- somente após validar o modelo

Exemplos conceituais, ainda não definitivos:

``` dax
Valor Lançamentos =
SUM ( fato_lancamentos_financeiros[valor] )
```

``` dax
Valor Lançamentos Realizados =
CALCULATE (
    [Valor Lançamentos],
    fato_lancamentos_financeiros[status_lancamento] = "Realizado"
)
```

``` dax
Valor Lançamentos Pendentes =
CALCULATE (
    [Valor Lançamentos],
    fato_lancamentos_financeiros[status_lancamento] = "Pendente"
)
```

``` dax
Valor Orçado =
SUM ( fato_orcamento[valor_orcado] )
```

``` dax
Valor Fluxo de Caixa =
SUM ( fato_fluxo_caixa[valor_movimento] )
```

Essas medidas são apenas ponto de partida. Não representam
automaticamente receita líquida, lucro, despesa líquida ou saldo de
caixa. O tratamento de sinais e o significado gerencial devem ser
formalizados antes dos KPIs executivos.

------------------------------------------------------------------------

# 9. Decisões ainda necessárias

Antes da implementação final, confirmar:

1.  Qual coluna temporal da folha representa a competência.
2.  Se `valor` em lançamentos está armazenado sempre positivo, conforme
    observado, e como deve ser tratado em indicadores.
3.  Se orçamento compara com lançamentos Realizados, movimentos de caixa
    ou outra definição de realizado.
4.  Como representar receita, despesa e investimento em medidas
    financeiras.
5.  Definição oficial de `Confirmado` e `Conciliado`.
6.  Se o modelo será construído inicialmente no Power BI ou em uma
    camada SQL/Python antes do Power BI.

------------------------------------------------------------------------

# 10. Próxima atividade prática

A próxima atividade será **validar os campos exatos e as chaves
temporais antes de implementar relacionamentos**.

Ordem recomendada:

1.  Inspecionar as colunas completas de `fato_folha_pagamento.csv`.
2.  Confirmar a competência da folha.
3.  Revisar as colunas temporais da dimensão calendário.
4.  Confirmar se orçamento e folha usam datas no primeiro dia do mês.
5.  Atualizar calendário até 31/01/2027.
6.  Só então criar os relacionamentos no Power BI.

**Ponto de controle:** não criar ainda relacionamentos fato-fato nem
medidas de lucro, margem ou saldo de caixa sem definição formal das
regras de negócio.

------------------------------------------------------------------------

## Encerramento

Este documento estabelece a proposta inicial de modelagem dimensional da
FinVERTEX Analytics. A implementação deve seguir após a validação das
chaves e campos temporais, preservando a granularidade e evitando
duplicações de valores.
