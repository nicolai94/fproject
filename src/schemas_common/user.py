from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserCreate(BaseModel):
    username: str
    password: str
