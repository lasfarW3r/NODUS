from pathlib import Path

from backend.indexer.scanner import scan_folder
from backend.models.document import Document
from backend.parser.parser import parse


def index_folder(folder: Path) -> list[Document]:
    """
    Scan a folder and parse all supported files.
    """

    files = scan_folder(folder)
    documents: list[Document] = []

    for file in files:
        try:
            document = parse(file)
            documents.append(document)
        except ValueError:
            # Unsupported file type, skip it
            pass

    return documents


if __name__ == "__main__":
    documents = index_folder(Path("C:/NODUS/tests"))

    for document in documents:
        print(document)