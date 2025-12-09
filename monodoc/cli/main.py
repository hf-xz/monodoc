from pathlib import Path

import rich
import typer
from typer import Option

from monodoc.config import init_settings

from . import repo

app = typer.Typer(
    context_settings={
        "help_option_names": ["-h", "--help"],
    }
)
app.add_typer(repo.app, name="repo", help="Manage Git repositories.")


if __name__ == "__main__":
    app()


@app.command()
def hello(name: str):
    print(f"Hello {name}, from monodoc!")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.callback()
def main(
    config_file: Path | None = Option(None, "--config", "-c", help="Path to configuration file."),
    data_dir: Path | None = Option(None, "--data-dir", help="Path to data directory."),
    log_dir: Path | None = Option(None, "--log-dir", help="Path to log directory."),
    debug: bool = Option(None, "--debug", "-d", help="Enable debug mode."),
):
    """monodoc CLI entry point."""

    # Initialize settings
    settings = init_settings(
        config_file=config_file,
        data_dir=data_dir,
        log_dir=log_dir,
        debug=debug,
    )

    if settings.debug:
        rich.print("[bold red]Debug mode is ON[/bold red]")
        rich.print("[bold green]Current Settings:[/bold green]")
        rich.print(settings.model_dump_json(indent=4))
