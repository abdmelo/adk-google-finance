import streamlit as st
import os
import time
from dotenv import load_dotenv

# Carrega variáveis de ambiente ANTES de importar módulos que dependem delas
load_dotenv()

from agents import Orchestrator

def stream_text(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

st.set_page_config(page_title="Sistema Multi-Agente de Crédito", page_icon="None", layout="wide")

st.title("Sistema Multi-Agente: Análise e Concessão de Crédito")
st.markdown("""
Este sistema demonstra a **orquestração de agentes**.
1. **Analista de Risco**: Calcula score e avalia perfil.
2. **Gerente de Empréstimos**: Decide aprovação e taxas com base na análise.
""")

# Configuração
with st.sidebar:
    st.header("Configurações")
    if os.getenv("GOOGLE_API_KEY"):
        st.success("Análise de Crédito com Agentes de IA.")
    else:
        api_key = st.text_input("Google API Key", type="password")
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key

# Inputs
col1, col2 = st.columns(2)
with col1:
    renda = st.number_input("Renda Mensal (R$)", min_value=0.0, value=5000.0)
    divida = st.number_input("Dívida Total (R$)", min_value=0.0, value=1000.0)
with col2:
    historico = st.selectbox("Histórico de Pagamento", ["Bom", "Medio", "Ruim"])
    valor_emprestimo = st.number_input("Valor do Empréstimo Desejado (R$)", min_value=0.0, value=10000.0)

if st.button("Iniciar Análise Multi-Agente", type="primary"):
    if not os.environ.get("GOOGLE_API_KEY"):
        st.error("Configure a API Key na barra lateral.")
    else:
        try:
            orchestrator = Orchestrator()
            
            # Construção do prompt natural para os agentes
            user_prompt = f"Cliente com renda de {renda}, dívida de {divida}, histórico {historico}. Solicita empréstimo de {valor_emprestimo}."
            
            with st.spinner("Orquestrando agentes..."):
                result = orchestrator.process_request(user_prompt)
            
            # Exibição do Processo (Trace)
            st.subheader("Trace da Execução")
            for step in result["steps"]:
                st.write_stream(stream_text(step))
                st.divider()
            
            # Resultado Final em Destaque
            st.success("Processo Concluído!")
            st.subheader("Decisão Final")
            st.write_stream(stream_text(result["final_result"]))
            
        except Exception as e:
            st.error(f"Erro na execução: {e}")
