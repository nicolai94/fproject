from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FProject"
    DB_URL: str = "postgresql+psycopg2://postgres:password@db:5432/db"
    API_V1_STR: str = "/api/v1"
    REDIS_HOST: str = "redis"
    REDIS_DB: int = 0


settings = Settings()
