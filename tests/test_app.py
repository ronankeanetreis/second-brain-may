import re

from second_brain.app import main


def test_main_logs_greeting(capfd):
    main()
    captured = capfd.readouterr()
    assert "Hello from second_brain!" in captured.err


def test_log_format_no_milliseconds(capfd):
    main()
    captured = capfd.readouterr()
    assert re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \|", captured.err)
    assert not re.search(r"\d{2}:\d{2}:\d{2}\.\d+", captured.err)


def test_log_format_single_letter_level(capfd):
    main()
    captured = capfd.readouterr()
    assert re.search(r"\| [A-Z] \|", captured.err)


def test_log_format_pipe_before_message(capfd):
    main()
    captured = capfd.readouterr()
    assert "| Hello from second_brain!" in captured.err
    assert "- Hello from second_brain!" not in captured.err
