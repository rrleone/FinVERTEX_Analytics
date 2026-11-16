import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "01_Fonte_Dados"

arquivo_funcionario = DATA_DIR / "dim_funcionario.csv"
arquivo_folha = DATA_DIR / "fato_folha_pagamento.csv"

funcionarios = pd.read_csv(
    arquivo_funcionario,
    sep=";",
    encoding="utf-8-sig"
)

folha = pd.read_csv(
    arquivo_folha,
    sep=";",
    encoding="utf-8-sig"
)

ids_com_folha = set(folha["id_funcionario"].unique())

sem_folha = funcionarios[
    ~funcionarios["id_funcionario"].isin(ids_com_folha)
].copy()

print("\nINVESTIGAÇÃO DE FUNCIONÁRIOS SEM FOLHA")
print("=" * 70)

print("\n1. FUNCIONÁRIOS SEM REGISTRO NA FOLHA")
print(sem_folha.to_string(index=False))

print("\n2. COLUNAS DA DIMENSÃO FUNCIONÁRIO")
print(funcionarios.columns.tolist())

print("\n3. RESUMO")
print("Total de funcionários sem folha:", len(sem_folha))

print("\nINVESTIGAÇÃO CONCLUÍDA")