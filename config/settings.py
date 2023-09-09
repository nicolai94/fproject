from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FProject"
    DB_URL: str = "sqlite:///./app.db"


settings = Settings()
