import httpx

from config.settings import settings
from logger import get_logger
from src.clients.weather.exceptions import WeatherError
from src.clients.weather.schemas import WeatherClientResponse

logger = get_logger("weather_client")


class WeatherClient:
    BASE_URL: str = f"https://api.openweathermap.org/data/2.5/weather?lat={settings.LATITUDE}&lon={settings.LONGITUDE}&appid={settings.WEATHER_API_KEY}"

    async def get_weather(self):
        try:
            async with httpx.AsyncClient() as client:
                response: httpx.Response = await client.get(url=self.BASE_URL)

            response.raise_for_status()
            logger.debug("Weather", data=response.json())
            return WeatherClientResponse(**response.json())

        except httpx.HTTPError as exc:
            logger.exception("Error while try to get weather", exc_info=exc)
            raise WeatherError("Error while try to get weather") from exc
