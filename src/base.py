from pydantic import BaseModel
from humps.camel import case


def to_camel(string: str) -> str:
    return case(string)


class BaseSchema(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True
