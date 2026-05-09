import os
import google.generativeai as genai
from tools.search import web_search
from graph.state import AgentState
from dotenv import load_dotenv
import time

load_dotenv()

def researcher_agent(state: AgentState):
    """
    Agente responsável por buscar informações na web usando a biblioteca nativa do Google.
    """
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash') # Trocando para 1.5 que tem cota maior
    
    topic = state['topic']
    feedback = state.get('feedback', "")
    
    query_prompt = f"Crie uma query de busca otimizada (em uma única linha) para pesquisar sobre: {topic}."
    if feedback:
        query_prompt += f" Considere este feedback: {feedback}"
        
    # Retry loop robusto
    for i in range(3):
        try:
            response = model.generate_content(query_prompt)
            query = response.text.strip()
            break
        except Exception as e:
            if "429" in str(e) and i < 2:
                print(f"\n[Aviso] Quota cheia. Esperando 40s para tentar novamente...")
                time.sleep(40)
                continue
            # Se falhar o 1.5, tenta o 2.0 como última alternativa
            if i == 2:
                 model = genai.GenerativeModel('gemini-2.0-flash')
                 query = topic # Simplifica a query se tudo der errado
    
    search_results = web_search(query)
    
    return {
        "context": [search_results],
        "messages": [f"Researcher buscou por: {query}"]
    }
