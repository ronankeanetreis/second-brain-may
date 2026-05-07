import argparse
import sys

from loguru import logger

from second_brain.notes import save_note


def configure_logging():
    """Configure loguru for console and file logging.

    Removes the default handler and sets up:
    - stderr handler at LOG_LEVEL (default: INFO, configurable via env var)
    - File handler at DEBUG level writing to LOG_FILE (default: app.log)
    """
    import os

    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_file = os.environ.get("LOG_FILE", "app.log")
    logger.remove()
    logger.add(sys.stderr, level=log_level)
    logger.add(log_file, level="DEBUG", rotation="50 KB", retention=1)


@logger.catch
def main():
    """Run the application."""
    configure_logging()
    parser = argparse.ArgumentParser(prog="second_brain")
    subparsers = parser.add_subparsers(dest="command")

    new_parser = subparsers.add_parser("new", help="Save a quick note as a markdown file")
    new_parser.add_argument("text", help="Note text to save")

    args = parser.parse_args()

    if args.command == "new":
        path = save_note(args.text)
        print(path)
    else:
        parser.print_help()
