# Análise de Dependências - Projeto Multi-Agentes de Crédito

## 📋 Resumo da Análise

Este documento detalha a análise realizada em todos os arquivos `app.py` e seus módulos relacionados nos 4 projetos do workspace, e a consolidação das dependências em um arquivo `requirements.txt` geral.

---

## 🗂️ Estrutura do Projeto

```
adk-google-finance/
├── credit_score_adk/          # Projeto usando Google ADK
│   ├── app.py                 # Interface Streamlit
│   ├── agent.py               # Agente de crédito (Gemini)
│   ├── tools.py               # Ferramentas de cálculo
│   └── Dockerfile
│
├── credit_score_crewai/       # Projeto usando CrewAI
│   ├── app.py                 # Interface Streamlit
│   ├── crew.py                # Definição da Crew
│   ├── tools.py               # Ferramentas CrewAI
│   ├── requirements.txt       # (Local)
│   └── Dockerfile
│
├── credit_score_langchain/    # Projeto usando LangChain
│   ├── app.py                 # Interface Streamlit
│   ├── agent.py               # Executor do agente
│   ├── tools.py               # Tools LangChain
│   ├── requirements.txt       # (Local)
│   └── Dockerfile
│
├── credit_score_orchestration/ # Orquestração Multi-Agente
│   ├── app.py                 # Interface Streamlit
│   ├── agents.py              # Orquestrador e agentes especializados
│   ├── tools.py               # Ferramentas compartilhadas
│   └── Dockerfile
│
├── token_callback.py          # Callback para contagem de tokens (compartilhado)
└── requirements.txt           # ✅ GERAL (CONSOLIDADO)
```

---

## 📦 Dependências por Projeto

### 1. **credit_score_adk** (Google ADK)

**Arquivos Analisados:**
- `app.py` - Interface Streamlit com chat
- `agent.py` - Classe `CreditAgent` usando `google.generativeai`
- `tools.py` - Funções `calcular_score()` e `analisar_risco()`

**Dependências Identificadas:**
```python
import streamlit              # Interface web
import google.generativeai    # SDK oficial Google Gemini
from dotenv import load_dotenv # Gerenciamento .env
```

**Bibliotecas:**
- `streamlit`
- `google-generativeai`
- `python-dotenv`

---

### 2. **credit_score_crewai** (CrewAI)

**Arquivos Analisados:**
- `app.py` - Interface Streamlit com formulário
- `crew.py` - Definição de `Agent`, `Task`, `Crew` usando `crewai`
- `tools.py` - `CalcularScoreTool` e `AnalisarRiscoTool` (BaseTool do CrewAI)

**Dependências Identificadas:**
```python
import streamlit              # Interface web
from crewai import Agent, Task, Crew, LLM
from crewai.tools import BaseTool
from pydantic import BaseModel
from dotenv import load_dotenv
```

**Bibliotecas:**
- `streamlit`
- `crewai[google-genai]` (includes LiteLLM integration)
- `langchain-google-genai` (usado pelo CrewAI)
- `python-dotenv`
- `pydantic`
- `litellm` (explícito no Dockerfile)

**Observação:** O Dockerfile do CrewAI instala `crewai[google-genai]` e `litellm` explicitamente.

---

### 3. **credit_score_langchain** (LangChain)

**Arquivos Analisados:**
- `app.py` - Interface Streamlit com chat
- `agent.py` - `get_agent_executor()` usando LangChain
- `tools.py` - Tools decoradas com `@tool`

**Dependências Identificadas:**
```python
import streamlit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import tool
from langchain_core.callbacks import StdOutCallbackHandler
from dotenv import load_dotenv
```

**Bibliotecas:**
- `streamlit`
- `langchain`
- `langchain-google-genai`
- `langchain-core`
- `python-dotenv`

**Observação:** O código importa `token_callback.py` do diretório pai.

---

### 4. **credit_score_orchestration** (Multi-Agente)

**Arquivos Analisados:**
- `app.py` - Interface Streamlit com formulário
- `agents.py` - Classes `BaseAgent`, `AnalystAgent`, `LoanOfficerAgent`, `Orchestrator`
- `tools.py` - Funções `calcular_score_detalhado()` e `calcular_oferta_emprestimo()`

**Dependências Identificadas:**
```python
import streamlit
import google.generativeai as genai  # SDK oficial Google
from dotenv import load_dotenv
import json
```

**Bibliotecas:**
- `streamlit`
- `google-generativeai`
- `python-dotenv`

