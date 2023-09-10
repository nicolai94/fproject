from collections.abc import Generator

from src.database import SessionLocal


def get_db() -> Generator[SessionLocal, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
