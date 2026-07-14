from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".txt",
    ".py",
    ".cpp",
    ".c",
    ".md",
    ".json",
    ".pdf",
    ".docx",
    ".odt",
}


IGNORED_FILES = {
    ".git",
}


def scan_folder(folder: Path) -> list[Path]:
    files: list[Path] = []

    for file in folder.rglob("*"):

        if not file.is_file():
            continue

        # Ignore LibreOffice temporary lock files
        if file.name.startswith(".~lock"):
            continue

        # Ignore hidden files
        if file.name.startswith("."):
            continue

        # Ignore unsupported extensions
        if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        files.append(file)

    return files