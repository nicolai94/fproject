from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Body, Query
from sqlalchemy.orm import Session
from starlette import status

from src.clients.weather.client import WeatherClient
from src.dependencies import get_db
from src.models.item import Item
from src.schemas import ItemResponse, ItemData, ItemCreateResponse

router = APIRouter()


@router.get("/weather")
async def get_weather():
    weather_client = WeatherClient()
    result = await weather_client.get_weather()
    return result


@router.get("/{id}", response_model=ItemResponse)
def get_item(
    id: Annotated[int, Path(title="Here is id of Item", ge=0, le=1000)], db: Session = Depends(get_db)
) -> ItemResponse:
    item = db.query(Item).filter(Item.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return ItemResponse(id=item.id, title=item.title, description=item.description)


@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=ItemCreateResponse)
def create_item(
    data: Annotated[ItemData, Body(examples=[{"title": "some_title", "description": "some-description"}])],
    db: Session = Depends(get_db),
) -> ItemCreateResponse:
    item = Item(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return ItemCreateResponse(id=item.id, title=item.title, description=item.description)


@router.get("s", response_model=list[ItemResponse])
def get_all_items(query: Annotated[str, Query(max_length=20)], db: Session = Depends(get_db)) -> list[ItemResponse]:
    items = db.query(Item).all()
    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Items not found")
    return [ItemResponse(id=item.id, title=item.title, description=item.description) for item in items]
