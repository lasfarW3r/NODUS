def scan_folder(folder: Path) -> list[Path]:

    if not folder.is_dir():
        raise FileNotFoundError(...)

    files = []

    for file in folder.rglob("*"):
        if file.is_file():
            files.append(file)

    return files