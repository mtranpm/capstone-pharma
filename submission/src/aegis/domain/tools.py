from __future__ import annotations

from aegis.contracts.base import ToolCallArgs, TypedError
from aegis.domain.prohibited import is_prohibited
from pydantic import ValidationError


def validate_tool_call(payload: dict) -> ToolCallArgs | TypedError:
    try:
        args = ToolCallArgs.model_validate(payload)
    except ValidationError as exc:
        return TypedError(
            code="TOOL_ARGS_INVALID",
            message="Tool arguments failed strict validation",
            details={"errors": exc.errors()},
            retryable=False,
        )
    if is_prohibited(args.tool_name):
        return TypedError(
            code="PROHIBITED_ACTION",
            message=f"Tool '{args.tool_name}' is prohibited in advisory mode",
            details={"tool_name": args.tool_name},
            retryable=False,
        )
    return args
