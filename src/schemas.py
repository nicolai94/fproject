from src.base import BaseSchema


class Item(BaseSchema):
    id: int
    title: str
    description: str


class ItemResponse(Item):
    ...


class ItemData(BaseSchema):
    title: str
    description: str


class ItemCreateResponse(Item):
    ...
