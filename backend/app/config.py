"""Application configuration."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        extra="ignore",
    )

    secret_key: str = Field(
        default_factory=str,
        validation_alias="SECRET_KEY",
    )

    jwt_algorithm: str = Field(
        default="HS256",
        validation_alias="JWT_ALGORITHM",
    )

    session_duration: int = Field(
        default=86400,
        validation_alias="SESSION_DURATION",
    )

    mongo_uri: str = Field(
        default_factory=str,
        validation_alias="MONGO_URI",
    )


@lru_cache
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()
