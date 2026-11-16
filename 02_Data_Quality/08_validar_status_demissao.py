import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = BASE_DIR / "01_Fonte_Dados" / "dim_funcionario.csv"

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

# ============================================================
# PREPARAÇÃO DOS DADOS
# ============================================================

df["data_demissao"] = pd.to_datetime(
    df["data_demissao"],
    errors="coerce"
)

df["status_funcionario"] = (
    df["status_funcionario"]
    .astype(str)
    .str.strip()
    .str.lower()
)

# ============================================================
# REGRAS DE NEGÓCIO
# ============================================================

ativos_com_demissao = df[
    (df["status_funcionario"] == "ativo") &
    (df["data_demissao"].notna())
]

desligados_sem_demissao = df[
    (df["status_funcionario"] == "desligado") &
    (df["data_demissao"].isna())
]

# ============================================================
# RESULTADOS
# ============================================================

print("\nVALIDAÇÃO — STATUS x DATA DE DEMISSÃO")
print("=" * 60)

print("Total de funcionários:", len(df))

print(
    "Funcionários ativos:",
    (df["status_funcionario"] == "ativo").sum()
)

print(
    "Funcionários desligados:",
    (df["status_funcionario"] == "desligado").sum()
)

print(
    "\nAtivos com data de demissão preenchida:",
    len(ativos_com_demissao)
)

print(
    "Desligados sem data de demissão:",
    len(desligados_sem_demissao)
)

# ============================================================
# DIAGNÓSTICO
# ============================================================

if (
    len(ativos_com_demissao) == 0
    and len(desligados_sem_demissao) == 0
):
    print(
        "\nResultado: OK — regras de negócio consistentes."
    )

else:
    print(
        "\nResultado: verificar inconsistências."
    )

    if len(ativos_com_demissao) > 0:
        print("\nAtivos com data de demissão:")

        print(
            ativos_com_demissao[
                [
                    "id_funcionario",
                    "nome_completo",
                    "status_funcionario",
                    "data_demissao"
                ]
            ].to_string(index=False)
        )

    if len(desligados_sem_demissao) > 0:
        print("\nDesligados sem data de demissão:")

        print(
            desligados_sem_demissao[
                [
                    "id_funcionario",
                    "nome_completo",
                    "status_funcionario",
                    "data_demissao"
                ]
            ].to_string(index=False)
        )

# ============================================================
# DISTRIBUIÇÃO DOS STATUS
# ============================================================

print("\nDISTRIBUIÇÃO DOS STATUS")
print("=" * 40)

print(
    df["status_funcionario"]
    .value_counts(dropna=False)
    .to_string()
)