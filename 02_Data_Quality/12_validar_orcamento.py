import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_orcamento.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

# ============================================================
# VALIDAÇÕES
# ============================================================

# Chave primária
pk_nulos = df["id_orcamento"].isna().sum()

pk_duplicados = df["id_orcamento"].duplicated().sum()

# Valores financeiros
valores_nulos = df["valor_orcado"].isna().sum()

valores_negativos = (df["valor_orcado"] < 0).sum()

valores_zero = (df["valor_orcado"] == 0).sum()

# Combinação de negócio
chaves_negocio = [
    "competencia",
    "id_conta",
    "id_centro_custo"
]

duplicidades_negocio = df.duplicated(
    subset=chaves_negocio,
    keep=False
)

# Status
status_nulos = df["status_orcamento"].isna().sum()

status_distintos = df["status_orcamento"].unique()

# ============================================================
# RESULTADOS
# ============================================================

print("\nVALIDAÇÃO — ORÇAMENTO FINANCEIRO")
print("=" * 60)

print("\nCHAVE PRIMÁRIA")
print("IDs nulos:", pk_nulos)
print("IDs duplicados:", pk_duplicados)

print("\nVALORES FINANCEIROS")
print("Valores orçados nulos:", valores_nulos)
print("Valores negativos:", valores_negativos)
print("Valores iguais a zero:", valores_zero)

print("\nCHAVE DE NEGÓCIO")
print(
    "Registros envolvidos em duplicidades:",
    duplicidades_negocio.sum()
)

print("\nSTATUS")
print("Status ausentes:", status_nulos)
print("Status encontrados:", list(status_distintos))

# ============================================================
# DETALHAMENTO DE DUPLICIDADES
# ============================================================

if duplicidades_negocio.any():

    print("\nREGISTROS COM DUPLICIDADE DE NEGÓCIO")

    print(
        df.loc[
            duplicidades_negocio,
            chaves_negocio + ["id_orcamento", "valor_orcado"]
        ]
        .sort_values(chaves_negocio)
        .head(20)
        .to_string(index=False)
    )

# ============================================================
# CONCLUSÃO
# ============================================================

if (
    pk_nulos == 0
    and pk_duplicados == 0
    and valores_nulos == 0
    and valores_negativos == 0
    and duplicidades_negocio.sum() == 0
):

    print("\nResultado: OK — validações principais aprovadas.")

else:

    print("\nResultado: investigar ocorrências identificadas.")