# ATLAS 🛰️ | Multi-Agent Intelligence System

O **ATLAS** é um sistema avançado de orquestração de agentes de IA projetado para realizar pesquisas técnicas profundas e gerar relatórios estruturados de forma autônoma.

Diferente de scripts lineares, o ATLAS utiliza a arquitetura de **Grafos de Estado (LangGraph)**, permitindo que os agentes colaborem, revisem e refinem o trabalho uns dos outros em um ciclo de melhoria contínua.

## 🤖 Os Agentes

-   **Researcher**: Utiliza a **Tavily Search API** para minerar dados técnicos na web. Ele recebe feedbacks do Critic para aprofundar buscas em pontos específicos.
-   **Analyst/Writer**: Transforma dados brutos em relatórios Markdown profissionais, focando em clareza, estrutura e precisão técnica.
-   **Critic/Reviewer**: O guardião da qualidade. Ele analisa o relatório final e decide se o trabalho está aprovado ou se precisa de mais uma rodada de pesquisa e escrita.

## 🛠️ Stack Tecnológica

-   **Python 3.11+**
-   **LangGraph**: Orquestração de estado e ciclos.
-   **Google Generative AI (Native SDK)**: Integração robusta com a API do Google.
-   **Gemini 1.5 Flash**: Modelo de linguagem otimizado para velocidade e alta quota.
-   **Tavily API**: Web search otimizada para agentes de IA.
-   **Rich**: Interface de terminal (CLI) moderna e estilizada.

## 🚀 Como Executar

1.  **Clone o repositório**:
    ```bash
    git clone https://github.com/wilsonborges/atlas-agents.git
    cd atlas-agents
    ```

2.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure o `.env`**:
    Crie um arquivo `.env` baseado no `.env.example`:
    ```env
    GOOGLE_API_KEY=sua_chave_aqui
    TAVILY_API_KEY=sua_chave_aqui
    ```

4.  **Inicie o sistema**:
    ```bash
    python main.py
    ```

---
*Desenvolvido por wilson borges.*
