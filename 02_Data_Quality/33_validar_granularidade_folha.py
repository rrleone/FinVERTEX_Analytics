import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "01_Fonte_Dados"

arquivo_folha = DATA_DIR / "fato_folha_pagamento.csv"
arquivo_funcionario = DATA_DIR / "dim_funcionario.csv"

folha = pd.read_csv(
    arquivo_folha,
    sep=";",
    encoding="utf-8-sig"
)

funcionarios = pd.read_csv(
    arquivo_funcionario,
    sep=";",
    encoding="utf-8-sig"
)

print("\nVALIDAÇÃO DA GRANULARIDADE DA FOLHA")
print("=" * 70)

# 1. Verificar duplicidade funcionário + competência
duplicados = folha[
    folha.duplicated(
        subset=["id_funcionario", "competencia"],
        keep=False
    )
].sort_values(["id_funcionario", "competencia"])

print("\n1. DUPLICIDADES FUNCIONÁRIO + COMPETÊNCIA")
print("Total de combinações duplicadas:", len(duplicados))

if not duplicados.empty:
    print(duplicados.to_string(index=False))
else:
    print("Nenhuma duplicidade encontrada.")

# 2. Funcionários presentes na folha
ids_folha = set(folha["id_funcionario"].unique())
ids_dimensao = set(funcionarios["id_funcionario"].unique())

print("\n2. FUNCIONÁRIOS")
print("Funcionários na dimensão:", len(ids_dimensao))
print("Funcionários na folha:", len(ids_folha))
print("Funcionários da dimensão sem folha:", len(ids_dimensao - ids_folha))
print("IDs sem registros na folha:", sorted(ids_dimensao - ids_folha))

# 3. Funcionários da folha que não existem na dimensão
ids_sem_dimensao = ids_folha - ids_dimensao

print("\nFuncionários na folha sem correspondência na dimensão:",
      len(ids_sem_dimensao))

if ids_sem_dimensao:
    print("IDs:", sorted(ids_sem_dimensao))

# 4. Quantidade de registros por competência
print("\n3. REGISTROS POR COMPETÊNCIA")
print(
    folha.groupby("competencia")
    .size()
    .sort_index()
    .to_string()
)

# 5. Quantidade de competências por funcionário
competencias_funcionario = (
    folha.groupby("id_funcionario")["competencia"]
    .nunique()
)

print("\n4. COMPETÊNCIAS POR FUNCIONÁRIO")
print(competencias_funcionario.describe())

print("\n5. MENOR E MAIOR COMPETÊNCIA")
print("Menor:", folha["competencia"].min())
print("Maior:", folha["competencia"].max())

print("\nVALIDAÇÃO CONCLUÍDA")