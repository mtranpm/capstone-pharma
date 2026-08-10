from __future__ import annotations

import time
from typing import Any, Callable, Optional, TypeVar

import httpx
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class TypedHttpClient:
    """HTTP client with retries/backoff and Pydantic response validation."""

    def __init__(
        self,
        base_url: str,
        *,
        max_attempts: int = 3,
        base_delay_s: float = 0.05,
        transport: Optional[httpx.BaseTransport] = None,
    ) -> None:
        self._base_url = base_url.rstrip("/")
        self._max_attempts = max_attempts
        self._base_delay_s = base_delay_s
        self._client = httpx.Client(base_url=self._base_url, transport=transport, timeout=30.0)

    def close(self) -> None:
        self._client.close()

    def get_model(self, path: str, model: type[T], *, retryable: Callable[[httpx.Response], bool] | None = None) -> T:
        last_exc: Exception | None = None
        for attempt in range(1, self._max_attempts + 1):
            try:
                response = self._client.get(path)
                if response.status_code >= 500 or (retryable and retryable(response)):
                    raise httpx.HTTPStatusError(
                        "retryable status",
                        request=response.request,
                        response=response,
                    )
                response.raise_for_status()
                return model.model_validate(response.json())
            except (httpx.TransportError, httpx.HTTPStatusError) as exc:
                last_exc = exc
                if attempt >= self._max_attempts:
                    break
                time.sleep(self._base_delay_s * (2 ** (attempt - 1)))
        assert last_exc is not None
        raise last_exc

    def get_json(self, path: str) -> dict[str, Any]:
        response = self._client.get(path)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, dict):
            raise TypeError("expected JSON object")
        return data
