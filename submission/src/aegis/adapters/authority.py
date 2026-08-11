from __future__ import annotations

from typing import Any


class StaticAuthorityAdapter:
    """Minimal authority classifier for scaffold; expanded in Phase 7."""

    UNTRUSTED = {"MALICIOUS_SUPPLIER_DEVIATION", "poisoned", "untrusted"}

    def classify_document(self, doc_id: str) -> dict[str, Any]:
        lowered = doc_id.lower()
        if any(u.lower() in lowered for u in self.UNTRUSTED):
            return {
                "doc_id": doc_id,
                "status": "untrusted",
                "usable_as_authority": False,
                "reason": "document marked untrusted or adversarial",
            }
        if "superseded" in lowered:
            return {
                "doc_id": doc_id,
                "status": "superseded",
                "usable_as_authority": False,
                "reason": "superseded — historical citation only",
            }
        return {
            "doc_id": doc_id,
            "status": "approved",
            "usable_as_authority": True,
            "reason": "default approved for synthetic training",
        }
