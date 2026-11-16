import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo_caixa = (
    BASE_DIR / "01_Fonte_Dados" / "fato_fluxo_caixa.csv"
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
# CRUZAMENTO
# ============================================================

df = caixa.merge(
    lancamentos[
        ["id_lancamento", "tipo_lancamento"]
    ],
    on="id_lancamento",
    how="left"
)

# ============================================================
# REGRAS DE NEGÓCIO
# ============================================================

# Entrada deve corresponder a Receita
entradas_inconsistentes = df[
    (df["tipo_movimento"] == "Entrada") &
    (df["tipo_lancamento"] != "Receita")
]

# Saída deve corresponder a Despesa ou Investimento
saidas_inconsistentes = df[
    (df["tipo_movimento"] == "Saída") &
    (~df["tipo_lancamento"].isin(["Despesa", "Investimento"]))
]

# ============================================================
# RESULTADOS
# ============================================================

print("\nVALIDAÇÃO — TIPO DE MOVIMENTO")
print("=" * 60)

print("Total de movimentos:", len(df))

print(
    "\nEntradas inconsistentes:",
    len(entradas_inconsistentes)
)

print(
    "Saídas inconsistentes:",
    len(saidas_inconsistentes)
)

# ============================================================
# DETALHAMENTO
# ============================================================

if len(entradas_inconsistentes) > 0:

    print("\nENTRADAS INCONSISTENTES")

    print(
        entradas_inconsistentes[
            [
                "id_movimento_caixa",
                "id_lancamento",
                "tipo_movimento",
                "tipo_lancamento"
            ]
        ].to_string(index=False)
    )

if len(saidas_inconsistentes) > 0:

    print("\nSAÍDAS INCONSISTENTES")

    print(
        saidas_inconsistentes[
            [
                "id_movimento_caixa",
                "id_lancamento",
                "tipo_movimento",
                "tipo_lancamento"
            ]
        ].to_string(index=False)
    )

# ============================================================
# CONCLUSÃO
# ============================================================

if (
    len(entradas_inconsistentes) == 0
    and len(saidas_inconsistentes) == 0
):

    print(
        "\nResultado: OK — tipos de movimento consistentes."
    )

else:

    print(
        "\nResultado: investigar inconsistências."
    )