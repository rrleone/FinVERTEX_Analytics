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
    BASE_DIR / "01_Fonte_Dados"
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
# RESULTADOS
# ============================================================

print("\nINSPEÇÃO — TIPO DE MOVIMENTO x TIPO DE LANÇAMENTO")
print("=" * 65)

print("\nTipos de lançamento financeiro:")
print(
    lancamentos["tipo_lancamento"]
    .value_counts(dropna=False)
    .to_string()
)

print("\nCruzamento entre movimento de caixa e lançamento:")
print(
    pd.crosstab(
        df["tipo_movimento"],
        df["tipo_lancamento"],
        margins=True
    ).to_string()
)

print("\nExemplos dos registros:")
print(
    df[
        [
            "id_movimento_caixa",
            "id_lancamento",
            "tipo_movimento",
            "tipo_lancamento"
        ]
    ].head(20).to_string(index=False)
)