"""User service module."""

from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext

from backend.app.config import get_settings
from backend.app.domain.user import UserEntity, UserRegister, UserResponse
from backend.app.repositories.user_repository import UserRepository
from di import register

settings = get_settings()


@register(dependencies=[UserRepository])
class UserService:
    """Service layer for user operations."""

    def __init__(self, user_repository: UserRepository) -> None:
        """Initialize the user service."""
        self.user_repository = user_repository
        self.pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(self, password: str) -> str:
        """Hash a password using bcrypt."""
        return self.pwd_cxt.hash(password)

    def verify(self, normal: str, hashed: str) -> bool:
        """Verify a password against a hash."""
        return self.pwd_cxt.verify(normal, hashed)

    def create_user(self, user: UserRegister) -> UserEntity:
        """Create a new user."""
        hashed_password = self.bcrypt(user.password)
        user_entity = UserEntity.model_validate(
            {**user.model_dump(), "password": hashed_password}
        )
        return self.user_repository.create(user_entity)

    def create_access_token(self, data: dict) -> str:
        """Create a JWT access token."""
        to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(minutes=settings.session_duration)
        to_encode.update({"exp": expire})
        return jwt.encode(
            to_encode, settings.secret_key, algorithm=settings.jwt_algorithm
        )

    def verify_token(self, token: str) -> dict | None:
        """Verify a JWT token and return its payload."""
        try:
            payload = jwt.decode(
                token, settings.secret_key, algorithms=[settings.jwt_algorithm]
            )
        except JWTError:
            return None
        username: str | None = payload.get("username")
        if username is None:
            return None
        return payload

    def get_users(self) -> list[UserResponse]:
        """Get all users."""
        users = self.user_repository.find(include_id=True)
        return [UserResponse(**user.model_dump()) for user in users]
