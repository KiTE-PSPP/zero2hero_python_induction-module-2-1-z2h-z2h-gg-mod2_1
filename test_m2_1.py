import m2_1
import pytest


def test_input_and_display(monkeypatch, capsys):
    # Phase 1: Test Case
    user_input = "3"
    expected_output = "You guessed 3"

    # Phase 2: Run Program
    monkeypatch.setattr("builtins.input", lambda _: user_input)
    m2_1.input_and_display()
    captured = capsys.readouterr()

    # Answer Validation
    assert expected_output in captured.out

