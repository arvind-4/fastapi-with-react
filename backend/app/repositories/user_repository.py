"""User repository module."""

from typing import Any

from backend.app.domain.user import UserEntity
from backend.app.infrastructure.mongo_db.mongo_client import CustomMongoClient
from backend.app.repositories.base import BaseRepository
from di import register


@register(dependencies=[CustomMongoClient])
class UserRepository(BaseRepository):
    """Repository for user CRUD operations."""

    collection_name = "users"

    def to_domain(self, json: dict[str, Any]) -> UserEntity:
        """Convert a MongoDB document to a UserEntity."""
        return UserEntity(**json)

    def create(self, user: UserEntity) -> UserEntity:
        """Create a new user in the database."""
        user_dict = user.model_dump()
        user_id = self.session.insert_one(user_dict).inserted_id
        if user_id is None:
            msg = "Failed to retrieve created user"
            raise RuntimeError(msg)
        return self.to_domain({**user_dict, "user_id": user_id})

    def find(self, include_id: bool | None = None) -> list[UserEntity]:
        """Find all users, optionally including the _id field."""
        projection = {} if include_id else {"_id": 0}
        users = self.session.find({}, projection)
        return [UserEntity(**user) for user in users]
