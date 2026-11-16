
from pathlib import Path
import pandas as pd

# ==================================================
# FINVERTEX ANALYTICS
# Etapa 03 - Data Profiling
# ==================================================

# Caminho principal do projeto
PROJECT_PATH = Path(__file__).resolve().parent.parent

# Pasta onde estão os arquivos CSV
DATA_PATH = PROJECT_PATH / "01_Fonte_Dados"

# Configuração dos arquivos
SEPARATOR = ";"
ENCODING = "utf-8-sig"


def analisar_csv(caminho_arquivo):
    """Analisa estrutura e qualidade inicial de um CSV."""

    df = pd.read_csv(
        caminho_arquivo,
        sep=SEPARATOR,
        encoding=ENCODING
    )

    print("\n" + "=" * 70)
    print(f"ARQUIVO: {caminho_arquivo.name}")
    print("=" * 70)

    print(f"Registros: {df.shape[0]:,}")
    print(f"Colunas: {df.shape[1]}")

    print("\nTipos de dados:")
    print(df.dtypes)

    print("\nValores nulos por coluna:")
    print(df.isnull().sum())

    print(f"\nLinhas duplicadas: {df.duplicated().sum():,}")

    print(f"\nMemória utilizada: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")


def main():
    arquivos_csv = list(DATA_PATH.glob("*.csv"))

    if not arquivos_csv:
        print("Nenhum CSV encontrado na pasta de fontes.")
        return

    print(f"FinVERTEX Analytics | Data Profiling")
    print(f"Arquivos encontrados: {len(arquivos_csv)}")

    for arquivo in sorted(arquivos_csv):
        analisar_csv(arquivo)


if __name__ == "__main__":
    main()
