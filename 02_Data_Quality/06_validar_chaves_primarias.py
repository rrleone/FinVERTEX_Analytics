
from pathlib import Path
import pandas as pd

PROJECT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_PATH / "01_Fonte_Dados"


def carregar_tabela(nome):
    return pd.read_csv(
        DATA_PATH / f"{nome}.csv",
        sep=";",
        encoding="utf-8-sig"
    )


def validar_chave_primaria(df, coluna, nome_tabela):
    nulos = df[coluna].isna().sum()
    duplicados = df[coluna].duplicated().sum()

    print(f"\nTabela: {nome_tabela}")
    print("-" * 60)
    print(f"Total de registros: {len(df)}")
    print(f"Valores nulos na chave: {nulos}")
    print(f"Valores duplicados na chave: {duplicados}")

    if nulos == 0 and duplicados == 0:
        print("Resultado: OK")
    else:
        print("Resultado: FALHA")


tabelas = {
    "dim_funcionario": ("dim_funcionario", "id_funcionario"),
    "dim_cliente": ("dim_cliente", "id_cliente"),
    "dim_fornecedor": ("dim_fornecedor", "id_fornecedor"),
    "dim_centro_custo": ("dim_centro_custo", "id_centro_custo"),
    "dim_plano_contas": ("dim_plano_contas", "id_conta"),
    "fato_lancamentos_financeiros": ("fato_lancamentos_financeiros", "id_lancamento"),
    "fato_orcamento": ("fato_orcamento", "id_orcamento"),
    "fato_fluxo_caixa": ("fato_fluxo_caixa", "id_movimento_caixa"),
    "fato_folha_pagamento": ("fato_folha_pagamento", "id_folha"),
}

print("\nVALIDAÇÃO DE CHAVES PRIMÁRIAS")
print("=" * 70)

for nome, (arquivo, coluna) in tabelas.items():
    df = carregar_tabela(arquivo)
    validar_chave_primaria(df, coluna, nome)
