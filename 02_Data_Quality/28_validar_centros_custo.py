
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "dim_centro_custo.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\nVALIDAÇÃO — CENTROS DE CUSTO")
print("=" * 60)

# 1. Validar chave primária
print("\n1. VALIDAR ID_CENTRO_CUSTO")

print("IDs nulos:", df["id_centro_custo"].isna().sum())
print("IDs duplicados:", df["id_centro_custo"].duplicated().sum())

# 2. Validar código
print("\n2. VALIDAR CODIGO_CENTRO")

print("Códigos nulos:", df["codigo_centro"].isna().sum())
print("Códigos duplicados:", df["codigo_centro"].duplicated().sum())

# 3. Validar nome
print("\n3. VALIDAR NOME_CENTRO_CUSTO")

print("Nomes nulos:", df["nome_centro_custo"].isna().sum())
print("Nomes duplicados:", df["nome_centro_custo"].duplicated().sum())

# 4. Validar grupo de custo
print("\n4. VALIDAR GRUPO_CUSTO")

print("Grupos nulos:", df["grupo_custo"].isna().sum())

print("Grupos encontrados:")
print(
    df["grupo_custo"]
    .value_counts()
    .to_string()
)

# 5. Verificar campos vazios ou somente espaços
print("\n5. VALIDAR CAMPOS VAZIOS")

colunas_texto = [
    "codigo_centro",
    "nome_centro_custo",
    "grupo_custo"
]

for coluna in colunas_texto:
    vazios = (
        df[coluna]
        .astype("string")
        .str.strip()
        .eq("")
        .sum()
    )

    print(f"{coluna}: {vazios} vazios")

# 6. Resultado consolidado
print("\n6. RESUMO")

validacoes_ok = (
    df["id_centro_custo"].isna().sum() == 0
    and df["id_centro_custo"].duplicated().sum() == 0
    and df["codigo_centro"].isna().sum() == 0
    and df["codigo_centro"].duplicated().sum() == 0
    and df["nome_centro_custo"].isna().sum() == 0
    and df["nome_centro_custo"].duplicated().sum() == 0
    and df["grupo_custo"].isna().sum() == 0
    and all(
        df[coluna].astype("string").str.strip().ne("").all()
        for coluna in colunas_texto
    )
)

if validacoes_ok:
    print("RESULTADO: Todas as validações foram aprovadas.")
else:
    print("RESULTADO: Foram identificadas inconsistências.")

print("\nVALIDAÇÃO CONCLUÍDA")
