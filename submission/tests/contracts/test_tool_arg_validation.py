from __future__ import annotations

from aegis.contracts.base import TypedError
from aegis.domain.tools import validate_tool_call


def test_valid_tool_args() -> None:
    result = validate_tool_call({"tool_name": "summarize_evidence", "arguments": {"batch_id": "X"}})
    assert not isinstance(result, TypedError)
    assert result.tool_name == "summarize_evidence"


def test_prohibited_tool_returns_typed_error() -> None:
    result = validate_tool_call({"tool_name": "release_batch", "arguments": {}})
    assert isinstance(result, TypedError)
    assert result.code == "PROHIBITED_ACTION"


def test_invalid_payload_typed_error() -> None:
    result = validate_tool_call({"arguments": {}})  # missing tool_name
    assert isinstance(result, TypedError)
    assert result.code == "TOOL_ARGS_INVALID"
