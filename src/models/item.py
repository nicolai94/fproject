from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from src.database import Base


class Item(Base):
    __tablename__ = "model_items"
    id: Mapped[int] = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
