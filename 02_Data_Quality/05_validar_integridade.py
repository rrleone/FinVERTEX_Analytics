
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


def validar_chave(
    tabela_origem,
    coluna_origem,
    tabela_referencia,
    coluna_referencia,
    nome_relacionamento
):
    # Ignora valores nulos na chave estrangeira
    valores_origem = tabela_origem[coluna_origem].dropna()

    # IDs existentes na tabela de referência
    valores_referencia = tabela_referencia[
        coluna_referencia
    ].dropna()

    ids_origem = set(valores_origem)
    ids_referencia = set(valores_referencia)

    # IDs usados na origem que não existem na referência
    ids_invalidos = ids_origem - ids_referencia

    quantidade_invalidos = tabela_origem[
        tabela_origem[coluna_origem].isin(ids_invalidos)
    ].shape[0]

    print(f"\nRelacionamento: {nome_relacionamento}")
    print("-" * 70)
    print(f"Registros analisados: {len(valores_origem)}")
    print(f"IDs inválidos encontrados: {len(ids_invalidos)}")
    print(f"Linhas afetadas: {quantidade_invalidos}")

    if ids_invalidos:
        print("IDs sem correspondência:", ids_invalidos)
        print("Resultado: FALHA")
    else:
        print("Resultado: OK")


# Carregar dimensões
funcionario = carregar_tabela("dim_funcionario")
cliente = carregar_tabela("dim_cliente")
fornecedor = carregar_tabela("dim_fornecedor")
centro_custo = carregar_tabela("dim_centro_custo")
plano_contas = carregar_tabela("dim_plano_contas")

# Carregar tabelas fato
lancamentos = carregar_tabela("fato_lancamentos_financeiros")
orcamento = carregar_tabela("fato_orcamento")
fluxo_caixa = carregar_tabela("fato_fluxo_caixa")
folha = carregar_tabela("fato_folha_pagamento")


print("\nVALIDAÇÃO DE INTEGRIDADE REFERENCIAL")
print("=" * 70)


# 1. Folha de pagamento → Funcionários
validar_chave(
    folha, "id_funcionario",
    funcionario, "id_funcionario",
    "Folha de pagamento → Funcionários"
)

# 2. Lançamentos → Plano de contas
validar_chave(
    lancamentos, "id_conta",
    plano_contas, "id_conta",
    "Lançamentos → Plano de contas"
)

# 3. Lançamentos → Centro de custo
validar_chave(
    lancamentos, "id_centro_custo",
    centro_custo, "id_centro_custo",
    "Lançamentos → Centro de custo"
)

# 4. Lançamentos → Clientes
validar_chave(
    lancamentos, "id_cliente",
    cliente, "id_cliente",
    "Lançamentos → Clientes"
)

# 5. Lançamentos → Fornecedores
validar_chave(
    lancamentos, "id_fornecedor",
    fornecedor, "id_fornecedor",
    "Lançamentos → Fornecedores"
)

# 6. Orçamento → Plano de contas
validar_chave(
    orcamento, "id_conta",
    plano_contas, "id_conta",
    "Orçamento → Plano de contas"
)

# 7. Orçamento → Centro de custo
validar_chave(
    orcamento, "id_centro_custo",
    centro_custo, "id_centro_custo",
    "Orçamento → Centro de custo"
)

# 8. Fluxo de caixa → Lançamentos
validar_chave(
    fluxo_caixa, "id_lancamento",
    lancamentos, "id_lancamento",
    "Fluxo de caixa → Lançamentos financeiros"
)

# 9. Fluxo de caixa → Plano de contas
validar_chave(
    fluxo_caixa, "id_conta",
    plano_contas, "id_conta",
    "Fluxo de caixa → Plano de contas"
)

# 10. Fluxo de caixa → Centro de custo
validar_chave(
    fluxo_caixa, "id_centro_custo",
    centro_custo, "id_centro_custo",
    "Fluxo de caixa → Centro de custo"
)

print("\nVALIDAÇÃO FINALIZADA")
