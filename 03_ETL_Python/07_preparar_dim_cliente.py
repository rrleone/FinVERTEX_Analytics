from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
FONTE = BASE_DIR / "01_Fonte_Dados" / "dim_cliente.csv"
SAIDA = BASE_DIR / "03_ETL_Python" / "dim_cliente_modelada.csv"

def ler_csv(caminho):
    try:
        df = pd.read_csv(caminho, sep=";", encoding="utf-8-sig")
        if df.shape[1] == 1:
            df = pd.read_csv(caminho, sep=",", encoding="utf-8-sig")
        return df
    except UnicodeDecodeError:
        df = pd.read_csv(caminho, sep=";", encoding="latin-1")
        if df.shape[1] == 1:
            df = pd.read_csv(caminho, sep=",", encoding="latin-1")
        return df

def main():
    if not FONTE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {FONTE}")
    df = ler_csv(FONTE)
    df.to_csv(SAIDA, index=False, sep=";", encoding="utf-8-sig")
    print("=" * 60)
    print("ETL 07 — DIM_CLIENTE")
    print(f"Registros originais: {len(df)}")
    print(f"Registros exportados: {len(df)}")
    print(f"Colunas: {len(df.columns)}")
    print(f"Arquivo gerado: {SAIDA}")

if __name__ == "__main__":
    main()
