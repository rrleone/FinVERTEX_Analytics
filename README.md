&#x20;\<div align="center">

\<img src="03_Images/Capa_FinVERTEX_Analytics.png" alt="FinVERTEX Analytics" width="100%"/>

# FinVERTEX Analytics

### Inteligência Financeira · Business Intelligence · Data Analytics

Projeto de Business Intelligence desenvolvido por Renato Leone.

\<img src="[https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge\&logo=powerbi\&logoColor=black)"/> \<img src="[https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)"/> \<img src="[https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge\&logo=postgresql\&logoColor=white)"/> \<img src="[https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=sqlite&logoColor=white](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge\&logo=sqlite\&logoColor=white)"/> \<img src="[https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge\&logo=googlegemini\&logoColor=white)"/> \<img src="[https://img.shields.io/badge/Data%20Quality-008577?style=for-the-badge](https://img.shields.io/badge/Data%20Quality-008577?style=for-the-badge)"/> \<img src="[https://img.shields.io/badge/Business%20Intelligence-0078D4?style=for-the-badge](https://img.shields.io/badge/Business%20Intelligence-0078D4?style=for-the-badge)"/>

**Transformando dados financeiros em indicadores, análises e insights para apoiar decisões estratégicas.**

\</div>

---

## Visão geral do projeto

O **FinVERTEX Analytics** é um projeto de Business Intelligence voltado à análise financeira, desenvolvido para demonstrar como a integração de dados, a qualidade da informação e a análise de indicadores podem apoiar o acompanhamento e a gestão financeira de uma organização.

A solução contempla diferentes perspectivas financeiras, incluindo receitas, despesas, fluxo de caixa, orçamento, custos, centros de custo e folha de pagamento.

O projeto percorre um fluxo analítico que envolve preparação e validação dos dados, processamento com Python, armazenamento em PostgreSQL, consultas SQL, modelagem de dados e desenvolvimento de dashboards interativos no Power BI.

Como diferencial, o projeto também explora a aplicação de Inteligência Artificial no processo de Data Quality, por meio de um agente desenvolvido em Python e integrado ao Google Gemini.

**DATA ENGINEERING · DATA QUALITY · FINANCIAL ANALYTICS · BUSINESS INTELLIGENCE**

Dados → Qualidade → ETL → PostgreSQL → Análises → Indicadores → Dashboards → Insights

---

## Problema de negócio e objetivos

A gestão financeira precisa acompanhar diferentes dimensões da operação para compreender os resultados, controlar despesas, monitorar o fluxo de caixa e avaliar a execução orçamentária.

Quando essas informações são analisadas isoladamente, torna-se mais difícil identificar variações, compreender a composição dos custos e obter uma visão consolidada do desempenho financeiro.

O FinVERTEX Analytics busca estruturar essas informações em um ambiente analítico integrado.

**Objetivos do projeto:**

- Acompanhar receitas, despesas e resultado financeiro.
- Analisar entradas, saídas e movimentações de caixa.
- Avaliar a evolução financeira ao longo dos períodos.
- Comparar valores orçados e realizados.
- Identificar desvios e variações orçamentárias.
- Analisar custos por centro de custo e categoria de conta.
- Acompanhar indicadores relacionados à folha de pagamento.
- Aplicar validações de Data Quality para aumentar a confiabilidade dos dados.
- Explorar a utilização de IA para apoiar processos de tratamento e validação de informações.
- Desenvolver dashboards para apoiar decisões gerenciais.

---

## Dados utilizados

A base utilizada foi desenvolvida para fins de estudo, simulação e portfólio, representando informações de uma operação financeira.

**Características da base:**

- **Origem:** dados simulados.
- **Segmento:** gestão financeira.
- **Banco de dados:** PostgreSQL.
- **Processamento:** Python e SQL.
- **Finalidade:** análise financeira e desenvolvimento de Business Intelligence.
- **Período de referência:** 2024 a 2026.

### Tabelas utilizadas

