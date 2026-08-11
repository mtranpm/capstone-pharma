from __future__ import annotations

import json
from pathlib import Path


class FileToolManifestAdapter:
    def is_approved(self, manifest_path: str) -> bool:
        path = Path(manifest_path)
        if not path.is_file():
            return False
        name = path.name.lower()
        if "poisoned" in name:
            return False
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return False
        if data.get("status") == "poisoned" or data.get("trusted") is False:
            return False
        if "approved" in name:
            return True
        return bool(data.get("approved", False) or data.get("status") == "approved")
