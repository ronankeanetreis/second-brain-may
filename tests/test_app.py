import sys

from second_brain.app import main


def test_new_command_prints_path(monkeypatch, tmp_path, capsys):
    monkeypatch.setenv("SECOND_BRAIN_DIR", str(tmp_path))
    monkeypatch.setattr(sys, "argv", ["second_brain", "new", "My brilliant idea about caching"])
    main()
    captured = capsys.readouterr()
    assert ".md" in captured.out


def test_no_subcommand_prints_help(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["second_brain"])
    main()
    captured = capsys.readouterr()
    assert "usage" in captured.out.lower() or "usage" in captured.err.lower()
