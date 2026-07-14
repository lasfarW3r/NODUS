from pathlib import Path

from odf.opendocument import load
from odf.text import P

from backend.models.document import Document


def parse_odt(file: Path) -> Document:
    doc = load(file)

    content = ""

    for paragraph in doc.getElementsByType(P):
        content += str(paragraph) + "\n"

    return Document(
        path=file,
        extension=file.suffix,
        size=file.stat().st_size,
        modified_time=file.stat().st_mtime,
        content=content,
    )