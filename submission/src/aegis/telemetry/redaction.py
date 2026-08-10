from __future__ import annotations

from typing import Any

FORBIDDEN_KEYS = {
    "password",
    "api_key",
    "apikey",
    "secret",
    "authorization_header",
    "system_prompt",
    "raw_narrative",
    "pregnancy",
    "ssn",
    "connection_string",
}


def redact_attributes(attributes: dict[str, Any] | None) -> dict[str, Any]:
    if not attributes:
        return {}
    clean: dict[str, Any] = {}
    for key, value in attributes.items():
        lowered = key.lower()
        if lowered in FORBIDDEN_KEYS or any(f in lowered for f in ("password", "secret", "prompt")):
            continue
        clean[key] = value
    return clean
