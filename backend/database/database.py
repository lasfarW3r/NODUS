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
            path TEXT NOT NULL,
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


if __name__ == "__main__":
    create_database()