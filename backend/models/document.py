from dataclasses import dataclass
from pathlib import Path

@dataclass
class Document:
    path: Path
    extension: str
    size: int
    modified_time: float
    content: str
    
