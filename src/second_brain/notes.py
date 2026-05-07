import os
import re
from datetime import date
from pathlib import Path


def make_slug(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def get_notes_dir() -> Path:
    return Path(os.environ.get("SECOND_BRAIN_DIR", Path.home() / "second_brain")).expanduser()


def save_note(text: str) -> Path:
    notes_dir = get_notes_dir()
    notes_dir.mkdir(parents=True, exist_ok=True)
    slug = make_slug(text)
    base = f"{date.today()}-{slug}"
    path = notes_dir / f"{base}.md"
    counter = 2
    while path.exists():
        path = notes_dir / f"{base}-{counter}.md"
        counter += 1
    path.write_text(text, encoding="utf-8")
    return path
