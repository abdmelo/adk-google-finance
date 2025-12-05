"""
Frontend Streamlit para LangChain.
"""
import streamlit as st
import os
import time
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

from agent import get_agent_executor

def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

st.set_page_config(page_title="Agente de Crédito (LangChain)", page_icon="None")

st.title("Agente de Crédito com LangChain")

with st.sidebar:
    if os.getenv("GOOGLE_API_KEY"):
        st.success("Análise de Crédito com Agentes de IA.")
    else:
        api_key = st.text_input("Google API Key", type="password")
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ex: Calcule score para renda 5000, dívida 1000, histórico bom"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    if not os.environ.get("GOOGLE_API_KEY"):
        st.error("Configure a API Key.")
    else:
        try:
            with st.spinner("Processando com LangChain..."):
                executor = get_agent_executor()
                response = executor.invoke({"input": prompt})
                result = response["output"]
                
            st.session_state.messages.append({"role": "assistant", "content": result})
            st.chat_message("assistant").write_stream(stream_text(result))
        except Exception as e:
            st.error(f"Erro: {e}")
