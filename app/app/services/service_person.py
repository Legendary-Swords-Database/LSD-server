"""
This module defines an abstract base class AbstractPersonService
and PersonService that work with Person
"""
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Type, Annotated
from fastapi import Depends

from services import CrudServiceBase
from models import Person
from crud import CRUDPerson
from schemas import PersonCreate, PersonUpdate
from db import get_db

from sqlalchemy.orm import Session


class AbstractPersonService(CrudServiceBase[
                                Person,
                                CRUDPerson,
                                PersonCreate,
                                PersonUpdate
                            ], ABC):
    """
    This abstract class defines the interface for a person service
    that provides CRUD operations for a specific PersonModel.
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


class PersonService(AbstractPersonService):
    """
    Class DocumentService represent service that work with Document
    """

    def __init__(self, db: Annotated[Session, Depends(get_db)]):
        super().__init__(CRUDPerson(db))

    def get_by_document_number(self, document_number: UUID) -> Person | None:
        return self.crud.get_by_document_number(document_number)

    def get_by_name_all(self, person_name: str) -> list[Type[Person]]:
        return self.crud.get_by_name_all(person_name)

    def get_by_surname_all(self, person_surname: str) -> list[Type[Person]]:
        return self.crud.get_by_surname_all(person_surname)
