"""Base repository module."""

from abc import ABC

from bson import ObjectId
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema

from backend.app.infrastructure.mongo_db.mongo_client import CustomMongoClient


class BaseRepository(ABC):
    """Abstract base class for MongoDB repositories."""

    collection_name: str

    def __init__(self, mongo_client: CustomMongoClient) -> None:
        """Initialize with a MongoDB client and bind to the configured collection."""
        if not getattr(self, "collection_name", None):
            msg = f"{type(self).__name__} must define collection_name"
            raise TypeError(msg)
        self.session = mongo_client.get_collection(self.collection_name)


class PyObjectId(ObjectId):
    """MongoDB ObjectId type for Pydantic models."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: type,
        handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        """Get the Pydantic core schema for ObjectId."""
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(ObjectId),
                    core_schema.chain_schema(
                        [
                            core_schema.str_schema(),
                            core_schema.no_info_plain_validator_function(cls.validate),
                        ]
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                str, when_used="json"
            ),
        )

    @classmethod
    def validate(cls, value: str) -> ObjectId:
        """Validate that a string is a valid ObjectId."""
        if not ObjectId.is_valid(value):
            msg = f"Invalid ObjectId: {value}"
            raise ValueError(msg)
        return ObjectId(value)

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        schema: core_schema.CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        """Get the JSON schema for ObjectId."""
        return {"type": "string"}
