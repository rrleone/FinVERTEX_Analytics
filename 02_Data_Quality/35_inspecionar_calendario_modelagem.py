
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "01_Fonte_Dados"

arquivo = DATA_DIR / "dim_calendario.csv"

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\nINSPEÇÃO DO CALENDÁRIO — MODELAGEM")
print("=" * 70)

print("\n1. COLUNAS")
print(df.columns.tolist())

print("\n2. TIPOS DE DADOS")
print(df.dtypes)

print("\n3. PRIMEIRAS 10 LINHAS")
print(df.head(10).to_string(index=False))

print("\n4. ÚLTIMAS 10 LINHAS")
print(df.tail(10).to_string(index=False))

print("\n5. PERÍODO")
coluna_data = next(
    coluna for coluna in df.columns
    if "data" in coluna.lower()
)

df[coluna_data] = pd.to_datetime(df[coluna_data])

print("Data mínima:", df[coluna_data].min())
print("Data máxima:", df[coluna_data].max())
print("Total de registros:", len(df))

print("\n6. ANO E MÊS DISPONÍVEIS")
for coluna in df.columns:
    if coluna.lower() in ["ano", "mes", "mês", "ano_mes", "ano-mes"]:
        print(f"\n{coluna}:")
        print(df[coluna].value_counts().sort_index().to_string())

print("\nINSPEÇÃO CONCLUÍDA")
