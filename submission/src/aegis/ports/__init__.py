from __future__ import annotations

from typing import Any, Optional, Protocol, runtime_checkable


@runtime_checkable
class FixturePort(Protocol):
    def load_fixture(self, fixture_id: str) -> dict[str, Any]: ...


@runtime_checkable
class AuthorityPort(Protocol):
    def classify_document(self, doc_id: str) -> dict[str, Any]: ...


@runtime_checkable
class GraphPort(Protocol):
    def query_subgraph(self, workflow: str, focus_id: Optional[str] = None) -> dict[str, Any]: ...

    def list_ontology(self) -> dict[str, Any]: ...


@runtime_checkable
class AuditPort(Protocol):
    def emit(self, event: dict[str, Any]) -> str: ...


@runtime_checkable
class TelemetryPort(Protocol):
    def start_span(self, name: str, attributes: Optional[dict[str, Any]] = None) -> Any: ...

    def end_span(self, span: Any, *, status: str = "ok") -> None: ...

    def counter(self, name: str, value: int = 1, attributes: Optional[dict[str, Any]] = None) -> None: ...


@runtime_checkable
class ToolManifestPort(Protocol):
    def is_approved(self, manifest_path: str) -> bool: ...


@runtime_checkable
class LlmPort(Protocol):
    def complete(self, prompt: str, *, system: str | None = None) -> str: ...
