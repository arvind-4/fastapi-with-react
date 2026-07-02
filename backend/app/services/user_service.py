"""User service module."""

from datetime import (
    UTC,
    datetime,
    timedelta,
)

from jose import (
    JWTError,
    jwt,
)
from passlib.context import CryptContext

from backend.app.config import get_settings
from backend.app.domain.user import UserEntity, UserRegister
from backend.app.infrastructure.mongo_db.mongo_client import CustomMongoClient
from backend.app.repositories.user_repository import UserRepository
from di import register

settings = get_settings()

SECRET_KEY = settings.secret_key
ALGORITHM = settings.jwt_algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.session_duration


@register(dependencies=[UserRepository, CustomMongoClient])
class UserService:
    """Service layer for user operations."""

    def __init__(
        self, user_repository: UserRepository, mongo_client: "CustomMongoClient"
    ) -> None:
        """Initialize the user service."""
        self.user_repository = user_repository
        self.mongo_client = mongo_client
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
        expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def verify_token(self, token: str) -> dict | None:
        """Verify a JWT token and return its payload."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            return None
        username: str | None = payload.get("username")
        if username is None:
            return None
        return payload

    def get_users(self) -> list[UserEntity]:
        """Get all users."""
        return self.user_repository.find(include_id=True)
