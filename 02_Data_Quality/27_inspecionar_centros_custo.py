
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "dim_centro_custo.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\nINSPEÇÃO — CENTROS DE CUSTO")
print("=" * 60)

# 1. Dimensão
print("\n1. DIMENSÃO")
print("Linhas:", len(df))
print("Colunas:", len(df.columns))

# 2. Colunas
print("\n2. COLUNAS")
print(df.columns.tolist())

# 3. Primeiros registros
print("\n3. PRIMEIROS REGISTROS")
print(df.head(10).to_string(index=False))

# 4. Valores ausentes
print("\n4. VALORES AUSENTES")
print(df.isna().sum().to_string())

# 5. Tipos de dados
print("\n5. TIPOS DE DADOS")
print(df.dtypes.to_string())

# 6. Valores únicos por coluna
print("\n6. VALORES ÚNICOS POR COLUNA")

for coluna in df.columns:
    print(f"\n{coluna}:")
    print(df[coluna].value_counts(dropna=False).to_string())

# 7. Registros completos
print("\n7. REGISTROS COMPLETOS")
print(df.to_string(index=False))

print("\nINSPEÇÃO CONCLUÍDA")
