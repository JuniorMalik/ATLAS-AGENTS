import os
import google.generativeai as genai
from graph.state import AgentState
from dotenv import load_dotenv
import time

load_dotenv()

def writer_agent(state: AgentState):
    """
    Agente responsável por escrever o relatório markdown usando SDK nativo.
    """
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    topic = state['topic']
    context = "\n".join(state['context'])
    
    prompt = f"""
    Você é um Analista Técnico de elite. Sua tarefa é escrever um relatório profundo sobre '{topic}'.
    Use o seguinte contexto coletado: {context}
    O relatório deve ser em Markdown com Título, Resumo, Detalhes, Conclusão e Fontes.
    Escreva apenas o relatório.
    """
    
    for i in range(3):
        try:
            response = model.generate_content(prompt)
            report = response.text
            break
        except Exception as e:
            if "429" in str(e) and i < 2:
                time.sleep(40)
                continue
            report = "Erro ao gerar relatório devido a limites de quota da API."
            
    return {
        "report": report,
        "messages": ["Writer gerou o relatório."]
    }
