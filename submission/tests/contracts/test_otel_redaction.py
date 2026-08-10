from __future__ import annotations

from aegis.telemetry.redaction import redact_attributes


def test_redacts_forbidden_keys() -> None:
    clean = redact_attributes(
        {
            "request_id": "R1",
            "password": "x",
            "api_key": "y",
            "system_prompt": "secret",
            "workflow": "batch",
        }
    )
    assert clean == {"request_id": "R1", "workflow": "batch"}


def test_redacts_substring_secret() -> None:
    clean = redact_attributes({"my_secret_token": "abc", "batch_id": "B1"})
    assert "my_secret_token" not in clean
    assert clean["batch_id"] == "B1"
