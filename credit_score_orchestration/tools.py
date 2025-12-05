"""
Módulo de Ferramentas (Tools) Compartilhado.
Contém funções puras para cálculo de score e simulação de empréstimo.
"""

def calcular_score_detalhado(renda: float, divida_total: float, historico_pagamento: str) -> dict:
    """
    Calcula o score de crédito e retorna detalhes do cálculo.
    """
    score_base = 500
    score_base += (renda * 0.05)
    score_base -= (divida_total * 0.1)
    
    historico = historico_pagamento.lower().strip()
    fator_historico = 0
    if historico == 'bom':
        fator_historico = 200
    elif historico == 'medio':
        fator_historico = 50
    elif historico == 'ruim':
        fator_historico = -200
    
    score_base += fator_historico
    score_final = max(0, min(1000, int(score_base)))
    
    return {
        "score": score_final,
        "detalhes": {
            "fator_renda": renda * 0.05,
            "fator_divida": -(divida_total * 0.1),
            "fator_historico": fator_historico
        }
    }

def calcular_oferta_emprestimo(score: int, renda: float, valor_solicitado: float) -> dict:
    """
    Calcula a oferta de empréstimo baseada no score e renda.
    """
    if score < 400:
        return {"aprovado": False, "motivo": "Score insuficiente."}
    
    # Taxa de juros baseada no score (inversamente proporcional)
    taxa_juros = max(1.5, 10.0 - (score / 100))
    
    # Limite máximo de parcela (30% da renda)
    limite_parcela = renda * 0.30
    
    # Simulação simples de 12 meses
    parcela_estimada = (valor_solicitado * (1 + (taxa_juros/100))) / 12
    
    if parcela_estimada > limite_parcela:
        return {
            "aprovado": False, 
            "motivo": f"Parcela estimada ({parcela_estimada:.2f}) excede 30% da renda ({limite_parcela:.2f}).",
            "sugestao": "Tente um valor menor ou mais parcelas."
        }
        
    return {
        "aprovado": True,
        "taxa_juros_mensal": f"{taxa_juros:.2f}%",
        "limite_parcela": limite_parcela,
        "valor_aprovado": valor_solicitado,
        "prazo_sugerido": 12
    }