| Tabela                         | Descrição                                      |
| ------------------------------ | ---------------------------------------------- |
| `dim_calendario`               | Dimensão de datas e períodos                   |
| `dim_funcionario`              | Cadastro e informações dos funcionários        |
| `dim_cliente`                  | Informações cadastrais dos clientes            |
| `dim_fornecedor`               | Informações dos fornecedores                   |
| `dim_centro_custo`             | Classificação dos centros de custo             |
| `dim_plano_contas`             | Estrutura e classificação do plano de contas   |
| `fato_lancamentos_financeiros` | Lançamentos de receitas e despesas             |
| `fato_fluxo_caixa`             | Movimentações financeiras de entradas e saídas |
| `fato_orcamento`               | Informações de planejamento orçamentário       |

---

## Ferramentas e tecnologias

| Tecnologia              | Aplicação                                     |
| ----------------------- | --------------------------------------------- |
| Python                  | Processamento, automação e validação de dados |
| Pandas                  | Manipulação e transformação de dados          |
| Google Gemini 2.5 Flash | Apoio inteligente à análise de dados          |
| Google AI Studio        | Integração com o modelo Gemini                |
| PostgreSQL              | Armazenamento e organização dos dados         |
| SQL                     | Consultas, validações e análises financeiras  |
| Power BI Desktop        | Desenvolvimento dos dashboards                |
| Power Query (M)         | Preparação e transformação dos dados          |
| DAX                     | Criação de medidas e indicadores              |
| Modelagem de dados      | Integração das dimensões e tabelas fato       |

---

## Etapas do projeto

### 1. Perfilamento e qualidade dos dados

Foi realizada uma avaliação das bases para compreender suas estruturas e identificar ocorrências que poderiam comprometer a análise financeira.

As verificações contemplaram:

- Quantidade de registros e colunas.
- Tipos de dados.
- Valores nulos e inválidos.
- Duplicidade de registros.
- Unicidade das chaves.
- Integridade referencial entre tabelas.
- Consistência de datas e valores financeiros.
- Conformidade com regras de negócio.

### 2. Tratamento e transformação dos dados

O tratamento foi estruturado utilizando Python e processos de ETL, considerando as necessidades de padronização e preparação das informações.

As principais atividades envolveram:

- Leitura e processamento dos arquivos de origem.
- Padronização de informações.
- Tratamento de inconsistências.
- Aplicação de regras de negócio.
- Preparação das estruturas para armazenamento.
- Validação dos dados processados.

### 3. ETL e integração com Inteligência Artificial

Foi desenvolvido um fluxo de processamento de dados que explora a integração entre Python e recursos de IA generativa.

O projeto utiliza o Google Gemini 2.5 Flash, por meio do Google AI Studio, como apoio à interpretação e ao tratamento de informações.

A proposta é utilizar a IA para acelerar tarefas específicas do processo, mantendo a responsabilidade do analista na definição das regras, validação das respostas e aprovação dos resultados.

### 4. Agente de IA para Data Quality

Foi desenvolvido um agente de Data Quality em Python integrado ao Gemini 2.5 Flash.

O agente foi concebido para apoiar a análise de arquivos e identificar possíveis problemas de qualidade, produzindo avaliações que auxiliam o processo de validação dos dados.

A solução demonstra a aplicação prática de Inteligência Artificial em atividades de preparação e controle da qualidade das informações.

### 5. Banco de dados e SQL Analytics

Os dados foram organizados no PostgreSQL, utilizando estruturas dimensionais e tabelas fato para integrar as informações financeiras.

O SQL foi utilizado para consultas, validações e análises necessárias à construção dos indicadores e à verificação dos resultados.

### 6. Modelagem de dados

Foi estruturado um modelo analítico para integrar as diferentes perspectivas financeiras.

A modelagem contempla relacionamentos entre calendário, plano de contas, centros de custo, funcionários e tabelas de movimentações financeiras.

Essa organização permite explorar os indicadores por diferentes períodos, categorias e dimensões de negócio.

### 7. Indicadores e medidas DAX

Foram desenvolvidas medidas para acompanhar o desempenho financeiro e apoiar a análise gerencial.

Entre os principais indicadores:

