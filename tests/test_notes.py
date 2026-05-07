import re
from pathlib import Path

import pytest

from second_brain.notes import get_notes_dir, make_slug, save_note


def test_make_slug_lowercases():
    assert make_slug("My Idea") == "my-idea"


def test_make_slug_collapses_punctuation():
    assert make_slug("My brilliant idea about caching") == "my-brilliant-idea-about-caching"


def test_make_slug_strips_punctuation():
    assert make_slug("!hello?") == "hello"


def test_get_notes_dir_default(monkeypatch):
    monkeypatch.delenv("SECOND_BRAIN_DIR", raising=False)
    assert get_notes_dir() == Path.home() / "second_brain"


def test_get_notes_dir_from_env(monkeypatch, tmp_path):
    monkeypatch.setenv("SECOND_BRAIN_DIR", str(tmp_path))
    assert get_notes_dir() == tmp_path


def test_save_note_creates_file(monkeypatch, tmp_path):
    monkeypatch.setenv("SECOND_BRAIN_DIR", str(tmp_path))
    path = save_note("Hello world")
    assert path.exists()
    assert path.read_text() == "Hello world"


def test_save_note_filename_format(monkeypatch, tmp_path):
    monkeypatch.setenv("SECOND_BRAIN_DIR", str(tmp_path))
    path = save_note("My idea")
    assert re.match(r"\d{4}-\d{2}-\d{2}-my-idea\.md", path.name)


def test_save_note_creates_directory_if_missing(monkeypatch, tmp_path):
    notes_dir = tmp_path / "nested" / "notes"
    monkeypatch.setenv("SECOND_BRAIN_DIR", str(notes_dir))
    save_note("Test")
    assert notes_dir.exists()


def test_save_note_returns_path(monkeypatch, tmp_path):
    monkeypatch.setenv("SECOND_BRAIN_DIR", str(tmp_path))
    result = save_note("My idea")
    assert isinstance(result, Path)
    assert result.suffix == ".md"
