from __future__ import annotations

from typing import Any, Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from aegis.composition import AppContainer, build_container
from aegis.contracts.base import TypedError
from aegis.domain.tools import validate_tool_call
from aegis.services.orchestrator import ProhibitedActionError, run_fixture_workflow

_container: AppContainer | None = None


def get_container() -> AppContainer:
    global _container
    if _container is None:
        _container = build_container()
    return _container


def create_app() -> FastAPI:
    app = FastAPI(
        title="AEGIS Evidence Orchestrator",
        version="0.2.0",
        description="Advisory evidence orchestration — no regulated execution.",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "aegis"}

    @app.get("/v1/ontology")
    def ontology() -> dict[str, Any]:
        c = get_container()
        span = c.telemetry.start_span("ontology.list")
        try:
            return c.graph.list_ontology()  # type: ignore[no-any-return]
        finally:
            c.telemetry.end_span(span)

    @app.get("/v1/graph")
    def graph(
        workflow: str = Query("batch"),
        focus_id: Optional[str] = Query(None),
    ) -> dict[str, Any]:
        c = get_container()
        span = c.telemetry.start_span(
            "graph.query",
            {"workflow": workflow, "focus_id": focus_id or ""},
        )
        try:
            return c.graph.query_subgraph(workflow, focus_id)  # type: ignore[no-any-return]
        finally:
            c.telemetry.end_span(span)

    @app.get("/v1/fixtures/{fixture_id}")
    def fixture(fixture_id: str) -> dict[str, Any]:
        c = get_container()
        try:
            return c.fixtures.load_fixture(fixture_id)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.post("/v1/workflows/run/{fixture_id}")
    def run_workflow(fixture_id: str, attempted_action: Optional[str] = None) -> dict[str, Any]:
        c = get_container()
        try:
            return run_fixture_workflow(c, fixture_id, attempted_action=attempted_action)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except ProhibitedActionError as exc:
            err = TypedError(
                code="PROHIBITED_ACTION",
                message=str(exc),
                details={"attempted_action": attempted_action},
                retryable=False,
            )
            raise HTTPException(status_code=403, detail=err.model_dump()) from exc

    @app.post("/v1/tools/validate", response_model=None)
    def tools_validate(payload: dict[str, Any]) -> dict[str, Any]:
        result = validate_tool_call(payload)
        if isinstance(result, TypedError):
            return result.model_dump()
        return {"ok": True, "tool": result.model_dump()}

    @app.get("/v1/workflows/sample")
    def sample_workflow() -> dict[str, Any]:
        c = get_container()
        return run_fixture_workflow(c, "PUB-01", request_id="REQ-SAMPLE")

    @app.exception_handler(ValidationError)
    async def validation_exception_handler(_request: Any, exc: ValidationError) -> Any:
        from fastapi.responses import JSONResponse

        err = TypedError(
            code="VALIDATION_ERROR",
            message="Request failed strict validation",
            details={"errors": exc.errors()},
            retryable=False,
        )
        return JSONResponse(status_code=422, content=err.model_dump())

    return app


app = create_app()
