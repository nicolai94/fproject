from pydantic import validator

from src.base import BaseSchema
from src.utils import format_weather_temperature


class WeatherParams(BaseSchema):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: float
    humidity: int
    sea_level: int
    grnd_level: int

    _format_datetime = validator("temp", "feels_like", "temp_min", "temp_max", allow_reuse=True)(format_weather_temperature)


class WeatherClientResponse(BaseSchema):
    main: WeatherParams
