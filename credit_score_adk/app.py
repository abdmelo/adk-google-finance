"""
Aplicação Frontend (Streamlit) para o Agente de Crédito.
"""
import streamlit as st
import os
import time
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

from agent import CreditAgent

def stream_text(text):
    """Gera o texto palavra por palavra para efeito de digitação."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

# Configuração da Página
st.set_page_config(
    page_title="Agente de Análise de Crédito",
    page_icon="None",
    layout="wide"
)

# Título e Descrição
st.title("Agente de Análise de Crédito (Google ADK)")
st.markdown("""
Este sistema utiliza Inteligência Artificial para analisar riscos financeiros.
O agente pode calcular seu score de crédito e fornecer recomendações baseadas em sua renda, dívidas e histórico.
""")

# Barra Lateral para Configuração
with st.sidebar:
    st.header("Configurações")
    
    # Verifica se a API Key já está no ambiente
    if os.getenv("GOOGLE_API_KEY"):
        st.success("Análise de Crédito com Agentes de IA.")
    else:
        api_key = st.text_input("Google API Key", type="password", help="Insira sua chave de API do Google Gemini.")
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key
    
    st.divider()
    st.markdown("### Como usar")
    st.markdown("1. Digite os dados do cliente no chat.")
    st.markdown("Exemplo: *'Calcule o score para renda de 5000, dívida de 1200 e histórico bom.'*")

# Inicialização do Agente na Sessão
if "agent" not in st.session_state:
    # Só inicializa se a API Key estiver presente (ou no env ou no input)
    if os.environ.get("GOOGLE_API_KEY"):
        try:
            st.session_state.agent = CreditAgent()
            st.session_state.messages = []
        except Exception as e:
            st.error(f"Erro ao inicializar o agente: {e}")
    else:
        st.warning("Por favor, insira sua Google API Key na barra lateral para começar.")

# Interface de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do Usuário
if prompt := st.chat_input("Digite sua solicitação aqui..."):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Processar resposta do agente
    if "agent" in st.session_state:
        with st.chat_message("assistant"):
            # Chama o agente (com spinner para indicar processamento)
            with st.spinner("Analisando..."):
                full_response = st.session_state.agent.send_message(prompt)
            
            # Aplica o efeito de digitação na resposta completa
            st.write_stream(stream_text(full_response))
        
        # Adicionar resposta do agente ao histórico
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    else:
        st.error("Agente não inicializado. Verifique a API Key.")
