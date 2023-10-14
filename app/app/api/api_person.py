"""
API controllers for person.
"""
from uuid import UUID
from fastapi import APIRouter, status, Depends, Path, Body, responses
from typing import List, Any, Annotated

from api import utils
from schemas import Person, PersonCreate, PersonUpdate
from services import PersonService

router = APIRouter(
    prefix='/person',
    tags=[utils.fastapi_docs.SWORD_TAG['name']]
)


@router.post("/",
             response_model=Person,
             responses={
                 400: {"model": utils.Message, "description": "Couldn't create person."},
             },
             status_code=status.HTTP_201_CREATED)
async def create_person(service: Annotated[PersonService, Depends(PersonService)],
                        person: PersonCreate) -> Any:
    """
    Create person, save it to db and return its uuid.

    :param service: Person service.
    :param person: PersonCreate schema.
    :return: Fastapi response with status code and location view for person.
    """
    person_created = service.create(person)
    if not person_created:
        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'message': "Could not create person."
            }
        )
    return person_created


@router.get("/",
            response_model=List[Person],
            status_code=status.HTTP_200_OK)
async def get_all_person(service: Annotated[PersonService, Depends(PersonService)]) -> Any:
    """
    Get all person from database.

    :param service: Person service.
    :return: List of all person or None if there are no person in db.
    """
    return service.get_all()


@router.get("/{person_uuid}",
            response_model=Person,
            responses={
                **utils.EntityNotFoundException.RESPONSE,
            },
            status_code=status.HTTP_200_OK)
async def get_person(service: Annotated[PersonService, Depends(PersonService)],
                     person_uuid: Annotated[UUID, Path()]) -> Any:
    """
    Get person by its uuid.

    :param service: Person service.
    :param person_uuid: uuid of the person.
    :return: Person with uuid equal to person_uuid
             or None if no such person exists.
    """
    person = service.get(person_uuid)
    if not person:
        raise utils.EntityNotFoundException(utils.Entity.PERSON, person_uuid)
    return person


@router.put("/{person_uuid}",
            response_model=Person,
            responses={
                **utils.EntityNotFoundException.RESPONSE,
            },
            status_code=status.HTTP_200_OK
            )
async def update_person(service: Annotated[PersonService, Depends(PersonService)],
                        person_uuid: Annotated[UUID, Path()],
                        person: Annotated[PersonUpdate, Body()]) -> Any:
    """
    Update person with uuid equal to person_uuid.

    :param service: Person service.
    :param person_uuid: uuid of the person.
    :param person: PersonUpdate schema.
    """
    person = service.update(person_uuid, person)
    if not person:
        raise utils.EntityNotFoundException(utils.Entity.PERSON, person_uuid)
    return person


@router.delete("/{person_uuid}",
               response_model=Person,
               responses={
                   **utils.EntityNotFoundException.RESPONSE,
               },
               status_code=status.HTTP_200_OK)
async def delete_person(service: Annotated[PersonService, Depends(PersonService)],
                        person_uuid: Annotated[UUID, Path()]) -> Any:
    """Delete person with uuid equal to person_uuid.

    :param service: Person service.
    :param person_uuid: uuid of the person.
    """
    person = service.remove(person_uuid)
    if not person:
        raise utils.EntityNotFoundException(utils.Entity.PERSON, person_uuid)
    return person
