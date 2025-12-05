"""
Ferramentas para CrewAI.
"""
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class CalcularScoreInput(BaseModel):
    renda: float = Field(..., description="Renda mensal do cliente.")
    divida_total: float = Field(..., description="Total de dívidas do cliente.")
    historico_pagamento: str = Field(..., description="Histórico de pagamento: 'bom', 'medio' ou 'ruim'.")

class CalcularScoreTool(BaseTool):
    name: str = "Calcular Score de Crédito"
    description: str = "Calcula o score de crédito (0-1000) baseado em renda, dívida e histórico."
    args_schema: Type[BaseModel] = CalcularScoreInput

    def _run(self, renda: float, divida_total: float, historico_pagamento: str) -> int:
        score_base = 500
        score_base += (float(renda) * 0.05)
        score_base -= (float(divida_total) * 0.1)
        
        historico = historico_pagamento.lower().strip()
        if historico == 'bom':
            score_base += 200
        elif historico == 'medio':
            score_base += 50
        elif historico == 'ruim':
            score_base -= 200
        
        return max(0, min(1000, int(score_base)))

class AnalisarRiscoInput(BaseModel):
    score: int = Field(..., description="O score de crédito calculado (0-1000).")

class AnalisarRiscoTool(BaseTool):
    name: str = "Analisar Risco de Crédito"
    description: str = "Analisa o risco com base no score numérico e retorna a categoria."
    args_schema: Type[BaseModel] = AnalisarRiscoInput

    def _run(self, score: int) -> str:
        score = int(score)
        if score >= 800:
            return "Baixo Risco"
        elif score >= 500:
            return "Médio Risco"
        else:
            return "Alto Risco"
