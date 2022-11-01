import typer

app = typer.Typer()


@app.command()
def hello(name: str = typer.Option(..., "--name", "-n", prompt="Name")):
    typer.echo(f"Hello {name}")


@app.command()
def bye(name: str = typer.Option(..., "--name", "-n", prompt="Name")):
    typer.echo(f"Bye {name}")


if __name__ == "__main__":
    app()
