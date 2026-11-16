import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_orcamento.csv"
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

print("\nINSPEÇÃO — ORÇAMENTO FINANCEIRO")
print("=" * 60)

print("\nDimensão da tabela:")
print("Linhas:", len(df))
print("Colunas:", len(df.columns))

print("\nColunas disponíveis:")
print(df.columns.tolist())

print("\nPrimeiros 10 registros:")
print(df.head(10).to_string(index=False))

print("\nValores ausentes por coluna:")
print(df.isna().sum().to_string())

print("\nResumo estatístico:")
print(
    df[
        [
            "valor_orcado"
        ]
    ].describe().round(2).to_string()
)

print("\nDistribuição dos status:")
print(
    df["status_orcamento"]
    .value_counts(dropna=False)
    .to_string()
)

print("\nCompetências:")
print("Menor competência:", df["competencia"].min())
print("Maior competência:", df["competencia"].max())