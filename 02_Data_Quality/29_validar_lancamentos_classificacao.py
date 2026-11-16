
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "01_Fonte_Dados"

# --------------------------------------------------
# 1. CARREGAR TABELAS
# --------------------------------------------------

lancamentos = pd.read_csv(
    DATA_DIR / "fato_lancamentos_financeiros.csv",
    sep=";",
    encoding="utf-8-sig"
)

plano_contas = pd.read_csv(
    DATA_DIR / "dim_plano_contas.csv",
    sep=";",
    encoding="utf-8-sig"
)

centros_custo = pd.read_csv(
    DATA_DIR / "dim_centro_custo.csv",
    sep=";",
    encoding="utf-8-sig"
)

print("\nVALIDAÇÃO — CLASSIFICAÇÃO DOS LANÇAMENTOS")
print("=" * 70)

# --------------------------------------------------
# 2. ASSOCIAR PLANO DE CONTAS
# --------------------------------------------------

df = lancamentos.merge(
    plano_contas[
        ["id_conta", "nome_conta", "tipo_conta", "grupo_dre", "natureza"]
    ],
    on="id_conta",
    how="left",
    indicator="merge_conta"
)

print("\n1. INTEGRIDADE DO PLANO DE CONTAS")

print(
    "Lançamentos sem correspondência:",
    (df["merge_conta"] == "left_only").sum()
)

# --------------------------------------------------
# 3. ASSOCIAR CENTROS DE CUSTO
# --------------------------------------------------

df = df.merge(
    centros_custo[
        [
            "id_centro_custo",
            "codigo_centro",
            "nome_centro_custo",
            "grupo_custo"
        ]
    ],
    on="id_centro_custo",
    how="left",
    indicator="merge_centro"
)

print("\n2. INTEGRIDADE DOS CENTROS DE CUSTO")

print(
    "Lançamentos sem correspondência:",
    (df["merge_centro"] == "left_only").sum()
)

# --------------------------------------------------
# 4. COMPARAR TIPO DO LANÇAMENTO × TIPO DA CONTA
# --------------------------------------------------

print("\n3. TIPO DO LANÇAMENTO × TIPO DA CONTA")

regras_tipo = {
    "Receita": "Receita",
    "Despesa": "Despesa",
    "Investimento": "Investimento"
}

df["tipo_conta_esperado"] = (
    df["tipo_lancamento"].map(regras_tipo)
)

df["classificacao_coerente"] = (
    df["tipo_conta"] == df["tipo_conta_esperado"]
)

inconsistencias_tipo = df[
    ~df["classificacao_coerente"]
]

print("Total de lançamentos:", len(df))
print(
    "Classificações coerentes:",
    df["classificacao_coerente"].sum()
)
print(
    "Classificações incoerentes:",
    len(inconsistencias_tipo)
)

if not inconsistencias_tipo.empty:
    print("\nDetalhamento das inconsistências:")

    print(
        inconsistencias_tipo[
            [
                "id_lancamento",
                "tipo_lancamento",
                "id_conta",
                "nome_conta",
                "tipo_conta",
                "tipo_conta_esperado"
            ]
        ].to_string(index=False)
    )

# --------------------------------------------------
# 5. DISTRIBUIÇÃO POR TIPO E CONTA
# --------------------------------------------------

print("\n4. DISTRIBUIÇÃO TIPO_LANCAMENTO × TIPO_CONTA")

print(
    pd.crosstab(
        df["tipo_lancamento"],
        df["tipo_conta"],
        margins=True
    ).to_string()
)

# --------------------------------------------------
# 6. DISTRIBUIÇÃO POR CENTRO DE CUSTO
# --------------------------------------------------

print("\n5. LANÇAMENTOS POR CENTRO DE CUSTO")

print(
    df.groupby(
        ["codigo_centro", "nome_centro_custo", "grupo_custo"],
        dropna=False
    )
    .agg(
        quantidade_lancamentos=("id_lancamento", "count"),
        valor_total=("valor", "sum")
    )
    .sort_values("valor_total", ascending=False)
    .to_string()
)

# --------------------------------------------------
# 7. RESUMO
# --------------------------------------------------

print("\n6. RESUMO FINAL")

print("Lançamentos analisados:", len(df))
print("Inconsistências tipo × conta:", len(inconsistencias_tipo))

print("\nANÁLISE CONCLUÍDA")
