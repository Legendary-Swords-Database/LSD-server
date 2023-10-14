"""
Module to run FastAPI application, where API routers are connecting application to API modules.
In other words it is an entry point of the application.
"""

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import utils, api_sword, api_person
from core import settings
from db import init_db

app = FastAPI(
    title=utils.fastapi_docs.NAME,
    description=utils.fastapi_docs.DESCRIPTION,
    version=utils.fastapi_docs.VERSION,
    openapi_tags=utils.fastapi_docs.get_tags_metadata()
)
app.include_router(api_sword.router)
app.include_router(api_person.router)

app.add_exception_handler(
    utils.MethodNotAllowedException, utils.method_not_allowed_exception_handler
)
app.add_exception_handler(
    utils.EntityNotFoundException, utils.entity_not_found_exception_handler
)
app.add_exception_handler(
    utils.NotImplementedException, utils.not_implemented_exception_handler
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """
    Is called on the application startup, before it is ready to accept requests.
    Is used for app initialization, like here it is creating db tables if they are not created.
    """
    print(f'Starting {settings.APP_NAME}.')
    init_db()


if __name__ == "__main__":
    uvicorn.run("main:app",
                host=settings.APP_SERVER_HOST,
                port=settings.APP_SERVER_PORT,
                reload=settings.APP_SERVER_USE_RELOAD,
                proxy_headers=settings.APP_SERVER_USE_PROXY_HEADERS)
