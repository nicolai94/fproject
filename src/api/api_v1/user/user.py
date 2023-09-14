from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.auth import pwd_context, get_current_user
from src.dependencies import get_db
from src.models import User
from src.schemas_common.user import UserCreate

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    create_user = User(username=user_data.username, password=pwd_context.hash(user_data.password))
    db.add(create_user)
    db.commit()
    return f"User {user_data.username} was created"


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: Annotated[dict, Depends(get_current_user)]):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication failed")
    return {"User": user}
