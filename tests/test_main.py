import pytest
from typer.testing import CliRunner
from vin_cli.cli.main import app

runner = CliRunner()


def test_app_runs():
    """测试应用能够正常运行"""
    result = runner.invoke(app, input="q\n")
    assert result.exit_code == 0
    assert "Welcome to Vin!" in result.stdout


def test_hi_command():
    """测试输入 hi 返回 hello world"""
    result = runner.invoke(app, input="hi\nq\n")
    assert result.exit_code == 0
    assert "hello world" in result.stdout


def test_exit_commands():
    """测试退出命令"""
    for cmd in ["exit", "quit", "q"]:
        result = runner.invoke(app, input=f"{cmd}\n")
        assert result.exit_code == 0
        assert "Goodbye!" in result.stdout


def test_other_input():
    """测试其他输入"""
    result = runner.invoke(app, input="test input\nq\n")
    assert result.exit_code == 0
    assert "You typed: test input" in result.stdout
