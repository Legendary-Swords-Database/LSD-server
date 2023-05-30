"""DTO schemes for Sword entity."""
from pydantic import BaseModel
from uuid import UUID
from models import SwordCondition, SwordValue


class SwordBase(BaseModel):
    """Shared properties of Sword."""
    sword_typ: str | None = None
    sword_condition: SwordCondition | None = None
    sword_value: SwordValue | None = None
    price: int | None = None


class SwordCreate(SwordBase):
    """Properties to receive via API on creation."""
    sword_typ: str
    sword_condition: SwordCondition
    sword_value: SwordValue
    price: int


class SwordUpdate(SwordBase):
    """Properties to receive via API on update."""


class SwordInDBBase(SwordBase):
    """Base model for sword in database."""
    uuid: UUID
    uuid_insurance: UUID
    sword_type: str
    sword_condition: SwordCondition
    sword_value: SwordValue
    price: int | None = None
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