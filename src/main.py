import redis
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.settings import settings
from src import models
from src.api.api_v1.api import api_router
from src.database import engine
from src.auth import router as auth_router

models.item.Base.metadata.create_all(bind=engine)


class DynamicCORSMiddleware(CORSMiddleware):
    def is_allowed_origin(self, origin: str) -> bool:
        return True


rd = redis.Redis(host="localhost", port=6379, db=0)


def create_app() -> FastAPI:
    app = FastAPI(
        title="ChimichangApp",
        description="new description",
        summary="Deadpool's favorite app. Nuff said.",
        version="0.0.1",
        terms_of_service="http://example.com/terms/",
        contact={
            "name": "Deadpoolio the Amazing",
            "url": "http://x-force.example.com/contact/",
            "email": "dp@x-force.example.com",
        },
        license_info={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )

    origins = ["*"]

    app.add_middleware(
        DynamicCORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix=settings.API_V1_STR)
    app.include_router(auth_router, prefix="/auth", tags=["auth"])

    return app


app = create_app()
