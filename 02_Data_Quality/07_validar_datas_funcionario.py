
from pathlib import Path
import pandas as pd

PROJECT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_PATH / "01_Fonte_Dados"

df = pd.read_csv(
    DATA_PATH / "dim_funcionario.csv",
    sep=";",
    encoding="utf-8-sig"
)

df["data_admissao"] = pd.to_datetime(
    df["data_admissao"],
    errors="coerce"
)

df["data_demissao"] = pd.to_datetime(
    df["data_demissao"],
    errors="coerce"
)

# Funcionários cuja demissão ocorreu antes da admissão
inconsistencias = df[
    df["data_demissao"].notna()
    & (df["data_demissao"] < df["data_admissao"])
]

print("\nVALIDAÇÃO DE DATAS — FUNCIONÁRIOS")
print("=" * 60)

print("Total de funcionários:", len(df))
print("Datas de admissão inválidas:", df["data_admissao"].isna().sum())
nulos_demissao = df["data_demissao"].isna().sum()
print("Datas de demissão ausentes:", nulos_demissao)
print("Demissões anteriores à admissão:", len(inconsistencias))

if len(inconsistencias) > 0:
    print("\nRegistros inconsistentes:")
    print(
        inconsistencias[
            ["id_funcionario", "nome_completo",
             "data_admissao", "data_demissao"]
        ].to_string(index=False)
    )
else:
    print("\nResultado: OK")

print(
    "Funcionários com status ativo:",
    (df["status_funcionario"] == "Ativo").sum()
)
