"""DTO schemes for Sword entity."""
from pydantic import BaseModel
from uuid import UUID
from models import SwordCondition, SwordValue


class SwordBase(BaseModel):
    """Shared properties of Sword."""
    type: str | None = None
    price: int | None = None


class SwordCreate(SwordBase):
    """Properties to receive via API on creation."""
    type: str
    condition: SwordCondition
    value: SwordValue
    price: int


class SwordUpdate(SwordBase):
    """Properties to receive via API on update."""


class SwordInDBBase(SwordBase):
    """Base model for sword in database."""
    uuid: UUID
    uuid_insurance: UUID
    condition: SwordCondition
    value: SwordValue
    rented: bool
    on_sale: bool
    weight: int | None = None
    length: int | None = None

    class Config:  # pylint: disable=too-few-public-methods
        """Config class for database document model."""
        orm_mode = True


class Sword(SwordInDBBase):
    """Additional properties of document to return via API."""


class SwordInDB(SwordInDBBase):
    """Additional properties stored in DB"""
