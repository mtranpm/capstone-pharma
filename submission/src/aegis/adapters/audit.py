from __future__ import annotations

from typing import Any
from uuid import uuid4


class InMemoryAuditAdapter:
    def __init__(self) -> None:
        self.events: list[dict[str, Any]] = []

    def emit(self, event: dict[str, Any]) -> str:
        event_id = event.get("event_id") or f"AUD-{uuid4().hex[:8]}"
        payload = {**event, "event_id": event_id}
        self.events.append(payload)
        return event_id
