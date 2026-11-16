
import pandas as pd
from pathlib import Path

# ============================================================
# FINVERTEX ANALYTICS
# ETL 05 - Preparação do fluxo de caixa
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "01_Fonte_Dados"
ETL_DIR = BASE_DIR / "03_ETL_Python"

arquivo_entrada = DATA_DIR / "fato_fluxo_caixa.csv"
arquivo_saida = ETL_DIR / "fato_fluxo_caixa_modelado.csv"

df = pd.read_csv(
    arquivo_entrada,
    sep=";",
    encoding="utf-8-sig"
)

print("\nETL 05 — FLUXO DE CAIXA")
print("=" * 60)

print("Registros originais:", len(df))

# Criar coluna de data para relacionamento
df["data_movimento_data"] = pd.to_datetime(
    df["data_movimento"],
    format="%Y-%m-%d"
)

df["data_movimento_data"] = (
    df["data_movimento_data"].dt.strftime("%Y-%m-%d")
)

# Posicionar coluna nova ao lado da data original
colunas = list(df.columns)
colunas.remove("data_movimento_data")

posicao = colunas.index("data_movimento") + 1
colunas.insert(posicao, "data_movimento_data")

df = df[colunas]

df.to_csv(
    arquivo_saida,
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("Arquivo gerado:", arquivo_saida)
print("Total de registros:", len(df))

print("\nTipos de movimento:")
print(df["tipo_movimento"].value_counts())

print("\nStatus de conciliação:")
print(df["status_conciliacao"].value_counts())

print("\nPeríodo:")
print("Data inicial:", df["data_movimento_data"].min())
print("Data final:", df["data_movimento_data"].max())

print("\nETL 05 CONCLUÍDO")
