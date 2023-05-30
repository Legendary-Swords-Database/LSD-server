"""
This module defines the CRUD operations for the Sword model, including an
abstract base class (AbstractCRUDSword) and a concrete implementation (CRUDSword)
using SQLAlchemy.
"""
from abc import ABC, abstractmethod
from typing import Type
from uuid import UUID

from sqlalchemy.orm import Session

from crud import CRUDBase
from models import Sword, SwordCondition, SwordValue
from schemas import SwordCreate, SwordUpdate


class AbstractCRUDSword(CRUDBase[
                            Sword,
                            SwordCreate,
                            SwordUpdate
                        ], ABC):
    """
    Abstract class for CRUD operations specific to the Sword model.
    It extends the generic CRUDBase class and defines additional abstract methods
    for querying and manipulating Sword instances.
    """

    @abstractmethod
    def get_by_insurance_uuid(self, uuid_insurance: UUID) -> Sword | None:
        """
        Retrieves a Sword instance by its insurance UUID.

        :param uuid_insurance: The insurance UUID of the Sword.
        :return: The Sword instance if found, None otherwise.
        """

    @abstractmethod
    def get_by_type_all(self, sword_type: str) -> list[Type[Sword]]:
        """
        Retrieves all Sword instances with the given type.

        :param sword_type: The type of the Sword.
        :return: A list of Sword instances with the given type.
        """

    @abstractmethod
    def get_by_condition_all(self, sword_condition: SwordCondition) -> list[Type[Sword]]:
        """
        Retrieves all Sword instances with the given condition.

        :param sword_condition: The condition of the Sword.
        :return: A list of Sword instances with the given condition.
        """

    @abstractmethod
    def get_by_value_all(self, sword_value: SwordValue) -> list[Type[Sword]]:
        """
        Retrieves all Sword instances with the given value.

        :param sword_value: The value of the Sword.
        :return: A list of Sword instances with the given value.
        """

    @abstractmethod
    def get_by_rented_all(self, rented: bool) -> list[Type[Sword]]:
        """
        Retrieves all Sword instances which are rented or not.

        :param rented: Sword are rented or not.
        :return: A list of Sword instances which are rented or not.
        """

    @abstractmethod
    def get_by_on_sale_all(self, on_sale: bool) -> list[Type[Sword]]:
        """
        Retrieves all Sword instances which are on sale or not.

        :param on_sale: Sword are on sale or not.
        :return: A list of Sword instances which are on sale or not.
        """


class CRUDSword(AbstractCRUDSword):
    """
    Concrete class for CRUD operations specific to the Sword model.
    It extends the abstract AbstractCRUDSword class and implements the required methods
    for querying and manipulating Sword instances.
    """

    def __init__(self, db: Session):
        super().__init__(Sword, db)

    def get_by_insurance_uuid(self, uuid_insurance: UUID) -> Sword | None:
        return self.db.query(self.model) \
            .filter(self.model.uuid_insurance == uuid_insurance) \
            .first()

    def get_by_type_all(self, sword_type: str) -> list[Type[Sword]]:
        return self.db.query(self.model) \
            .filter(self.model.sword_type == sword_type) \
            .all()

    def get_by_condition_all(self, sword_condition: SwordCondition) -> list[Type[Sword]]:
        return self.db.query(self.model) \
            .filter(self.model.sword_condition == sword_condition) \
            .all()

    def get_by_value_all(self, sword_value: SwordValue) -> list[Type[Sword]]:
        return self.db.query(self.model) \
            .filter(self.model.sword_value == sword_value) \
            .all()

    def get_by_rented_all(self, rented: bool) -> list[Type[Sword]]:
        return self.db.query(self.model) \
            .filter(self.model.rented == rented) \
            .all()

    def get_by_on_sale_all(self, on_sale: bool) -> list[Type[Sword]]:
        return self.db.query(self.model) \
            .filter(self.model.on_sale == on_sale) \
            .all()
