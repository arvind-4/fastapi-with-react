"""API router registration."""

from fastapi import FastAPI

from backend.app.api.v1.user_endpoints import router as user_router_v1


def register_v1_api_routes(app: FastAPI) -> None:
    """Register v1 API routes on the FastAPI app."""
    app.include_router(user_router_v1, prefix="/api/v1")
