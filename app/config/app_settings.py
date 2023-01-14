from functools import lru_cache
from pydantic import BaseSettings, HttpUrl

class AppSettings(BaseSettings):
    """
    """
    url_one: HttpUrl

@lru_cache
def get_settings():
    return AppSettings()
