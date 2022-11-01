from typer.testing import CliRunner
from python_poetry_example import main

runner = CliRunner()


def test_hello_cli_call():
    result = runner.invoke(main.app, ["hello", "--name", "John"])
    assert result.exit_code == 0
    assert "Hello John" in result.stdout


def test_bye_cli_call():
    result = runner.invoke(main.app, ["bye", "--name", "John"])
    assert result.exit_code == 0
    assert "Bye John" in result.stdout
