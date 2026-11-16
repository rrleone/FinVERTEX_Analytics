import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo_caixa = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_fluxo_caixa.csv"
)

arquivo_lancamentos = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_lancamentos_financeiros.csv"
)

# ============================================================
# LEITURA
# ============================================================

caixa = pd.read_csv(
    arquivo_caixa,
    sep=";",
    encoding="utf-8-sig"
)

lancamentos = pd.read_csv(
    arquivo_lancamentos,
    sep=";",
    encoding="utf-8-sig"
)

# ============================================================
# PREPARAÇÃO
# ============================================================

caixa["data_movimento"] = pd.to_datetime(
    caixa["data_movimento"],
    errors="coerce"
)

lancamentos["data_lancamento"] = pd.to_datetime(
    lancamentos["data_lancamento"],
    errors="coerce"
)

# ============================================================
# JUNÇÃO DAS TABELAS
# ============================================================

df = caixa.merge(
    lancamentos,
    on="id_lancamento",
    how="left",
    suffixes=("_caixa", "_lancamento"),
    indicator=True
)

# ============================================================
# VALIDAÇÕES
# ============================================================

# Lançamentos sem correspondência
sem_correspondencia = df[
    df["_merge"] != "both"
]

# Diferença entre valores
df["diferenca_valor"] = (
    df["valor_movimento"] - df["valor"]
).round(2)

divergencias_valor = df[
    df["diferenca_valor"] != 0
]

# Diferença de datas
df["diferenca_dias"] = (
    df["data_movimento"] - df["data_lancamento"]
).dt.days

# ============================================================
# RESULTADOS
# ============================================================

print("\nVALIDAÇÃO — CAIXA x LANÇAMENTOS")
print("=" * 60)

print("Movimentos de caixa:", len(caixa))
print("Lançamentos financeiros:", len(lancamentos))

print(
    "\nMovimentos sem lançamento correspondente:",
    len(sem_correspondencia)
)

print(
    "Divergências de valor:",
    len(divergencias_valor)
)

print("\nDISTRIBUIÇÃO DA DIFERENÇA DE DATAS")
print(
    df["diferenca_dias"]
    .describe()
    .to_string()
)

print(
    "\nMovimentos anteriores ao lançamento:",
    (df["diferenca_dias"] < 0).sum()
)

print(
    "Movimentos no mesmo dia:",
    (df["diferenca_dias"] == 0).sum()
)

print(
    "Movimentos posteriores ao lançamento:",
    (df["diferenca_dias"] > 0).sum()
)

# ============================================================
# DETALHAMENTO DAS DIVERGÊNCIAS
# ============================================================

if len(divergencias_valor) > 0:

    print("\nDIVERGÊNCIAS DE VALOR — PRIMEIROS 20")

    print(
        divergencias_valor[
            [
                "id_movimento_caixa",
                "id_lancamento",
                "valor_movimento",
                "valor",
                "diferenca_valor"
            ]
        ].head(20).to_string(index=False)
    )

# ============================================================
# CONCLUSÃO
# ============================================================

if (
    len(sem_correspondencia) == 0
    and len(divergencias_valor) == 0
):

    print(
        "\nResultado: OK — correspondência e valores consistentes."
    )

else:

    print(
        "\nResultado: investigar divergências."
    )