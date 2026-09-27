from __future__ import annotations

import json
from pathlib import Path

DEFAULTS = {
    "font_family": "JetBrains Mono",
    "font_size": 12,
    "shell": "/bin/bash",
    "history_lines": 10000,
    "working_directory": "~",
}


class Config:
    def __init__(self) -> None:
        self.directory = Path.home() / ".config" / "calyx-terminal"
        self.path = self.directory / "config.json"
        self.data = DEFAULTS.copy()
        self.load()

    def load(self) -> None:
        try:
            loaded = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                self.data.update(loaded)
        except (FileNotFoundError, OSError, ValueError):
            pass

    def save(self) -> None:
        self.directory.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.data, indent=2) + "\n", encoding="utf-8")

    def __getitem__(self, key: str):
        return self.data[key]
