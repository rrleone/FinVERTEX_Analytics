import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "01_Fonte_Dados"

arquivo = DATA_DIR / "fato_folha_pagamento.csv"

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\nINSPEÇÃO DA FOLHA — MODELAGEM DIMENSIONAL")
print("=" * 70)

print("\n1. COLUNAS")
print(df.columns.tolist())

print("\n2. TIPOS DE DADOS")
print(df.dtypes)

print("\n3. PRIMEIRAS 10 LINHAS")
print(df.head(10).to_string(index=False))

print("\n4. ESTATÍSTICAS TEMPORAIS")
for coluna in df.columns:
    if "data" in coluna.lower() or "compet" in coluna.lower():
        print(f"\nColuna: {coluna}")
        print(df[coluna].value_counts().sort_index().head(15))

print("\n5. CHAVES E GRANULARIDADE")
for coluna in df.columns:
    if "id_funcionario" in coluna.lower():
        print("Funcionários distintos:", df[coluna].nunique())

print("\nTotal de registros:", len(df))

print("\nINSPEÇÃO CONCLUÍDA")