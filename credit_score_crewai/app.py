"""
Frontend Streamlit para CrewAI.
"""
import streamlit as st
import os
import time
from dotenv import load_dotenv
from crew import run_crew

# Carrega variáveis de ambiente
load_dotenv()

def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

st.set_page_config(page_title="Equipe de Crédito (CrewAI)", page_icon="None")

st.title("Equipe de Crédito com CrewAI")
st.markdown("Uma equipe de agentes autônomos trabalhando para você.")

with st.sidebar:
    if os.getenv("GOOGLE_API_KEY"):
        st.success("Análise de Crédito com Agentes de IA.")
    else:
        api_key = st.text_input("Google API Key", type="password")
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key

col1, col2 = st.columns(2)
with col1:
    renda = st.number_input("Renda", value=5000.0)
    divida = st.number_input("Dívida", value=1000.0)
with col2:
    historico = st.selectbox("Histórico", ["bom", "medio", "ruim"])

if st.button("Iniciar Análise da Equipe"):
    if not os.environ.get("GOOGLE_API_KEY"):
        st.error("Configure a API Key.")
    else:
        try:
            with st.spinner("A equipe está trabalhando... (Isso pode levar alguns segundos)"):
                inputs = {"renda": renda, "divida": divida, "historico": historico}
                resultado = run_crew(inputs)
                
            st.success("Análise Concluída!")
            st.markdown("### Resultado Final")
            st.write_stream(stream_text(str(resultado)))
            
        except Exception as e:
            st.error(f"Erro na execução da Crew: {e}")
