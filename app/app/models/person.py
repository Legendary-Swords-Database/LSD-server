"""
Module which includes Person ORM model and its dependencies.
"""
from uuid import uuid4
from datetime import datetime
from enum import Enum
from sqlalchemy import Column, String, DateTime
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from db.base_class import Base


class Person(Base):
    """
    Used to create and manipulate person entity in the database.
    """
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    document_number = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
