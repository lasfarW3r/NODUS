from pathlib import Path

from backend.models.document import Document
from backend.parser.text_parser import parse_text_file


def parse(file: Path) -> Document:
    """
    Dispatch the file to the appropriate parser.
    """

    if file.suffix.lower() == ".txt":
        return parse_text_file(file)

    raise ValueError(
        f"No parser available for '{file.suffix}' files."
    )