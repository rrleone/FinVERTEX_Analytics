import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_lancamentos_financeiros.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\nANÁLISE — STATUS POR TIPO DE LANÇAMENTO")
print("=" * 60)

print("\n1. CONTAGEM POR TIPO E STATUS")

print(pd.crosstab(
    df["tipo_lancamento"],
    df["status_lancamento"]
).to_string())

print("\n2. PERCENTUAL DE STATUS DENTRO DE CADA TIPO")

percentual = pd.crosstab(
    df["tipo_lancamento"],
    df["status_lancamento"],
    normalize="index"
) * 100

print(percentual.round(2).to_string())

print("\n3. VALORES FINANCEIROS POR TIPO E STATUS")

print(
    df.groupby(
        ["tipo_lancamento", "status_lancamento"]
    )["valor"]
    .agg(["count", "sum", "mean"])
    .round(2)
    .to_string()
)

print("\nANÁLISE CONCLUÍDA")