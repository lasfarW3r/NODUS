from dataclasses import dataclass
from pathlib import Path


@dataclass
class Document:
    path: Path
    extension: str
    size: int
    modified_time: float
    content: str

    @property
    def name(self) -> str:
        return self.path.name

    @property
    def word_count(self) -> int:
        return len(self.content.split())