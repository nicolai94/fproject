import redis

from config.settings import settings


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Cache(metaclass=Singleton):
    def __init__(self):
        self.pool = redis.ConnectionPool(host=settings.REDIS_HOST, db=settings.REDIS_CACHE_DB)
        self._redis = None

    def close(self):
        if self._redis:
            self._redis.close()

    @property
    def redis(self):
        if not hasattr(self, "_conn"):
            self.get_connection()
        return self._redis

    def get_connection(self):
        self._redis = redis.Redis(connection_pool=self.pool)

    def get(self, key):
        return self.redis.get(_prefix_key(key))

    def set(self, key, value, ttl=None):
        return self.redis.set(_prefix_key(key), value, ex=ttl)

    def incr(self, key, amount=1):
        return self.redis.incr(_prefix_key(key), amount=amount)

    def delete(self, key):
        return self.redis.delete(_prefix_key(key))

    def clean_by_key(self, key: str) -> None:
        keys = self.redis.keys(f"{key}_*")
        for key in keys:
            self.redis.delete(key)


def _prefix_key(key: str) -> str:
    return f"{settings.PROJECT_NAME}:{key}"


cache = Cache()
