from fastapi import APIRouter

from src.api.api_v1.common.common import router as common_router

api_router = APIRouter()

api_router.include_router(common_router, prefix="/item", tags=["Items"])
