from fastapi import FastAPI

from app.routers.api import router

app = FastAPI()

app.include_router(
    router,
    prefix="/api/v1"
)
