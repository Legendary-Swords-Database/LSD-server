"""
API controllers for sword.
"""
from uuid import UUID
from fastapi import APIRouter, status, Depends, Path, Body, responses
from typing import List, Any, Annotated

from api import utils
from schemas import Sword, SwordUpdate, SwordCreate
from services import SwordService

router = APIRouter(
    prefix='/sword',
    tags=[utils.fastapi_docs.SWORD_TAG['name']]
)


@router.post("/",
             response_model=Sword,
             responses={
                 400: {"model": utils.Message, "description": "Couldn't create sword."},
             },
             status_code=status.HTTP_201_CREATED)
async def create_sword(service: Annotated[SwordService, Depends(SwordService)],
                       sword: SwordCreate) -> Any:
    """
    Create sword, save it to db and return its uuid.

    :param service: Sword service.
    :param sword: SwordCreate schema.
    :return: Fastapi response with status code and location view for sword.
    """
    sword_created = service.create(sword)
    if not sword_created:
        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'message': "Could not create sword."
            }
        )
    return sword_created


@router.get("/",
            response_model=List[Sword],
            status_code=status.HTTP_200_OK)
async def get_all_sword(service: Annotated[SwordService, Depends(SwordService)]) -> Any:
    """
    Get all sword from database.

    :param service: Sword service.
    :return: List of all sword or None if there are no sword in db.
    """
    return service.get_all()


@router.get("/{sword_uuid}",
            response_model=Sword,
            responses={
                **utils.EntityNotFoundException.RESPONSE,
            },
            status_code=status.HTTP_200_OK)
async def get_sword(service: Annotated[SwordService, Depends(SwordService)],
                    sword_uuid: Annotated[UUID, Path()]) -> Any:
    """
    Get sword by its uuid.

    :param service: Sword service.
    :param sword_uuid: uuid of the sword.
    :return: Sword with uuid equal to sword_uuid
             or None if no such sword exists.
    """
    sword = service.get(sword_uuid)
    if not sword:
        raise utils.EntityNotFoundException(utils.Entity.SWORD, sword_uuid)
    return sword


@router.put("/{sword_uuid}",
            response_model=Sword,
            responses={
                **utils.EntityNotFoundException.RESPONSE,
            },
            status_code=status.HTTP_200_OK
            )
async def update_sword(service: Annotated[SwordService, Depends(SwordService)],
                       sword_uuid: Annotated[UUID, Path()],
                       sword: Annotated[SwordUpdate, Body()]) -> Any:
    """
    Update sword with uuid equal to sword_uuid.

    :param service: Sword service.
    :param sword_uuid: uuid of the sword.
    :param sword: SwordUpdate schema.
    """
    sword = service.update(sword_uuid, sword)
    if not sword:
        raise utils.EntityNotFoundException(utils.Entity.SWORD, sword_uuid)
    return sword


@router.delete("/{sword_uuid}",
               response_model=Sword,
               responses={
                   **utils.EntityNotFoundException.RESPONSE,
               },
               status_code=status.HTTP_200_OK)
async def delete_sword(service: Annotated[SwordService, Depends(SwordService)],
                       sword_uuid: Annotated[UUID, Path()]) -> Any:
    """Delete sword with uuid equal to sword_uuid.

    :param service: Sword service.
    :param sword_uuid: uuid of the sword.
    """
    sword = service.remove(sword_uuid)
    if not sword:
        raise utils.EntityNotFoundException(utils.Entity.SWORD, sword_uuid)
    return sword
