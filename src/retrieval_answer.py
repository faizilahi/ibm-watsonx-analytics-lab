from pathlib import Path

def retrieve(path: Path) -> int:
    return int(path.read_text(encoding="utf-8").strip())
