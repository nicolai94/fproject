def format_weather_temperature(value: float) -> float:
    result = value - 273.15
    return round(result, 2)
