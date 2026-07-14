from pathlib import Path

from backend.database.database import create_database, load_documents, print_database
from backend.indexer.index import index_folder
from backend.search.engine import search_documents


def main():
    create_database()
    index_folder(Path("C:/NODUS/tests"))
   # print_database()

    documents = load_documents()

    query = input("Type your query: ")

    results = search_documents(query)

    for document in results:
        print(document.path)


if __name__ == "__main__":
    main()