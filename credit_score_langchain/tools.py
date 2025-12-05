"""
Módulo de Ferramentas (Tools) para LangChain.
"""
from langchain.tools import tool

@tool
def calcular_score(renda: float, divida_total: float, historico_pagamento: str) -> int:
    """
    Calcula o score de crédito baseado na renda, dívida e histórico.
    Args:
        renda: Renda mensal do cliente.
        divida_total: Total de dívidas.
        historico_pagamento: 'bom', 'medio' ou 'ruim'.
    Returns:
        Um inteiro representando o score (0-1000).
    """
    score_base = 500
    score_base += (renda * 0.05)
    score_base -= (divida_total * 0.1)
    
    historico = historico_pagamento.lower().strip()
    if historico == 'bom':
        score_base += 200
    elif historico == 'medio':
        score_base += 50
    elif historico == 'ruim':
        score_base -= 200
    
    return max(0, min(1000, int(score_base)))

@tool
def analisar_risco(score: int) -> str:
    """
    Analisa o risco com base no score numérico.
    Args:
        score: O score de crédito (0-1000).
    Returns:
        Uma string descrevendo o risco e recomendação.
    """
    if score >= 800:
        return "Baixo Risco: Aprovar com taxas preferenciais."
    elif score >= 500:
        return "Médio Risco: Aprovar com taxas padrão."
    else:
        return "Alto Risco: Recusar ou solicitar garantias."
