from pathlib import Path

from backend.indexer.scanner import scan_folder
from backend.models.document import Document
from backend.parser.parser import parse
from backend.database.database import save_document, delete_missing_documents


def index_folder(folder: Path) -> list[Document]:
    files = scan_folder(folder)
    file_paths = [str(file) for file in files]

    documents: list[Document] = []

    for file in files:
        try:
            document = parse(file)
            documents.append(document)
            save_document(document)

        except Exception as error:
            print(f"Failed to index {file}: {error}")

    delete_missing_documents(file_paths)

    return documents