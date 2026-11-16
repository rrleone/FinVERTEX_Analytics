from pathlib import Path
import pandas as pd

PROJECT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_PATH / "01_Fonte_Dados"

arquivo = DATA_PATH / "fato_fluxo_caixa.csv"

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

df["data_movimento"] = pd.to_datetime(
    df["data_movimento"],
    errors="coerce"
)

movimentos_fora_periodo = df[
    df["data_movimento"] > "2026-12-31"
]

print("\nMOVIMENTAÇÕES FORA DO PERÍODO")
print("=" * 60)

print(movimentos_fora_periodo.to_string(index=False))

print("\nQuantidade de registros:")
print(len(movimentos_fora_periodo))