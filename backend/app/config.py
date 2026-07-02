"""Application configuration."""

from functools import lru_cache
from typing import TypedDict, Unpack

from pydantic_settings import BaseSettings, SettingsConfigDict


class _SettingsKwargs(TypedDict, total=False):
    secret_key: str
    jwt_algorithm: str
    session_duration: int
    mongo_uri: str


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(extra="ignore")

    secret_key: str
    jwt_algorithm: str = "HS256"
    session_duration: int = 86400
    mongo_uri: str

    def __init__(self, **kwargs: Unpack[_SettingsKwargs]) -> None:
        """Values are loaded from environment variables by BaseSettings."""
        super().__init__(**kwargs)


@lru_cache
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()
