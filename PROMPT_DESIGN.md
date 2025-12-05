# Design de Prompt Estruturado

Este documento apresenta o prompt estruturado utilizado para gerar a solução de Dockerização e Deploy, seguindo as melhores práticas de Engenharia de Prompt.

---

## Contexto e Persona
**Persona:** Engenheiro DevOps Sênior e Especialista em Google Cloud Platform (GCP).
**Objetivo:** Criar uma infraestrutura robusta, escalável e containerizada para um conjunto de aplicações de IA (Streamlit + Python).
**Restrições:** Usar Docker, Docker Compose e preparar para Google Vertex AI / Cloud Run.

## O Prompt (Simulado)

```markdown
# Role
Você é um Arquiteto de Soluções Cloud Sênior especializado em MLOps e containerização.

# Task
Sua tarefa é containerizar um projeto monorepo contendo 4 micro-frontends em Streamlit e configurar um pipeline de CI/CD para o Google Cloud.

# Requirements
1. **Dockerização Individual**: Cada sub-projeto (adk, crewai, langchain, orchestration) deve ter seu próprio `Dockerfile` otimizado.
2. **Orquestração Local**: Crie um `docker-compose.yml` que levante todos os serviços simultaneamente, mapeando portas distintas.
3. **Pipeline de Deploy**: Crie um arquivo `cloudbuild.yaml` para automatizar o build e deploy no Google Cloud Run (ambiente serverless ideal para Streamlit).
4. **Documentação**: Gere um guia `DEPLOYMENT.md` claro e objetivo.

# Contexto do Projeto
- Linguagem: Python 3.11
- Framework Web: Streamlit
- Dependências: requirements.txt na raiz
- Estrutura de Pastas:
  /root
    /credit_score_adk
    /credit_score_crewai
    /credit_score_langchain
    /credit_score_orchestration
    requirements.txt

# Output Format
- Arquivos de código completos e prontos para uso.
- Markdown para documentação.
```

## Racional da Solução
1.  **Cloud Run vs Vertex AI Pipelines**: Embora o usuário tenha mencionado "Vertex Engine pipeline", para aplicações web interativas (Streamlit), o **Cloud Run** é a solução de hospedagem correta no GCP. Vertex AI Pipelines é para *treinamento* e *processamento em lote* de modelos ML, não para servir interfaces web. O prompt foi ajustado para entregar a solução arquiteturalmente correta (Cloud Run) mantendo a integração com os modelos Gemini (Vertex AI).
2.  **Docker Context**: A estratégia de usar a raiz como contexto de build (`docker build -f subfolder/Dockerfile .`) permite compartilhar o `requirements.txt` e módulos comuns (`token_callback.py`) sem duplicar arquivos.
