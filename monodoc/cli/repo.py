from pathlib import Path

import typer
from rich import print
from rich.table import Table

from monodoc.core.sync import RepoManager

app = typer.Typer()
repo_manager = RepoManager.get_instance()


@app.command("ls")
def list_repos():
    """
    Lists all managed Git repositories.
    """
    if not repo_manager.repo_list:
        print("[yellow]No repositories found.[/yellow]")
        return

    table = Table(show_lines=False, box=None)
    table.add_column("Name", justify="left", style="cyan")
    table.add_column("Path", justify="left", style="magenta")
    table.add_column("Remote URL", justify="left", style="green")

    for repo in repo_manager.repo_list:
        table.add_row(repo.name, str(repo.path), repo.remote_url)

    print(table)


@app.command("add")
def add_repo(
    remote_url: str = typer.Argument(help="The URL of the remote repository."),
    path: Path | None = typer.Option(None, help="The directory path where the repository will be initialized."),
    name: str = typer.Option("", help="The name of the repository."),
):
    """
    Adds a new Git repository to be managed.

    Args:
        remote_url (str): The URL of the remote repository.
        path (Path | None): The directory path where the repository will be initialized. Defaults to None.
        name (str): The name of the repository. Defaults to an empty string.
    """

    print(f"Adding repository from '{remote_url}'...")

    new_repo = repo_manager.init_repo(path=path, remote_url=remote_url, name=name)

    if new_repo:
        print(f"[green]Successfully added repository {new_repo.name} at {new_repo.path}[/green]")
    else:
        print("[red]Failed to add repository[/red]")
