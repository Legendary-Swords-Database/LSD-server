"""
Module for testing sword service
"""
import pytest

from services import SwordService
from schemas import SwordCreate
from models import SwordCondition, SwordValue, Sword


@pytest.fixture()
def service_sword(db_session) -> SwordService:
    """Return DocumentService."""
    return SwordService(db=db_session)


@pytest.fixture(scope="module")
def create_sword() -> SwordCreate:
    """Return create_schema_data for document."""
    return SwordCreate(
        type="Katana.",
        price=21421,
        condition=SwordCondition.NOT_BAD,
        value=SwordValue.B
    )


def test_create_sword(service_sword, create_sword) -> Sword:
    """
    Test for create method in SwordService
    """
    sword_in_db = service_sword.create(create_sword)
    assert sword_in_db is not None
    return sword_in_db