- Receita Total.
- Despesas Totais.
- Resultado Financeiro.
- Índice de Despesas sobre Receitas.
- Entradas de Caixa.
- Saídas de Caixa.
- Saldo Líquido de Caixa.
- Valores Orçados.
- Valores Realizados.
- Desvio Orçamentário.
- Percentual de Execução Orçamentária.
- Custos por Centro de Custo.
- Indicadores da Folha de Pagamento.

Os indicadores permitem analisar resultados, comparar períodos, acompanhar variações e identificar oportunidades de melhoria.

---

## Dashboards

O relatório foi estruturado em seis páginas analíticas, cada uma dedicada a uma perspectiva da gestão financeira.

### 01 — Visão Financeira Executiva

Apresenta uma visão consolidada dos principais indicadores financeiros.



**Principais elementos:**

- Receita Total.
- Despesas Totais.
- Resultado Financeiro.
- Saldo de Caixa.
- Evolução Financeira por Quadrimestre.
- Movimentação de Caixa por Quadrimestre.
- Despesas por Categoria de Conta.
- Insights sobre desempenho financeiro, estrutura de despesas e posição de caixa.

### 02 — Fluxo de Caixa

Apresenta o comportamento das movimentações financeiras e a evolução do fluxo líquido de caixa.



**Principais análises:**

- Entradas e Saídas de Caixa.
- Saldo Líquido do Período.
- Saldo Acumulado.
- Movimentações por Status de Conciliação.
- Evolução Mensal do Saldo Líquido de Caixa.
- Evolução Acumulada do Fluxo Líquido por Quadrimestre.

### 03 — Receitas e Despesas

Apresenta a composição das receitas e despesas e o desempenho financeiro ao longo dos períodos.



**Principais análises:**

- Receita Total.
- Despesas Totais.
- Resultado Financeiro.
- Índice de Despesas sobre Receitas.
- Composição das Despesas por Conta.
- Evolução do Resultado Financeiro por Quadrimestre.
- Comparação entre receitas e despesas.

### 04 — Orçado vs. Realizado

Permite acompanhar o planejamento financeiro e avaliar os desvios entre valores orçados e realizados.



**Principais análises:**

- Valor Orçado.
- Valor Realizado.
- Desvio Orçamentário.
- Percentual de Execução.
- Orçado vs. Realizado por Quadrimestre.
- Desvio Orçamentário por Centro de Custo.
- Evolução do Percentual de Execução Orçamentária.

### 05 — Custos e Centros de Custo

Apresenta a distribuição dos custos e permite avaliar sua concentração entre os diferentes centros de custo e categorias financeiras.



**Principais análises:**

- Custos Totais.
- Custo Médio por Centro de Custo.
- Maior Custo por Centro.
- Concentração de Custos.
- Evolução dos Custos por Quadrimestre.
- Custos Totais por Centro de Custo.
- Composição dos Custos por Categoria de Conta.

### 06 — Folha de Pagamento

Apresenta uma visão analítica dos custos relacionados à remuneração, benefícios e encargos dos colaboradores.



**Principais análises:**

- Custo Total da Folha.
- Custo Médio por Centro de Custo.
- Custo Médio por Colaborador.
- Variação da Folha.
- Composição do Custo Total por Quadrimestre.
- Evolução do Custo Total da Folha por Quadrimestre.
- Intensidade do Custo da Folha por Mês.

---

## Principais insights

O projeto reúne indicadores que permitem acompanhar diferentes dimensões do desempenho financeiro.

Entre os resultados observados na base simulada:

- A receita total registrada foi de aproximadamente **R$ 134,28 milhões**.
- As despesas realizadas totalizaram aproximadamente **R$ 60,21 milhões**.
- O resultado financeiro foi de aproximadamente **R$ 74,07 milhões**.
- O índice de despesas sobre receitas foi de **44,84%**, classificado como moderado conforme a regra de negócio adotada.
- O fluxo de caixa permite investigar as movimentações de entradas e saídas, considerando os respectivos status de conciliação.
- A análise orçamentária permite acompanhar a execução e identificar diferenças entre planejamento e realização.
- A análise de custos evidencia a distribuição dos valores entre centros de custo e categorias de contas.
- A folha de pagamento permite acompanhar a composição e a evolução dos custos com pessoal.

