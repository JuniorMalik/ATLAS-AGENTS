from typing import TypedDict, Annotated, List, Union
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    # O tópico da pesquisa
    topic: str
    # O contexto coletado pelo Researcher
    context: List[str]
    # O relatório atual gerado pelo Writer
    report: str
    # Feedback do Critic
    feedback: str
    # Contador de revisões para evitar loops infinitos
    revision_count: int
    # Histórico de mensagens (opcional, mas bom para debug)
    messages: Annotated[List[BaseMessage], operator.add]
