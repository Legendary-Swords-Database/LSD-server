"""
Module to run FastAPI application, where API routers are connecting application to API modules.
In other words it is an entry point of the application.
"""

import uvicorn
from fastapi import FastAPI

from core import settings
from db import init_db

app = FastAPI(

)

origins = ["*"]


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
