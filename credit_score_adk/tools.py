"""
Módulo de Ferramentas (Tools) para o Agente de Crédito.
Este módulo contém as funções que o agente pode invocar para realizar cálculos.
"""

def calcular_score(renda: float, divida_total: float, historico_pagamento: str) -> int:
    """
    Calcula o score de crédito com base na renda, dívida e histórico.

    Args:
        renda (float): A renda mensal do cliente.
        divida_total (float): O total de dívidas do cliente.
        historico_pagamento (str): O histórico de pagamentos ('bom', 'medio', 'ruim').

    Returns:
        int: O score de crédito calculado (0 a 1000).
    """
    score_base = 500  # Score inicial

    # Fator Renda (peso positivo)
    score_base += (renda * 0.05)

    # Fator Dívida (peso negativo)
    score_base -= (divida_total * 0.1)

    # Fator Histórico
    historico = historico_pagamento.lower().strip()
    if historico == 'bom':
        score_base += 200
    elif historico == 'medio':
        score_base += 50
    elif historico == 'ruim':
        score_base -= 200
    
    # Normalização para garantir 0-1000
    score_final = max(0, min(1000, int(score_base)))
    
    return score_final

def analisar_risco(score: int) -> dict:
    """
    Analisa o risco com base no score de crédito.

    Args:
        score (int): O score de crédito do cliente.

    Returns:
        dict: Dicionário contendo a categoria de risco e uma recomendação.
    """
    if score >= 800:
        return {
            "categoria": "Baixo Risco",
            "recomendacao": "Aprovar crédito com taxas preferenciais."
        }
    elif score >= 500:
        return {
            "categoria": "Médio Risco",
            "recomendacao": "Aprovar crédito com taxas padrão. Solicitar comprovante de renda adicional se necessário."
        }
    else:
        return {
            "categoria": "Alto Risco",
            "recomendacao": "Recusar crédito ou solicitar garantias substanciais."
        }
