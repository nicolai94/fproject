import httpx


class WeatherError(httpx.HTTPError):
    pass
