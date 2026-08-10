from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional
from uuid import uuid4

from aegis.telemetry.redaction import redact_attributes


@dataclass
class _Span:
    name: str
    attributes: dict[str, Any] = field(default_factory=dict)
    span_id: str = field(default_factory=lambda: uuid4().hex[:16])
    status: str = "ok"


class ConsoleTelemetryAdapter:
    """Offline TelemetryPort — records spans in memory and prints compact lines."""

    def __init__(self) -> None:
        self.spans: list[_Span] = []

    def start_span(self, name: str, attributes: Optional[dict[str, Any]] = None) -> _Span:
        span = _Span(name=name, attributes=redact_attributes(attributes))
        self.spans.append(span)
        print(f"[otel] start span={span.name} id={span.span_id} attrs={span.attributes}")
        return span

    def end_span(self, span: Any, *, status: str = "ok") -> None:
        if isinstance(span, _Span):
            span.status = status
            print(f"[otel] end span={span.name} id={span.span_id} status={status}")

    def counter(self, name: str, value: int = 1, attributes: Optional[dict[str, Any]] = None) -> None:
        attrs = redact_attributes(attributes)
        print(f"[otel] counter={name} value={value} attrs={attrs}")
