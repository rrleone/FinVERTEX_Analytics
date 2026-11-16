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

df["data_movimento"] = pd.to_datetime(df["data_movimento"])

df["ano"] = df["data_movimento"].dt.year
df["ano_mes"] = df["data_movimento"].dt.to_period("M").astype(str)

print("\nANÁLISE TEMPORAL — CONCILIAÇÃO DO FLUXO DE CAIXA")
print("=" * 65)

# 1. Status por ano
print("\n1. STATUS POR ANO")
print(pd.crosstab(
    df["ano"],
    df["status_conciliacao"]
).to_string())

# 2. Status por mês
print("\n2. STATUS POR MÊS")
print(pd.crosstab(
    df["ano_mes"],
    df["status_conciliacao"]
).to_string())

# 3. Percentual de cada status por ano
print("\n3. DISTRIBUIÇÃO PERCENTUAL POR ANO")
percentual = pd.crosstab(
    df["ano"],
    df["status_conciliacao"],
    normalize="index"
) * 100

print(percentual.round(2).to_string())

# 4. Datas mais recentes por status
print("\n4. ÚLTIMAS 10 DATAS POR STATUS")

for status in sorted(df["status_conciliacao"].unique()):
    subset = df[df["status_conciliacao"] == status]

    print(f"\nStatus: {status}")
    print(
        subset.sort_values("data_movimento", ascending=False)
        [["data_movimento", "tipo_movimento", "valor_movimento"]]
        .head(10)
        .to_string(index=False)
    )

print("\nANÁLISE CONCLUÍDA")