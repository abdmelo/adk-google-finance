"""
Módulo do Agente (Agent) de Crédito.
Este módulo configura o modelo Generative AI e define a classe do agente.
"""
import os
import google.generativeai as genai
from google.generativeai.types import content_types
from collections.abc import Iterable
import tools

# Configuração da API Key
# É esperado que a variável de ambiente GOOGLE_API_KEY esteja definida.
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

class CreditAgent:
    """
    Classe que representa o Agente de Análise de Crédito.
    Gerencia a sessão de chat e a interação com o modelo Gemini.
    """
    def __init__(self):
        """
        Inicializa o agente, configurando o modelo e as ferramentas.
        """
        self.tools_list = [tools.calcular_score, tools.analisar_risco]
        
        # Instruções do sistema para o agente
        self.system_instruction = """
        Você é um especialista em análise de crédito bancário.
        Sua função é ajudar usuários a calcular o score de crédito e analisar riscos.
        Você DEVE usar as ferramentas fornecidas ('calcular_score' e 'analisar_risco') sempre que necessário.
        
        Ao receber dados do usuário (renda, dívida, histórico), siga estes passos:
        1. Chame a ferramenta 'calcular_score'.
        2. Com o resultado do score, chame a ferramenta 'analisar_risco'.
        3. Apresente o resultado final ao usuário de forma clara e profissional, explicando o score e a recomendação.
        
        Se faltarem dados, pergunte ao usuário educadamente.
        Responda sempre em Português do Brasil.
        """

        self.model = genai.GenerativeModel(
            model_name='gemini-2.0-flash', # Ou outro modelo disponível
            tools=self.tools_list,
            system_instruction=self.system_instruction
        )
        
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def send_message(self, message: str) -> str:
        """
        Envia uma mensagem para o agente e retorna a resposta.

        Args:
            message (str): A mensagem do usuário.

        Returns:
            str: A resposta do agente.
        """
        try:
            print(f"\n[LOG] --- Enviando Prompt para o Modelo ---")
            print(f"[LOG] User Message: {message}")
            
            response = self.chat.send_message(message)
            
            print(f"[LOG] --- Resposta Recebida ---")
            print(f"[LOG] Response Text: {response.text}")
            
            if response.usage_metadata:
                in_tokens = response.usage_metadata.prompt_token_count
                out_tokens = response.usage_metadata.candidates_token_count
                total_tokens = response.usage_metadata.total_token_count
                print(f"[LOG] Token Usage -> Input: {in_tokens} | Output: {out_tokens} | Total: {total_tokens}")
            
            return response.text
        except Exception as e:
            print(f"[ERROR] Erro na chamada do modelo: {e}")
            return f"Ocorreu um erro ao processar sua solicitação: {str(e)}"

    def get_history(self):
        """Retorna o histórico da conversa."""
        return self.chat.history
