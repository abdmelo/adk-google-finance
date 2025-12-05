# Sistema de Crédito com CrewAI

Implementação utilizando o framework **CrewAI** para orquestração de agentes baseados em papéis.

## Estrutura da Equipe (Crew)
1.  **Analista de Crédito**: Usa ferramentas para calcular dados exatos.
2.  **Gerente de Relacionamento**: Consome os dados e gera a resposta final.

## Instalação
```bash
pip install crewai langchain-google-genai streamlit
```

## Execução
1.  Testes: `python tests.py`
2.  App: `streamlit run app.py`

## Arquivos
*   `crew.py`: Definição dos agentes e tarefas.
*   `tools.py`: Ferramentas customizadas.
*   `app.py`: Interface do usuário.
