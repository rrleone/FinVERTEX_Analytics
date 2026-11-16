
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "dim_plano_contas.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

print("\nVALIDAÇÃO — PLANO DE CONTAS")
print("=" * 60)

# 1. Chave primária
print("\n1. VALIDAR ID_CONTA")

print("IDs nulos:", df["id_conta"].isna().sum())
print("IDs duplicados:", df["id_conta"].duplicated().sum())

# 2. Nome da conta
print("\n2. VALIDAR NOME_CONTA")

print("Nomes nulos:", df["nome_conta"].isna().sum())
print("Nomes duplicados:", df["nome_conta"].duplicated().sum())

# 3. Tipos de conta permitidos
print("\n3. VALIDAR TIPO_CONTA")

tipos_validos = {
    "Receita",
    "Despesa",
    "Investimento"
}

tipos_encontrados = set(df["tipo_conta"].dropna().unique())

tipos_invalidos = tipos_encontrados - tipos_validos

print("Tipos encontrados:", sorted(tipos_encontrados))
print("Tipos inválidos:", tipos_invalidos)

# 4. Naturezas permitidas
print("\n4. VALIDAR NATUREZA")

naturezas_validas = {
    "Credora",
    "Devedora"
}

naturezas_encontradas = set(df["natureza"].dropna().unique())

naturezas_invalidas = naturezas_encontradas - naturezas_validas

print("Naturezas encontradas:", sorted(naturezas_encontradas))
print("Naturezas inválidas:", naturezas_invalidas)

# 5. Coerência entre tipo e natureza
print("\n5. VALIDAR COERÊNCIA TIPO_CONTA × NATUREZA")

regras = {
    "Receita": "Credora",
    "Despesa": "Devedora",
    "Investimento": "Devedora"
}

df["natureza_esperada"] = df["tipo_conta"].map(regras)

inconsistencias = df[
    df["natureza"] != df["natureza_esperada"]
]

print("Inconsistências encontradas:", len(inconsistencias))

if not inconsistencias.empty:
    print("\nContas inconsistentes:")
    print(
        inconsistencias[
            [
                "id_conta",
                "nome_conta",
                "tipo_conta",
                "natureza",
                "natureza_esperada"
            ]
        ].to_string(index=False)
    )

# 6. Resultado final
print("\n6. RESUMO")

total_validacoes = 5

validacoes_ok = (
    df["id_conta"].isna().sum() == 0
    and df["id_conta"].duplicated().sum() == 0
    and df["nome_conta"].isna().sum() == 0
    and df["nome_conta"].duplicated().sum() == 0
    and len(tipos_invalidos) == 0
    and len(naturezas_invalidas) == 0
    and len(inconsistencias) == 0
)

if validacoes_ok:
    print("RESULTADO: Todas as validações foram aprovadas.")
else:
    print("RESULTADO: Foram identificadas inconsistências.")

print("\nVALIDAÇÃO CONCLUÍDA")
