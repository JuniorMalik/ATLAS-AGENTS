from langgraph.graph import StateGraph, END
from graph.state import AgentState
from agents.researcher import researcher_agent
from agents.writer import writer_agent
from agents.critic import critic_agent

def create_workflow():
    workflow = StateGraph(AgentState)

    # Adicionando os nós (agentes)
    workflow.add_node("researcher", researcher_agent)
    workflow.add_node("writer", writer_agent)
    workflow.add_node("critic", critic_agent)

    # Definindo as arestas (fluxo)
    workflow.set_entry_point("researcher")
    
    workflow.add_edge("researcher", "writer")
    workflow.add_edge("writer", "critic")

    # Lógica condicional: Se o crítico aprovar, termina. Se não, volta pro pesquisador.
    def should_continue(state):
        if "APROVADO" in state["feedback"] or state["revision_count"] >= 2:
            return "end"
        return "continue"

    workflow.add_conditional_edges(
        "critic",
        should_continue,
        {
            "continue": "researcher",
            "end": END
        }
    )

    return workflow.compile()
