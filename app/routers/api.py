"""
Module consolidate the routers
"""
from fastapi import APIRouter

from app.routers.v1.scores import router_score

router = APIRouter()

router.include_router(
    router_score,
    tags=["Score"]
)
