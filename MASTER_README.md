# Projeto Google ADK Finance

Este repositório contém múltiplas implementações de sistemas de análise de crédito utilizando Google Gen AI, demonstrando diferentes frameworks e padrões.

## 1. Versão Simples (`credit_score_adk`)
Um agente único que calcula score e analisa risco. Ideal para iniciantes.
*   **Framework**: Google Generative AI SDK (Puro)
*   **Código**: [Pasta](./credit_score_adk/)
*   **Guia**: [Walkthrough](./walkthrough.md)

## 2. Versão Orquestrada (`credit_score_orchestration`)
Sistema multi-agente com orquestrador manual em Python.
*   **Framework**: Google Generative AI SDK (Puro + Padrão Orquestrador)
*   **Código**: [Pasta](./credit_score_orchestration/)
*   **Guia**: [Walkthrough Orquestração](./walkthrough_orchestration.md)

## 3. Versão LangChain (`credit_score_langchain`)
Implementação utilizando o ecossistema LangChain.
*   **Framework**: LangChain + LangChain Google GenAI
*   **Código**: [Pasta](./credit_score_langchain/)
*   **Documentação**: [README](./credit_score_langchain/README.md)

## 4. Versão CrewAI (`credit_score_crewai`)
Implementação utilizando CrewAI para orquestração baseada em papéis.
*   **Framework**: CrewAI
*   **Código**: [Pasta](./credit_score_crewai/)
*   **Documentação**: [README](./credit_score_crewai/README.md)

## Como Executar
Cada subpasta possui seu próprio `README.md` e arquivo de requisitos.
De modo geral, você precisará de:
```bash
pip install google-generativeai langchain langchain-google-genai crewai streamlit
```
E configurar sua `GOOGLE_API_KEY`.
