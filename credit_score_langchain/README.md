# Sistema de Crédito com LangChain

Implementação do sistema de análise de crédito utilizando o framework **LangChain**.

## Características
*   Uso de `ChatGoogleGenerativeAI` (Gemini).
*   Ferramentas definidas com `@tool`.
*   Agente do tipo `tool-calling`.

## Instalação
```bash
pip install langchain langchain-google-genai streamlit
```

## Execução
1.  Testes: `python tests.py`
2.  App: `streamlit run app.py`

## Estrutura
*   `agent.py`: Configuração do Executor.
*   `tools.py`: Lógica de cálculo.
*   `app.py`: Interface.
