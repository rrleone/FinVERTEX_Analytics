
import pandas as pd
from pathlib import Path

# ============================================================
# FINVERTEX ANALYTICS
# ETL 03 - Preparação do orçamento
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "01_Fonte_Dados"
ETL_DIR = BASE_DIR / "03_ETL_Python"

arquivo_entrada = DATA_DIR / "fato_orcamento.csv"
arquivo_saida = ETL_DIR / "fato_orcamento_modelado.csv"

df = pd.read_csv(
    arquivo_entrada,
    sep=";",
    encoding="utf-8-sig"
)

print("\nETL 03 — ORÇAMENTO")
print("=" * 60)

print("Registros originais:", len(df))

# Converter competência mensal para data
df["competencia_data"] = pd.to_datetime(
    df["competencia"] + "-01",
    format="%Y-%m-%d"
)

# Formato de exportação
df["competencia_data"] = (
    df["competencia_data"].dt.strftime("%Y-%m-%d")
)

# Posicionar a data ao lado da competência
colunas = list(df.columns)
colunas.remove("competencia_data")

posicao = colunas.index("competencia") + 1
colunas.insert(posicao, "competencia_data")

df = df[colunas]

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

print("\nETL 03 CONCLUÍDO")
