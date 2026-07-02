"""User API endpoints for v1."""

from fastapi import (
    APIRouter,
)

from backend.app.domain.user import (
    UserRegister,
)
from backend.app.services.user_service import UserService
from di import inject

router = APIRouter(prefix="/users")


@router.post("/register")
@inject(user_service=UserService)
def create_user(payload: UserRegister, user_service: UserService) -> dict[str, str]:
    """Register a new user."""
    user_service.create_user(payload)
    return {"message": "User created"}


@router.get("")
@inject(user_service=UserService)
def get_all_users(user_service: UserService) -> dict[str, list]:
    """Get all registered users."""
    users = user_service.get_users()
    return {"users": users}
