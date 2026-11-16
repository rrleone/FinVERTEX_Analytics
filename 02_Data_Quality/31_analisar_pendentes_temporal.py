
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "01_Fonte_Dados"

# --------------------------------------------------
# 1. CARREGAR LANÇAMENTOS
# --------------------------------------------------

df = pd.read_csv(
    DATA_DIR / "fato_lancamentos_financeiros.csv",
    sep=";",
    encoding="utf-8-sig"
)

df["data_lancamento"] = pd.to_datetime(
    df["data_lancamento"],
    errors="coerce"
)

# --------------------------------------------------
# 2. FILTRAR PENDENTES
# --------------------------------------------------

pendentes = df[
    df["status_lancamento"] == "Pendente"
].copy()

pendentes["ano"] = pendentes["data_lancamento"].dt.year

pendentes["mes"] = pendentes["data_lancamento"].dt.month

pendentes["ano_mes"] = (
    pendentes["data_lancamento"]
    .dt.to_period("M")
    .astype(str)
)

print("\nANÁLISE TEMPORAL — LANÇAMENTOS PENDENTES")
print("=" * 70)

# --------------------------------------------------
# 3. INDICADORES GERAIS
# --------------------------------------------------

print("\n1. INDICADORES GERAIS")

print("Total pendentes:", len(pendentes))
print("Valor total pendente:", round(pendentes["valor"].sum(), 2))

print(
    "Período:",
    pendentes["data_lancamento"].min(),
    "até",
    pendentes["data_lancamento"].max()
)

# --------------------------------------------------
# 4. PENDENTES POR ANO
# --------------------------------------------------

print("\n2. PENDENTES POR ANO")

por_ano = (
    pendentes.groupby("ano")
    .agg(
        quantidade=("id_lancamento", "count"),
        valor_total=("valor", "sum"),
        valor_medio=("valor", "mean")
    )
    .round(2)
)

print(por_ano.to_string())

# --------------------------------------------------
# 5. PENDENTES POR MÊS
# --------------------------------------------------

print("\n3. PENDENTES POR MÊS")

por_mes = (
    pendentes.groupby("ano_mes")
    .agg(
        quantidade=("id_lancamento", "count"),
        valor_total=("valor", "sum"),
        valor_medio=("valor", "mean")
    )
    .sort_index()
    .round(2)
)

print(por_mes.to_string())

# --------------------------------------------------
# 6. VALOR PENDENTE POR MÊS DO ANO
# --------------------------------------------------

print("\n4. DISTRIBUIÇÃO POR MÊS DO ANO")

por_mes_calendario = (
    pendentes.groupby("mes")
    .agg(
        quantidade=("id_lancamento", "count"),
        valor_total=("valor", "sum"),
        valor_medio=("valor", "mean")
    )
    .round(2)
)

print(por_mes_calendario.to_string())

# --------------------------------------------------
# 7. MÊS COM MAIOR VALOR PENDENTE
# --------------------------------------------------

print("\n5. MÊS COM MAIOR VALOR PENDENTE")

mes_max = por_mes["valor_total"].idxmax()

print("Mês:", mes_max)
print("Valor:", por_mes.loc[mes_max, "valor_total"])
print("Quantidade:", por_mes.loc[mes_max, "quantidade"])

# --------------------------------------------------
# 8. MÊS COM MENOR VALOR PENDENTE
# --------------------------------------------------

print("\n6. MÊS COM MENOR VALOR PENDENTE")

mes_min = por_mes["valor_total"].idxmin()

print("Mês:", mes_min)
print("Valor:", por_mes.loc[mes_min, "valor_total"])
print("Quantidade:", por_mes.loc[mes_min, "quantidade"])

# --------------------------------------------------
# 9. RESUMO
# --------------------------------------------------

print("\n7. RESUMO FINAL")

print("Análise temporal concluída.")
print("Pendências analisadas:", len(pendentes))

print("\nANÁLISE CONCLUÍDA")
