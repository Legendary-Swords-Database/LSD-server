"""
API controllers for sword.
"""
from uuid import UUID
from fastapi import APIRouter, status, Depends, Path, Body
from typing import List, Any, Annotated

from api import utils
from schemas import Sword, SwordUpdate
from services import SwordService

router = APIRouter(
    prefix='/sword',
    tags=[utils.fastapi_docs.SWORD_TAG['name']]
)


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
