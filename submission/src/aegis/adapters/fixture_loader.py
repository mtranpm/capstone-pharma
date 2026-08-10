from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class FileFixtureAdapter:
    """Load evaluation public fixtures from the challenge package (read-only)."""

    def __init__(self, fixtures_dir: Path) -> None:
        self._fixtures_dir = fixtures_dir

    def load_fixture(self, fixture_id: str) -> dict[str, Any]:
        path = self._fixtures_dir / f"{fixture_id}.json"
        if not path.is_file():
            raise FileNotFoundError(f"fixture not found: {fixture_id}")
        return json.loads(path.read_text(encoding="utf-8"))
