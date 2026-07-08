"""MongoDB client module."""

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from backend.app.config import get_settings
from di import register

settings = get_settings()


@register(dependencies=[])
class CustomMongoClient:
    """Custom MongoDB client wrapper."""

    def __init__(self) -> None:
        """Initialize the MongoDB client wrapper."""
        self._client: MongoClient | None = None

    def get_db(self) -> Database:
        """Get the Auth database, connecting if necessary."""
        if self._client is None:
            self._client = MongoClient(settings.mongo_uri)
        return self._client["Auth"]

    def get_collection(self, collection_name: str) -> Collection:
        """Get a collection from the Auth database."""
        return self.get_db()[collection_name]
