from pathlib import Path

from pypdf import PdfReader

from backend.models.document import Document


def parse_pdf(file: Path) -> Document:
    reader = PdfReader(file)

    content = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            content += text + "\n"

    return Document(
        path=file,
        extension=file.suffix,
        size=file.stat().st_size,
        modified_time=file.stat().st_mtime,
        content=content,
    )