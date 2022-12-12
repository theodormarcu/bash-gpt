import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
import requests

# BashGPT
# Explain what the last command does.
# Explain this prompt
# Generate a command

GENERATE_PROMPT = "Generate a terminal command that respects the following prompt: "

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


def main(
    prompt: str = typer.Argument(...),
        generate: bool = typer.Option(False),
):
    typer.echo(f"Prompt: {prompt}")
    typer.echo(f"Generate: {generate}")
    if generate:
        generate_command(prompt)
    else:
        explain_command(prompt)


if __name__ == "__main__":
    typer.run(main)
