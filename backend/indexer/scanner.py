from pathlib import Path


def scan_folder(folder: Path) -> list[Path]:
    """
    Recursively scan a directory and return all files.
    """

    if not folder.is_dir():
        raise FileNotFoundError(
            f"'{folder}' is not a valid directory."
        )

    files: list[Path] = []

    for file in folder.rglob("*"):
        if file.is_file():
            files.append(file)

    return files


if __name__ == "__main__":
    files = scan_folder(Path("C:/NODUS/tests"))

    for file in files:
        print(file)