from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import Response

from src.dependencies import get_db
from src.models import Item
from src.schemas import ItemResponse, ItemData, ItemCreateResponse

router = APIRouter()


@router.get("/item/{id}", response_model=ItemResponse)
async def get_item(id: int, db: Session = Depends(get_db)) -> ItemResponse:
    item = db.query(Item).filter(Item.id == id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item.dict()


@router.post("/item/create", status_code=status.HTTP_201_CREATED, response_model=ItemCreateResponse)
async def create_item(data: ItemData, db: Session = Depends(get_db)) -> ItemCreateResponse:
    item = Item(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return ItemCreateResponse(id=item.id, title=item.title, description=item.description)


@router.get("/items", response_model=list[ItemResponse])
async def get_all_items(db: Session = Depends(get_db)) -> list[ItemResponse]:
    items = db.query(Item).all()
    return [ItemResponse(id=item.id, title=item.title, description=item.description) for item in items]
