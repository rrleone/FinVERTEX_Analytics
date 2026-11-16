from pathlib import Path
import pandas as pd

PROJECT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_PATH / "01_Fonte_Dados"

df_caixa = pd.read_csv(
    DATA_PATH / "fato_fluxo_caixa.csv",
    sep=";",
    encoding="utf-8-sig"
)

df_lancamentos = pd.read_csv(
    DATA_PATH / "fato_lancamentos_financeiros.csv",
    sep=";",
    encoding="utf-8-sig"
)

df_caixa["data_movimento"] = pd.to_datetime(
    df_caixa["data_movimento"],
    errors="coerce"
)

df_lancamentos["data_lancamento"] = pd.to_datetime(
    df_lancamentos["data_lancamento"],
    errors="coerce"
)

df_fora_periodo = df_caixa[
    df_caixa["data_movimento"] > "2026-12-31"
]

resultado = df_fora_periodo.merge(
    df_lancamentos[
        ["id_lancamento", "data_lancamento"]
    ],
    on="id_lancamento",
    how="left"
)

print("\nVALIDAÇÃO: FLUXO DE CAIXA X LANÇAMENTOS")
print("=" * 70)

print(
    resultado[
        [
            "id_movimento_caixa",
            "data_movimento",
            "id_lancamento",
            "data_lancamento"
        ]
    ].to_string(index=False)
)

print("\nQuantidade de registros:", len(resultado))
print(
    "Lançamentos sem correspondência:",
    resultado["data_lancamento"].isna().sum()
)