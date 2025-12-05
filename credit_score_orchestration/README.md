# Sistema de Crédito Multi-Agente (Orquestração)

Este projeto é uma variação avançada do sistema de Credit Score, demonstrando o padrão de **Orquestração de Agentes**.

## Conceito
Em vez de um único agente fazer tudo, temos especialistas:
1.  **Analista de Risco (`AnalystAgent`)**: Focado puramente em dados técnicos e cálculo de risco.
2.  **Gerente de Empréstimos (`LoanOfficerAgent`)**: Focado em negócios, taxas e aprovação comercial.
3.  **Orquestrador (`Orchestrator`)**: Código Python que gerencia o fluxo de informação entre os agentes.

## Estrutura
*   `agents.py`: Definição das classes dos agentes e do orquestrador.
*   `tools.py`: Ferramentas de cálculo (Score Detalhado, Simulação de Empréstimo).
*   `app.py`: Interface Streamlit que aciona o orquestrador.
*   `tests/`: Testes unitários para garantir a lógica das ferramentas.

## Como Executar

1.  Instale as dependências (se ainda não instalou):
    ```bash
    pip install google-generativeai streamlit
    ```

2.  Execute a aplicação:
    ```bash
    streamlit run app.py
    ```

3.  Insira sua API Key e teste diferentes cenários.

## Verificação e Testes

Para verificar se a lógica interna (ferramentas) está correta, execute o script de teste incluído:

```bash
python tests/test_tools.py
```

### Resultados Esperados
*   **Cenário 1 (Ideal)**: Renda alta, dívida baixa, histórico bom.
    *   *Analista*: Score alto (>800), Risco Baixo.
    *   *Gerente*: Aprova o empréstimo com taxa de juros baixa.
*   **Cenário 2 (Recusa por Score)**: Histórico ruim.
    *   *Analista*: Score baixo (<400), Risco Alto.
    *   *Gerente*: Nega o empréstimo imediatamente.
*   **Cenário 3 (Recusa por Renda)**: Renda baixa, pedido de empréstimo alto.
    *   *Analista*: Score bom (se histórico bom).
    *   *Gerente*: Nega ou sugere valor menor, pois a parcela excederia 30% da renda.

## Diferenças para a Versão Simples
| Característica | Versão Simples (`credit_score_adk`) | Versão Orquestrada (`credit_score_orchestration`) |
| :--- | :--- | :--- |
| **Agentes** | 1 Agente Generalista | 2 Especialistas + 1 Orquestrador |
| **Fluxo** | Linear (Agente decide tudo) | Controlado (Analista -> Gerente) |
| **Complexidade** | Baixa | Média (Melhor separação de responsabilidades) |
