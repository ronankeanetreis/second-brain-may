# Usage

## Installation

Clone the repository and install dependencies:

```bash
uv sync
```

## Running

Save a quick note from the terminal:

```bash
uv run second_brain new "My brilliant idea about caching"
# => /home/user/second_brain/2026-05-07-my-brilliant-idea-about-caching.md
```

With dev environment variables loaded:

```bash
uv run --env-file .env second_brain new "My idea"
```

Or as a Python module:

```bash
uv run python -m second_brain new "My idea"
```

## Environment Variables

| Variable           | Default           | Description                          |
|--------------------|-------------------|--------------------------------------|
| `SECOND_BRAIN_DIR` | `~/second_brain/` | Directory where notes are saved. Created automatically if missing. |
| `LOG_LEVEL`        | `INFO`            | Console log level (DEBUG, INFO, …)   |
| `LOG_FILE`         | `app.log`         | Path to the log file                 |

Copy `.env.example` to `.env` for development defaults, then run with `uv run --env-file .env`.

### Log format

```
2026-05-06 14:32:07 | I | second_brain.app:main:29 | Hello from second_brain!
```

Timestamp has no milliseconds; level is a single uppercase letter (`D`, `I`, `W`, `E`, `C`); all fields separated by `|`.
