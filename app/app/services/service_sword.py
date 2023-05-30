"""
This module defines an abstract base class AbstractSwordService
and SwordService that work with Sword
"""
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Type, Annotated
from fastapi import Depends

from services import CrudServiceBase
from models import Sword, SwordCondition, SwordValue
from crud import CRUDSword
from schemas import SwordCreate, SwordUpdate
from db import get_db

from sqlalchemy.orm import Session


class AbstractSwordService(CrudServiceBase[
                                  Sword,
                                  CRUDSword,
                                  SwordCreate,
                                  SwordUpdate
                              ], ABC):
    """
    This abstract class defines the interface for a sword service
    that provides CRUD operations for a specific SwordModel.
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


class SwordService(AbstractSwordService):
    """
    Class SwordService represent service that work with Sword
    """

    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        super().__init__(CRUDSword(db))

    def get_by_insurance_uuid(self, uuid_insurance: UUID) -> Sword | None:
        return self.crud.get_by_insurance_uuid(uuid_insurance)

    def get_by_type_all(self, sword_type: str) -> list[Type[Sword]]:
        return self.crud.get_by_type_all(sword_type)

    def get_by_condition_all(self, sword_condition: SwordCondition) -> list[Type[Sword]]:
        return self.crud.get_by_condition_all(sword_condition)

    def get_by_value_all(self, sword_value: SwordValue) -> list[Type[Sword]]:
        return self.crud.get_by_value_all(sword_value)

    def get_by_rented_all(self, rented: bool) -> list[Type[Sword]]:
        return self.crud.get_by_rented_all(rented)

    def get_by_on_sale_all(self, on_sale: bool) -> list[Type[Sword]]:
        return self.crud.get_by_on_sale_all(on_sale)
