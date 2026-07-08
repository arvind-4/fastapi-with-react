"""Main FastAPI application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.router import register_v1_api_routes
from di import load_all_deps


def create_app() -> FastAPI:
    """Entrypoint function for app."""
    load_all_deps()

    origins = ["*"]

    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    register_v1_api_routes(app=app)

    return app


app = create_app()
