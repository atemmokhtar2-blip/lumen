import os
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field

from templates import get_awareness_template

APP_NAME = os.getenv("APP_NAME", "DAF Defensive Awareness Framework")
app = FastAPI(title=APP_NAME, version="1.0.0", docs_url="/docs", redoc_url=None)


class HealthResponse(BaseModel):
    status: str
    mode: str


class DisabledAction(BaseModel):
    action: str = Field(min_length=1, max_length=100)
    reason: str


@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; style-src 'self' 'unsafe-inline'; "
        "script-src 'self'; img-src 'self' data:; connect-src 'none'; "
        "frame-ancestors 'none'; base-uri 'none'; form-action 'none'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = (
        "camera=(), microphone=(), geolocation=(), display-capture=(), "
        "clipboard-read=(), clipboard-write=()"
    )
    return response


@app.get("/", response_class=HTMLResponse)
async def index() -> str:
    return get_awareness_template(APP_NAME)


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok", mode="defensive-awareness")


@app.get("/api/v1/capabilities")
async def capabilities() -> dict[str, Any]:
    return {
        "mode": "defensive-awareness",
        "collection": False,
        "remote_control": False,
        "browser_media_access": False,
        "available": ["security-awareness-page", "safe-health-check"],
    }


@app.api_route("/api/v1/{path:path}", methods=["POST", "PUT", "PATCH", "DELETE"])
async def reject_sensitive_api(path: str) -> JSONResponse:
    payload = DisabledAction(
        action=path,
        reason="DAF defensive mode does not collect telemetry or execute remote commands.",
    )
    return JSONResponse(status_code=410, content=payload.model_dump())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
