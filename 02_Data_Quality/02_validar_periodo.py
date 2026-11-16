from pathlib import Path
import pandas as pd

PROJECT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_PATH / "01_Fonte_Dados"

colunas_data = {
    "dim_calendario.csv": ["data"],
    "dim_funcionario.csv": ["data_admissao", "data_demissao"],
    "fato_fluxo_caixa.csv": ["data_movimento"],
    "fato_folha_pagamento.csv": ["competencia"],
    "fato_lancamentos_financeiros.csv": ["data_lancamento"],
    "fato_orcamento.csv": ["competencia"],
}

for arquivo, colunas in colunas_data.items():

    caminho = DATA_PATH / arquivo

    df = pd.read_csv(
        caminho,
        sep=";",
        encoding="utf-8-sig"
    )

    print("\n" + "=" * 60)
    print(f"ARQUIVO: {arquivo}")

    for coluna in colunas:

        datas = pd.to_datetime(
            df[coluna],
            errors="coerce"
        ).dropna()

        if not datas.empty:
            print(
                f"{coluna}: "
                f"{datas.min().date()} até "
                f"{datas.max().date()}"
            )