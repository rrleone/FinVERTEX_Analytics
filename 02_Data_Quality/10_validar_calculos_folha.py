import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_folha_pagamento.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

# ============================================================
# CÁLCULO DOS VALORES ESPERADOS
# ============================================================

df["salario_liquido_calculado"] = (
    df["salario_base"]
    + df["valor_horas_extras"]
    + df["beneficios"]
    - df["descontos"]
).round(2)

df["custo_empresa_calculado"] = (
    df["salario_base"]
    + df["valor_horas_extras"]
    + df["beneficios"]
    + df["encargos"]
).round(2)

# ============================================================
# COMPARAÇÃO COM OS VALORES DA BASE
# ============================================================

df["dif_salario_liquido"] = (
    df["salario_liquido_estimado"]
    - df["salario_liquido_calculado"]
).round(2)

df["dif_custo_empresa"] = (
    df["custo_total_empresa"]
    - df["custo_empresa_calculado"]
).round(2)

inconsistencias_liquido = df[
    df["dif_salario_liquido"] != 0
]

inconsistencias_custo = df[
    df["dif_custo_empresa"] != 0
]

# ============================================================
# RESULTADOS
# ============================================================

print("\nVALIDAÇÃO FINANCEIRA — FOLHA DE PAGAMENTO")
print("=" * 60)

print("Total de registros:", len(df))

print(
    "\nInconsistências no salário líquido:",
    len(inconsistencias_liquido)
)

print(
    "Inconsistências no custo total da empresa:",
    len(inconsistencias_custo)
)

# ============================================================
# DETALHAMENTO
# ============================================================

if len(inconsistencias_liquido) > 0:

    print("\nREGISTROS COM SALÁRIO LÍQUIDO INCONSISTENTE")

    print(
        inconsistencias_liquido[
            [
                "id_folha",
                "salario_liquido_estimado",
                "salario_liquido_calculado",
                "dif_salario_liquido"
            ]
        ].head(20).to_string(index=False)
    )

if len(inconsistencias_custo) > 0:

    print("\nREGISTROS COM CUSTO EMPRESA INCONSISTENTE")

    print(
        inconsistencias_custo[
            [
                "id_folha",
                "custo_total_empresa",
                "custo_empresa_calculado",
                "dif_custo_empresa"
            ]
        ].head(20).to_string(index=False)
    )

# ============================================================
# CONCLUSÃO
# ============================================================

if (
    len(inconsistencias_liquido) == 0
    and len(inconsistencias_custo) == 0
):

    print(
        "\nResultado: OK — cálculos financeiros consistentes."
    )

else:

    print(
        "\nResultado: foram encontradas divergências."
    )