
import pandas as pd
from pathlib import Path

# ============================================================
# FINVERTEX ANALYTICS
# ETL 02 - Preparação da folha de pagamento
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "01_Fonte_Dados"
ETL_DIR = BASE_DIR / "03_ETL_Python"

arquivo_entrada = DATA_DIR / "fato_folha_pagamento.csv"
arquivo_saida = ETL_DIR / "fato_folha_pagamento_modelada.csv"

# Leitura da fonte original
df = pd.read_csv(
    arquivo_entrada,
    sep=";",
    encoding="utf-8-sig"
)

print("\nETL 02 — FOLHA DE PAGAMENTO")
print("=" * 60)

print("Registros originais:", len(df))

# Converter competência mensal para data
df["competencia_data"] = pd.to_datetime(
    df["competencia"] + "-01",
    format="%Y-%m-%d"
)

# Formatar data para exportação
df["competencia_data"] = (
    df["competencia_data"].dt.strftime("%Y-%m-%d")
)

# Organizar coluna de competência junto da data correspondente
colunas = list(df.columns)

colunas.remove("competencia_data")

posicao = colunas.index("competencia") + 1
colunas.insert(posicao, "competencia_data")

df = df[colunas]

# Exportar sem alterar a fonte original
df.to_csv(
    arquivo_saida,
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("Arquivo gerado:", arquivo_saida)
print("Total de registros:", len(df))

print("\nExemplos:")
print(
    df[["competencia", "competencia_data"]]
    .drop_duplicates()
    .head(10)
    .to_string(index=False)
)

print("\nETL 02 CONCLUÍDO")
