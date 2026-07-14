from pathlib import Path

from backend.database.database import get_connection
from backend.models.document import Document


def search_documents(query: str) -> list[Document]:
    connection = get_connection()
    cursor = connection.cursor()

    search_pattern = f"%{query}%"

    cursor.execute(
        """
        SELECT
            path,
            extension,
            size,
            modified_time,
            content
        FROM documents
        WHERE
            path LIKE ?
            OR content LIKE ?
            OR extension LIKE ?
        """,
        (
            search_pattern,
            search_pattern,
            search_pattern,
        ),
    )

    rows = cursor.fetchall()

    documents: list[Document] = []

    for row in rows:
        documents.append(
            Document(
                path=Path(row[0]),
                extension=row[1],
                size=row[2],
                modified_time=row[3],
                content=row[4],
            )
        )

    connection.close()

    return documents