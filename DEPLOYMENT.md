# Guia de Deploy e Docker

Este documento descreve como executar as aplicações localmente usando Docker e como fazer o deploy no Google Cloud Platform (GCP) usando Cloud Run.

## 1. Execução Local com Docker Compose

Para rodar todas as 4 aplicações simultaneamente em containers isolados:

1.  Certifique-se de ter o **Docker** e **Docker Compose** instalados.
2.  Na raiz do projeto, execute:
    ```bash
    docker-compose up --build
    ```
3.  Acesse as aplicações nos seguintes endereços:
    *   **ADK**: [http://localhost:8501](http://localhost:8501)
    *   **CrewAI**: [http://localhost:8502](http://localhost:8502)
    *   **LangChain**: [http://localhost:8503](http://localhost:8503)
    *   **Orchestration**: [http://localhost:8504](http://localhost:8504)

## 2. Deploy no Google Cloud (Cloud Run)

O pipeline de deploy está configurado no arquivo `cloudbuild.yaml`. Ele constrói as imagens Docker e as envia para o Google Container Registry (GCR), e em seguida faz o deploy (exemplo configurado para o ADK).

### Pré-requisitos
*   Projeto no Google Cloud com faturamento ativado.
*   APIs habilitadas: Cloud Build API, Cloud Run API, Container Registry API (ou Artifact Registry).
*   `gcloud` CLI instalado e autenticado.

### Passo a Passo

1.  **Submeter o Build:**
    Execute o comando abaixo na raiz do projeto (substitua `SEU_PROJECT_ID` pelo ID do seu projeto GCP):
    ```bash
    gcloud builds submit --config cloudbuild.yaml .
    ```

2.  **Verificar Deploy:**
    Acesse o console do Cloud Run para ver os serviços implantados e obter as URLs públicas.

### Estrutura dos Containers
Cada aplicação roda em um container `python:3.11-slim` independente, expondo a porta 8080 (padrão do Cloud Run). As dependências são instaladas a partir do `requirements.txt` na raiz.
