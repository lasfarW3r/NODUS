from pathlib import Path

from backend.models.document import Document


def parse_text_file(file: Path) -> Document:
    """
    Parse a .txt file into a Document.
    """

    if not file.is_file():
        raise FileNotFoundError(
            f"'{file}' is not a valid file."
        )

    if file.suffix.lower() != ".txt":
        raise ValueError(
            f"Expected a .txt file, got '{file.suffix}'."
        )

    return Document(
        path=file,
        extension=file.suffix,
        content=file.read_text(encoding="utf-8"),
    )


if __name__ == "__main__":
    document = parse_text_file(Path("C:/NODUS/tests/test.txt"))

    print(document)