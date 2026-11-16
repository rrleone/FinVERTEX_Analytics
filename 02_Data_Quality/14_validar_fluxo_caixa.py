import pandas as pd
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo = (
    BASE_DIR
    / "01_Fonte_Dados"
    / "fato_fluxo_caixa.csv"
)

df = pd.read_csv(
    arquivo,
    sep=";",
    encoding="utf-8-sig"
)

# Converter datas
df["data_movimento"] = pd.to_datetime(
    df["data_movimento"],
    errors="coerce"
)

# ============================================================
# VALIDAÇÕES
# ============================================================

# Chave primária
pk_nulos = df["id_movimento_caixa"].isna().sum()

pk_duplicados = df["id_movimento_caixa"].duplicated().sum()

# ID do lançamento
lancamentos_nulos = df["id_lancamento"].isna().sum()

lancamentos_duplicados = df["id_lancamento"].duplicated().sum()

# Valores financeiros
valores_nulos = df["valor_movimento"].isna().sum()

valores_zero = (df["valor_movimento"] == 0).sum()

valores_negativos = (df["valor_movimento"] < 0).sum()

# Datas
datas_invalidas = df["data_movimento"].isna().sum()

movimentos_fora_periodo = (
    df["data_movimento"] > "2026-12-31"
).sum()

# Categorias
tipos_encontrados = df["tipo_movimento"].unique()

status_encontrados = df["status_conciliacao"].unique()

# ============================================================
# RESULTADOS
# ============================================================

print("\nVALIDAÇÃO — FLUXO DE CAIXA")
print("=" * 60)

print("\nCHAVE PRIMÁRIA")
print("IDs nulos:", pk_nulos)
print("IDs duplicados:", pk_duplicados)

print("\nID DO LANÇAMENTO")
print("Lançamentos nulos:", lancamentos_nulos)
print("Lançamentos duplicados:", lancamentos_duplicados)

print("\nVALORES FINANCEIROS")
print("Valores nulos:", valores_nulos)
print("Valores iguais a zero:", valores_zero)
print("Valores negativos:", valores_negativos)

print("\nDATAS")
print("Datas inválidas:", datas_invalidas)
print("Movimentos após 31/12/2026:", movimentos_fora_periodo)

print("\nTIPOS DE MOVIMENTO")
print(list(tipos_encontrados))

print("\nSTATUS DE CONCILIAÇÃO")
print(list(status_encontrados))

# ============================================================
# DISTRIBUIÇÕES
# ============================================================

print("\nDISTRIBUIÇÃO DOS MOVIMENTOS")
print(df["tipo_movimento"].value_counts().to_string())

print("\nDISTRIBUIÇÃO DA CONCILIAÇÃO")
print(df["status_conciliacao"].value_counts().to_string())

# ============================================================
# CONCLUSÃO
# ============================================================

if (
    pk_nulos == 0
    and pk_duplicados == 0
    and lancamentos_nulos == 0
    and valores_nulos == 0
    and valores_zero == 0
    and valores_negativos == 0
    and datas_invalidas == 0
):

    print("\nResultado: OK — validações principais aprovadas.")

else:

    print("\nResultado: investigar ocorrências identificadas.")