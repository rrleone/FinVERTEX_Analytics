import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_fluxo_caixa.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\nINSPEÇÃO — CONCILIAÇÃO DO FLUXO DE CAIXA")
print("=" * 60)

print("\n1. Status de conciliação:")
print(df["status_conciliacao"].value_counts().to_string())

print("\n2. Tipo de movimento x status:")
print(pd.crosstab(
    df["tipo_movimento"],
    df["status_conciliacao"]
).to_string())

print("\n3. Estatísticas de valores por status:")
print(df.groupby("status_conciliacao")["valor_movimento"].agg(
    ["count", "sum", "mean", "min", "max"]
).round(2).to_string())

print("\n4. Período por status:")
print(df.groupby("status_conciliacao")["data_movimento"].agg(
    ["min", "max"]
).to_string())

print("\n5. Instituição financeira por status:")
print(pd.crosstab(
    df["instituicao_financeira"],
    df["status_conciliacao"]
).to_string())

print("\nINSPEÇÃO CONCLUÍDA")