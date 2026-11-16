
import pandas as pd
from pathlib import Path

# ============================================================
# FINVERTEX ANALYTICS
# ETL 04 - Preparação dos lançamentos financeiros
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "01_Fonte_Dados"
ETL_DIR = BASE_DIR / "03_ETL_Python"

arquivo_entrada = DATA_DIR / "fato_lancamentos_financeiros.csv"
arquivo_saida = ETL_DIR / "fato_lancamentos_financeiros_modelada.csv"

df = pd.read_csv(
    arquivo_entrada,
    sep=";",
    encoding="utf-8-sig"
)

print("\nETL 04 — LANÇAMENTOS FINANCEIROS")
print("=" * 60)

print("Registros originais:", len(df))

# ------------------------------------------------------------
# Corrigir identificadores para números inteiros
# Int64 do pandas permite inteiros e valores nulos
# ------------------------------------------------------------

colunas_id = [
    "id_lancamento",
    "id_conta",
    "id_centro_custo",
    "id_cliente",
    "id_fornecedor"
]

for coluna in colunas_id:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="raise"
    ).astype("Int64")

# ------------------------------------------------------------
# Criar coluna de data para relacionamento com calendário
# ------------------------------------------------------------

df["data_lancamento_data"] = pd.to_datetime(
    df["data_lancamento"],
    format="%Y-%m-%d"
)

df["data_lancamento_data"] = (
    df["data_lancamento_data"].dt.strftime("%Y-%m-%d")
)

# ------------------------------------------------------------
# Posicionar coluna nova ao lado da data original
# ------------------------------------------------------------

colunas = list(df.columns)
colunas.remove("data_lancamento_data")

posicao = colunas.index("data_lancamento") + 1
colunas.insert(posicao, "data_lancamento_data")

df = df[colunas]

# ------------------------------------------------------------
# Exportar arquivo modelado
# ------------------------------------------------------------

df.to_csv(
    arquivo_saida,
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("Arquivo gerado:", arquivo_saida)
print("Total de registros:", len(df))

print("\nTipos de lançamento:")
print(df["tipo_lancamento"].value_counts())

print("\nStatus:")
print(df["status_lancamento"].value_counts())

print("\nExemplos de identificadores:")
print(df[colunas_id].head(10).to_string(index=False))

print("\nExemplos de datas:")
print(
    df[["data_lancamento", "data_lancamento_data"]]
    .head(5)
    .to_string(index=False)
)

print("\nETL 04 CONCLUÍDO")
