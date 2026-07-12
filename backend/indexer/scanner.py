from pathlib import Path

def scan_folder(folder: Path) -> list[Path]:

    if not folder.is_dir():
        raise FileNotFoundError(
            f"'{folder}' is not a valid directory."
        )

    files = []

    for file in folder.rglob("*"):
        if file.is_file():
            files.append(file)

    return files


files = scan_folder(Path("C:/NODUS/tests"))

for file in files:
    print(file)