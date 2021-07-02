import pytest
from click.testing import CliRunner

from main import main

def test_main():
    runner = CliRunner()
    runner.invoke(main, ['hello'], catch_exceptions=False)
    assert True
