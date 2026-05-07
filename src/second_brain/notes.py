import os
import re
from datetime import date
from pathlib import Path


def make_slug(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def get_notes_dir() -> Path:
    return Path(os.environ.get("SECOND_BRAIN_DIR", Path.home() / "second_brain"))


def save_note(text: str) -> Path:
    notes_dir = get_notes_dir()
    notes_dir.mkdir(parents=True, exist_ok=True)
    slug = make_slug(text)
    filename = f"{date.today()}-{slug}.md"
    path = notes_dir / filename
    path.write_text(text)
    return path
