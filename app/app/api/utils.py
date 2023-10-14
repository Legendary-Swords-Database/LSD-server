"""Utils for API."""
from enum import Enum
from uuid import UUID

from fastapi import status, Request, responses
from pydantic import BaseModel


class Message(BaseModel):
    """Model for response message."""
    message: str


class Entity(Enum):
    """Enum for entity names."""
    SWORD = "Sword"
    PERSON = 'Person'


# pylint: disable=unused-argument
# reason: Exception handlers require request and exception parameter.

def get_exception_response_detail(status_code: int, desc: str) -> dict:
    """Get exception response detail for openAPI documentation.

    :param status_code: Status code of the exception.
    :param desc: Description of the exception.
    :return dict: Exception response detail.
    """
    return {
        status_code: {
            "model": Message,
            "description": desc
        }
    }


class MethodNotAllowedException(Exception):
    """Exception for not allowed methods."""
    STATUS_CODE = status.HTTP_405_METHOD_NOT_ALLOWED
    DESCRIPTION = "Method not allowed."
    RESPONSE = get_exception_response_detail(STATUS_CODE, DESCRIPTION)

    def __init__(self, entity: Entity):
        self.entity = entity


def method_not_allowed_exception_handler(
        request: Request, exc: MethodNotAllowedException
) -> responses.JSONResponse:
    """Exception handler for MethodNotAllowedException.

    :param request: Request that caused the exception.
    :param exc: The exception.
    """
    return responses.JSONResponse(
        status_code=exc.STATUS_CODE,
        content={
            "message": f"Method {request.method} is not allowed for entity {exc.entity.value}"
        },
    )


class EntityNotFoundException(Exception):
    """Exception for when entity is not found in database."""
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DESCRIPTION = "Entity not found."
    RESPONSE = get_exception_response_detail(STATUS_CODE, DESCRIPTION)

    def __init__(self, entity: Entity, entity_uuid: UUID):
        self.entity = entity
        self.entity_uuid = entity_uuid


def entity_not_found_exception_handler(
        request: Request, exc: EntityNotFoundException
) -> responses.JSONResponse:
    """Exception handler for EntityNotFoundException.

    :param request: Request that caused the exception.
    :param exc: The exception.
    """
    return responses.JSONResponse(
        status_code=exc.STATUS_CODE,
        content={
            "message": f"Entity {exc.entity.value} with uuid {exc.entity_uuid} was not found."
        },
    )


class NotImplementedException(Exception):
    """Exception for when a functionality is not yet implemented."""
    STATUS_CODE = status.HTTP_501_NOT_IMPLEMENTED
    DESCRIPTION = "Method not implemented."
    RESPONSE = get_exception_response_detail(STATUS_CODE, DESCRIPTION)


def not_implemented_exception_handler(
        request: Request, exc: NotImplementedException
) -> responses.JSONResponse:
    """Exception handler for NotImplementedException.

    :param request: Request that caused the exception.
    :param exc: The exception.
    """
    return responses.JSONResponse(
        status_code=exc.STATUS_CODE,
        content={
            "message": exc.DESCRIPTION
        },
    )

# pylint: enable=unused-argument


# pylint: disable=too-few-public-methods
# reason: no more public methods needed.
class FastApiDocs:
    """Information for fastapi documentation."""
    NAME = "Legendary Swords Database"
    DESCRIPTION = """Legendary Swords Database API is a **REST API** that offers you an access to
    our application's swords and more!"""
    VERSION = "1.0.0"
    SWORD_TAG = {
        "name": "swords",
        "description": "Operations with swords.",
    }
    PERSON_TAG = {
        "name": "persons",
        "description": "Operations with persons.",
    }

    def get_tags_metadata(self):
        """Get tags metadata."""
        return [
            self.SWORD_TAG,
            self.PERSON_TAG
        ]


fastapi_docs = FastApiDocs()

# pylint: enable=too-few-public-methods
