"""
Definição da Crew (Agentes e Tarefas).
"""
import os
from crewai import Agent, Task, Crew, Process, LLM
from tools import CalcularScoreTool, AnalisarRiscoTool
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente da pasta atual
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

def run_crew(inputs):
    """
    Executa a Crew de análise de crédito.
    Args:
        inputs (dict): Dicionário com 'renda', 'divida', 'historico'.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY ausente no .env local")

    # Modelo Gemini via CrewAI LLM (Nativo)
    # O prefixo 'gemini/' indica o provider para o LiteLLM
    llm = LLM(
        model="gemini/gemini-2.0-flash",
        api_key=api_key
    )
    
    # Instancia as ferramentas
    calc_tool = CalcularScoreTool()
    risk_tool = AnalisarRiscoTool()

    # Agentes
    analista = Agent(
        role='Analista de Crédito Sênior',
        goal='Calcular o score de crédito exato e determinar o risco.',
        backstory='Você é um especialista matemático focado em precisão. Você DEVE usar as ferramentas de cálculo.',
        tools=[calc_tool, risk_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    gerente = Agent(
        role='Gerente de Relacionamento',
        goal='Comunicar a decisão final ao cliente de forma clara e educada.',
        backstory='Você recebe a análise técnica e a traduz para o cliente, oferecendo recomendações.',
        llm=llm,
        verbose=True,
        allow_delegation=False
    )

    # Tarefas
    tarefa_analise = Task(
        description=f"""
        1. Calcule o score para um cliente com Renda: {inputs['renda']}, Dívida: {inputs['divida']}, Histórico: {inputs['historico']}.
        2. Com base no score, analise o risco.
        Retorne o valor numérico do score e a categoria de risco.
        """,
        agent=analista,
        expected_output="Um relatório técnico com Score e Risco."
    )

    tarefa_comunicacao = Task(
        description="""
        Com base no relatório do Analista, escreva uma resposta final para o cliente.
        Explique o resultado e dê uma recomendação.
        """,
        agent=gerente,
        expected_output="Uma mensagem amigável e profissional para o cliente.",
        context=[tarefa_analise]
    )

    # Crew
    crew = Crew(
        agents=[analista, gerente],
        tasks=[tarefa_analise, tarefa_comunicacao],
        process=Process.sequential,
        verbose=True
    )

    print("\n[LOG] --- Iniciando CrewAI ---")
    result = crew.kickoff()
    print(f"[LOG] --- CrewAI Finalizado ---")
    print(f"[LOG] Resultado: {result}")
    
    # Contabilização de Tokens (via CrewOutput)
    if hasattr(result, 'token_usage'):
        usage = result.token_usage
        # CrewAI retorna usage como objeto ou dict, vamos tentar acessar
        # Formato esperado: {'total_tokens': X, 'prompt_tokens': Y, 'completion_tokens': Z}
        # Ou atributos do objeto
        try:
            # Tenta acessar como atributos (padrão recente)
            in_tokens = getattr(usage, 'prompt_tokens', 0)
            out_tokens = getattr(usage, 'completion_tokens', 0)
            total_tokens = getattr(usage, 'total_tokens', 0)
            
            # Se for zero, tenta como dicionário
            if total_tokens == 0 and isinstance(usage, dict):
                in_tokens = usage.get('prompt_tokens', 0)
                out_tokens = usage.get('completion_tokens', 0)
                total_tokens = usage.get('total_tokens', 0)

            print(f"[LOG] Token Usage -> Input: {in_tokens} | Output: {out_tokens} | Total: {total_tokens}")
        except Exception as e:
            print(f"[LOG] Erro ao ler tokens: {e}")
    else:
        print("[LOG] Token Usage -> Não disponível no objeto result.")

    return result