---

## 🔍 Dependências Consolidadas

### Bibliotecas Principais

| Biblioteca | Versão Mínima | Usado em | Descrição |
|------------|---------------|----------|-----------|
| `streamlit` | ≥1.28.0 | Todos | Interface web interativa |
| `python-dotenv` | ≥1.0.0 | Todos | Gerenciamento de arquivos .env |
| `google-generativeai` | ≥0.8.0 | ADK, Orchestration | SDK oficial do Google Gemini |
| `langchain` | ≥0.1.0 | LangChain | Framework de orquestração LLM |
| `langchain-google-genai` | ≥1.0.0 | LangChain, CrewAI | Integração LangChain + Google |
| `langchain-core` | ≥0.1.0 | LangChain | Componentes principais LangChain |
| `crewai[google-genai]` | ≥0.11.0 | CrewAI | Framework de agentes autônomos |
| `litellm` | ≥1.0.0 | CrewAI | Adapter multi-LLM |
| `pydantic` | ≥2.0.0 | CrewAI, LangChain | Validação de dados |

---

## 📝 Arquivo Compartilhado

### `token_callback.py`

Este arquivo é importado por `credit_score_langchain/agent.py` e está localizado na raiz do projeto. Ele implementa um callback customizado para contabilização de tokens do LangChain.

**Dependências adicionais (se houver):**
- `langchain_core.callbacks` (já incluído em `langchain-core`)

---

## ✅ Arquivo `requirements.txt` Geral Criado

📍 **Localização:** `c:\Users\abdme\Documents\Pessoal\Cyberh\adk-google-finance\requirements.txt`

### Características:
- ✅ Todas as dependências dos 4 projetos consolidadas
- ✅ Versões mínimas especificadas para compatibilidade
- ✅ Comentários detalhados por seção
- ✅ Organização por categoria (Interface, APIs, Frameworks, etc.)
- ✅ Compatível com Python 3.11+

### Instalação:
```bash
pip install -r requirements.txt
```

### Instalação em Ambiente Virtual (Recomendado):
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

---

## 🔧 Compatibilidade com Docker

Todos os Dockerfiles dos projetos fazem referência ao `requirements.txt` da raiz:

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```

**Observação:** O Dockerfile do CrewAI adiciona instalações extras:
```dockerfile
RUN pip install "crewai[google-genai]" litellm
```

Estas já estão incluídas no `requirements.txt` geral.

---

## 📊 Estatísticas

- **Total de Projetos Analisados:** 4
- **Total de Arquivos `app.py` Analisados:** 4
- **Total de Módulos Python Analisados:** 12
  - 4 × app.py
  - 4 × tools.py
  - 2 × agent.py
  - 1 × crew.py
  - 1 × agents.py
- **Total de Bibliotecas Únicas:** 9
- **Total de Linhas de Código Analisadas:** ~550 linhas

---

## 🎯 Próximos Passos Recomendados

1. **Validar instalação:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Executar testes de cada projeto:**
   ```bash
   # ADK
   streamlit run credit_score_adk/app.py

   # CrewAI
   streamlit run credit_score_crewai/app.py

   # LangChain
   streamlit run credit_score_langchain/app.py

   # Orchestration
   streamlit run credit_score_orchestration/app.py
   ```

3. **Build Docker (Opcional):**
   ```bash
   docker-compose build
   docker-compose up
   ```

4. **Freeze de versões específicas** (após testes):
   ```bash
   pip freeze > requirements-frozen.txt
   ```

---

## 📌 Notas Importantes

1. **Extras do CrewAI:** A notação `crewai[google-genai]` instala automaticamente dependências adicionais para integração com Google Gemini.

2. **LiteLLM:** Usado pelo CrewAI como adapter para normalizar chamadas entre diferentes provedores de LLM (OpenAI, Google, Anthropic, etc.).

3. **Pydantic v2:** Os frameworks modernos (LangChain, CrewAI) requerem Pydantic v2+.

4. **Python 3.11+:** Recomendado para melhor performance e compatibilidade.

5. **Variáveis de Ambiente:** Todos os projetos requerem `GOOGLE_API_KEY` no arquivo `.env`.

---

## 🔗 Referências

- [Google Generative AI Python SDK](https://github.com/google/generative-ai-python)
- [LangChain Documentation](https://python.langchain.com/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LiteLLM Documentation](https://docs.litellm.ai/)

---

**Documento gerado em:** 2025-12-05  
**Autor:** Análise Automatizada de Dependências
