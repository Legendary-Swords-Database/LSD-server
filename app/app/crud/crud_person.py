"""
This module defines the CRUD operations for the Person model, including an
abstract base class (AbstractCRUDPerson) and a concrete implementation (CRUDPerson)
using SQLAlchemy.
"""
from abc import ABC, abstractmethod
from typing import Type
from uuid import UUID

from sqlalchemy.orm import Session

from crud import CRUDBase
from models import Person
from schemas import PersonCreate, PersonUpdate


class AbstractCRUDPerson(CRUDBase[
                             Person,
                             PersonCreate,
                             PersonUpdate
                         ], ABC):
    """
    Abstract class for CRUD operations specific to the Person model.
    It extends the generic CRUDBase class and defines additional abstract methods
    for querying and manipulating Person instances.
    """

    @abstractmethod
    def get_by_document_number(self, document_number: UUID) -> Person | None:
        """
        Retrieves a Person instance by its document number.

        :param document_number: The document number of the Person.
        :return: The Person instance if found, None otherwise.
        """

    @abstractmethod
    def get_by_name_all(self, person_name: str) -> list[Type[Person]]:
        """
        Retrieves all Sword instances with the given name.

        :param person_name: The name of the Person.
        :return: A list of Sword instances with the given name.
        """

    @abstractmethod
    def get_by_surname_all(self, person_surname: str) -> list[Type[Person]]:
        """
        Retrieves all Sword instances with the given surname.

        :param person_surname: The surname of the Sword.
        :return: A list of Sword instances with the given surname.
        """


class CRUDPerson(AbstractCRUDPerson):
    """
    Concrete class for CRUD operations specific to the Person model.
    It extends the abstract AbstractCRUDDocument class and implements the required methods
    for querying and manipulating Person instances.
    """

    def __init__(self, db: Session):
        super().__init__(Person, db)

    def get_by_document_number(self, document_number: UUID) -> Person | None:
        return self.db.query(self.model) \
            .filter(self.model.document_number == document_number) \
            .first()

    def get_by_name_all(self, person_name: str) -> list[Type[Person]]:
        return self.db.query(self.model) \
            .filter(self.model.name == person_name) \
            .all()

    @abstractmethod
    def get_by_surname_all(self, person_surname: str) -> list[Type[Person]]:
        return self.db.query(self.model) \
            .filter(self.model.surname == person_surname) \
            .all()
