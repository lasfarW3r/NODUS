import sqlite3
from pathlib import Path

from backend.models.document import Document


def get_connection() -> sqlite3.Connection:
    database_path = Path("data/nodus.db")
    return sqlite3.connect(database_path)


def create_database() -> None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT NOT NULL UNIQUE,
            extension TEXT NOT NULL,
            size INTEGER NOT NULL,
            modified_time REAL NOT NULL,
            content TEXT NOT NULL
        );
    """)

    connection.commit()
    connection.close()


def save_document(document: Document) -> None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO documents (
            path,
            extension,
            size,
            modified_time,
            content
        )
        VALUES (?, ?, ?, ?, ?)

        ON CONFLICT(path) DO UPDATE SET
            size = excluded.size,
            modified_time = excluded.modified_time,
            content = excluded.content;
        """,
        (
            str(document.path),
            document.extension,
            document.size,
            document.modified_time,
            document.content,
        ),
    )

    connection.commit()
    connection.close()


def load_documents() -> list[Document]:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            path,
            extension,
            size,
            modified_time,
            content
        FROM documents
    """)

    rows = cursor.fetchall()

    documents: list[Document] = []

    for row in rows:
        document = Document(
            path=Path(row[0]),
            extension=row[1],
            size=row[2],
            modified_time=row[3],
            content=row[4],
        )

        documents.append(document)

    connection.close()

    return documents
def print_database() -> None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            path,
            extension,
            size,
            modified_time,
            content
        FROM documents
    """)

    rows = cursor.fetchall()

    print("\n===== DATABASE =====")

    for row in rows:
        print(row)

    print("====================\n")

    connection.close()



def delete_missing_documents(existing_paths: list[str]) -> None:
    connection = get_connection()
    cursor = connection.cursor()

    if not existing_paths:
        cursor.execute("DELETE FROM documents")
    else:
        placeholders = ",".join("?" for _ in existing_paths)

        cursor.execute(
            f"""
            DELETE FROM documents
            WHERE path NOT IN ({placeholders})
            """,
            existing_paths,
        )

    connection.commit()
    connection.close()
if __name__ == "__main__":
    create_database()