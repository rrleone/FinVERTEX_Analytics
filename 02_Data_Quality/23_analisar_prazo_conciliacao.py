import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo_lancamentos = (
    BASE_DIR / "01_Fonte_Dados" / "fato_lancamentos_financeiros.csv"
)

arquivo_caixa = (
    BASE_DIR / "01_Fonte_Dados" / "fato_fluxo_caixa.csv"
)

lancamentos = pd.read_csv(
    arquivo_lancamentos,
    sep=";",
    encoding="utf-8-sig"
)

caixa = pd.read_csv(
    arquivo_caixa,
    sep=";",
    encoding="utf-8-sig"
)

lancamentos["data_lancamento"] = pd.to_datetime(
    lancamentos["data_lancamento"]
)

caixa["data_movimento"] = pd.to_datetime(
    caixa["data_movimento"]
)

df = caixa.merge(
    lancamentos[["id_lancamento", "data_lancamento"]],
    on="id_lancamento",
    how="left",
    validate="one_to_one"
)

df["dias_ate_movimento"] = (
    df["data_movimento"] - df["data_lancamento"]
).dt.days

print("\nANÁLISE — PRAZO ATÉ MOVIMENTO DE CAIXA POR STATUS")
print("=" * 65)

print("\n1. ESTATÍSTICAS POR STATUS")

print(
    df.groupby("status_conciliacao")["dias_ate_movimento"]
    .agg(["count", "mean", "median", "min", "max", "std"])
    .round(2)
    .to_string()
)

print("\n2. DISTRIBUIÇÃO DOS PRAZOS POR STATUS")

print(
    df.groupby(
        ["status_conciliacao", "dias_ate_movimento"]
    ).size().unstack(fill_value=0).to_string()
)

print("\n3. MÉDIA DE PRAZO POR STATUS E TIPO DE MOVIMENTO")

print(
    df.groupby(
        ["status_conciliacao", "tipo_movimento"]
    )["dias_ate_movimento"]
    .mean()
    .round(2)
    .to_string()
)

print("\nANÁLISE CONCLUÍDA")