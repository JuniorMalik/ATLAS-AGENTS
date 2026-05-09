import os
import sys
from dotenv import load_dotenv
from graph.workflow import create_workflow
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.markdown import Markdown
import time

# Forçar UTF-8 no Windows para evitar erros de encode com emojis
if sys.platform == "win32":
    import codecs
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
console = Console()

def main():
    console.clear()
    console.print(Panel.fit("[bold cyan]ATLAS: Multi-Agent Intelligence System[/bold cyan]", border_style="cyan"))
    
    topic = console.input("\n[bold yellow]Sobre qual tópico deseja pesquisar? [/bold yellow]")
    
    if not topic:
        console.print("[red]Erro: Tópico não pode ser vazio.[/red]")
        return

    app = create_workflow()
    
    # Estado inicial
    inputs = {
        "topic": topic,
        "context": [],
        "report": "",
        "feedback": "",
        "revision_count": 0,
        "messages": []
    }

    console.print("\n[bold green]Iniciando Orquestração de Agentes...[/bold green]\n")

    with console.status("[bold blue]Agentes trabalhando...[/bold blue]") as status:
        # Executando o grafo e capturando cada passo
        for output in app.stream(inputs):
            for node_name, state_update in output.items():
                console.print(f"[bold magenta]Agente {node_name.upper()} finalizou sua tarefa.[/bold magenta]")
                time.sleep(1)

    # Pegando o resultado final
    final_state = app.invoke(inputs)
    
    console.print("\n" + "="*50 + "\n")
    console.print(Panel(Markdown(final_state['report']), title="RELATÓRIO FINAL", border_style="green"))
    console.print(f"\n[bold yellow]Total de revisões realizadas:[/bold yellow] {final_state['revision_count']}")
    
    # Salvar em arquivo
    safe_topic = "".join([c if c.isalnum() else "_" for c in topic])
    filename = f"report_{safe_topic}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_state['report'])
    
    console.print(f"\n[bold cyan]Relatório salvo em: {filename}[/bold cyan]")

if __name__ == "__main__":
    main()
