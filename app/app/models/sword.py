"""
Module which includes Sword ORM model and its dependencies.
"""
from uuid import uuid4
from enum import Enum
from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from db.base_class import Base


class SwordCondition(Enum):
    """
    Condition of the sword.

    it says here all the condition that swords can be
    """
    FALLING_APART = "falling apart"
    SHABBY = "shabby"
    NOT_BAD = "not bad"
    GOOD = "good"
    VERY_WORN_OUT = "very worn out"
    EXCELLENT = "excellent"


class SwordValue(Enum):
    """
    Value of the sword.

    it says here all the value that swords can be
    """
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


class Sword(Base):
    """
    Used to create and manipulate sword entity in the database.
    """
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    uuid_insurance = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid4)
    sword_type = Column(String, nullable=False)
    sword_condition = Column(SQLEnum(SwordCondition, name="sword_condition"), nullable=False)
    sword_value = Column(SQLEnum(SwordValue, name="sword_value"), nullable=False)
    price = Column(Integer, nullable=False, default=0)
    rented = Column(Boolean, nullable=False, default=False)
    on_sale = Column(Boolean, nullable=False, default=False)
    weight = Column(Integer, nullable=True)
    length = Column(Integer, nullable=True)
