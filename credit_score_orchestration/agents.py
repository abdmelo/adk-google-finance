"""
Módulo de Orquestração de Agentes.
Define agentes especializados e um orquestrador.
"""
import os
import google.generativeai as genai
import tools
import json

# Configuração da API
def configure_genai():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY não encontrada. Verifique o arquivo .env.")
    genai.configure(api_key=api_key)

class BaseAgent:
    def __init__(self, model_name, system_instruction, tools_list=None):
        configure_genai() # Garante configuração na inicialização
        self.model = genai.GenerativeModel(
            model_name=model_name,
            tools=tools_list,
            system_instruction=system_instruction
        )
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def send(self, message):
        try:
            print(f"\n[LOG] --- Agente {self.model.model_name} ---")
            print(f"[LOG] Input: {message}")
            
            response = self.chat.send_message(message)
            
            print(f"[LOG] Output: {response.text}")
            if response.usage_metadata:
                in_tokens = response.usage_metadata.prompt_token_count
                out_tokens = response.usage_metadata.candidates_token_count
                total_tokens = response.usage_metadata.total_token_count
                print(f"[LOG] Token Usage -> Input: {in_tokens} | Output: {out_tokens} | Total: {total_tokens}")
                
            return response.text
        except Exception as e:
            print(f"[ERROR] {e}")
            return f"Erro no agente: {str(e)}"

class AnalystAgent(BaseAgent):
    """Especialista em Análise de Risco."""
    def __init__(self):
        super().__init__(
            model_name='gemini-2.0-flash',
            tools_list=[tools.calcular_score_detalhado],
            system_instruction="""
            Você é um Analista de Risco Sênior.
            Sua responsabilidade é calcular o score de crédito detalhado.
            Receba os dados (renda, dívida, histórico), chame a ferramenta 'calcular_score_detalhado'
            e retorne um resumo técnico JSON contendo o score e a categoria de risco (Baixo/Médio/Alto).
            NÃO dê recomendações de empréstimo, apenas analise o risco.
            """
        )

class LoanOfficerAgent(BaseAgent):
    """Especialista em Ofertas de Crédito."""
    def __init__(self):
        super().__init__(
            model_name='gemini-2.0-flash',
            tools_list=[tools.calcular_oferta_emprestimo],
            system_instruction="""
            Você é um Gerente de Empréstimos.
            Sua responsabilidade é decidir sobre a aprovação de crédito.
            Você receberá uma análise de risco e dados financeiros.
            Use a ferramenta 'calcular_oferta_emprestimo' para validar se o cliente pode pagar.
            Se aprovado, formalize a proposta. Se negado, explique o motivo educadamente.
            """
        )

class Orchestrator:
    """Gerencia o fluxo entre os agentes."""
    def __init__(self):
        self.analyst = AnalystAgent()
        self.loan_officer = LoanOfficerAgent()
    
    def process_request(self, user_input: str) -> dict:
        """
        Executa o pipeline de orquestração.
        1. Analista calcula risco.
        2. Gerente decide oferta.
        """
        steps = []
        
        # Passo 1: Análise
        steps.append("**Orquestrador**: Enviando dados para o Analista de Risco...")
        analyst_response = self.analyst.send(f"Analise este caso: {user_input}")
        steps.append(f"**Analista**: {analyst_response}")
        
        # Passo 2: Decisão
        steps.append("**Orquestrador**: Encaminhando análise para o Gerente de Empréstimos...")
        # Passamos o contexto original + a análise técnica para o gerente
        loan_input = f"Dados do cliente: {user_input}. Análise de Risco: {analyst_response}. Verifique oferta para empréstimo de 10000 (valor padrão se não informado)."
        final_decision = self.loan_officer.send(loan_input)
        steps.append(f"**Gerente**: {final_decision}")
        
        return {
            "final_result": final_decision,
            "steps": steps
        }
