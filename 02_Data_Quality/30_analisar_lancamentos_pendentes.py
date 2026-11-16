
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

# --------------------------------------------------
# 2. FILTRAR LANÇAMENTOS PENDENTES
# --------------------------------------------------

pendentes = lancamentos[
    lancamentos["status_lancamento"] == "Pendente"
].copy()

print("\nANÁLISE — LANÇAMENTOS PENDENTES")
print("=" * 70)

print("\n1. INDICADORES GERAIS")

print("Total de lançamentos:", len(lancamentos))
print("Lançamentos pendentes:", len(pendentes))
print(
    "Percentual pendente:",
    round(len(pendentes) / len(lancamentos) * 100, 2),
    "%"
)

print(
    "Valor total pendente: R$",
    round(pendentes["valor"].sum(), 2)
)

# --------------------------------------------------
# 3. ENRIQUECER COM PLANO DE CONTAS
# --------------------------------------------------

pendentes = pendentes.merge(
    plano_contas[
        ["id_conta", "nome_conta", "tipo_conta", "grupo_dre"]
    ],
    on="id_conta",
    how="left"
)

# --------------------------------------------------
# 4. ENRIQUECER COM CENTRO DE CUSTO
# --------------------------------------------------

pendentes = pendentes.merge(
    centros_custo[
        [
            "id_centro_custo",
            "codigo_centro",
            "nome_centro_custo",
            "grupo_custo"
        ]
    ],
    on="id_centro_custo",
    how="left"
)

# --------------------------------------------------
# 5. PENDENTES POR TIPO DE LANÇAMENTO
# --------------------------------------------------

print("\n2. PENDENTES POR TIPO DE LANÇAMENTO")

print(
    pendentes.groupby("tipo_lancamento")
    .agg(
        quantidade=("id_lancamento", "count"),
        valor_total=("valor", "sum"),
        valor_medio=("valor", "mean")
    )
    .sort_values("valor_total", ascending=False)
    .round(2)
    .to_string()
)

# --------------------------------------------------
# 6. PENDENTES POR CONTA CONTÁBIL
# --------------------------------------------------

print("\n3. PENDENTES POR CONTA CONTÁBIL")

print(
    pendentes.groupby(
        ["id_conta", "nome_conta", "tipo_conta", "grupo_dre"]
    )
    .agg(
        quantidade=("id_lancamento", "count"),
        valor_total=("valor", "sum"),
        valor_medio=("valor", "mean")
    )
    .sort_values("valor_total", ascending=False)
    .round(2)
    .to_string()
)

# --------------------------------------------------
# 7. PENDENTES POR CENTRO DE CUSTO
# --------------------------------------------------

print("\n4. PENDENTES POR CENTRO DE CUSTO")

print(
    pendentes.groupby(
        ["codigo_centro", "nome_centro_custo", "grupo_custo"]
    )
    .agg(
        quantidade=("id_lancamento", "count"),
        valor_total=("valor", "sum"),
        valor_medio=("valor", "mean")
    )
    .sort_values("valor_total", ascending=False)
    .round(2)
    .to_string()
)

# --------------------------------------------------
# 8. PENDENTES POR GRUPO DRE
# --------------------------------------------------

print("\n5. PENDENTES POR GRUPO DRE")

print(
    pendentes.groupby("grupo_dre")
    .agg(
        quantidade=("id_lancamento", "count"),
        valor_total=("valor", "sum")
    )
    .sort_values("valor_total", ascending=False)
    .round(2)
    .to_string()
)

# --------------------------------------------------
# 9. RESUMO
# --------------------------------------------------

print("\n6. RESUMO FINAL")

print("Quantidade pendente:", len(pendentes))
print("Valor total pendente:", round(pendentes["valor"].sum(), 2))

print("\nANÁLISE CONCLUÍDA")
