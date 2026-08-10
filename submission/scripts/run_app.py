#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC))

import uvicorn


def main() -> None:
    uvicorn.run("aegis.api.app:app", host="127.0.0.1", port=8000, reload=False)


if __name__ == "__main__":
    main()