Os resultados representam o comportamento observado na base simulada e devem ser interpretados considerando as regras de negócio e as características dos dados utilizados.

---

## Conclusão e recomendações

O FinVERTEX Analytics demonstra a aplicação integrada de conceitos de Engenharia de Dados, Data Quality, ETL, SQL, Inteligência Artificial e Business Intelligence em um contexto de gestão financeira.

O projeto evidencia como a organização e a validação dos dados constituem a base para a construção de indicadores confiáveis e análises que apoiam decisões gerenciais.

Como oportunidades de acompanhamento e evolução, recomenda-se:

- Monitorar a evolução das receitas e despesas.
- Avaliar a eficiência da estrutura de custos.
- Acompanhar a execução orçamentária e seus desvios.
- Investigar a evolução do fluxo de caixa.
- Monitorar os custos por centro de custo.
- Avaliar a evolução dos custos com pessoal.
- Ampliar a automação do agente de Data Quality.
- Evoluir a integração entre processamento, validação e disponibilização dos dados.

---

## Estrutura do repositório

```text
FinVERTEX_Analytics/
│
├── 01_Fonte_Dados/
├── 02_Data_Quality/
├── 03_ETL_Python/
├── 04_PostgreSQL/
├── 05_SQL_Analytics/
│
├── 06_PowerBI/
│   └── FinVERTEX_Analytics.pbix
│
├── 07_Documentacao/
├── 08_Insights/
│
├── 03_Images/
│   ├── Capa_FinVERTEX_Analytics.png
│   ├── dashboard_01_visao_financeira_executiva.png
│   ├── dashboard_02_fluxo_de_caixa.png
│   ├── dashboard_03_receitas_despesas.png
│   ├── dashboard_04_orcado_realizado.png
│   ├── dashboard_05_custos_centros_custo.png
│   └── dashboard_06_folha_pagamento.png
│
└── README.md
```

---

## Como reproduzir o projeto

1. Clone ou baixe o repositório.
2. Consulte a pasta `01_Fonte_Dados` para conhecer as bases utilizadas.
3. Acesse `02_Data_Quality` para verificar as rotinas de validação.
4. Consulte `03_ETL_Python` para acompanhar os processos de preparação e transformação.
5. Configure o PostgreSQL conforme a documentação disponível em `04_PostgreSQL`.
6. Consulte as análises e consultas SQL em `05_SQL_Analytics`.
7. Acesse a pasta `06_PowerBI`.
8. Abra `FinVERTEX_Analytics.pbix` no Power BI Desktop.
9. Verifique os caminhos das fontes de dados e atualize as conexões, caso necessário.
10. Navegue pelas seis páginas do relatório.

Os dados utilizados são simulados e destinados a fins de estudo, demonstração técnica e portfólio. A reprodução poderá exigir ajustes nas conexões e nos caminhos das fontes de dados.

**Segurança:** credenciais de banco de dados, senhas e chaves de API não devem ser publicadas no repositório.

---

## Autor

**Renato Leone**
Analista de Dados | Business Intelligence

Projeto desenvolvido individualmente para demonstrar competências em análise financeira, qualidade de dados, automação com Python, integração com IA, PostgreSQL, SQL, modelagem analítica, DAX e desenvolvimento de dashboards no Power BI.

### Competências demonstradas

- Análise e interpretação de dados.
- Data Profiling e Data Quality.
- ETL com Python.
- Inteligência Artificial aplicada à análise de dados.
- Integração com Google Gemini.
- SQL e PostgreSQL.
- Modelagem de dados.
- Power Query (M).
- DAX e indicadores financeiros.
- Business Intelligence.
- Visualização e comunicação de insights.

### Portfólio e contato profissional

- **GitHub:** [github.com/rrleone](https://github.com/rrleone)
- **Repositório:** [FinVERTEX Analytics](https://github.com/rrleone/FinVERTEX_Analytics)
- **Portfólio:** [Renato Leone — Data Analytics & BI](https://sites.google.com/view/renatoleone/)

---

**FINVERTEX ANALYTICS**

Dados · Qualidade · Inteligência · Decisões

**RENATO LEONE | DATA ANALYTICS & BUSINESS INTELLIGENCE**
