from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    ENV: str = "local"
    VERSION: str = "0.1.0"
    WEATHER_API_KEY: str = "79a53350a68c7ea12db3223614bf7120"
    LATITUDE: float = 60.024
    LONGITUDE: float = 30.214

    PROJECT_NAME: str = "FProject"
    DB_URL: str = "postgresql+psycopg2://postgres:password@db:5432/db"
    API_V1_STR: str = "/api/v1"
    REDIS_HOST: str = "redis"
    REDIS_DB: int = 0


settings = Settings()
