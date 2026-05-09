import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

def web_search(query: str):
    """
    Realiza uma busca técnica na web usando a API da Tavily.
    Retorna um resumo formatado dos resultados.
    """
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    
    # Busca focada em profundidade e conteúdo técnico
    response = client.search(query, search_depth="advanced", max_results=5)
    
    context = ""
    for result in response['results']:
        context += f"\n---\nFonte: {result['url']}\nTítulo: {result['title']}\nConteúdo: {result['content']}\n"
    
    return context
