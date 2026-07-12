from pathlib import Path

from backend.indexer.index import index_folder
from backend.search.engine import search_documents


def main():
    documents = index_folder(Path("C:/NODUS/tests"))

    query = input("Type your query: ")

    results = search_documents(query, documents)

    for document in results:
        print(document.path)


if __name__ == "__main__":
    main()