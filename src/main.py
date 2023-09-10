import redis
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from config.settings import settings
from src import models
from src.api.api_v1.api import api_router
from src.database import engine

models.item.Base.metadata.create_all(bind=engine)

rd = redis.Redis(host="localhost", port=6379, db=0)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/tasks/{task_id}")
def get_status(task_id):
    return JSONResponse(task_id)
