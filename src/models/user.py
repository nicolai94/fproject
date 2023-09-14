from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped

from src.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = Column(Integer, primary_key=True, unique=True)
    username: str = Column(String, nullable=False)
    password: str = Column(String, nullable=False)
    email: str = Column(String, nullable=True)
    full_name: str = Column(String, nullable=True)
    disabled: bool = Column(Boolean, default=False)
