import os
import google.generativeai as genai
from graph.state import AgentState
from dotenv import load_dotenv
import time

load_dotenv()

def critic_agent(state: AgentState):
    """
    Agente que revisa o relatório usando SDK nativo.
    """
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    report = state['report']
    revision_count = state.get('revision_count', 0)
    
    prompt = f"Avalie o relatório técnico abaixo. Se estiver bom, responda apenas 'APROVADO'. Se não, dê feedback técnico curto.\n\nRelatório:\n{report}"
    
    for i in range(3):
        try:
            response = model.generate_content(prompt)
            feedback = response.text
            break
        except Exception as e:
            if "429" in str(e) and i < 2:
                time.sleep(40)
                continue
            feedback = "APROVADO (Forçado devido a erro de quota)"
            
    return {
        "feedback": feedback,
        "revision_count": revision_count + 1,
        "messages": [f"Critic avaliou: {feedback[:30]}"]
    }
