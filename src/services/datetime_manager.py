from datetime import datetime, timedelta
from typing import Literal

import pytz

from config.settings import settings


class LocalDatetimeManager:
    utc_tz = pytz.timezone("UTC")

    def __init__(
        self,
        utc_datetime: datetime,
        tz: str = settings.DEFAULT_TIMEZONE,
        period: Literal["month", "day", "week", "year_by_week", "year_by_month"] = "month",
    ):
        """
        :param utc_datetime: datetime: время по UTC
        :param tz: str: название часового пояса в pytz
        """
        self.tz = tz
        utc_datetime = utc_datetime.replace(tzinfo=None)
        self.utc_datetime = self.utc_tz.localize(utc_datetime)
        self.local_tz = pytz.timezone(tz)
        self.local_datetime = self.utc_datetime.astimezone(self.local_tz)
        self.period = period

    @property
    def day_start_by_utc(self) -> datetime:
        """Начало дня в часовом поясе по UTC"""
        local_day_start = self.local_datetime.replace(hour=0, minute=0, second=0, microsecond=0)

        return local_day_start.astimezone(self.utc_tz).replace(tzinfo=None)

    @property
    def week_start_by_utc(self) -> datetime:
        """Начало недели в часовом поясе по UTC"""
        first_day_of_week = self.local_datetime - timedelta(days=self.local_datetime.weekday())
        local_week_start = first_day_of_week.replace(hour=0, minute=0, second=0, microsecond=0)

        return local_week_start.astimezone(self.utc_tz).replace(tzinfo=None)

    @property
    def month_start_by_utc(self) -> datetime:
        """Начало месяца в часовом поясе по UTC"""
        local_month_start = self.local_datetime.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

        return local_month_start.astimezone(self.utc_tz).replace(tzinfo=None)

    @property
    def year_start_by_utc(self) -> datetime:
        """Начало года в часовом поясе по UTC"""
        local_year_start = self.local_datetime.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)

        return local_year_start.astimezone(self.utc_tz).replace(tzinfo=None)

    @classmethod
    def from_local_datetime(
        cls, local_datetime: datetime, tz: str = settings.DEFAULT_TIMEZONE
    ) -> "LocalDatetimeManager":
        """Конструирование объекта LocalDatetimeManager от местного времени"""
        local_datetime = local_datetime.replace(tzinfo=None)
        local_tz = pytz.timezone(tz)
        utc_datetime = local_tz.localize(local_datetime).astimezone(cls.utc_tz)

        return LocalDatetimeManager(utc_datetime, tz=tz)
