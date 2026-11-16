
import pandas as pd
from pathlib import Path

# ============================================================
# FINVERTEX ANALYTICS
# ETL 01 - Preparação da dimensão calendário
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "01_Fonte_Dados"
ETL_DIR = BASE_DIR / "03_ETL_Python"

arquivo_entrada = DATA_DIR / "dim_calendario.csv"
arquivo_saida = ETL_DIR / "dim_calendario_modelada.csv"

# Leitura do calendário original
df_original = pd.read_csv(
    arquivo_entrada,
    sep=";",
    encoding="utf-8-sig"
)

# Criar calendário completo até janeiro de 2027
datas = pd.date_range(
    start="2024-01-01",
    end="2027-01-31",
    freq="D"
)

df = pd.DataFrame({"data": datas})

# Tradução dos meses
meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

# Tradução dos dias da semana
dias_semana = {
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "Sexta-feira",
    6: "Sábado",
    7: "Domingo"
}

# Atributos temporais
df["ano"] = df["data"].dt.year
df["trimestre"] = df["data"].dt.quarter
df["mes_numero"] = df["data"].dt.month
df["mes_nome"] = df["mes_numero"].map(meses)

df["ano_mes"] = df["data"].dt.strftime("%Y-%m")
df["dia"] = df["data"].dt.day

# Segunda-feira = 1; domingo = 7
df["dia_semana_numero"] = df["data"].dt.dayofweek + 1
df["dia_semana_nome"] = df["dia_semana_numero"].map(dias_semana)

df["fim_de_semana"] = (
    df["dia_semana_numero"].isin([6, 7]).astype(int)
)

# Formato de data para exportação
df["data"] = df["data"].dt.strftime("%Y-%m-%d")

# Exportar dimensão preparada
df.to_csv(
    arquivo_saida,
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("\nETL 01 — DIMENSÃO CALENDÁRIO")
print("=" * 60)

print("Arquivo original:", arquivo_entrada)
print("Arquivo gerado:", arquivo_saida)
print("Registros originais:", len(df_original))
print("Registros modelados:", len(df))
print("Data inicial:", df["data"].min())
print("Data final:", df["data"].max())

print("\nMeses:")
print(df["mes_nome"].unique())

print("\nÚltimos registros:")
print(df.tail(5).to_string(index=False))

print("\nETL CONCLUÍDO")
