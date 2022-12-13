import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
import requests

# BashGPT
# Explain what the last command does.
# Explain this prompt
# Generate a command

GENERATE_PROMPT = "You will be asked to generate a shell command and only respond with the code. You will not add any explanations. Generate a temrinal command that respects the following prompt: "

EXPLAIN_PROMPT = "Explain the following terminal command: "


def generate_command(prompt: str):
    """Generate a command (use at your own risk)"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(
            description="Asking Chat GPT to generate a terminal command...", total=1)

        while not progress.finished:
            response = requests.get(
                f"http://localhost:5001/chat?q={GENERATE_PROMPT}{prompt}",
            )
            typer.echo(f"\nResponse from Chat GPT:\n{response.text}")
            typer.echo('Use this command at your own risk!')
            progress.update(task, advance=1)


def explain_command(prompt: str):
    """Explain a command (use at your own risk)"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(
            description="Asking Chat GPT to explain a command...", total=1)

        while not progress.finished:
            response = requests.get(
                f"http://localhost:5001/chat?q={EXPLAIN_PROMPT}{prompt}",
            )
            typer.echo(f"\nResponse from Chat GPT:\n{response.text}\n")
            typer.echo("Note: Chat GPT may be wrong.")
            progress.update(task, advance=1)


def generate_chat(prompt: str):
    """Just chat"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(
            description="Asking Chat GPT...", total=1)

        while not progress.finished:
            response = requests.get(
                f"http://localhost:5001/chat?q={prompt}",
            )
            typer.echo(f"\nResponse from Chat GPT:\n{response.text}\n")
            progress.update(task, advance=1)


def main(
    prompt: str = typer.Argument(...),
        explain: bool = typer.Option(False),
        chat: bool = typer.Option(False),
):
    if explain:
        explain_command(prompt)
    elif chat:
        generate_chat(prompt)
    else:
        generate_command(prompt)


if __name__ == "__main__":
    typer.run(main)
