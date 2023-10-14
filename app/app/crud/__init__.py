"""
Package for CRUD repositories for each domain type, used to handle
operations over database.
"""
from .crud_base import AbstractCRUDBase, CRUDBase
from .crud_sword import AbstractCRUDSword, CRUDSword
from .crud_person import AbstractCRUDPerson, CRUDPerson

__all__ = [
    'AbstractCRUDBase', 'CRUDBase',
    'AbstractCRUDSword', 'CRUDSword',
    'AbstractCRUDPerson', 'CRUDPerson'
]