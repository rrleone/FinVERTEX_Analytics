import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_lancamentos_financeiros.csv"
)

# ============================================================
# LEITURA
# ============================================================

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

# ============================================================
# INSPEÇÃO
# ============================================================

print("\nINSPEÇÃO — LANÇAMENTOS FINANCEIROS")
print("=" * 60)

print("\nDimensão:")
print("Linhas:", len(df))
print("Colunas:", len(df.columns))

print("\nColunas:")
print(df.columns.tolist())

print("\nPrimeiros 10 registros:")
print(df.head(10).to_string(index=False))

print("\nValores ausentes:")
print(df.isna().sum().to_string())

print("\nResumo estatístico dos valores:")
print(
    df[["valor"]]
    .describe()
    .round(2)
    .to_string()
)

print("\nTipos de lançamento:")
print(df["tipo_lancamento"].value_counts().to_string())

print("\nStatus dos lançamentos:")
print(df["status_lancamento"].value_counts().to_string())

print("\nMeios de pagamento:")
print(df["meio_pagamento"].value_counts().to_string())

print("\nPeríodo:")
print("Data inicial:", df["data_lancamento"].min())
print("Data final:", df["data_lancamento"].max())