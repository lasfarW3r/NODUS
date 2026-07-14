from pathlib import Path

from backend.models.document import Document
from backend.parser.text_parser import parse_text
from backend.parser.pdf_parser import parse_pdf
from backend.parser.docx_parser import parse_docx
from backend.parser.odt_parser import parse_odt


TEXT_EXTENSIONS = {
    ".txt",
    ".py",
    ".cpp",
    ".c",
    ".md",
    ".json",  
}


def parse(file: Path) -> Document:
    extension = file.suffix.lower()

    if extension in TEXT_EXTENSIONS:
        return parse_text(file)

    if extension == ".pdf":
        return parse_pdf(file)

    if extension == ".docx":
        return parse_docx(file)
    if extension == ".odt":
        return parse_odt(file)

    raise ValueError(f"Unsupported file type: {extension}")