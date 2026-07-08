"""User domain models."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from backend.app.repositories.base import PyObjectId


class UserEntity(BaseModel):
    """Domain entity representing a user."""

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
    user_id: PyObjectId | None = Field(default=None, alias="_id")
    email: EmailStr
    password: str
    avatar: str | None = None
    is_super_user: bool = False
    is_active: bool = True
    updated_at: datetime | None = None
    created_at: datetime | None = None


class UserRegister(BaseModel):
    """Schema for user registration requests."""

    username: str
    password: str
    email: EmailStr
    avatar: str | None = None
    is_super_user: bool = False
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class UserLogin(BaseModel):
    """Schema for user login requests."""

    username: str
    password: str


class UserResponse(BaseModel):
    """User response schema."""

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
    user_id: PyObjectId | None = None
    email: EmailStr
    avatar: str | None = None
    is_super_user: bool = False
    is_active: bool = True
    updated_at: datetime | None = None
    created_at: datetime | None = None
