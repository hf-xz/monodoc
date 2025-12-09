import typer

app = typer.Typer()


@app.command()
def hi():
    typer.echo("hi")
