from fastapi import APIRouter

from src.api.api_v1.common.common import router as common_router
from src.api.api_v1.user.user import router as user_router

api_router = APIRouter()

api_router.include_router(common_router, prefix="/item", tags=["Items"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
