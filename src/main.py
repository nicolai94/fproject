import redis
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.settings import settings
from src import models
from src.api.api_v1.api import api_router
from src.database import engine

models.item.Base.metadata.create_all(bind=engine)


class DynamicCORSMiddleware(CORSMiddleware):
    def is_allowed_origin(self, origin: str) -> bool:
        return True


rd = redis.Redis(host="localhost", port=6379, db=0)

def create_app() -> FastAPI:

    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        DynamicCORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.API_V1_STR)

    return app


app = create_app()
