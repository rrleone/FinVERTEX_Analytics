from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
ETL_DIR = BASE_DIR / "03_ETL_Python"

ARQUIVOS = [
    "dim_calendario_modelada.csv",
    "dim_funcionario_modelada.csv",
    "dim_cliente_modelada.csv",
    "dim_fornecedor_modelada.csv",
    "dim_plano_contas_modelada.csv",
    "dim_centro_custo_modelada.csv",
    "fato_lancamentos_financeiros_modelada.csv",
    "fato_orcamento_modelado.csv",
    "fato_fluxo_caixa_modelado.csv",
    "fato_folha_pagamento_modelada.csv",
]

def main():
    print("=" * 70)
    print("ETL 11 — VERIFICAÇÃO DOS ARQUIVOS MODELADOS")
    print("=" * 70)
    faltantes = []
    for nome in ARQUIVOS:
        caminho = ETL_DIR / nome
        if not caminho.exists():
            faltantes.append(nome)
            print(f"[FALTANDO] {nome}")
            continue
        try:
            df = pd.read_csv(caminho, sep=";", encoding="utf-8-sig")
            print(f"[OK] {nome:<48} {len(df):>7} linhas | {len(df.columns):>2} colunas")
        except Exception as e:
            print(f"[ERRO LEITURA] {nome}: {e}")
    print("-" * 70)
    if faltantes:
        print(f"Arquivos ainda não encontrados: {len(faltantes)}")
        print("Execute os ETLs correspondentes antes da carga/modelagem.")
    else:
        print("Todos os 10 arquivos modelados foram encontrados e lidos.")
        print("ETL PREPARATÓRIO CONCLUÍDO.")

if __name__ == "__main__":
    main()
