"""DTO schemes for Person entity."""
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class PersonBase(BaseModel):
    """Shared properties of Person."""
    name: str | None = None
    surname: str | None = None


class PersonCreate(PersonBase):
    """Properties to receive via API on creation."""
    name: str
    surname: str


class PersonUpdate(PersonBase):
    """Properties to receive via API on update."""


class PersonInDBBase(PersonBase):
    """Base model for person in database."""
    uuid: UUID
    document_number: UUID

    class Config:  # pylint: disable=too-few-public-methods
        """Config class for database person model."""
        orm_mode = True


class Person(PersonInDBBase):
    """Additional properties of person to return via API."""


class PersonInDb(PersonInDBBase):
    """Additional properties stored in DB"""
