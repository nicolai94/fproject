import os
import time

from celery import Celery
from starlette.responses import JSONResponse

celery = Celery(__name__)
celery.conf.broker_url = "redis://redis:6379/0"
celery.conf.result_backend = "redis://redis:6379/0"


@celery.task(name="new_task")
def new_task(value):
    return JSONResponse({"Value": value})
