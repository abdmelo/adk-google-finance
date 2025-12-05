"""
Configuração do Agente LangChain.
"""
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from tools import calcular_score, analisar_risco

def get_agent_executor():
    """
    Cria e retorna o executor do agente LangChain.
    """
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY não configurada.")

    import sys
    # Adiciona o diretório pai ao path para importar token_callback
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from token_callback import TokenUsageCallback

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", 
        google_api_key=api_key,
        callbacks=[TokenUsageCallback()]
    )
    
    tools = [calcular_score, analisar_risco]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um especialista em crédito. Use as ferramentas para calcular score e analisar risco. Responda em Português."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    from langchain_core.callbacks import StdOutCallbackHandler
    
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    # Adicionando handler para logs detalhados no console
    handler = StdOutCallbackHandler()
    
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True,
        callbacks=[handler],
        handle_parsing_errors=True
    )
    
    return agent_executor
