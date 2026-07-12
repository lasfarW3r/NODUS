import sqlite3
from pathlib import Path


def create_database() -> None:
    database_path = Path("data/nodus.db")

    connection = sqlite3.connect(database_path)

    connection.close()


if __name__ == "__main__":
    create_database()