from __future__ import annotations

from pathlib import Path

from aegis.adapters.tool_manifest import FileToolManifestAdapter

ROOT = Path(__file__).resolve().parents[3]


def test_rejects_poisoned_manifest_name() -> None:
    adapter = FileToolManifestAdapter()
    poisoned = ROOT / "starter" / "api_samples" / "tool_manifest_poisoned.json"
    if poisoned.is_file():
        assert adapter.is_approved(str(poisoned)) is False


def test_accepts_approved_manifest_name() -> None:
    adapter = FileToolManifestAdapter()
    approved = ROOT / "starter" / "api_samples" / "tool_manifest_approved.json"
    if approved.is_file():
        assert adapter.is_approved(str(approved)) is True
