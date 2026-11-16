import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

arquivo_lancamentos = (
    BASE_DIR / "01_Fonte_Dados" / "fato_lancamentos_financeiros.csv"
)

arquivo_caixa = (
    BASE_DIR / "01_Fonte_Dados" / "fato_fluxo_caixa.csv"
)

lancamentos = pd.read_csv(
    arquivo_lancamentos,
    sep=";",
    encoding="utf-8-sig"
)

caixa = pd.read_csv(
    arquivo_caixa,
    sep=";",
    encoding="utf-8-sig"
)

print("\nVALIDAÇÃO — STATUS DOS LANÇAMENTOS VS FLUXO DE CAIXA")
print("=" * 65)

# IDs presentes no fluxo de caixa
ids_caixa = set(caixa["id_lancamento"])

# Lançamentos realizados e pendentes
realizados = lancamentos[
    lancamentos["status_lancamento"] == "Realizado"
]

pendentes = lancamentos[
    lancamentos["status_lancamento"] == "Pendente"
]

# Realizados sem movimento de caixa
realizados_sem_caixa = realizados[
    ~realizados["id_lancamento"].isin(ids_caixa)
]

# Pendentes que aparecem no fluxo de caixa
pendentes_com_caixa = pendentes[
    pendentes["id_lancamento"].isin(ids_caixa)
]

print("\n1. LANÇAMENTOS REALIZADOS")
print("Total:", len(realizados))
print("Sem movimento de caixa:", len(realizados_sem_caixa))

print("\n2. LANÇAMENTOS PENDENTES")
print("Total:", len(pendentes))
print("Com movimento de caixa:", len(pendentes_com_caixa))

print("\n3. RESUMO")
print("Total de lançamentos:", len(lancamentos))
print("Total de movimentos de caixa:", len(caixa))
print("Correspondência de status:", 
      len(realizados_sem_caixa) == 0 and len(pendentes_com_caixa) == 0)

if len(realizados_sem_caixa) > 0:
    print("\nExemplos de realizados sem caixa:")
    print(realizados_sem_caixa[
        ["id_lancamento", "status_lancamento", "valor"]
    ].head(10).to_string(index=False))

if len(pendentes_com_caixa) > 0:
    print("\nExemplos de pendentes com caixa:")
    print(pendentes_com_caixa[
        ["id_lancamento", "status_lancamento", "valor"]
    ].head(10).to_string(index=False))

print("\nVALIDAÇÃO CONCLUÍDA")