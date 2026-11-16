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

# ============================================================
# LEITURA
# ============================================================

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

# ============================================================
# INSPEÇÃO
# ============================================================

print("\nINSPEÇÃO — FOLHA DE PAGAMENTO")
print("=" * 60)

print("\nDimensão da tabela:")
print("Linhas:", len(df))
print("Colunas:", len(df.columns))

print("\nColunas disponíveis:")
print(df.columns.tolist())

print("\nPrimeiros 10 registros:")
print(df.head(10).to_string(index=False))

print("\nResumo estatístico:")
print(
    df[
        [
            "salario_base",
            "horas_extras",
            "valor_horas_extras",
            "beneficios",
            "encargos",
            "descontos",
            "salario_liquido_estimado",
            "custo_total_empresa"
        ]
    ].describe().round(2).to_string()
)