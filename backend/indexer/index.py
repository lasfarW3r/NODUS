from pathlib import Path

from backend.indexer.scanner import scan_folder
from backend.models.document import Document
from backend.parser.text_parser import parse_text_file


def index_folder(folder: Path) -> list[Document]:
    files = scan_folder(folder)
    documents: list[Document] = []

    for file in files:
        if file.suffix.lower() == ".txt":
            document = parse_text_file(file)
            documents.append(document)

    return documents
if __name__ == "__main__":
    documents = index_folder(Path("C:/NODUS/tests"))

    for document in documents:
        print(document)