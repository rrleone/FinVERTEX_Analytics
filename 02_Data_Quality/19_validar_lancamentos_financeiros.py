import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_lancamentos_financeiros.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\nVALIDAÇÃO — LANÇAMENTOS FINANCEIROS")
print("=" * 60)

# 1. Valores financeiros
print("\n1. VALIDAÇÃO DOS VALORES")

print("Valores nulos:", df["valor"].isna().sum())
print("Valores iguais a zero:", (df["valor"] == 0).sum())
print("Valores negativos:", (df["valor"] < 0).sum())

# 2. Tipos de lançamento
tipos_validos = ["Receita", "Despesa", "Investimento"]

tipos_invalidos = df[
    ~df["tipo_lancamento"].isin(tipos_validos)
]

print("\n2. TIPOS DE LANÇAMENTO")
print("Tipos encontrados:", sorted(df["tipo_lancamento"].unique()))
print("Tipos inválidos:", len(tipos_invalidos))

# 3. Status
status_validos = ["Realizado", "Pendente"]

status_invalidos = df[
    ~df["status_lancamento"].isin(status_validos)
]

print("\n3. STATUS DOS LANÇAMENTOS")
print("Status encontrados:", sorted(df["status_lancamento"].unique()))
print("Status inválidos:", len(status_invalidos))

# 4. Chave primária
print("\n4. CHAVE PRIMÁRIA")
print("IDs nulos:", df["id_lancamento"].isna().sum())
print("IDs duplicados:", df["id_lancamento"].duplicated().sum())

# 5. Chave de negócio
print("\n5. DUPLICIDADES DE NEGÓCIO")

colunas_chave = [
    "data_lancamento",
    "tipo_lancamento",
    "id_conta",
    "id_centro_custo",
    "valor",
    "descricao"
]

duplicados_negocio = df.duplicated(
    subset=colunas_chave,
    keep=False
)

print("Registros em possíveis duplicidades:", duplicados_negocio.sum())

# 6. Resumo
print("\n6. RESUMO")
print("Total de lançamentos:", len(df))
print("Total realizado:", (df["status_lancamento"] == "Realizado").sum())
print("Total pendente:", (df["status_lancamento"] == "Pendente").sum())

print("\nVALIDAÇÃO CONCLUÍDA")